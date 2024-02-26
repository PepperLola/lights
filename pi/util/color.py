from colorsys import hsv_to_rgb
import itertools

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def to_tuple(self):
        return (self.r, self.g, self.b)

    def to_hex(self):
        return "#%02x%02x%02x" % self.to_tuple()

    def to_hex_int(self):
        return self.r << 16 | self.g << 8 | self.b

class ColorRamp:
    _colors: list[tuple[Color, float]]

    def __init__(self, colors: list[tuple[Color, float]]):
        self._colors = colors

    def get_color(self, t: float):
        if t <= 0:
            return sorted(self._colors, key=lambda c: c[1], reverse=False)[0][0]
        elif t >= 1:
            return sorted(self._colors, key=lambda c: c[1], reverse=True)[0][0]
        color_from = None
        color_to = None
        from_pos = 0
        to_pos = 0
        for ((color1, pos1), (color2, pos2)) in itertools.pairwise(self._colors):
            if pos1 <= t <= pos2:
                color_from = color1
                color_to = color2
                from_pos = pos1
                to_pos = pos2
                break

        return blend(color_from, color_to, (t - from_pos) / (to_pos - from_pos))

    def get_colors(self) -> list[tuple[Color, float]]:
        return self._colors

def from_int(c):
    b = c & 255
    g = (c >> 8) & 255
    r = (c >> 16) & 255
    return Color(r, g, b)

def hsv(h, s, v):
    color = hsv_to_rgb(h, s, v)
    return Color(int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))

def _lerp(a, b, t):
    return a + (b - a) * t

def blend(color1, color2, t):
    r = _lerp(color1.r, color2.r, t)
    g = _lerp(color1.g, color2.g, t)
    b = _lerp(color1.b, color2.b, t)
    return Color(int(r), int(g), int(b))

BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
ORANGE = Color(255, 165, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
PURPLE = Color(75, 48, 71)
