from networktables import NetworkTable
from effects.led_effect import LEDEffect
from util.color import Color, RED, BLUE, from_int
from lights.led_segment import LEDSegment

class SolidAllianceEffect(LEDEffect):
    _red_color: Color = RED 
    _blue_color: Color = BLUE

    def __init__(self, segment: LEDSegment, red_color: Color, blue_color: Color):
        super().__init__(segment)
        self._red_color = red_color
        self._blue_color = blue_color

    def update(self, game_info_table: NetworkTable):
        alliance = "red" if game_info_table is None else game_info_table.getEntry("alliance").getString("red")
        c = self._red_color
        if alliance == "blue":
            c = self._blue_color
        self.get_segment().fill(c)

def parse(segment: LEDSegment, data):
    red_color = RED 
    blue_color = BLUE

    if "red_color" in data.keys():
        c = data["red_color"]
        if isinstance(c, int):
            red_color = from_int(c)
        else:
            red_color = Color(c[0], c[1], c[2])

    if "blue_color" in data.keys():
        c = data["blue_color"]
        if isinstance(c, int):
            blue_color = from_int(c)
        else:
            blue_color = Color(c[0], c[1], c[2])

    return SolidAllianceEffect(segment, red_color, blue_color)
