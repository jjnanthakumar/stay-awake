# Changelog

All notable changes to NJStayAwake will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-04-28

### Added
- 🎨 Graphical User Interface (GUI) with real-time monitoring
- 💻 Command-line interface (CLI) with comprehensive arguments
- 🎯 Multiple activity modes:
  - Minimal: Single key press (least intrusive)
  - Mouse: Mouse movement only
  - Keyboard: Multiple key presses
  - Full: Combined mouse and keyboard activity
- 🔄 Three mouse movement patterns:
  - Linear: Simple back-and-forth movement
  - Circle: Smooth circular motion
  - Random: Unpredictable nearby positions
- 💾 Configuration file support (JSON format)
  - Save current settings
  - Load saved configurations
  - Default config location per platform
- 📊 Real-time statistics and monitoring:
  - Activity count
  - Uptime display
  - Status indicators
- 📝 Comprehensive logging system:
  - Console output
  - File logging (optional)
  - Multiple log levels (DEBUG, INFO, WARNING, ERROR)
- ⚙️ Configurable settings:
  - Interval between activities
  - Mouse movement duration
  - Mouse movement distance
  - Keyboard key selection (dropdown)
  - Number of key presses
- 🛑 Graceful shutdown handling (Ctrl+C)
- 🏗️ Executable build support:
  - Windows (NJStayAwake.exe, njstayawake-cli.exe)
  - Linux (NJStayAwake, njstayawake-cli)
  - macOS (NJStayAwake, njstayawake-cli)
- 🔄 GitHub Actions CI/CD:
  - Automatic builds on tag push
  - Multi-platform support
  - Artifact publishing
  - Automatic releases
  - **Automatic PyPI publishing**
  - **Version sync across GitHub and PyPI**
- 📖 Comprehensive documentation:
  - README with usage examples
  - Quick Start guide for non-technical users
  - Build guide for developers
  - Usage comparison guide
  - Release process documentation
- ⚖️ MIT License
- 🌍 Cross-platform support (Windows, macOS, Linux)

### Changed
- Updated from simple script to full application
- Improved user experience with GUI
- Enhanced configurability

### Security
- No network connections
- No data collection
- All processing local
- Open source for transparency

## [Unreleased]

### Planned Features
- System tray icon support
- Scheduler for automatic start/stop
- Profiles for different scenarios
- More mouse movement patterns
- Custom keyboard shortcuts
- Activity presets
- Dark mode for GUI
- Multi-language support

---

[1.0.0]: https://github.com/jjnanthakumar/stay-awake/releases/tag/v1.0.0
