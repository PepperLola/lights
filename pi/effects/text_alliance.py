from lights.led_panel_segment import LEDPanelSegment
from networktables import NetworkTable
from effects.led_effect import LEDEffect
from lights.led_segment import LEDSegment
from lights.led_panel import LEDPanel
from util.color import Color, blend, BLACK, RED, BLUE, from_int
from constants import SECONDS_PER_TICK
import math

class TextAllianceEffect(LEDEffect):
    _text: str
    _led_panel_segment: LEDPanelSegment

    def __init__(self, segment: LEDSegment, text: str, red_color: Color, blue_color: Color):
        super().__init__(segment, panel_only=True)
        self._led_panel_segment = segment
        self._text = text
        self._red_color = red_color
        self._blue_color = blue_color

    def get_segment(self):
        return self._led_panel_segment

    def update(self, game_info_table: NetworkTable):
        alliance = "red" if game_info_table is None else game_info_table.getEntry("alliance").getString("red")
        c = self._red_color
        if alliance == "blue":
            c = self._blue_color

        self.get_segment().fill(BLACK)
        self.get_segment().get_buffer().text(self._text, 0, 0, c.to_hex_int())
        self.get_segment().get_buffer().display()

def parse(segment: LEDSegment, data):
    text = ""
    red_color = RED
    blue_color = BLUE

    if "text" in data.keys():
        text = data["text"]

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

    return TextAllianceEffect(segment, text, red_color, blue_color)
