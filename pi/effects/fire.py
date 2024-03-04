from networktables import NetworkTable
from effects.led_effect import LEDEffect
from lights.led_segment import LEDSegment
from util.color import Color, ColorRamp, blend, BLACK, RED, ORANGE, YELLOW, BLUE, PURPLE, WHITE, from_int
from constants import SECONDS_PER_TICK
import math
import random
import time

class FireEffect(LEDEffect):
    _len: int
    _colors: ColorRamp
    _height: float
    _flare_chance: float
    _flare_brightness: float
    _buf: list[float]

    def __init__(self, segment: LEDSegment, colors: ColorRamp, height: float, flare_chance: float, flare_brightness: float):
        super().__init__(segment)
        self._colors = colors
        self._height = height
        self._flare_chance = flare_chance
        self._flare_brightness = max(0, min(flare_brightness, 1))
        self._len = self.get_segment().get_length()
        self._buf = [1] * self._len

    def start(self):
        self.get_segment().fill(BLACK)

    def update(self, game_info_table: NetworkTable):
        for i in range(self._len - 1, 0, -1):
            self._buf[i] = self._buf[i-1] + random.random() / (self._height * 10)
        self._buf[0] = 0 if random.random() < self._flare_chance else random.random() * self._flare_brightness
        for i in range(self._len):
            self.get_segment().set_index(i, self._colors.get_color(self._buf[i]))

def parse(segment: LEDSegment, data):
    colors = ColorRamp([(RED, 0), (ORANGE, 0.5), (YELLOW, 0.7), (BLACK, 0.75), (BLACK, 1)])
    height = 3
    flare_chance = 0.65
    flare_brightness = 0.25

    if "colors" in data.keys():
        c = data["colors"]
        cl = []
        if isinstance(c, list):
            for (color, pos) in c:
                if isinstance(color, tuple) or isinstance(color, list):
                    cl.append((Color(color[0], color[1], color[2]), pos))
                elif isinstance(color, int):
                    cl.append((from_int(color), pos))
        colors = ColorRamp(cl)

    if "height" in data.keys():
        height = float(data["height"])

    if "flare_chance" in data.keys():
        flare_chance = float(data["flare_chance"])

    if "flare_brightness" in data.keys():
        flare_brightness = float(data["flare_brightness"])

    return FireEffect(segment, colors, height, flare_chance, flare_brightness)
