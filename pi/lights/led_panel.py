from lights.led_device import LEDDevice
from adafruit_pixel_framebuf import PixelFramebuffer

class LEDPanel(LEDDevice):
    _width: int = 0
    _height: int = 0
    _buffer: PixelFramebuffer
    def __init__(self, name, port, width, height, is_sim=False):
        super().__init__(name, port, height * width, is_sim=is_sim)
        self._width = width
        self._height = height
        self._buffer = PixelFramebuffer(super().get_device(), width, height)

    def get_buffer(self):
        return self._buffer
