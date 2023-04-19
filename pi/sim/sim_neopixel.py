import adafruit_pixelbuf

try:
    from typing import Optional, Type
    from types import TracebackType
except ImportError:
    pass

class NeoPixel(adafruit_pixelbuf.PixelBuf):
    def __init__(self, pin, n: int, *, bpp: int = 3, brightness: float = 1.0, auto_write: bool = True, pixel_order: str = "RGB"):
        super().__init__(n, brightness=brightness, byteorder=pixel_order, auto_write=auto_write)

    def deinit(self):
        self.fill(0)
        self.show()
        pass

    def __enter__(self):
        return self

    def __exit__(
            self,
            exception_type: Optional[Type[BaseException]],
            exception_value: Optional[BaseException],
            traceback: Optional[TracebackType]
    ):
        self.deinit()

    def __repr__(self):
        return "[" + ", ".join([str(x) for x in self]) + "]"

    @property
    def n(self) -> int:
        return len(self)

    def write(self) -> None:
        self.show()

    def _transmit(self, buffer: bytearray):
        s = ""
        max_w = len(str(len(self._post_brightness_buffer) // 3))
        for i in range(0, len(self._post_brightness_buffer), 3):
            r = self._post_brightness_buffer[i]
            g = self._post_brightness_buffer[i + 1]
            b = self._post_brightness_buffer[i + 2]
            s += "\033[48;2;%s;%s;%sm" % (r, g, b) + ("{:<" + str(max_w) + "}").format(i // 3) + "\033[0m "
        print(s, end="\r")
