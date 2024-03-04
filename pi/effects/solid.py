from effects.led_effect import LEDEffect
from util.color import Color, BLACK, PURPLE, from_int
from lights.led_segment import LEDSegment

class SolidEffect(LEDEffect):
    _color: Color = BLACK

    def __init__(self, segment: LEDSegment, color: Color):
        super().__init__(segment)
        self._color = color

    def start(self):
        self.get_segment().fill(self._color)

def parse(segment: LEDSegment, data):
    color = PURPLE
    if "color" in data.keys():
        c = data["color"]
        if isinstance(c, int):
            color = from_int(c)
        else:
            color = Color(c[0], c[1], c[2])

    return SolidEffect(segment, color)
