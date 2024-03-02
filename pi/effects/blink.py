from networktables import NetworkTable
from effects.led_effect import LEDEffect
from lights.led_device import LEDDevice
from util.color import Color, blend, BLACK, PURPLE, from_int
from constants import SECONDS_PER_TICK
import math
import time

from util.time import current_time_millis

class BlinkEffect(LEDEffect):
    _on: bool
    _interval: float
    _last_change: int

    def __init__(self, device: LEDDevice, color: Color, interval: float):
        super().__init__(device)
        self._color = color
        self._interval = interval
        self._on = False

    def start(self):
        self.get_device().get_neopixel().fill(BLACK.to_tuple())
        self._last_change = current_time_millis()

    def update(self, game_info_table: NetworkTable):
        current_time = current_time_millis()
        if (current_time - self._last_change) / 1000 > self._interval:
            self._last_change = current_time
            self._on = not self._on
            if self._on:
                self.get_device().get_neopixel().fill(self._color.to_tuple())
            else:
                self.get_device().get_neopixel().fill(BLACK.to_tuple())

def parse(device: LEDDevice, data):
    color = PURPLE
    interval = 0.5

    if "color" in data.keys():
        c = data["color"]
        if isinstance(c, int):
            color = from_int(c)
        else:
            color = Color(c[0], c[1], c[2])

    if "interval" in data.keys():
        interval = data["interval"]

    return BlinkEffect(device, color, interval)
