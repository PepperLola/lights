from effects.led_effect import LEDEffect
from lights.led_device import LEDDevice
from util.color import Color, blend, BLACK, PURPLE, from_int
from constants import SECONDS_PER_TICK
import math

class TextEffect(LEDEffect):
    _text: str

    def __init__(self, device: LEDDevice, text: str, color: Color):
        super().__init__(device, panel_only=True)
        self._text = text
        self._color = color

    def start(self):
        self.get_device().get_neopixel().fill(BLACK.to_tuple())
        self.get_device().get_buffer().text(self._text, 0, 0, self._color.to_hex_int())
        self.get_device().get_buffer().display()

    def update(self):
        pass

def parse(device: LEDDevice, data):
    text = ""
    color = PURPLE

    if "text" in data.keys():
        text = data["text"]

    if "color" in data.keys():
        c = data["color"]
        if isinstance(c, int):
            color = from_int(c)
        else:
            color = Color(c[0], c[1], c[2])

    return TextEffect(device, text, color)
