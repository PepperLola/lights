from networktables import NetworkTable
from effects.led_effect import LEDEffect
from lights.led_segment import LEDSegment
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

    def __init__(self, segment: LEDSegment, path: str, fps: int):
        super().__init__(segment, panel_only=True)
        self._path = path
        self._fps = fps

        self._frame_duration = 1.0 / fps

        self._gif = Image.open(path)
        self._iterator = ImageSequence.Iterator(self._gif)

    def start(self):
        self.get_segment().fill(BLACK)

    def update(self, game_info_table: NetworkTable):
        current_time = time.time()
        elapsed_time = current_time - self._last_update_time
        if elapsed_time >= self._frame_duration:
            frame = next(self._iterator)
            self.get_segment().get_buffer().image(frame.convert("RGB"))
            self.get_segment().get_buffer().display()
            self._last_update_time = current_time

def parse(segment: LEDSegment, data):
    path = "animations/bad_apple.gif"
    speed = 24

    if "speed" in data.keys():
        speed = data["speed"]

    if "path" in data.keys():
        path = data["path"]

    return AnimationEffect(segment, path, speed)
