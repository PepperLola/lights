from effects.text import TextEffect
from lights.led_panel_segment import LEDPanelSegment
from networktables import NetworkTable
from effects.led_effect import LEDEffect
from lights.led_segment import LEDSegment
from lights.led_panel import LEDPanel
from util.color import Color, blend, BLACK, RED, BLUE, from_int
from constants import SECONDS_PER_TICK
import math

class TextAllianceEffect(TextEffect):
    _red_color: Color
    _blue_color: Color

    def __init__(self, segment: LEDSegment, text: str, x: int, y: int, red_color: Color, blue_color: Color, scroll_speed: int = 0, loop: bool = True):
        super().__init__(segment, text, x, y, red_color, scroll_speed, loop)
        self._red_color = red_color
        self._blue_color = blue_color

    def get_color(self, game_info_table: NetworkTable):
        alliance = "red" if game_info_table is None else game_info_table.getEntry("alliance").getString("red")
        c = self._red_color
        if alliance == "blue":
            c = self._blue_color

        return c

def parse(segment: LEDSegment, data):
    x = 0
    y = 0
    text = ""
    red_color = RED
    blue_color = BLUE
    scroll_speed = 0
    loop = True

    if "x" in data.keys() and isinstance(data['x'], int):
        x = int(data['x'])

    if "y" in data.keys() and isinstance(data['y'], int):
        y = int(data['y'])

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

    if "scroll_speed" in data.keys():
        if isinstance(data['scroll_speed'], int):
            scroll_speed = int(data['scroll_speed'])

    if "loop" in data.keys():
        if isinstance(data['loop'], bool):
            loop = bool(data['loop'])

    return TextAllianceEffect(segment, text, x, y, red_color, blue_color, scroll_speed, loop)
