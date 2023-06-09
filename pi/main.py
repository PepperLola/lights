from networktables import NetworkTables
from lights.led_device import LEDDevice
from lights.led_strip import LEDStrip
from lights.led_panel import LEDPanel
from effects.solid import SolidEffect
from effects.breathe import BreatheEffect
from effects.rainbow import RainbowEffect
from led_manager import LEDManager
from util.color import Color
from effects.importer import import_effect
import logging
import time
import json
from constants import SECONDS_PER_TICK

MAIN_TABLE_NAME = "PiLED"
LED_TABLE_NAME = "led_devices"
EFFECTS_TABLE_NAME = "led_effects"

logging.basicConfig(level=logging.DEBUG)

led_manager = LEDManager()

#
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
        print("Registering LED " + data["type"].lower() + " on port " + str(device.get_port()) + " with length " + str(device.get_length()))
    elif table.path == f"/{MAIN_TABLE_NAME}/{EFFECTS_TABLE_NAME}":
        name = key
        if not led_manager.is_device_registered(name):
            return
        device = led_manager.get_device(name)
        data = json.loads(value)
        effect = led_manager.parse_led_effect(device, data)
        if effect == None:
            return
        led_manager.set_device_effect(device, effect)
            
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

main_table = NetworkTables.getTable(MAIN_TABLE_NAME)
lights_table = main_table.getSubTable(LED_TABLE_NAME)
lights_table.addEntryListener(valueChanged)
lights_table.addSubTableListener(valueChanged)
effects_table = main_table.getSubTable(EFFECTS_TABLE_NAME)
effects_table.addEntryListener(valueChanged)
effects_table.addSubTableListener(valueChanged)


if __name__ == "__main__":
    # valueChanged(lights_table, "strip", '{"type": "panel", "port": 0, "width": 16, "height": 16, "alternating": true}', True)
    # valueChanged(lights_table, "strip", '{"type": "strip", "port": 0, "length": 64}', True)
    # valueChanged(effects_table, "strip", '{"name": "text", "text": "test"}', True)

    while True:
        led_manager.update_effects()
        time.sleep(SECONDS_PER_TICK)

