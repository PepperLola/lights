from colorsys import hsv_to_rgb

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
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
PURPLE = Color(75, 48, 71)
