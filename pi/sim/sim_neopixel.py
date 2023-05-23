import adafruit_pixelbuf
import tkinter as tk

try:
    from typing import Optional, Type
    from types import TracebackType
except ImportError:
    pass

class NeoPixel(adafruit_pixelbuf.PixelBuf):
    def __init__(self, pin, n: int, *, bpp: int = 3, brightness: float = 1.0, auto_write: bool = True, pixel_order: str = "RGB", is_panel = False, width = 1, alternating = False):
        super().__init__(n, brightness=brightness, byteorder=pixel_order, auto_write=auto_write)
        self._is_panel = is_panel
        self._width = width
        self._alternating = alternating
        tk_width = 800
        tk_height = 800
        self._square_w = int(tk_width / (n if not self._is_panel else self._width))
        if not self._is_panel:
            tk_height = self._square_w
        self._tk_root = tk.Tk()
        self._tk_root.geometry(f"{tk_width}x{tk_height}")
        self._tk_root.title("NeoPixel Sim")
        self._canvas = tk.Canvas(self._tk_root, width=800, height=800, bg='white')
        self._canvas.pack(anchor=tk.CENTER, expand=True)
        self._tk_root.update()

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
        self._canvas.delete("all")
        length = len(buffer) // 3
        for i in range(0, len(buffer), 3):
            start_x = self._square_w * (i // 3 if not self._is_panel else i // 3 % self._width)
            start_y = self._square_w * (0 if not self._is_panel else i // (3 * (length // self._width)))
            if self._alternating and (start_y // self._square_w) % 2 == 1:
                start_x = (self._width - 1) * self._square_w - start_x - 1
            self._canvas.create_rectangle((start_x, start_y), (start_x + self._square_w + 1, start_y + self._square_w + 1), fill="#%02x%02x%02x" % (buffer[i], buffer[i + 1], buffer[i + 2]))

        self._tk_root.update()

        # s = ""
        # for i in range(0, len(self._post_brightness_buffer), 3):
        #     r = self._post_brightness_buffer[i]
        #     g = self._post_brightness_buffer[i + 1]
        #     b = self._post_brightness_buffer[i + 2]
        #     s += "\033[48;2;%s;%s;%sm" % (r, g, b) + ("{:<" + str(max_w) + "}").format(i // 3) + "\033[0m "
        # print(s, end="\r")
