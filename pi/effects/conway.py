from networktables import NetworkTable
from effects.led_effect import LEDEffect
from lights.led_device import LEDDevice
from util.color import Color, blend, BLACK, PURPLE, from_int
from constants import SECONDS_PER_TICK
import math
import copy
import random
import time

class ConwayEffect(LEDEffect):
    _color: Color
    _buf: list[list[int]]

    def __init__(self, device: LEDDevice, color, fullness=0.5, initial_pattern=None):
        super().__init__(device, panel_only=True)
        self._color = color
        if initial_pattern is not None:
            self._buf = initial_pattern
        else:
            self._buf = [[1 if random.random() > fullness else 0 for _ in range(self._device.get_width())] for _ in range(self._device.get_width())]
            print(self._buf)

    def start(self):
        w, h = len(self._buf[0]), len(self._buf)
        for y in range(h):
            for x in range(w):
                self._device.get_buffer().pixel(x, y, self._color.to_hex_int() if self._buf[y][x] else 0x000000)
        self._device.get_buffer().display()

    def update(self, game_info_table: NetworkTable):
        new_buf = copy.deepcopy(self._buf)
        w, h = len(self._buf[0]), len(self._buf)
        for y in range(h):
            for x in range(w):
                neighbors = 0
                if x > 0:
                    neighbors += self._buf[y][x-1]
                    if y > 0:
                        neighbors += self._buf[y-1][x-1]
                    if y < h - 1:
                        neighbors += self._buf[y+1][x-1]
                if y > 0:
                    neighbors += self._buf[y-1][x]
                if x < w - 1:
                    neighbors += self._buf[y][x+1]
                    if y < h - 1:
                        neighbors += self._buf[y+1][x+1]
                    if y > 0:
                        neighbors += self._buf[y-1][x+1]
                if y < h - 1:
                    neighbors += self._buf[y+1][x]

                if neighbors == 3:
                    new_buf[y][x] = 1
                elif neighbors != 2:
                    new_buf[y][x] = 0

                self._device.get_buffer().pixel(x, y, self._color.to_hex_int() if new_buf[y][x] else 0x000000)
        self._device.get_buffer().display()

        self._buf = new_buf

def parse(device: LEDDevice, data):
    color = PURPLE
    initial_pattern = None
    fullness = 0.5

    if "initial_pattern" in data.keys():
        initial_pattern = data['initial_pattern']

    if "fullness" in data.keys():
        fullness = data['fullness']

    if "color" in data.keys():
        c = data["color"]
        if isinstance(c, int):
            color = from_int(c)
        else:
            color = Color(c[0], c[1], c[2])

    return ConwayEffect(device, color, fullness=fullness, initial_pattern=initial_pattern)
