from networktables import NetworkTable
from effects.led_effect import LEDEffect
from lights.led_segment import LEDSegment
from util.color import Color, blend, BLACK, PURPLE, RED, from_int
from constants import SECONDS_PER_TICK
import math
from util.time import current_time_millis

class CylonEffect(LEDEffect):
    _color: Color
    _speed: int # pixels per second
    _center_x: int
    _dist: int
    _dir: int
    _last_update: int

    def __init__(self, segment: LEDSegment, color: Color, speed: int, dist: int):
        super().__init__(segment)
        self._color = color
        self._speed = speed
        self._dist = dist

    def start(self):
        self._center_x = 0
        self._dir = 1
        self._last_update = current_time_millis()

    def update(self, game_info_table: NetworkTable):
        current_time = current_time_millis()
        if (current_time - self._last_update) / 1000 > 1.0 / self._speed:
            self._last_update = current_time
            self.get_segment().fill(BLACK)
            for x in range(max(0, self._center_x - self._dist), min(self.get_segment().get_length(), self._center_x + self._dist)):
                self.get_segment().set_index(x, blend(self._color, BLACK, (abs(self._center_x - x) / self._dist)))
            if self._center_x + self._dir >= self.get_segment().get_length() or self._center_x + self._dir < 0:
                self._dir = -self._dir
            self._center_x += self._dir

def parse(segment: LEDSegment, data):
    color = RED
    speed = 32
    dist = 8

    if "color" in data.keys():
        c = data["color"]
        if isinstance(c, int):
            color = from_int(c)
        else:
            color = Color(c[0], c[1], c[2])

    if "speed" in data.keys() and isinstance(data["speed"], int):
        speed = int(data["speed"])

    if "dist" in data.keys() and isinstance(data["dist"], int):
        dist = int(data["dist"])

    return CylonEffect(segment, color, speed, dist)
