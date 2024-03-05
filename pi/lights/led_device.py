from lights.led_segment import LEDSegment
import sim.sim_neopixel

class LEDDevice:
    _name: str = ""
    _port: int = 0
    _length: int = 0
    _is_panel: bool = False
    _width: int = 1
    _height: int
    _alternating: bool
    _segments: dict[str, LEDSegment]

    def __init__(self, name, port, length, led_manager, is_sim = False, is_panel = False, width = 1, alternating = True, segments: dict[str, LEDSegment] = {}):
        self._name = name
        self._port = port
        self._length = length
        self._led_manager = led_manager
        self._is_panel = is_panel
        self._width = width
        self._height = length // width
        self._alternating = alternating
        self._segments = segments

        if not is_sim:
            try:
                import board
                pins = [board.D10, board.D12, board.D18, board.D21]
                import neopixel
                self._neopixel = neopixel.NeoPixel(pins[port], length, brightness=1.0, auto_write=False)
            except:
                self._neopixel = sim.sim_neopixel.NeoPixel(port, length, brightness=1.0, auto_write=False, is_panel=self._is_panel, width=self._width, alternating=alternating)
        else:
            self._neopixel = sim.sim_neopixel.NeoPixel(port, length, brightness=1.0, auto_write=False, is_panel=self._is_panel, width=self._width, alternating=alternating)

    def on_register(self):
        pass

    def on_unregister(self):
        self.get_neopixel().fill((0, 0, 0))

    def get_name(self):
        return self._name

    def get_port(self):
        return self._port

    def get_length(self):
        return self._length

    def get_led_manager(self):
        return self._led_manager

    def get_neopixel(self):
        return self._neopixel

    def is_panel(self):
        return self._is_panel

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_alternating(self):
        return self._alternating

    def get_segments(self):
        return self._segments

    def add_segment(self, segment: LEDSegment):
        self._segments[segment.get_name()] = segment
