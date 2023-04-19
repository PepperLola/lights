from networktables import NetworkTables
from lights.led_strip import LEDStrip
from effects.solid import SolidEffect
from effects.breathe import BreatheEffect
from effects.rainbow import RainbowEffect
from led_manager import LEDManager
from util.color import Color
import logging
import time
from constants import SECONDS_PER_TICK

# LED_TABLE_NAME = "led_devices"
#
# logging.basicConfig(level=logging.DEBUG)
#
led_manager = LEDManager()

strip = LEDStrip("text", 0, 25, is_sim=True)
led_manager.register_device(strip)

effect = RainbowEffect(strip, 0.01, 0.5)
led_manager.set_device_effect(strip, effect)

if __name__ == "__main__":
    while True:
        led_manager.update_effects()
        time.sleep(SECONDS_PER_TICK)
#
# ip = ""
#
# NetworkTables.initialize(server=ip)
#
# def connectionListener(connected, info):
#     print(info, "; Connected=%s" % connected)
#
# def valueChanged(table, key, value, isNew):
#     if table == LED_TABLE_NAME:
#         print("valueChanged: key: '%s'; value: %s; isNew: %s" % (key, value, isNew))
#         if isNew:
#             led_manager.register_device(LEDStrip(key, 0, 0))
#             # TODO change this once I know how networktables is formatted
#
# NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)
#
# sd = NetworkTables.getTable(LED_TABLE_NAME)
# sd.addEntryListener(valueChanged)
