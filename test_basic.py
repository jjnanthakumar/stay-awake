"""
Quick test script to verify Stay Awake functionality.
Run this to ensure all components are working correctly.
"""

import sys
import time
from config import Config
from modes import MinimalMode, MouseMode, KeyboardMode, FullMode, create_mode


def test_config():
    """Test configuration loading and validation."""
    print("Testing Configuration...")
    
    # Test default config
    config = Config()
    assert config.interval == 60
    assert config.mode == "minimal"
    print("✓ Default configuration works")
    
    # Test validation
    config.interval = -1
    errors = config.validate()
    assert len(errors) > 0
    print("✓ Validation catches errors")
    
    # Reset
    config.interval = 60
    errors = config.validate()
    assert len(errors) == 0
    print("✓ Valid configuration passes")


def test_modes():
    """Test all activity modes."""
    print("\nTesting Activity Modes...")
    
    # Test minimal mode
    minimal = MinimalMode()
    print(f"Minimal: {minimal.get_description()}")
    minimal.execute()
    print("✓ Minimal mode works")
    
    time.sleep(0.5)
    
    # Test mouse mode
    mouse = MouseMode(distance=10, pattern="linear", duration=0.2)
    print(f"Mouse: {mouse.get_description()}")
    mouse.execute()
    print("✓ Mouse mode works")
    
    time.sleep(0.5)
    
    # Test keyboard mode
    keyboard = KeyboardMode(presses=1)
    print(f"Keyboard: {keyboard.get_description()}")
    keyboard.execute()
    print("✓ Keyboard mode works")
    
    time.sleep(0.5)
    
    # Test full mode
    full = FullMode(mouse, keyboard)
    print(f"Full: {full.get_description()}")
    full.execute()
    print("✓ Full mode works")


def test_mode_creation():
    """Test mode creation from config."""
    print("\nTesting Mode Creation...")
    
    configs = [
        ("minimal", Config(mode="minimal")),
        ("mouse", Config(mode="mouse")),
        ("keyboard", Config(mode="keyboard")),
        ("full", Config(mode="full"))
    ]
    
    for name, config in configs:
        mode = create_mode(config)
        assert mode is not None
        print(f"✓ {name.capitalize()} mode created: {mode.get_description()}")


def main():
    """Run all tests."""
    print("=" * 60)
    print("Stay Awake - Functionality Test")
    print("=" * 60)
    
    try:
        test_config()
        test_modes()
        test_mode_creation()
        
        print("\n" + "=" * 60)
        print("✓ All tests passed successfully!")
        print("=" * 60)
        print("\nYou can now run the application with:")
        print("  python cli.py --help")
        return 0
        
    except Exception as e:
        print(f"\n✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
