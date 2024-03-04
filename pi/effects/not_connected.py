from lights.led_segment import LEDSegment
from util.color import RED
from effects.breathe import BreatheEffect


class NotConnectedEffect(BreatheEffect):
    def __init__(self, segment: LEDSegment):
        super().__init__(segment, RED, 0.5)
