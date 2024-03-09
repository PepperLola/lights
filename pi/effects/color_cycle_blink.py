from networktables import NetworkTable
from effects.led_effect import LEDEffect
from lights.led_segment import LEDSegment
from util.color import Color, blend, BLACK, PURPLE, from_color_array, from_int
from constants import SECONDS_PER_TICK
import math
import time

from util.time import current_time_millis

class ColorCycleBlinkEffect(LEDEffect):
    _colors: list[Color]
    _interval: int
    _index: int
    _on: bool

    def __init__(self, segment: LEDSegment, colors: list[Color], interval: int):
        super().__init__(segment)
        # disallow CycleEffect within CycleEffect?
        self._colors = colors
        self._interval = interval

    def start(self):
        self._last_change = current_time_millis()
        self._index = 0
        self._on = True
        self.get_segment().fill(self._colors[self._index])

    def update(self, game_info_table: NetworkTable):
        current_time = current_time_millis()

        if (current_time - self._last_change) / 1000 > self._interval:
            self._last_change = current_time
            if not self._on:
                self._index += 1
                self._index %= len(self._colors)
                self.get_segment().fill(self._colors[self._index])
                self._on = True
            else:
                self._on = False
                self.get_segment().fill(BLACK)


def parse(segment: LEDSegment, data):
    colors: list[Color] = []
    interval = 15

    if "interval" in data.keys():
        interval = data["interval"]

    if "colors" in data.keys():
        parsed = []
        for data in data["colors"]:
            print(data)
            if isinstance(data, list):
                parsed.append(Color(data[0], data[1], data[2]))
            elif isinstance(data, int):
                parsed.append(from_int(data))
        colors = parsed

    return ColorCycleBlinkEffect(segment, colors, interval)
