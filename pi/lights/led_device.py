import sim.sim_neopixel

class LEDDevice:
    _name = ""
    _port = 0
    _length = 0
    _is_panel = False
    _width = 1
    def __init__(self, name, port, length, is_sim = False, is_panel = False, width = 1):
        self._name = name
        self._port = port
        self._length = length
        self._is_panel = is_panel
        self._width = width

        if not is_sim:
            try:
                import neopixel
                self._neopixel = neopixel.NeoPixel(port, length, brightness=1.0, auto_write=False)
            except:
                self._neopixel = sim.sim_neopixel.NeoPixel(port, length, brightness=1.0, auto_write=False, is_panel=self._is_panel, width=self._width)
        else:
            self._neopixel = sim.sim_neopixel.NeoPixel(port, length, brightness=1.0, auto_write=False, is_panel=self._is_panel, width=self._width)

    def get_name(self):
        return self._name

    def get_port(self):
        return self._port

    def get_length(self):
        return self._length

    def get_neopixel(self):
        return self._neopixel

    def is_panel(self):
        return self._is_panel

    def get_width(self):
        return self._width
