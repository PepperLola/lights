from networktables import NetworkTable
from effects.led_effect import LEDEffect
from util.color import Color, BLACK, PURPLE, ColorRamp, from_color_array, from_int
from lights.led_segment import LEDSegment

class SolidEffect(LEDEffect):
    _colors: ColorRamp | Color = BLACK
    _is_ramp: bool

    def __init__(self, segment: LEDSegment, color: Color | ColorRamp):
        super().__init__(segment)
        self._colors = color
        self._is_ramp = isinstance(color, ColorRamp)

    def start(self):
        if not self._is_ramp:
            self.get_segment().fill(self._colors)

    def update(self, game_info_table: NetworkTable):
        if self._is_ramp:
            n = self.get_segment().get_length()
            for i in range(n):
                self.get_segment().set_index(i, self._colors.get_color(i / n))

def parse(segment: LEDSegment, data):
    color = PURPLE
    if "color" in data.keys():
        c = data["color"]
        if isinstance(c, int):
            color = from_int(c)
        elif isinstance(c, list):
            if len(c) > 0:
                if isinstance(c[0], list):
                    color = from_color_array(c)
                else:
                    color = Color(c[0], c[1], c[2])
        else:
            color = Color(c[0], c[1], c[2])

    return SolidEffect(segment, color)
