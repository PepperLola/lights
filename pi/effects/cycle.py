from networktables import NetworkTable
from effects.led_effect import LEDEffect
from lights.led_segment import LEDSegment
from util.color import Color, blend, BLACK, PURPLE, from_int
from constants import SECONDS_PER_TICK
import math
import time

from util.time import current_time_millis

class CycleEffect(LEDEffect):
    _effects: list[LEDEffect]
    _interval: int
    _index: int

    def __init__(self, segment: LEDSegment, effects: list[LEDEffect], interval: int):
        super().__init__(segment)
        # disallow CycleEffect within CycleEffect?
        self._effects = effects
        self._interval = interval

    def start(self):
        self.get_segment().fill(BLACK)
        self._last_change = current_time_millis()
        self._index = 0
        self._effects[self._index].start()

    def update(self, game_info_table: NetworkTable):
        current_time = current_time_millis()
        self._effects[self._index].update(game_info_table)

        if (current_time - self._last_change) / 1000 > self._interval:
            self._last_change = current_time
            self._index += 1
            self._index %= len(self._effects)
            self._effects[self._index].start()


def parse(segment: LEDSegment, data):
    effects: list[LEDEffect] = []
    interval = 15

    if "interval" in data.keys():
        interval = data["interval"]

    if "effects" in data.keys():
        parsed = []
        for data in data["effects"]:
            parsed.append(segment.get_device().get_led_manager().parse_led_effect(segment, data))
        if isinstance(parsed, list):
            effects = parsed

    return CycleEffect(segment, effects, interval)
