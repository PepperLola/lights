from util.color import Color

class LEDSegment:
    _name: str
    _ranges: list[tuple[int, int]]
    _length: int
    _height: int
    _width: int = 1

    def __init__(self, name: str, device, ranges: list[tuple[int, int]]):
        self._name = name
        self._device = device

        # TODO find a better solution
        for r in ranges:
            if r[1] <= r[0]:
                raise Exception("Second index must be greater than first.")
            if r[0] < 0 or r[1] < 0:
                raise Exception("Both indices must be greater than zero.")
            if r[1] > device.get_length():
                raise Exception("Range must fit on LED strip.")

        self._ranges = ranges
        self._length = sum(map(lambda r: r[1] - r[0], ranges))

    def get_name(self):
        return self._name

    def get_device(self):
        return self._device

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def set_index(self, i: int, color: Color):
        pass # implement in subclasses

    def fill(self, color: Color):
        pass # implement in subclasses
