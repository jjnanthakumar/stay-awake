"""
Build script to create standalone executables for Stay Awake.
Supports Windows (.exe), macOS (.app), and Linux builds.

Requirements:
    pip install pyinstaller

Usage:
    python build_exe.py
"""

import PyInstaller.__main__
import platform
import shutil
from pathlib import Path


def build_cli_exe():
    """Build CLI executable."""
    print("\n" + "=" * 60)
    print("Building CLI Executable...")
    print("=" * 60)
    
    args = [
        'cli.py',
        '--name=njstayawake-cli',
        '--onefile',
        '--console',
        '--icon=logo.png',
        '--add-data=config.py:.',
        '--add-data=modes.py:.',
        '--add-data=core.py:.',
        '--clean',
    ]
    
    PyInstaller.__main__.run(args)
    print("✓ CLI executable built successfully!")


def build_gui_exe():
    """Build GUI executable."""
    print("\n" + "=" * 60)
    print("Building GUI Executable...")
    print("=" * 60)
    
    args = [
        'gui.py',
        '--name=NJStayAwake',
        '--onefile',
        '--windowed',  # No console window
        '--icon=logo.png',
        '--add-data=logo.png:.',
        '--add-data=config.py:.',
        '--add-data=modes.py:.',
        '--add-data=core.py:.',
        '--clean',
    ]
    
    PyInstaller.__main__.run(args)
    print("✓ GUI executable built successfully!")


def main():
    """Main build process."""
    print("NJStayAwake - Executable Builder")
    print("=" * 60)
    print(f"Platform: {platform.system()}")
    print(f"Python: {platform.python_version()}")
    print("=" * 60)
    
    # Build both versions
    try:
        build_cli_exe()
        build_gui_exe()
        
        print("\n" + "=" * 60)
        print("Build Complete!")
        print("=" * 60)
        print("\nExecutables are located in the 'dist' folder:")
        
        if platform.system() == "Windows":
            print("  - StayAwake.exe (GUI version)")
            print("  - njstayawake-cli.exe (Command-line version)")
        elif platform.system() == "Darwin":  # macOS
            print("  - StayAwake (GUI version)")
            print("  - stay-awake-cli (Command-line version)")
        else:  # Linux
            print("  - StayAwake (GUI version)")
            print("  - stay-awake-cli (Command-line version)")
        
        print("\nYou can distribute these executables independently.")
        print("No Python installation required on target machines!")
        
    except Exception as e:
        print(f"\n✗ Build failed: {e}")
        return 1
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
