from networktables import NetworkTable
from effects.led_effect import LEDEffect
from lights.led_device import LEDDevice
from util.color import Color, blend, BLACK, PURPLE, from_int
from constants import SECONDS_PER_TICK
import math

from util.time import current_time_millis

class TextEffect(LEDEffect):
    _last_update: int
    _text: str
    _color: Color
    _scroll_speed: int # pixels per second
    _x: int
    _y: int
    _x_offset: int
    _loop: bool
    _text_width: int

    def __init__(self, device: LEDDevice, text: str, x: int, y: int, color: Color, scroll_speed: int = 0, loop: bool = True):
        super().__init__(device, panel_only=True)
        self._text = text
        self._x = x
        self._y = y
        self._color = color
        self._scroll_speed = scroll_speed
        self._loop = loop
        self._text_width = 6 * len(self._text) - 1

    def render_text(self):
        self.get_device().get_buffer().fill(BLACK.to_hex_int())
        self.get_device().get_buffer().text(self._text, self._x - self._x_offset, self._y, self._color.to_hex_int())
        self.get_device().get_buffer().display()

    def start(self):
        self._x_offset = 0
        self.render_text()
        self._last_update = current_time_millis()

    def update(self, game_info_table: NetworkTable):
        if self._scroll_speed > 0:
            current_time = current_time_millis()
            if (current_time - self._last_update) / 1000 > 1 / self._scroll_speed:
                self._last_update = current_time
                self._x_offset += 1
                if self._loop and self._x_offset > self._x + self._text_width:
                    # set x to 0 to keep looping, since original doesn't matter
                    self._x = 0
                    self._x_offset = -self.get_device().get_width()
                self.render_text()
        else:
            return

def parse(device: LEDDevice, data):
    x = 0
    y = 0
    text = ""
    color = PURPLE
    scroll_speed = 0
    loop = True

    if "x" in data.keys() and isinstance(data['x'], int):
        x = int(data['x'])

    if "y" in data.keys() and isinstance(data['y'], int):
        y = int(data['y'])

    if "text" in data.keys():
        text = data["text"]

    if "color" in data.keys():
        c = data["color"]
        if isinstance(c, int):
            color = from_int(c)
        else:
            color = Color(c[0], c[1], c[2])

    if "scroll_speed" in data.keys():
        if isinstance(data['scroll_speed'], int):
            scroll_speed = int(data['scroll_speed'])

    if "loop" in data.keys():
        if isinstance(data['loop'], bool):
            loop = bool(data['loop'])

    return TextEffect(device, text, x, y, color, scroll_speed=scroll_speed, loop=loop)
