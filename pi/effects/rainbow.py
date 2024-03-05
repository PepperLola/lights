from lights.led_panel_segment import LEDPanelSegment
from lights.led_strip_segment import LEDStripSegment
from networktables import NetworkTable
from effects.led_effect import LEDEffect
from util.color import Color, BLACK, hsv
from lights.led_segment import LEDSegment
from constants import SECONDS_PER_TICK, TPS

class RainbowEffect(LEDEffect):
    _len: int
    _offset: float = 0
    def __init__(self, segment: LEDSegment, increment: float, speed: float):
        self._segment = segment
        self._increment = increment
        self._speed = speed
        self._len = self.get_segment().get_length()

    def start(self):
        for i in range(self._len):
            hue = (int((i / self._len) * 180) % 180 / 180)
            color = hsv(hue, 1, 1)
            self.get_segment().set_index(i, color)

    def get_hue(self, i: int) -> float:
        segment = self.get_segment()
        if isinstance(segment, LEDPanelSegment):
            led_panel_segment: LEDPanelSegment = segment
            w, h = led_panel_segment.get_width(), led_panel_segment.get_height()
            x, y = i % w, i // h
            return (self._offset + int(((x + y) / (w + h) * 180)) % 180) / 180
        else:
            return ((self._offset + int((i / self._len) * 180)) % 180) / 180

    def update(self, game_info_table: NetworkTable):
        for i in range(self._len):
            hue = self.get_hue(i)
            color = hsv(hue, 1, 1)
            self.get_segment().set_index(i, color)
        self._offset += 180 * self._speed * SECONDS_PER_TICK
        self._offset %= 180

def parse(segment: LEDSegment, data):
    increment = 0.01
    speed = 0.5
    if "increment" in data.keys():
        increment = data["increment"]

    if "speed" in data.keys():
        speed = data["speed"]

    return RainbowEffect(segment, increment, speed)
