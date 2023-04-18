import sim.sim_neopixel

class LEDDevice:
    _name = ""
    _port = 0
    _length = 0
    def __init__(self, name, port, length, is_sim = False):
        self._name = name
        self._port = port
        self._length = length

        if not is_sim:
            try:
                import neopixel
                self._neopixel = neopixel.NeoPixel(port, length, brightness=0.1, auto_write=False)
            except:
                self._neopixel = sim.sim_neopixel.NeoPixel(port, length, brightness=0.1, auto_write=False)
        else:
            self._neopixel = sim.sim_neopixel.NeoPixel(port, length, brightness=0.1, auto_write=False)

    def get_name(self):
        return self._name

    def get_port(self):
        return self._port

    def get_length(self):
        return self._length

    def get_neopixel(self):
        return self._neopixel
