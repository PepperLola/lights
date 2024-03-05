from lights.led_device import LEDDevice

class LEDStrip(LEDDevice):

    def __init__(self, name, port, length, led_manager, is_sim=False):
        super().__init__(name, port, length, led_manager, is_sim=is_sim)
