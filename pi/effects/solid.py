from effects.led_effect import LEDEffect
from util.color import Color, BLACK, PURPLE
from lights.led_device import LEDDevice

class SolidEffect(LEDEffect):
    _color: Color = BLACK

    def __init__(self, device: LEDDevice, color: Color):
        super().__init__(device)
        self._color = color

    def start(self):
        self.get_device().get_neopixel().fill(self._color.to_tuple())

def parse(device: LEDDevice, data):
    color = PURPLE
    if "color" in data.keys():
        c = data["color"]
        color = Color(c[0], c[1], c[2])

    return SolidEffect(device, color)
