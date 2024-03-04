from lights.led_panel import LEDPanel
from lights.led_segment import LEDSegment
from adafruit_pixel_framebuf import PixelFramebuffer
from util.color import Color

class LEDPanelSegment(LEDSegment):
    _width: int
    _height: int
    _top_left: tuple[int, int]
    _bottom_right: tuple[int, int]
    def __init__(self, name: str, device: LEDPanel, top_left: tuple[int, int], bottom_right: tuple[int, int]):
        if bottom_right[0] <= top_left[0]:
            raise Exception("Right x must be greater than left x.")
        if bottom_right[1] <= top_left[1]:
            raise Exception("Bottom y must be greater than top y.")

        self._top_left = top_left
        self._bottom_right = bottom_right

        self._width = bottom_right[0] - top_left[0]
        self._height = bottom_right[1] - top_left[1]
        self._length = self._width * self._height

        ranges = []
        for y in range(top_left[1], bottom_right[1]):
            row_idx = y * self._height
            idx1 = row_idx + top_left[0]
            idx2 = row_idx + bottom_right[0]
            ranges.append((idx1, idx2))

        super().__init__(name, device, ranges)

        self._should_reverse = device.get_alternating() and top_left[0] // self._width % 2 == 1
        self._buffer = PixelFramebuffer(device.get_neopixel(), device.get_width(), device.get_height(), alternating=device.get_alternating(), top=top_left, bottom=bottom_right)

    def get_buffer(self):
        return self._buffer

    def transform_index(self, i: int):
        # un-reverse on reversed rows on alternating devices
        if self._should_reverse:
            i = i - 2 * (i % self._width) + self._width - 1

        return i

    def set_index(self, i: int, color: Color):
        i = self.transform_index(i)

        x, y = i % self._width, i // self._width
        if y >= self._height:
            return # TODO should raise exception?

        self.get_buffer().pixel(x, y, color.to_tuple())

    def fill(self, color: Color, fill_from: tuple[int, int] = (0, 0), fill_to: tuple[int, int] = (-1, -1)):
        from_x, from_y = fill_from
        to_x, to_y = fill_to
        if to_x == -1:
            to_x = self._width - 1
        if to_y == -1:
            to_y = self._height - 1

        for y in range(from_y, to_y + 1):
            for x in range(from_x, to_x + 1):
                self.get_buffer().pixel(x, y, color.to_tuple())
