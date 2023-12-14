from lights.led_device import LEDDevice
from util.color import RED
from effects.breathe import BreatheEffect


class NotConnectedEffect(BreatheEffect):
    def __init__(self, device: LEDDevice):
        super().__init__(device, RED, 0.5)
