from lights.led_panel_segment import LEDPanelSegment
from lights.led_strip_segment import LEDStripSegment
from networktables import NetworkTable
from effects.led_effect import LEDEffect
from util.color import GREEN, INDIGO, VIOLET, Color, ColorRamp, blend, BLACK, RED, ORANGE, YELLOW, BLUE, PURPLE, WHITE, from_color_array, from_int
from lights.led_segment import LEDSegment
from constants import SECONDS_PER_TICK, TPS

class WaveEffect(LEDEffect):
    _len: int
    _offset: float = 0
    _colors: ColorRamp

    def __init__(self, segment: LEDSegment, colors: ColorRamp, increment: float, speed: float):
        self._segment = segment
        self._colors = colors
        self._increment = increment
        self._speed = speed
        self._len = self.get_segment().get_length()

    def start(self):
        for i in range(self._len):
            color = self._colors.get_color(i / self._len)
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
            color = self._colors.get_color((self._offset + i / self._len) % 1)
            self.get_segment().set_index(i, color)
        self._offset += self._speed * SECONDS_PER_TICK
        self._offset %= 1

def parse(segment: LEDSegment, data):
    increment = 0.01
    speed = 0.5
    colors = ColorRamp([(RED, 0), (ORANGE, 0.14), (YELLOW, 0.29), (GREEN, 0.42), (BLUE, 0.57), (INDIGO, 0.71), (VIOLET, 0.85), (RED, 1)])

    if "colors" in data.keys():
        c = data["colors"]
        colors = from_color_array(c)

    if "increment" in data.keys():
        increment = data["increment"]

    if "speed" in data.keys():
        speed = data["speed"]

    return WaveEffect(segment, colors, increment, speed)
