from networktables import NetworkTables
from lights.led_device import LEDDevice
from lights.led_strip import LEDStrip
from lights.led_panel import LEDPanel
from effects.solid import SolidEffect
from effects.breathe import BreatheEffect
from effects.rainbow import RainbowEffect
from led_manager import LEDManager
from util.color import Color
import logging
import time
import json
from constants import SECONDS_PER_TICK

MAIN_TABLE_NAME = "PiLED"
LED_TABLE_NAME = "led_devices"
EFFECTS_TABLE_NAME = "led_effects"

logging.basicConfig(level=logging.DEBUG)

led_manager = LEDManager()

led_manager.parse_led_effect(LEDStrip("test", 0, 25, is_sim=True), json.loads('{"name": "rainbow"}'))

# strip = LEDStrip("text", 0, 25, is_sim=True)
# led_manager.register_device(strip)
#
# effect = RainbowEffect(strip, 0.01, 0.5)
# led_manager.set_device_effect(strip, effect)

ip = "10.27.33.2"

NetworkTables.initialize(server=ip)

def connectionListener(connected, info):
    print(info, "; Connected=%s" % connected)

def valueChanged(table, key, value, isNew):
    # if table == LED_TABLE_NAME:
    print(table.path + " valueChanged: key: '%s'; value: %s; isNew: %s" % (key, value, isNew))
    if table.path == f"/{MAIN_TABLE_NAME}/{LED_TABLE_NAME}":
        name = key
        if led_manager.is_device_registered(name):
            return
        data = json.loads(value)
        device = None
        if data["type"].lower() == "strip":
            device = LEDStrip(name, data["port"], data["length"], True)
        elif data["type"].lower() == "panel":
            device = LEDPanel(name, data["port"], data["length"], True)
        if device == None:
            return
        led_manager.register_device(device)
        led_manager.set_device_effect(device, RainbowEffect(device, 0.01, 0.5))
        print("Registering LED " + data["type"].lower() + " on port " + str(device.get_port()) + " with length " + str(device.get_length()))
    elif table.path == f"/{MAIN_TABLE_NAME}/${LED_TABLE_NAME}":
        name = key
        if not led_manager.is_device_registered(name):
            return
        device = led_manager.get_device(name)
        data = json.loads(value)
        effect = led_manager.parse_led_effect(device, data)
        led_manager.set_device_effect(device, effect)
            
                
    # if isNew:
    #     led_manager.register_device(LEDStrip(key, 0, 0))
            # TODO change this once I know how networktables is formatted

NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

main_table = NetworkTables.getTable(MAIN_TABLE_NAME)
lights_table = main_table.getSubTable(LED_TABLE_NAME)
lights_table.addEntryListener(valueChanged)
lights_table.addSubTableListener(valueChanged)


if __name__ == "__main__":
    while True:
        led_manager.update_effects()
        time.sleep(SECONDS_PER_TICK)

