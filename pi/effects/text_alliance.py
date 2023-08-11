from networktables import NetworkTable
from effects.led_effect import LEDEffect
from lights.led_device import LEDDevice
from lights.led_panel import LEDPanel
from util.color import Color, blend, BLACK, RED, BLUE, from_int
from constants import SECONDS_PER_TICK
import math

class TextAllianceEffect(LEDEffect):
    _text: str

    def __init__(self, device: LEDDevice, text: str, red_color: Color, blue_color: Color):
        super().__init__(device, panel_only=True)
        self._text = text
        self._red_color = red_color
        self._blue_color = blue_color

    def update(self, game_info_table: NetworkTable):
        alliance = "red" if game_info_table is None else game_info_table.getEntry("alliance").getString("red")
        c = self._red_color
        if alliance == "blue":
            c = self._blue_color

        self.get_device().get_neopixel().fill(BLACK.to_tuple())
        self.get_device().get_buffer().text(self._text, 0, 0, c.to_hex_int())
        self.get_device().get_buffer().display()

def parse(device: LEDDevice, data):
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

    return TextAllianceEffect(device, text, red_color, blue_color)
