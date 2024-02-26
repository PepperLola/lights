from networktables import NetworkTable
from effects.led_effect import LEDEffect
from lights.led_device import LEDDevice
from util.color import Color, blend, BLACK, PURPLE, from_int
from constants import SECONDS_PER_TICK
from PIL import Image, ImageSequence
import math
import time

class AnimationEffect(LEDEffect):
    _gif: Image.Image
    _iter: ImageSequence.Iterator
    _last_update_time: float = time.time()
    _frame_duration: float

    def __init__(self, device: LEDDevice, path: str, fps: int):
        super().__init__(device, panel_only=True)
        self._path = path
        self._fps = fps

        self._frame_duration = 1.0 / fps

        self._gif = Image.open(path)
        self._iterator = ImageSequence.Iterator(self._gif)

    def start(self):
        self.get_device().get_neopixel().fill(BLACK.to_tuple())

    def update(self, game_info_table: NetworkTable):
        current_time = time.time()
        elapsed_time = current_time - self._last_update_time
        if elapsed_time >= self._frame_duration:
            frame = next(self._iterator)
            self.get_device().get_buffer().image(frame.convert("RGB"))
            self.get_device().get_buffer().display()
            self._last_update_time = current_time

def parse(device: LEDDevice, data):
    path = "animations/bad_apple.gif"
    speed = 24

    if "speed" in data.keys():
        speed = data["speed"]

    if "path" in data.keys():
        path = data["path"]

    return AnimationEffect(device, path, speed)
