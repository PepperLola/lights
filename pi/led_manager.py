from lights.led_device import LEDDevice
from effects.led_effect import LEDEffect
import inspect
import effects

all_effects: dict = {}

for name, module in inspect.getmembers(effects, inspect.ismodule):
    all_effects[name] = module

print(all_effects)
print(effects)

class LEDManager:
    _devices: dict = {}
    _effects: dict = {}

    def __init__(self):
        pass

    def register_device(self, device: LEDDevice):
        self._devices[device.get_name()] = device

    def unregister_device(self, device: LEDDevice):
        del self._devices[device.get_name()]

    def get_devices(self):
        return self._devices

    def set_device_effect(self, device: LEDDevice, effect: LEDEffect):
        self._effects[device.get_name()] = effect
        effect.start()

    def update_effects(self):
        for effect in self._effects.values():
            effect.update()
        for device in self._devices.values():
            device.get_neopixel().show()
