# NJStayAwake

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![PyPI](https://img.shields.io/pypi/v/njstayawake.svg)

**NJStayAwake** is a lightweight, configurable Python application that prevents your computer from going to sleep by simulating user activity. Perfect for presentations, long downloads, or when you need to keep your system active.

## ✨ Features

- **Multiple Activity Modes**
  - 🎯 **Minimal**: Single key press (least intrusive)
  - 🖱️ **Mouse**: Mouse movement only
  - ⌨️ **Keyboard**: Multiple key presses
  - 🔄 **Full**: Combined mouse and keyboard activity

- **Flexible Mouse Patterns**
  - Linear: Simple back-and-forth movement
  - Circle: Smooth circular motion
  - Random: Unpredictable nearby positions

- **Comprehensive Configuration**
  - Command-line arguments for quick adjustments
  - JSON configuration file support
  - Customizable intervals, keys, and patterns
  - Adjustable logging levels

- **Professional Features**
  - Graceful shutdown with Ctrl+C
  - Activity logging and statistics
  - Configuration persistence
  - Cross-platform support (Windows, macOS, Linux)

## 📦 Installation

### Option 1: Download Standalone EXE (Easiest - No Python Required!)

**[📥 Download Latest Release](https://github.com/jjnanthakumar/njstayawake/releases/latest)**

**Windows:**
- 🖱️ GUI: Download `NJStayAwake.exe` - Just double-click to run!
- 💻 CLI: Download `njstayawake-cli.exe`

**Linux:**
- 🖱️ GUI: Download `NJStayAwake` - Run: `chmod +x NJStayAwake && ./NJStayAwake`
- 💻 CLI: Download `njstayawake-cli`

**macOS:**
- 🖱️ GUI: Download `NJStayAwake` - Right-click → Open (first time)
- 💻 CLI: Download `njstayawake-cli`

No extraction needed! Direct download and run! 🚀

### Option 2: Clone and Install (For Developers)

```bash
git clone https://github.com/jjnanthakumar/njstayawake.git
cd njstayawake
pip install -e .
```

### Option 3: Install via pip (Automatically Published!)

```bash
pip install njstayawake
```

Then run:
```bash
# GUI
njstayawake-gui

# CLI
njstayawake --mode mouse --interval 60
```

**Note:** PyPI package is automatically published when new versions are released on GitHub!

### Requirements (for Python installation)

- Python 3.8 or higher
- pyautogui (automatically installed)
- tkinter (comes with Python, for GUI)

## 🚀 Quick Start

### GUI Application (Easiest!)

```bash
# Run the graphical interface
python gui.py

# Or if installed via pip
njstayawake-gui

# Or just double-click NJStayAwake.exe (Windows)
```

The GUI provides:
- 🎨 User-friendly interface
- 📊 Real-time status and statistics
- ⚙️ Easy configuration
- 💾 Save/Load settings
- 🔴 Start/Stop buttons

### Command-Line Interface

```bash
# Run with default settings (minimal mode, 60 second interval)
python cli.py

# Or if installed via pip
njstayawake

# Or use njstayawake-cli.exe (Windows)
```

### Common Use Cases

```bash
# Presentation mode - minimal interference
python cli.py --mode minimal --interval 120

# Mouse movement only - subtle activity
python cli.py --mode mouse --pattern circle --interval 60

# Full activity mode for maximum effectiveness
python cli.py --mode full --interval 90

# Custom keyboard key
python cli.py --mode keyboard --key ctrl --presses 2

# Save your favorite configuration
python cli.py --mode mouse --pattern random --interval 45 --save-config
```

## 📖 Usage Examples

### GUI Application

The GUI is self-explanatory:

1. **Select Mode**: Choose from Minimal, Mouse, Keyboard, or Full
2. **Configure Settings**: Adjust intervals, patterns, and keys
3. **Click Start**: Begin preventing sleep
4. **View Stats**: See real-time activity count and uptime
5. **Click Stop**: Stop the service when done

**Features:**
- Visual status indicator (green = running, red = stopped)
- Real-time uptime counter
- Save/Load configuration files
- All settings in one window

### Command-Line Arguments

```bash
# Basic options
python cli.py --mode mouse              # Mouse movement mode
python cli.py --interval 30             # Activity every 30 seconds
python cli.py --duration 1.0            # Slower mouse movements

# Mouse customization
python cli.py --pattern circle          # Circular mouse pattern
python cli.py --mouse-distance 100      # Larger movement radius

# Keyboard customization
python cli.py --key f15                 # Use F15 key (less intrusive)
python cli.py --presses 5               # Multiple key presses

# Logging
python cli.py --log-level DEBUG         # Detailed logging
python cli.py --log-file stay-awake.log # Log to file

# Configuration management
python cli.py --show-config             # Show current settings
python cli.py --save-config             # Save settings to file
python cli.py --config custom.json      # Load custom config
```

### Configuration File

Create a configuration file to save your preferences:

```bash
python cli.py --mode full --interval 120 --pattern circle --save-config
```

This creates a config file at:
- Windows: `%APPDATA%\StayAwake\config.json`
- Linux/Mac: `~/.config/stay-awake/config.json`

**Example config.json:**

```json
{
  "interval": 120,
  "duration": 0.5,
  "mode": "full",
  "mouse_distance": 75,
  "mouse_pattern": "circle",
  "keyboard_key": "shift",
  "keyboard_presses": 2,
  "log_level": "INFO",
  "log_file": null,
  "enable_tray": false
}
```

### Programmatic Usage

```python
from config import Config
from core import StayAwake

# Create custom configuration
config = Config(
    mode="mouse",
    interval=60,
    mouse_pattern="circle",
    mouse_distance=50
)

# Start the service
app = StayAwake(config)
app.start()  # Runs until Ctrl+C
```

## 🎮 Activity Modes

### Minimal Mode
- **Best for**: When you need minimal interference
- **Activity**: Single shift key press
- **Detectability**: Very low
- **Use case**: Video calls, presentations

### Mouse Mode
- **Best for**: Keeping screen active
- **Activity**: Mouse movement (linear/circle/random)
- **Detectability**: Low to medium
- **Use case**: Watching videos, monitoring dashboards

### Keyboard Mode
- **Best for**: Applications that detect keyboard activity
- **Activity**: Multiple key presses
- **Detectability**: Medium
- **Use case**: Terminal sessions, SSH connections

### Full Mode
- **Best for**: Maximum reliability
- **Activity**: Both mouse movement and key presses
- **Detectability**: Medium to high
- **Use case**: Long running tasks, downloads

## 🛠️ Advanced Configuration

### Environment-Specific Settings

**Development:**
```bash
python cli.py --mode minimal --interval 30 --log-level DEBUG
```

**Production/Presentation:**
```bash
python cli.py --mode mouse --pattern circle --interval 120 --log-level WARNING
```

### Custom Patterns

The mouse patterns can be adjusted:
- `--mouse-distance 25` - Smaller, subtle movements
- `--mouse-distance 150` - Larger, more noticeable movements
- `--pattern random` - Less predictable pattern

### Keyboard Alternatives

Use less intrusive keys:
- F13-F24 function keys (rarely mapped)
- Scroll lock
- Num lock

Example:
```bash
python cli.py --mode keyboard --key f15 --presses 1
```

## 📊 Statistics and Monitoring

When you stop the service (Ctrl+C), you'll see statistics:

```
============================================================
Stay Awake Service Stopped
============================================================
Total activities performed: 42
Total runtime: 1h 15m 30s
============================================================
```

## 🏗️ Building Standalone Executables

### Automatic Builds via GitHub Actions

**No manual tagging needed!** Just commit and push:

```bash
git add .
git commit -m "feat: add new feature"  # Use conventional commits
git push origin main
```

GitHub Actions automatically:
- Analyzes your commit message
- Bumps version (patch/minor/major)
- Builds executables for Windows, Linux, and macOS
- Creates GitHub release with direct download links
- Uploads individual executables (no ZIP needed!)
- **Publishes package to PyPI with matching version**
- **Users can `pip install stay-awake` immediately!**

**Commit Message Guide:**
- `feat:` - New feature (bumps minor version)
- `fix:` - Bug fix (bumps patch version)
- `BREAKING CHANGE:` - Major change (bumps major version)

See [COMMITS.md](COMMITS.md) for full conventional commits guide.

### Manual Build (Local)

Create executables that run without Python installed:

### Build EXE (All Platforms)

```bash
# Install PyInstaller
pip install pyinstaller

# Run the build script
python build_exe.py
```

This creates:
- `dist/StayAwake.exe` - GUI application (Windows) or `StayAwake` (Linux/Mac)
- `dist/stay-awake-cli.exe` - CLI application (Windows) or `stay-awake-cli` (Linux/Mac)

### Manual Build Commands

```bash
# Build GUI version
pyinstaller --onefile --windowed --name=StayAwake gui.py

# Build CLI version
pyinstaller --onefile --console --name=stay-awake-cli cli.py
```

### Distribution

The executables in the `dist` folder can be:
- Shared with others
- Run on any computer (no Python needed)
- Placed anywhere on your system
- Added to Windows startup folder for auto-start

## ⚙️ Configuration Options

| Option | Description | Default |
|--------|-------------|---------|
| `--mode` | Activity mode (minimal/mouse/keyboard/full) | minimal |
| `--interval` | Seconds between activities | 60 |
| `--duration` | Mouse movement duration (seconds) | 0.5 |
| `--mouse-distance` | Mouse movement distance (pixels) | 50 |
| `--pattern` | Mouse pattern (linear/circle/random) | linear |
| `--key` | Keyboard key to press | shift |
| `--presses` | Number of key presses | 1 |
| `--log-level` | Logging level (DEBUG/INFO/WARNING/ERROR) | INFO |
| `--log-file` | Path to log file | None |
| `--config` | Load config from file | None |
| `--save-config` | Save current config | - |
| `--show-config` | Display current config | - |

## 🔧 Troubleshooting

### Permission Issues (macOS/Linux)
Some systems require accessibility permissions:
- macOS: System Preferences → Security & Privacy → Accessibility
- Linux: May need to run with appropriate permissions

### PyAutoGUI Errors
If you get failsafe errors, the application disables failsafe by default, but you can adjust the code if needed.

### High CPU Usage
Increase the interval between activities:
```bash
python cli.py --interval 300  # 5 minutes
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is intended for legitimate use cases such as:
- Preventing sleep during presentations
- Keeping connections alive during long tasks
- Development and testing purposes

Please use responsibly and in accordance with your organization's policies.

## 🎯 Three Ways to Use Stay Awake

### 1. 🖱️ GUI Application (Recommended for Most Users)
- **Best for**: Everyone, especially non-technical users
- **How to run**: 
  - Windows: Double-click `run_gui.bat` or `StayAwake.exe`
  - Mac/Linux: Run `./run_gui.sh` or `python gui.py`
- **Features**: Visual interface, real-time stats, easy configuration

### 2. 💻 Command-Line Interface (For Advanced Users)
- **Best for**: Automation, scripting, remote servers
- **How to run**: `python cli.py --mode mouse --interval 60`
- **Features**: Full control via arguments, scriptable, lightweight

### 3. 📦 Standalone Executable (No Python Required)
- **Best for**: Sharing with others, production use
- **How to build**: `python build_exe.py`
- **Features**: Runs anywhere, no installation needed

## 📝 Changelog

### Version 1.0.0
- ✅ GUI application with real-time monitoring
- ✅ CLI with comprehensive arguments
- ✅ Multiple activity modes (Minimal, Mouse, Keyboard, Full)
- ✅ Three mouse patterns (Linear, Circle, Random)
- ✅ Configuration file support (JSON)
- ✅ Comprehensive logging system
- ✅ Graceful shutdown handling
- ✅ Cross-platform support (Windows, macOS, Linux)
- ✅ Executable build support
- ✅ Statistics and monitoring

## 👤 Author

**Nanthakumar J J**
- GitHub: [@jjnanthakumar](https://github.com/jjnanthakumar)

## 🌟 Support

If you find this project helpful:
- ⭐ Star it on GitHub
- 🐛 Report bugs or request features
- 🤝 Contribute improvements
- 📢 Share with others who might find it useful

## 🙏 Acknowledgments

- Built with Python and PyAutoGUI
- Uses tkinter for GUI
- Packaged with PyInstaller