from lights.led_device import LEDDevice

class LEDPanel(LEDDevice):
    _width: int = 0
    _height: int = 0
    def __init__(self, name, port, width, height, is_sim=False, alternating=True):
        super().__init__(name, port, height * width, is_sim=is_sim, is_panel=True, width=width, alternating=alternating)
        self._width = width
        self._height = height

