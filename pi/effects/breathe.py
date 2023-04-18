from effects.led_effect import LEDEffect
from lights.led_device import LEDDevice
from util.color import Color, blend, BLACK
from constants import SECONDS_PER_TICK
import math

class BreatheEffect(LEDEffect):
    _intensity: float = 0
    _2pi: float = 2 * math.pi

    def __init__(self, device: LEDDevice, color: Color, speed: float):
        super().__init__(device)
        self._color = color
        self._speed = speed
        self._increment = self._2pi * (speed * SECONDS_PER_TICK)

    def start(self):
        self.get_device().get_neopixel().fill(BLACK.to_tuple())

    def update(self):
        self._intensity += self._increment
        self._intensity %= self._2pi
        self.get_device().get_neopixel().fill(blend(BLACK, self._color, (-math.cos(self._intensity) + 1) / 2).to_tuple())
