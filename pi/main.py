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

logging.basicConfig(level=logging.DEBUG)

led_manager = LEDManager()

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
    print(table + " valueChanged: key: '%s'; value: %s; isNew: %s" % (key, value, isNew))
    if table == LED_TABLE_NAME:
        if isNew:
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
            print("Registering LED " + data["type"].lower() + " on port " + device.get_port() + " with length " + device.get_length())
                
    # if isNew:
    #     led_manager.register_device(LEDStrip(key, 0, 0))
            # TODO change this once I know how networktables is formatted

NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

sd = NetworkTables.getTable(LED_TABLE_NAME)
sd.addEntryListener(valueChanged)
sd.addSubTableListener(valueChanged)


if __name__ == "__main__":
    while True:
        led_manager.update_effects()
        time.sleep(SECONDS_PER_TICK)

