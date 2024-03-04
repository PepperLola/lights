import threading
from lights.led_panel_segment import LEDPanelSegment
from lights.led_segment import LEDSegment
from lights.led_strip_segment import LEDStripSegment
from networktables import NetworkTables, NetworkTablesInstance
from lights.led_strip import LEDStrip
from lights.led_panel import LEDPanel
from util.color import RED
from led_manager import LEDManager
from effects.not_connected import NotConnectedEffect
from flask import Flask, send_from_directory, request
from util.morse import get_pauses, to_morse
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging
import time
import json
import os
import glob
import re
from constants import SECONDS_PER_TICK

MAIN_TABLE_NAME = "PiLED"
GAME_INFO_TABLE_NAME = "GameInfo"
LED_TABLE_NAME = "led_devices"
EFFECTS_TABLE_NAME = "led_effects"

logging.basicConfig(level=logging.DEBUG)

led_manager = LEDManager()

app = Flask(__name__, static_folder='server/dist')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'custom_effects')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# effect = RainbowEffect(strip, 0.01, 0.5)
# led_manager.set_device_effect(strip, effect)

ip = "10.27.33.2"
NetworkTables.initialize(server=ip)

def connectionListener(connected, info):
    if not connected:
        led_manager.unregister_all_devices()
    print(info, "; Connected=%s" % connected)

def valueChanged(table, key, value, isNew):
    print(table.path + " valueChanged: key: '%s'; value: %s; isNew: %s" % (key, value, isNew))
    if table.path == f"/{MAIN_TABLE_NAME}/{LED_TABLE_NAME}":
        name = key
        if led_manager.is_device_registered(name):
            return
        data = json.loads(value)
        device = None
        if data["type"].lower() == "strip":
            device = LEDStrip(name, data["port"], data["length"], False)
        elif data["type"].lower() == "panel":
            device = LEDPanel(name, data["port"], data["width"], data["height"], True, alternating=data["alternating"])
        if device == None:
            return
        led_manager.register_device(device)

        if "segments" in data.keys():
            for segment in data["segments"]:
                led_segment = None
                if isinstance(device, LEDStrip):
                    led_segment = LEDStripSegment(segment["name"], device, segment["range"])
                elif isinstance(device, LEDPanel):
                    led_segment = LEDPanelSegment(segment["name"], device, segment["top_left"], segment["bottom_right"])

                if led_segment is not None:
                    led_manager.register_segment(device.get_name(), led_segment)
        else:
            led_manager.register_default_segment(device)
        print("Registering LED " + data["type"].lower() + " on port " + str(device.get_port()) + " with length " + str(device.get_length()))
    elif table.path == f"/{MAIN_TABLE_NAME}/{EFFECTS_TABLE_NAME}":
        name = key
        if not led_manager.is_segment_registered(name):
            return
        data = json.loads(value)
        segment = led_manager.get_segment(name)
        print(segment)
        if segment == None:
            return
        effect = led_manager.parse_led_effect(segment, data)
        if effect == None:
            return
        led_manager.set_segment_effect(segment, effect)
            
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

main_table = NetworkTables.getTable(MAIN_TABLE_NAME)
game_info_table = main_table.getSubTable(GAME_INFO_TABLE_NAME)
lights_table = main_table.getSubTable(LED_TABLE_NAME)
lights_table.addEntryListener(valueChanged)
lights_table.addSubTableListener(valueChanged)
effects_table = main_table.getSubTable(EFFECTS_TABLE_NAME)
effects_table.addEntryListener(valueChanged)
effects_table.addSubTableListener(valueChanged)

@app.route("/")
def serve():
    return send_from_directory(str(app.static_folder), 'index.html')

@app.route("/devices")
@cross_origin()
def devices():
    return [
        {
            "name": led.get_name(),
            "port": led.get_port(),
            "length": led.get_length() # TODO add segments
            # "effect": led_manager.get_device_effect(led).get_name() if led.get_name() in led_manager.get_device_effects().keys() else ""
        } for led in led_manager.get_devices().values()
    ]

@app.route("/custom-effects", methods=[ "GET", "POST", "DELETE" ])
def upload_effect():
    if request.method == "GET":
        current_dir = os.path.dirname(os.path.realpath(__file__))
        root_dir = os.path.join(str(current_dir), "custom_effects")
        return glob.glob(root_dir=root_dir, pathname="*.py"), 200
    elif request.method == "POST":
        if 'file' not in request.files:
            return 'No file in the request', 400

        f = request.files['file']
        if f.filename == '':
            return 'Filename is empty', 400

        if not '.' in f.filename or f.filename.rsplit('.', 1)[1] != "py":
            return "Invalid filetype", 400

        contents = str(f.read())
        if re.findall(r"(class (\w|\d)+\(LEDEffect\))", contents):
            try:
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            except Exception as e:
                return f'Error saving file: {str(e)}', 500
            return 'File uploaded successfully', 200
        return 'Invalid effect file', 500
    elif request.method == "DELETE":
        if 'file' not in request.values:
            return 'No filename in the request', 400
        
        filename = request.values['file']
        if not '.' in filename or filename.rsplit('.', 1)[1] != "py":
            return "Invalid filetype", 400

        if os.path.exists(filename):
            parent_path = os.path.abspath(os.path.dirname(filename))
            if parent_path != app.config['UPLOAD_FOLDER']:
                return 'Invalid filename', 400
            os.remove(os.path.abspath(filename))
            return 'Deleted effect', 200
        else:
            if re.match(r"^[A-Za-z0-9\-_]+\.py$", filename):
                if os.path.exists(f'custom_effects/{filename}'):
                    os.remove(os.path.abspath(f'custom_effects/{filename}'))
                    return 'Deleted effect', 200
            return 'Invalid filename', 400

if __name__ == "__main__":
    # valueChanged(lights_table, "panel", '{"type": "panel", "port": 0, "width": 16, "height": 16, "alternating": true}', True)
    valueChanged(lights_table, "panel", '{"type": "panel", "port": 0, "width": 16, "height": 16, "alternating": true, "segments": [{"name":"segment1","top_left":[0,0],"bottom_right":[8,8]},{"name":"segment2","top_left":[8,0], "bottom_right":[16,8]},{"name":"segment3","top_left":[0,8], "bottom_right":[16,16]}]}', True)
    # valueChanged(lights_table, "strip", '{"type": "strip", "port": 0, "length": 64 }', True)
    # valueChanged(lights_table, "strip", '{"type": "strip", "port": 0, "length": 64, "segments": [{"name":"segment1","range": [0,32]},{"name":"segment2","range":[32,64]}]}', True)
    valueChanged(effects_table, "segment3", '{"name": "text", "text": "test", "scroll_speed": 5, "x": 0, "y": 0}', True)
    # valueChanged(effects_table, "strip", '{"name": "breathe_alliance", "red_color": [ 255, 0, 0 ], "blue_color": [ 0, 0, 255 ], "speed": 0.5}', True)
    # valueChanged(effects_table, "panel", '{"name": "cylon"}', True)
    # valueChanged(effects_table, "segment4", '{"name": "cylon"}', True)
    # valueChanged(effects_table, "segment1", '{"name": "fire"}', True)#, "colors": [[[ 0, 0, 0 ], 0], [[ 255, 255, 0 ], 0.5], [[ 255, 255, 255 ], 1]]}', True)
    # valueChanged(effects_table, "panel", '{"name": "conway"}', True)
    # valueChanged(effects_table, "segment1", '{"name": "blink"}', True)
    valueChanged(effects_table, "segment1", '{"name": "morse"}', True)
    valueChanged(effects_table, "segment2", '{"name": "rainbow", "speed": 0.5}', True)
    # valueChanged(effects_table, "segment3", '{"name": "rainbow", "speed": 0.5}', True)
    # valueChanged(effects_table, "segment1", '{"name": "animation"}', True)

    flask_thread = threading.Thread(target=lambda: app.run(port=2733, threaded=True, debug=True, use_reloader=False))
    flask_thread.daemon = True
    flask_thread.start()

    is_disconnected = False

    while True:
        if NetworkTablesInstance.getDefault().isConnected():
            is_disconnected = False
        elif not is_disconnected:
            # set all devices to red breathing not connected effect
            for name in led_manager.get_devices():
                device = led_manager.get_device(name)
                # led_manager.set_device_effect(device, NotConnectedEffect(device))
            is_disconnected = True
        led_manager.update_effects(game_info_table)
        time.sleep(SECONDS_PER_TICK)

