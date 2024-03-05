from lights.led_panel import LEDPanel
from lights.led_panel_segment import LEDPanelSegment
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
    _center_bias: float
    _bufs: list[list[float]]

    def __init__(self, segment: LEDSegment, colors: ColorRamp, height: float, flare_chance: float, flare_brightness: float, center_bias: float = 0):
        super().__init__(segment)
        self._colors = colors
        self._height = height
        self._flare_chance = flare_chance
        self._flare_brightness = max(0, min(flare_brightness, 1))
        self._center_bias = center_bias
        self._len = self.get_segment().get_length()
        if isinstance(segment, LEDPanelSegment):
            led_panel_segment: LEDPanelSegment = segment
            self._buf = [[1.0 for y in range(led_panel_segment.get_height())] for x in range(led_panel_segment.get_width())]
        else:
            self._buf = [[1.0] for y in range(self._len)]

    def start(self):
        self.get_segment().fill(BLACK)

    def update(self, game_info_table: NetworkTable):
        segment = self.get_segment()
        for x in range(len(self._buf)):
            height_bias = (abs(x - len(self._buf) // 2) / len(self._buf)) * self._center_bias / 5
            for y in range(len(self._buf[x]) - 1, 0, -1):
                self._buf[x][y] = self._buf[x][y-1] + random.random() / (self._height * 10) + height_bias
            self._buf[x][0] = 0 if random.random() < self._flare_chance else random.random() * self._flare_brightness
            for y in range(len(self._buf[x])):
                if isinstance(segment, LEDPanelSegment):
                    led_panel_segment: LEDPanelSegment = segment
                    # flip upside down so fire starts at bottom
                    led_panel_segment.get_buffer().pixel(x, len(self._buf[x]) - y, self._colors.get_color(self._buf[x][y]).to_tuple())
                else:
                    self.get_segment().set_index(y, self._colors.get_color(self._buf[x][y]))

def parse(segment: LEDSegment, data):
    colors = ColorRamp([(RED, 0), (ORANGE, 0.5), (YELLOW, 0.7), (BLACK, 0.75), (BLACK, 1)])
    height = 3
    flare_chance = 0.65
    flare_brightness = 0.25
    center_bias = 0

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

    if "center_bias" in data.keys():
        center_bias = float(data["center_bias"])

    return FireEffect(segment, colors, height, flare_chance, flare_brightness, center_bias)
