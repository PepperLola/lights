from networktables import NetworkTable
from effects.led_effect import LEDEffect
from lights.led_segment import LEDSegment
from util.color import Color, blend, BLACK, PURPLE, from_int
from constants import SECONDS_PER_TICK
import math

class BreatheEffect(LEDEffect):
    _intensity: float = 0
    _2pi: float = 2 * math.pi

    def __init__(self, segment: LEDSegment, color: Color, speed: float):
        super().__init__(segment)
        self._color = color
        self._speed = speed
        self._increment = self._2pi * (speed * SECONDS_PER_TICK)

    def start(self):
        self.get_segment().fill(BLACK)

    def update(self, game_info_table: NetworkTable):
        self._intensity += self._increment
        self._intensity %= self._2pi
        self.get_segment().fill(blend(BLACK, self._color, (-math.cos(self._intensity) + 1) / 2))

def parse(segment: LEDSegment, data):
    color = PURPLE
    speed = 0.5

    if "color" in data.keys():
        c = data["color"]
        if isinstance(c, int):
            color = from_int(c)
        else:
            color = Color(c[0], c[1], c[2])

    if "speed" in data.keys():
        speed = data["speed"]

    return BreatheEffect(segment, color, speed)
