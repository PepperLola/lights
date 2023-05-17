from lights.led_device import LEDDevice
from effects.led_effect import LEDEffect
import inspect
import effects

all_effects: dict = {}

for name, module in inspect.getmembers(effects, inspect.ismodule):
    all_effects[name] = module

class LEDManager:
    _devices: dict = {}
    _effects: dict = {}

    def __init__(self):
        pass

    def register_device(self, device: LEDDevice):
        self._devices[device.get_name()] = device

    def unregister_device(self, device: LEDDevice):
        del self._devices[device.get_name()]

    def is_device_registered(self, device_name: str):
        return device_name in self._devices.keys()

    def get_device(self, device_name: str):
        return self._devices[device_name]

    def get_devices(self):
        return self._devices

    def set_device_effect(self, device: LEDDevice, effect: LEDEffect):
        self._effects[device.get_name()] = effect
        effect.start()

    def get_device_effects(self):
        return self._effects

    def get_device_effect(self, device: LEDDevice):
        return self._effects[device.get_name()]

    def update_effects(self):
        for effect in self._effects.values():
            effect.update()
        for device in self._devices.values():
            device.get_neopixel().show()

    def parse_led_effect(self, device: LEDDevice, data):
        effect_name = data['name']
        if not effect_name in all_effects.keys():
            return None
        module = all_effects[effect_name]
        parse_funcs = inspect.getmembers(module, lambda m: inspect.isfunction(m) and "parse" in m.__name__)
        if len(parse_funcs) == 0:
            raise Exception(f"Module {module.__name__} has no parse function defined! Cannot create {effect_name} effect.")
        parse_func = parse_funcs[0][1]
        return parse_func(device, data)
        
