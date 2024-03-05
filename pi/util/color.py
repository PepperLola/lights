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
        self._colors = sorted(colors, key=lambda c: c[1], reverse=False)

    def binary_search_lower_color(self, t: float, lower=0, upper=-1) -> int:
        if upper == -1:
            upper = len(self._colors) - 1
        if lower >= upper:
            return -1
        mid = (upper - lower) // 2 + lower
        if self._colors[mid][1] == t:
            return mid
        elif self._colors[mid][1] <=t <= self._colors[mid+1][1]:
            return mid
        elif self._colors[mid][1] < t:
            return self.binary_search_lower_color(t, mid, upper)
        else:
            return self.binary_search_lower_color(t, lower, mid)

    def get_color(self, t: float):
        if t <= 0:
            return self._colors[0][0]
        elif t >= 1:
            return self._colors[len(self._colors) - 1][0]

        lower_color_idx: int = self.binary_search_lower_color(t)

        if lower_color_idx == -1:
            return self._colors[0][0] # what should this be?

        if lower_color_idx == len(self._colors) - 1:
            return self._colors[lower_color_idx][0]

        (color_from, pos_from) = self._colors[lower_color_idx]
        (color_to, pos_to) = self._colors[lower_color_idx+1]

        return blend(color_from, color_to, (t - pos_from) / (pos_to - pos_from))

    def get_colors(self) -> list[tuple[Color, float]]:
        return self._colors

def from_color_array(arr: list) -> ColorRamp:
    cl = []
    for (color, pos) in arr:
        print(color)
        if isinstance(color, tuple) or isinstance(color, list):
            cl.append((Color(color[0], color[1], color[2]), pos))
        elif isinstance(color, int):
            cl.append((from_int(color), pos))

    return ColorRamp(cl)

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
INDIGO = Color(75, 0, 130)
VIOLET = Color(148, 0, 211)
PURPLE = Color(75, 48, 71)
