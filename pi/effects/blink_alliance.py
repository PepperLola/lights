from networktables import NetworkTable
from effects.led_effect import LEDEffect
from lights.led_segment import LEDSegment
from util.color import Color, blend, BLACK, RED, BLUE, from_int
from constants import SECONDS_PER_TICK
import math

from util.time import current_time_millis

class BlinkAllianceEffect(LEDEffect):
    _on: bool
    _interval: float
    _last_change: int

    def __init__(self, segment: LEDSegment, red_color: Color, blue_color: Color, interval: float):
        super().__init__(segment)
        self._red_color = red_color
        self._blue_color = blue_color
        self._interval = interval
        self._on = False

    def start(self):
        self.get_segment().fill(BLACK)
        self._last_change = current_time_millis()

    def update(self, game_info_table: NetworkTable):
        alliance = "red" if game_info_table is None else game_info_table.getEntry("alliance").getString("red")
        c = self._red_color
        if alliance == "blue":
            c = self._blue_color
        current_time = current_time_millis()
        if (current_time - self._last_change) / 1000 > self._interval:
            self._last_change = current_time
            self._on = not self._on
            if self._on:
                self.get_segment().fill(c)
            else:
                self.get_segment().fill(BLACK)

def parse(segment: LEDSegment, data):
    red_color = RED 
    blue_color = BLUE
    interval = 0.5

    if "red_color" in data.keys():
        c = data["red_color"]
        if isinstance(c, int):
            red_color = from_int(c)
        else:
            red_color = Color(c[0], c[1], c[2])

    if "blue_color" in data.keys():
        c = data["blue_color"]
        if isinstance(c, int):
            blue_color = from_int(c)
        else:
            blue_color = Color(c[0], c[1], c[2])

    if "interval" in data.keys():
        interval = data["interval"]

    return BlinkAllianceEffect(segment, red_color, blue_color, interval)
