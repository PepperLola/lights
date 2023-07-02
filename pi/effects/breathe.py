from effects.led_effect import LEDEffect
from lights.led_device import LEDDevice
from util.color import Color, blend, BLACK, PURPLE, from_int
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

def parse(device: LEDDevice, data):
    color = PURPLE
    speed = 0.5

    if "color" in data.keys():
        c = data["color"]
        if isinstance(c, int):
            color = from_int(c)
        else:
            color = Color(c[0], c[1], c[2])

    if "speed" in data.keys():
        speed = data["speed"]

    return BreatheEffect(device, color, speed)
