from lights.led_panel import LEDPanel
from lights.led_panel_segment import LEDPanelSegment
from lights.led_segment import LEDSegment
from lights.led_strip import LEDStrip
from lights.led_strip_segment import LEDStripSegment
from networktables import NetworkTable
from lights.led_device import LEDDevice
from effects.led_effect import LEDEffect
from effects.importer import import_effect
import inspect
import effects

all_effects: dict = {}

for name, module in inspect.getmembers(effects, inspect.ismodule):
    all_effects[name] = module

class LEDManager:
    _devices: dict[str, LEDDevice] = {}
    _effects: dict[str, LEDEffect] = {}
    _segment_parents: dict[str, LEDDevice] = {}

    def __init__(self):
        pass

    def register_device(self, device: LEDDevice):
        device.on_register()
        self._devices[device.get_name()] = device

    def unregister_device(self, device: LEDDevice):
        self._devices[device.get_name()].on_unregister()
        del self._devices[device.get_name()]

    def unregister_all_devices(self):
        devices = list(self._devices.values())
        for device in devices:
            self.unregister_device(device)

    def is_device_registered(self, device_name: str):
        return device_name in self._devices.keys()

    def is_segment_registered(self, segment_name: str):
        return segment_name in self._segment_parents.keys()

    def get_device(self, device_name: str):
        return self._devices[device_name]

    def get_devices(self):
        return self._devices

    def register_segment(self, device_name: str, segment: LEDSegment):
        device = self.get_device(device_name)
        if device is not None:
            device.add_segment(segment)
            self._segment_parents[segment.get_name()] = device

    def register_default_segment(self, device: LEDDevice):
        segment = None
        if isinstance(device, LEDStrip):
            segment = LEDStripSegment(device.get_name(), device, (0, device.get_length()))
        elif isinstance(device, LEDPanel):
            segment = LEDPanelSegment(device.get_name(), device, (0, 0), (device.get_width(), device.get_height()))

        if segment is not None:
            self.register_segment(device.get_name(), segment)

    def set_segment_effect(self, segment: LEDSegment, effect: LEDEffect):
        self._effects[segment.get_name()] = effect
        effect.start()

    def get_device_effects(self):
        return self._effects

    def get_segment_parents(self):
        return self._segment_parents

    def get_segment(self, name: str) -> LEDSegment | None:
        device: LEDDevice = self.get_segment_parents()[name]
        if device is None:
            return None
        return device.get_segments()[name]

    def get_segment_effect(self, segment: LEDSegment):
        return self._effects[segment.get_name()]

    def update_effects(self, game_info_table: NetworkTable):
        for effect in self._effects.values():
            effect.update(game_info_table)
        for device in self._devices.values():
            device.get_neopixel().show()
            for segment in device.get_segments().values():
                if isinstance(segment, LEDPanelSegment):
                    led_panel_segment: LEDPanelSegment = segment
                    led_panel_segment.get_buffer().display()

    def parse_led_effect(self, segment: LEDSegment, data):
        effect_name = data['name']
        return import_effect(effect_name, segment, data)
