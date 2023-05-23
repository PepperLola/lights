from lights.led_device import LEDDevice

class LEDEffect:
    _device: LEDDevice
    _panel_only: bool = False
    def __init__(self, device, panel_only=False):
        self._device = device
        self._panel_only = panel_only
        if self._panel_only and not self._device.is_panel():
            raise Exception(f"Effect '{type(self).__name__}' can only be applied to an LED Panel")

    def get_device(self):
        return self._device

    def start(self):
        pass

    def update(self):
        pass

    def end(self):
        pass

    def get_panel_only(self):
        return self._panel_only
