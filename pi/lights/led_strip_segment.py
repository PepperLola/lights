from lights.led_segment import LEDSegment
from lights.led_strip import LEDStrip
from util.color import Color


class LEDStripSegment(LEDSegment):
    _range: tuple[int, int]
    def __init__(self, name: str, device: LEDStrip, index_range: tuple[int, int]):
        super().__init__(name, device, [index_range])
        self._range = index_range

    def set_index(self, i: int, color: Color):
        if i > self._length:
            return # TODO should raise exception?

        self.get_device().get_neopixel()[i + self._range[0]] = color.to_tuple()

    def fill(self, color: Color, fill_range: tuple[int, int] = (0, -1)):
        from_idx, to_idx = fill_range
        if to_idx == -1:
            to_idx = self._length

        for i in range(self._range[0] + from_idx, self._range[0] + to_idx):
            self.get_device().get_neopixel()[i] = color.to_tuple()
