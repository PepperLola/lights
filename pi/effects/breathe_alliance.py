from networktables import NetworkTable
from effects.led_effect import LEDEffect
from lights.led_device import LEDDevice
from util.color import Color, blend, BLACK, RED, BLUE, from_int
from constants import SECONDS_PER_TICK
import math

class BreatheAllianceEffect(LEDEffect):
    _intensity: float = 0
    _2pi: float = 2 * math.pi

    def __init__(self, device: LEDDevice, red_color: Color, blue_color: Color, speed: float):
        super().__init__(device)
        self._red_color = red_color
        self._blue_color = blue_color
        self._speed = speed
        self._increment = self._2pi * (speed * SECONDS_PER_TICK)

    def start(self):
        self.get_device().get_neopixel().fill(BLACK.to_tuple())

    def update(self, game_info_table: NetworkTable):
        self._intensity += self._increment
        self._intensity %= self._2pi
        alliance = "red" if game_info_table is None else game_info_table.getEntry("alliance").getString("red")
        c = self._red_color
        if alliance == "blue":
            c = self._blue_color
        self.get_device().get_neopixel().fill(blend(BLACK, c, (-math.cos(self._intensity) + 1) / 2).to_tuple())

def parse(device: LEDDevice, data):
    red_color = RED 
    blue_color = BLUE
    speed = 0.5

    if "red_color" in data.keys():
        c = data["red_color"]
        if isinstance(c, int):
            red_color = from_int(c)
        else:
            red_color = Color(c[0], c[1], c[2])

    if "blue_color" in data.keys():
        c = data["blue_color"]
        if isinstance(c, int):
            blue_color = from_int(c)
        else:
            blue_color = Color(c[0], c[1], c[2])

    if "speed" in data.keys():
        speed = data["speed"]

    return BreatheAllianceEffect(device, red_color, blue_color, speed)
