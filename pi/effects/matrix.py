from networktables import NetworkTable
from effects.led_effect import LEDEffect
from lights.led_segment import LEDSegment
from util.color import GREEN, WHITE, Color, ColorRamp, blend, BLACK, PURPLE, from_color_array, from_int
from constants import SECONDS_PER_TICK
import math
import time
import random

from util.time import current_time_millis

class MatrixEffect(LEDEffect):
    _drops: dict[int,  int | None]
    _color: ColorRamp
    _speed: int
    _interval: float
    _rain_length: int
    _last_change: int
    _last_move: int
    _free_spots: int

    def __init__(self, segment: LEDSegment, color: ColorRamp, speed: int, interval: float, rain_length: int):
        super().__init__(segment, panel_only=True)
        self._color = color
        self._speed = speed
        self._interval = interval
        self._rain_length = rain_length

        self._drops = {}
        self._free_spots = segment.get_width()
        for i in range(self._free_spots):
            self._drops[i] = None

    def start(self):
        self.get_segment().fill(BLACK)
        self._last_change = current_time_millis()
        self._last_move = current_time_millis()

    def cleanup_rain(self):
        for pos in self._drops.keys():
            y = self._drops[pos]
            if y is None:
                continue
            if y - self._rain_length > self.get_segment().get_height():
                self._drops[pos] = None
                self._free_spots += 1

    def create_new_drop(self):
        if self._free_spots <= 0:
            return
        random_slot = random.randint(0, self._free_spots)
        for i in range(random_slot, len(self._drops)):
            if self._drops[i] == None:
                self._drops[i] = 0
                self._free_spots -= 1
                break

    def update_rain(self):
        for (pos, y) in self._drops.items():
            if y is None:
                continue
            self._drops[pos] = y+1
            for i in range(y+1, y+1-self._rain_length, -1):
                if i >= 0:
                    self.get_segment().get_buffer().pixel(pos, i, self._color.get_color((y+1-i) / self._rain_length).to_tuple())
            to_clear = y+1-self._rain_length-1
            if to_clear >= 0:
                self.get_segment().get_buffer().pixel(pos, to_clear, BLACK.to_tuple())

    def update(self, game_info_table: NetworkTable):
        current_time = current_time_millis()
        if (current_time - self._last_change) / 1000 > self._interval:
            self.create_new_drop()
            self._last_change = current_time

        if (current_time - self._last_move) / 1000 > 1 / self._speed:
            self.cleanup_rain()
            self.update_rain()
            self._last_move = current_time

def parse(segment: LEDSegment, data):
    color = ColorRamp([(blend(GREEN, WHITE, 0.9), 0), (GREEN, 0.1), (BLACK, 1)])
    speed = 10
    interval = 0.5
    rain_length = 8

    if "color" in data.keys():
        color = from_color_array(data["color"])

    if "speed" in data.keys():
        speed = data["speed"]

    if "interval" in data.keys():
        interval = data["interval"]

    if "rain_length" in data.keys():
        rain_length = data["rain_length"]

    return MatrixEffect(segment, color, speed, interval, rain_length)
