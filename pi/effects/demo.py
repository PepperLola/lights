from effects.animation import AnimationEffect
from effects.blink import BlinkEffect
from effects.blink_alliance import BlinkAllianceEffect
from effects.breathe import BreatheEffect
from effects.breathe_alliance import BreatheAllianceEffect
from effects.conway import ConwayEffect
from effects.cylon import CylonEffect
from effects.fire import FireEffect
from effects.morse import MorseEffect
from effects.rainbow import RainbowEffect
from effects.solid import SolidEffect
from effects.solid_alliance import SolidAllianceEffect
from effects.wave import WaveEffect
from lights.led_panel_segment import LEDPanelSegment
from lights.led_segment import LEDSegment
from effects.cycle import CycleEffect
from util.color import *

class DemoEffect(CycleEffect):
    _interval: int
    def __init__(self, segment: LEDSegment, interval: int):
        self._interval = interval

        effects = [
            BlinkEffect(segment, PURPLE, 0.5),
            BlinkAllianceEffect(segment, RED, BLUE, 0.5),
            BreatheEffect(segment, PURPLE, 0.5),
            BreatheAllianceEffect(segment, RED, BLUE, 0.5),
            CylonEffect(segment, RED, 50, 5),
            MorseEffect(segment, "PIGMICE", PURPLE, 5),
            RainbowEffect(segment, 0.01, 0.5),
            SolidEffect(segment, PURPLE),
            SolidAllianceEffect(segment, RED, BLUE),
            WaveEffect(segment, ColorRamp([(BLACK, 0), (PURPLE, 0.5), (BLACK, 1)]), 0.01, 0.5, 4)
        ]
        if isinstance(segment, LEDPanelSegment):
            effects.append(ConwayEffect(segment, PURPLE))
            effects.append(FireEffect(segment, ColorRamp([(RED, 0), (ORANGE, 0.5), (YELLOW, 0.7), (BLACK, 0.75), (BLACK, 1)]), 0.7, 0.65, 0.25, 0.2))
            effects.append(AnimationEffect(segment, "animations/bad_apple.gif", 24))
        else:
            effects.append(FireEffect(segment, ColorRamp([(RED, 0), (ORANGE, 0.5), (YELLOW, 0.7), (BLACK, 0.75), (BLACK, 1)]), 3, 0.65, 0.25, 0))
        super().__init__(segment, effects, interval)

def parse(segment: LEDSegment, data):
    interval = 15

    if "interval" in data.keys():
        interval = data["interval"]

    return DemoEffect(segment, interval)
