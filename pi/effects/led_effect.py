from lights.led_segment import LEDSegment
from networktables import NetworkTable
from lights.led_device import LEDDevice

class LEDEffect:
    _segment: LEDSegment
    _panel_only: bool = False
    _name: str
    def __init__(self, segment: LEDSegment, panel_only: bool =False):
        self._segment = segment
        self._panel_only = panel_only
        if self._panel_only and not self._segment.get_device().is_panel():
            raise Exception(f"Effect '{type(self).__name__}' can only be applied to an LED Panel")

    def set_name(self, name: str):
        self._name = name

    def get_name(self):
        return self._name

    def get_segment(self):
        return self._segment

    def start(self):
        pass

    def update(self, game_info_table: NetworkTable):
        pass

    def end(self):
        pass

    def get_panel_only(self):
        return self._panel_only
