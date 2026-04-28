# Quick Start Guide - Stay Awake

## For Non-Technical Users

### \ud83d\udcbb Using the Standalone Executable (Easiest!)

1. **Download**: Get `StayAwake.exe` from the releases page
2. **Run**: Double-click the executable
3. **Configure**: 
   - Select your preferred mode (Minimal is recommended for most users)
   - Adjust the interval (60 seconds is a good default)
4. **Start**: Click the green "Start" button
5. **Stop**: Click the red "Stop" button when done

That's it! No installation or setup required.

---

## \ud83c\udfaf Recommended Settings

### For Presentations
- **Mode**: Minimal
- **Interval**: 120 seconds (2 minutes)
- **Why**: Least intrusive, won't interfere with your presentation

### For Video Watching
- **Mode**: Mouse
- **Pattern**: Circle
- **Interval**: 60 seconds
- **Why**: Subtle mouse movement keeps screen active

### For Long Downloads/Uploads
- **Mode**: Full
- **Interval**: 90 seconds
- **Why**: Maximum reliability ensures system stays awake

### For Working from Home
- **Mode**: Mouse
- **Pattern**: Random
- **Interval**: 45 seconds
- **Why**: Looks more natural, simulates real activity

---

## \ud83d\udd27 GUI Features Explained

### Status Section
- **\u25cf Running (Green)**: Service is active
- **\u25cf Stopped (Red)**: Service is not running
- Shows activity count and uptime when running

### Activity Modes
1. **Minimal**: Single shift key press (invisible to most apps)
2. **Mouse**: Moves mouse in a pattern (visible but subtle)
3. **Keyboard**: Multiple key presses (more noticeable)
4. **Full**: Both mouse and keyboard (most reliable)

### Timing Settings
- **Interval**: How often to perform activity (in seconds)
- **Duration**: How long mouse movements take (in seconds)

### Mouse Settings
- **Pattern**:
  - Linear: Back and forth in a line
  - Circle: Smooth circular motion
  - Random: Unpredictable movement
- **Distance**: How far the mouse moves (in pixels)

### Keyboard Settings
- **Key**: Which key to press (shift, ctrl, f15, etc.)
- **Presses**: How many times to press the key

### Buttons
- **Start**: Begin the service
- **Stop**: Stop the service
- **Load Config**: Load settings from a file
- **Save Config**: Save current settings to a file

---

## \u2753 FAQ

**Q: Will this work with my security software?**
A: Yes, it simulates normal user input. However, some corporate monitoring software may detect it.

**Q: Can I minimize the window while it runs?**
A: Yes! The service continues running even when minimized.

**Q: Does it drain battery?**
A: Minimal impact. The activity is very light and infrequent.

**Q: Can I use my computer normally while it runs?**
A: Yes! Use "Minimal" mode for the least interference.

**Q: How do I make it start automatically?**
A: Place the executable in your Windows Startup folder:
   `C:\\Users\\YourName\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup`

**Q: Can I run multiple instances?**
A: Not recommended - one instance is sufficient.

---

## \ud83d\udee0\ufe0f Troubleshooting

### Mouse Moves Too Much
- Reduce "Movement Distance" to 25-30 pixels
- Increase "Interval" to 120+ seconds

### Not Working / Computer Still Sleeps
- Try "Full" mode instead of "Minimal"
- Reduce interval to 30 seconds
- Check Windows power settings

### Interferes with Work
- Use "Minimal" mode
- Increase interval to 180+ seconds
- Consider using F15 key (rarely used)

### Application Won't Start
- Make sure you have permission to run executables
- Try "Run as Administrator" (right-click \u2192 Run as administrator)
- Check if antivirus is blocking it

---

## \ud83d\udd12 Privacy & Security

- **No Network Activity**: Stay Awake doesn't connect to the internet
- **No Data Collection**: Your settings stay on your computer
- **Open Source**: Code is available for review on GitHub
- **Local Only**: All activity happens on your machine

---

## \ud83d\udcde Support

If you encounter issues:
1. Check this guide first
2. Review the main README.md
3. Report issues on GitHub: https://github.com/jjnanthakumar/stay-awake/issues

---

**Enjoy Stay Awake! \u2615**
