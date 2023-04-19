from effects.led_effect import LEDEffect
from util.color import Color, BLACK, hsv
from lights.led_device import LEDDevice
from constants import SECONDS_PER_TICK, TPS

class RainbowEffect(LEDEffect):
    _len: int
    _offset: float = 0
    def __init__(self, device: LEDDevice, increment: float, speed: float):
        self._device = device
        self._increment = increment
        self._speed = speed
        self._len = self.get_device().get_length()

    def start(self):
        for i in range(self._len):
            hue = (int((i / self._len) * 180) % 180 / 180)
            color = hsv(hue, 1, 1).to_tuple()
            self.get_device().get_neopixel()[i] = color

    def update(self):
        for i in range(self._len):
            hue = ((self._offset + int((i / self._len) * 180)) % 180) / 180
            color = hsv(hue, 1, 1).to_tuple()
            self.get_device().get_neopixel()[i] = color
        self._offset += 180 * self._speed * SECONDS_PER_TICK
        self._offset %= 180
