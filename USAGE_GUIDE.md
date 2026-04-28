# NJStayAwake - Usage Comparison

## Choose Your Interface

| Feature | GUI | CLI | Executable |
|---------|-----|-----|------------|
| **Ease of Use** | ⭐⭐⭐⭐⭐ Easy | ⭐⭐⭐ Moderate | ⭐⭐⭐⭐⭐ Easy |
| **Requires Python** | Yes | Yes | No |
| **Visual Feedback** | ✅ Real-time | ❌ Text only | ✅ Real-time |
| **Configuration** | ✅ Point & click | ⚙️ Arguments | ✅ Point & click |
| **Automation** | ❌ No | ✅ Yes | ⚙️ Limited |
| **Resource Usage** | Medium | Low | Medium |
| **Best For** | Daily use | Scripts | Distribution |
| **Portability** | ❌ Needs Python | ❌ Needs Python | ✅ Runs anywhere |
| **File Size** | Small (KB) | Small (KB) | Large (15-25 MB) |

## When to Use Each

### Use GUI When:
- 👤 You prefer visual interfaces
- 📊 You want to see real-time statistics
- 🎮 You need easy configuration changes
- 💾 You want to save/load settings visually
- 🖱️ You use it daily on your own computer

**Example**: Running on your work laptop during presentations

### Use CLI When:
- 🤖 You need to automate or script
- 🖥️ Running on remote servers (SSH)
- ⚡ You want minimal resource usage
- 📝 You prefer command-line workflows
- 🔄 Integrating with other tools

**Example**: Adding to a startup script on a remote server

### Use Executable When:
- 📦 Sharing with non-technical users
- 🚀 Distributing to multiple computers
- 🔒 IT department restrictions (no Python install)
- 💼 Corporate environment
- 🎯 One-click solutions needed

**Example**: Giving to colleagues who don't have Python

## Feature Comparison

### GUI Features
```
✅ Visual mode selection
✅ Real-time status indicator
✅ Live activity counter
✅ Uptime display
✅ Configuration file browser
✅ Save/Load settings
✅ All options in one window
✅ Graceful stop button
✅ Help tooltips (future)
```

### CLI Features
```
✅ All configuration via arguments
✅ Scriptable and automatable
✅ Machine-readable output
✅ Config file support
✅ Pipe-able output
✅ Low resource usage
✅ Remote-friendly
✅ Detailed help text
✅ Exit codes for automation
```

### Executable Features
```
✅ No installation required
✅ Double-click to run
✅ Self-contained
✅ Version includes GUI
✅ Works on any computer
✅ Can be on USB drive
✅ No dependencies
✅ Antivirus-friendly (after scanning)
```

## Installation Comparison

### GUI/CLI (Python Required)
```bash
# Method 1: Clone repository
git clone https://github.com/jjnanthakumar/stay-awake.git
cd stay-awake
python gui.py  # or python cli.py

# Method 2: Install with pip
pip install njstayawake
njstayawake-gui  # or njstayawake
```

**Pros**: Latest features, easy updates  
**Cons**: Requires Python installation

### Executable (No Python Required)
```bash
# Method 1: Download from releases
1. Visit GitHub releases page
2. Download StayAwake.exe (or .app/.AppImage)
3. Double-click to run

# Method 2: Build yourself
pip install pyinstaller
python build_exe.py
# Executable in dist/ folder
```

**Pros**: Works everywhere, easy distribution  
**Cons**: Larger file size, manual updates

## Performance Comparison

| Metric | GUI | CLI | Executable |
|--------|-----|-----|------------|
| **Startup Time** | 1-2s | <1s | 2-3s |
| **Memory Usage** | ~50-80 MB | ~30-50 MB | ~50-80 MB |
| **CPU Usage** | <1% idle | <1% idle | <1% idle |
| **Disk Space** | ~100 KB | ~100 KB | 15-25 MB |

*Note: All versions have similar runtime performance*

## Quick Start Commands

### GUI
```bash
# Windows
python gui.py
# or double-click: run_gui.bat
# or if built: StayAwake.exe

# Mac/Linux
python3 gui.py
# or: ./run_gui.sh
```

### CLI
```bash
# Basic usage
python cli.py

# With options
python cli.py --mode mouse --pattern circle --interval 60

# Save configuration
python cli.py --mode full --interval 120 --save-config

# Show help
python cli.py --help
```

### Executable
```bash
# Windows
StayAwake.exe                    # GUI
stay-awake-cli.exe --help        # CLI

# Mac
open StayAwake.app               # GUI
./stay-awake-cli --help          # CLI

# Linux
./StayAwake                      # GUI
./stay-awake-cli --help          # CLI
```

## Configuration Files

All three interfaces use the same configuration format:

**Location**:
- Windows: `%APPDATA%\StayAwake\config.json`
- Mac: `~/.config/stay-awake/config.json`
- Linux: `~/.config/stay-awake/config.json`

**Format**:
```json
{
  "interval": 60,
  "mode": "minimal",
  "mouse_pattern": "linear",
  "mouse_distance": 50,
  "keyboard_key": "shift",
  "keyboard_presses": 1,
  "log_level": "INFO"
}
```

## Recommendations by Use Case

### 🏢 Corporate Environment
**Recommendation**: Executable (GUI)
- No admin rights needed
- No Python required
- IT-friendly

### 👨‍💻 Developer/Power User
**Recommendation**: CLI
- Scriptable
- Integrates with workflows
- Easy to automate

### 🏠 Home User
**Recommendation**: GUI (Python or Executable)
- Easy to use
- Visual feedback
- Intuitive controls

### 🖥️ System Administrator
**Recommendation**: CLI
- Remote management
- Batch deployment
- Script integration

### 📦 Software Distributor
**Recommendation**: Executable
- No dependencies
- Easy to package
- Professional appearance

## Summary

| If You Are... | Use This | Why |
|---------------|----------|-----|
| Regular user | GUI/Executable | Easy and visual |
| Developer | CLI | Automation & scripting |
| IT admin | CLI | Deployment & management |
| Sharing with others | Executable | No setup required |
| Learning the tool | GUI | See what each option does |

---

**Still Unsure?** Start with the GUI! It's the easiest way to learn what Stay Awake can do.
