from lights.led_device import LEDDevice

class LEDEffect:
    _device: LEDDevice
    def __init__(self, device):
        self._device = device

    def get_device(self):
        return self._device

    def start(self):
        pass

    def update(self):
        pass

    def end(self):
        pass
