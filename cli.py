"""Command-line interface for Stay Awake."""

import argparse
import sys
from pathlib import Path

from config import Config
from core import StayAwake


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        prog='stay-awake',
        description='Prevent your computer from going to sleep by simulating user activity.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  stay-awake                          # Run with default settings (minimal mode, 60s interval)
  stay-awake --mode mouse             # Use mouse movement mode
  stay-awake --interval 30            # Check every 30 seconds
  stay-awake --mode full --interval 120  # Full mode (mouse + keyboard) every 2 minutes
  stay-awake --config myconfig.json   # Load settings from config file
  stay-awake --save-config            # Save current settings to config file
  stay-awake --pattern circle         # Use circular mouse movement pattern

Modes:
  minimal  - Single key press (least intrusive)
  mouse    - Mouse movement only
  keyboard - Multiple key presses
  full     - Both mouse and keyboard activity

Mouse Patterns:
  linear   - Simple back-and-forth movement
  circle   - Circular motion
  random   - Random nearby positions
        """
    )
    
    # Mode settings
    parser.add_argument(
        '--mode', '-m',
        choices=['minimal', 'mouse', 'keyboard', 'full'],
        help='Activity mode (default: minimal)'
    )
    
    # Timing settings
    parser.add_argument(
        '--interval', '-i',
        type=int,
        help='Seconds between activities (default: 60)'
    )
    
    parser.add_argument(
        '--duration', '-d',
        type=float,
        help='Duration for mouse movements in seconds (default: 0.5)'
    )
    
    # Mouse settings
    parser.add_argument(
        '--mouse-distance',
        type=int,
        help='Pixels to move mouse (default: 50)'
    )
    
    parser.add_argument(
        '--pattern', '-p',
        choices=['linear', 'circle', 'random'],
        help='Mouse movement pattern (default: linear)'
    )
    
    # Keyboard settings
    parser.add_argument(
        '--key', '-k',
        help='Keyboard key to press (default: shift)'
    )
    
    parser.add_argument(
        '--presses',
        type=int,
        help='Number of key presses (default: 1 for minimal, 3 for keyboard/full)'
    )
    
    # Logging settings
    parser.add_argument(
        '--log-level',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        help='Logging level (default: INFO)'
    )
    
    parser.add_argument(
        '--log-file',
        type=str,
        help='Path to log file (default: console only)'
    )
    
    # Configuration file
    parser.add_argument(
        '--config', '-c',
        type=Path,
        help='Load configuration from JSON file'
    )
    
    parser.add_argument(
        '--save-config',
        action='store_true',
        help='Save current configuration to default config file and exit'
    )
    
    parser.add_argument(
        '--show-config',
        action='store_true',
        help='Show current configuration and exit'
    )
    
    parser.add_argument(
        '--version', '-v',
        action='version',
        version='%(prog)s 1.0.0'
    )
    
    return parser


def apply_args_to_config(config: Config, args: argparse.Namespace) -> Config:
    """Apply command-line arguments to configuration."""
    if args.mode:
        config.mode = args.mode
    if args.interval:
        config.interval = args.interval
    if args.duration:
        config.duration = args.duration
    if args.mouse_distance:
        config.mouse_distance = args.mouse_distance
    if args.pattern:
        config.mouse_pattern = args.pattern
    if args.key:
        config.keyboard_key = args.key
    if args.presses:
        config.keyboard_presses = args.presses
    if args.log_level:
        config.log_level = args.log_level
    if args.log_file:
        config.log_file = args.log_file
    
    return config


def main():
    """Main CLI entry point."""
    parser = create_parser()
    args = parser.parse_args()
    
    # Load configuration
    if args.config:
        config = Config.load(args.config)
    else:
        # Try to load from default location
        default_config = Config.get_default_config_path()
        if default_config.exists():
            config = Config.load(default_config)
        else:
            config = Config()
    
    # Apply command-line arguments (override config file)
    config = apply_args_to_config(config, args)
    
    # Handle special commands
    if args.show_config:
        print("Current Configuration:")
        print("-" * 40)
        print(f"Mode:              {config.mode}")
        print(f"Interval:          {config.interval} seconds")
        print(f"Duration:          {config.duration} seconds")
        print(f"Mouse Distance:    {config.mouse_distance} pixels")
        print(f"Mouse Pattern:     {config.mouse_pattern}")
        print(f"Keyboard Key:      {config.keyboard_key}")
        print(f"Keyboard Presses:  {config.keyboard_presses}")
        print(f"Log Level:         {config.log_level}")
        print(f"Log File:          {config.log_file or 'None'}")
        print("-" * 40)
        return 0
    
    if args.save_config:
        config_path = Config.get_default_config_path()
        config.save(config_path)
        print(f"Configuration saved to: {config_path}")
        return 0
    
    # Validate configuration
    errors = config.validate()
    if errors:
        print("Configuration errors:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    
    # Start Stay Awake
    try:
        app = StayAwake(config)
        app.start()
        return 0
    except KeyboardInterrupt:
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
