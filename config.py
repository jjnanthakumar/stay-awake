"""Configuration management for NJStayAwake."""

import json
import os
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional


@dataclass
class Config:
    """Configuration settings for NJStayAwake."""
    
    # Timing settings
    interval: int = 60  # Seconds between activities
    duration: float = 0.5  # Duration for mouse movements
    
    # Activity mode
    mode: str = "minimal"  # minimal, mouse, keyboard, or full
    
    # Mouse settings
    mouse_distance: int = 50  # Pixels to move mouse
    mouse_pattern: str = "linear"  # linear, circle, or random
    
    # Keyboard settings
    keyboard_key: str = "shift"  # Key to press
    keyboard_presses: int = 1  # Number of times to press
    
    # Logging settings
    log_level: str = "INFO"  # DEBUG, INFO, WARNING, ERROR
    log_file: Optional[str] = None  # Log file path (None for no file logging)
    
    # System tray
    enable_tray: bool = False  # Enable system tray icon
    
    @classmethod
    def load(cls, config_path: Optional[Path] = None) -> "Config":
        """Load configuration from file or create default."""
        if config_path and config_path.exists():
            with open(config_path, 'r') as f:
                data = json.load(f)
                return cls(**data)
        return cls()
    
    def save(self, config_path: Path) -> None:
        """Save configuration to file."""
        config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(config_path, 'w') as f:
            json.dump(asdict(self), f, indent=2)
    
    @staticmethod
    def get_default_config_path() -> Path:
        """Get the default configuration file path."""
        if os.name == 'nt':  # Windows
            config_dir = Path(os.environ.get('APPDATA', '~')) / 'StayAwake'
        else:  # Unix-like
            config_dir = Path.home() / '.config' / 'njstayawake'
        
        config_dir.mkdir(parents=True, exist_ok=True)
        return config_dir / 'config.json'
    
    def validate(self) -> list[str]:
        """Validate configuration and return list of errors."""
        errors = []
        
        if self.interval < 1:
            errors.append("Interval must be at least 1 second")
        
        if self.mode not in ["minimal", "mouse", "keyboard", "full"]:
            errors.append(f"Invalid mode: {self.mode}")
        
        if self.mouse_pattern not in ["linear", "circle", "random"]:
            errors.append(f"Invalid mouse pattern: {self.mouse_pattern}")
        
        if self.log_level not in ["DEBUG", "INFO", "WARNING", "ERROR"]:
            errors.append(f"Invalid log level: {self.log_level}")
        
        return errors
