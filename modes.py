"""Activity modes for preventing sleep."""

import random
import math
from abc import ABC, abstractmethod
import pyautogui


pyautogui.FAILSAFE = False


class ActivityMode(ABC):
    """Base class for activity modes."""
    
    @abstractmethod
    def execute(self) -> None:
        """Execute the activity."""
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        """Get a description of this mode."""
        pass


class MinimalMode(ActivityMode):
    """Minimal activity - just a single key press."""
    
    def __init__(self, key: str = "shift", presses: int = 1):
        self.key = key
        self.presses = presses
    
    def execute(self) -> None:
        """Press the configured key."""
        for _ in range(self.presses):
            pyautogui.press(self.key)
    
    def get_description(self) -> str:
        return f"Pressing {self.key} key {self.presses} time(s)"


class MouseMode(ActivityMode):
    """Mouse movement activity."""
    
    def __init__(self, distance: int = 50, pattern: str = "linear", duration: float = 0.5):
        self.distance = distance
        self.pattern = pattern
        self.duration = duration
    
    def execute(self) -> None:
        """Move mouse according to pattern."""
        current_x, current_y = pyautogui.position()
        
        if self.pattern == "linear":
            self._linear_movement(current_x, current_y)
        elif self.pattern == "circle":
            self._circle_movement(current_x, current_y)
        elif self.pattern == "random":
            self._random_movement(current_x, current_y)
    
    def _linear_movement(self, x: int, y: int) -> None:
        """Move mouse in a small linear pattern."""
        pyautogui.moveTo(x + self.distance, y, duration=self.duration)
        pyautogui.moveTo(x, y, duration=self.duration)
    
    def _circle_movement(self, x: int, y: int) -> None:
        """Move mouse in a small circle."""
        steps = 8
        for i in range(steps + 1):
            angle = (2 * math.pi * i) / steps
            new_x = x + int(self.distance * math.cos(angle))
            new_y = y + int(self.distance * math.sin(angle))
            pyautogui.moveTo(new_x, new_y, duration=self.duration / steps)
    
    def _random_movement(self, x: int, y: int) -> None:
        """Move mouse to a random nearby position."""
        offset_x = random.randint(-self.distance, self.distance)
        offset_y = random.randint(-self.distance, self.distance)
        pyautogui.moveTo(x + offset_x, y + offset_y, duration=self.duration)
        pyautogui.moveTo(x, y, duration=self.duration)
    
    def get_description(self) -> str:
        return f"Moving mouse in {self.pattern} pattern ({self.distance}px)"


class KeyboardMode(ActivityMode):
    """Keyboard activity."""
    
    def __init__(self, key: str = "shift", presses: int = 3):
        self.key = key
        self.presses = presses
    
    def execute(self) -> None:
        """Press the configured key multiple times."""
        for _ in range(self.presses):
            pyautogui.press(self.key)
    
    def get_description(self) -> str:
        return f"Pressing {self.key} key {self.presses} time(s)"


class FullMode(ActivityMode):
    """Combined mouse and keyboard activity."""
    
    def __init__(self, mouse_mode: MouseMode, keyboard_mode: KeyboardMode):
        self.mouse_mode = mouse_mode
        self.keyboard_mode = keyboard_mode
    
    def execute(self) -> None:
        """Execute both mouse and keyboard activities."""
        self.mouse_mode.execute()
        self.keyboard_mode.execute()
    
    def get_description(self) -> str:
        return f"{self.mouse_mode.get_description()} + {self.keyboard_mode.get_description()}"


def create_mode(config) -> ActivityMode:
    """Create an activity mode based on configuration."""
    mouse_mode = MouseMode(
        distance=config.mouse_distance,
        pattern=config.mouse_pattern,
        duration=config.duration
    )
    keyboard_mode = KeyboardMode(
        key=config.keyboard_key,
        presses=config.keyboard_presses
    )
    
    mode_map = {
        "minimal": MinimalMode(config.keyboard_key, 1),
        "mouse": mouse_mode,
        "keyboard": keyboard_mode,
        "full": FullMode(mouse_mode, keyboard_mode)
    }
    
    return mode_map.get(config.mode, MinimalMode())
