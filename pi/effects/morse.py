from networktables import NetworkTable
from effects.led_effect import LEDEffect
from lights.led_segment import LEDSegment
from util.color import Color, blend, BLACK, PURPLE, from_int
from constants import SECONDS_PER_TICK
import math
import time

from util.morse import to_morse, get_pauses
from util.time import current_time_millis

class MorseEffect(LEDEffect):
    _last_change: int
    _pauses: list[tuple[bool, int]]
    _pause_length: float
    _pause_idx: int
    _current_pause: tuple[bool, int]

    def __init__(self, segment: LEDSegment, text: str, color: Color, wpm: int):
        super().__init__(segment)
        self._color = color
        self._pause_length = 60.0 / (50.0 * wpm)
        self._pauses = get_pauses(to_morse(text))
        self._pause_idx = 0

    def start(self):
        self._last_change = current_time_millis()
        self._current_pause = self._pauses[self._pause_idx]
        if self._current_pause[0]:
            self.get_segment().fill(self._color)
        else:
            self.get_segment().fill(BLACK)

    def update(self, game_info_table: NetworkTable):
        current_time = current_time_millis()
        if (current_time - self._last_change) / 1000 > (self._pause_length * self._current_pause[1]):
            self._last_change = current_time
            self._pause_idx += 1
            self._pause_idx %= len(self._pauses)

            self._current_pause = self._pauses[self._pause_idx]
            if self._current_pause[0]:
                self.get_segment().fill(self._color)
            else:
                self.get_segment().fill(BLACK)

def parse(segment: LEDSegment, data):
    text = "PIGMICE"
    color = PURPLE
    wpm = 5

    if "text" in data.keys():
        text = data['text']

    if "color" in data.keys():
        c = data["color"]
        if isinstance(c, int):
            color = from_int(c)
        else:
            color = Color(c[0], c[1], c[2])

    if "wpm" in data.keys():
        wpm = data["wpm"]

    return MorseEffect(segment, text, color, wpm)
