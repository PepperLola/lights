from effects.led_effect import LEDEffect
from util.color import Color, BLACK
from lights.led_device import LEDDevice

class SolidEffect(LEDEffect):
    _color: Color = BLACK

    def __init__(self, device: LEDDevice, color: Color):
        super().__init__(device)
        self._color = color

    def start(self):
        self.get_device().get_neopixel().fill(self._color.to_tuple())
