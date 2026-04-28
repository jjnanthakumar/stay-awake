# Building and Distributing Stay Awake

## For Developers and Packagers

This guide covers building standalone executables and distributing Stay Awake.

## Prerequisites

```bash
pip install pyinstaller
```

## Building Executables

### Automated Build (Recommended)

The easiest way is to use the included build script:

```bash
python build_exe.py
```

This creates both CLI and GUI executables in the `dist` folder.

### Manual Building

#### GUI Application

```bash
# Windows
pyinstaller --onefile --windowed --name=StayAwake --icon=NONE gui.py

# macOS (creates .app bundle)
pyinstaller --onefile --windowed --name=StayAwake gui.py

# Linux
pyinstaller --onefile --windowed --name=StayAwake gui.py
```

#### CLI Application

```bash
# Windows
pyinstaller --onefile --console --name=stay-awake-cli cli.py

# macOS/Linux
pyinstaller --onefile --console --name=stay-awake-cli cli.py
```

### Advanced Options

```bash
# With custom icon (Windows)
pyinstaller --onefile --windowed --name=StayAwake --icon=icon.ico gui.py

# With custom icon (macOS)
pyinstaller --onefile --windowed --name=StayAwake --icon=icon.icns gui.py

# Include additional files
pyinstaller --onefile --add-data="config.example.json:." gui.py

# Optimize for size
pyinstaller --onefile --strip --windowed gui.py

# Debug mode (show console even for GUI)
pyinstaller --onefile --debug=all gui.py
```

## File Sizes

Typical executable sizes:
- Windows: ~15-25 MB
- macOS: ~20-30 MB
- Linux: ~15-25 MB

## Testing Executables

### Windows

```cmd
# Test CLI
dist\stay-awake-cli.exe --help
dist\stay-awake-cli.exe --mode mouse --interval 30

# Test GUI
dist\StayAwake.exe
```

### macOS/Linux

```bash
# Test CLI
./dist/stay-awake-cli --help
./dist/stay-awake-cli --mode mouse --interval 30

# Test GUI
./dist/StayAwake
```

## Distribution

### Windows

1. **ZIP Archive**:
   ```bash
   # Create distributable package
   mkdir StayAwake-v1.0.0-Windows
   copy dist\StayAwake.exe StayAwake-v1.0.0-Windows\
   copy dist\stay-awake-cli.exe StayAwake-v1.0.0-Windows\
   copy README.md StayAwake-v1.0.0-Windows\
   copy LICENSE StayAwake-v1.0.0-Windows\
   copy QUICK_START.md StayAwake-v1.0.0-Windows\
   tar -a -c -f StayAwake-v1.0.0-Windows.zip StayAwake-v1.0.0-Windows
   ```

2. **Installer (Advanced)**:
   - Use Inno Setup or NSIS
   - Create Start Menu shortcuts
   - Add to Windows Path
   - Desktop shortcut option

### macOS

1. **DMG Package**:
   ```bash
   # Create application bundle
   mkdir -p StayAwake.app/Contents/MacOS
   cp dist/StayAwake StayAwake.app/Contents/MacOS/
   
   # Create DMG
   hdiutil create -volname "Stay Awake" -srcfolder StayAwake.app -ov -format UDZO StayAwake-v1.0.0-macOS.dmg
   ```

2. **Code Signing** (for distribution):
   ```bash
   codesign --force --sign "Developer ID" StayAwake.app
   ```

### Linux

1. **AppImage** (Recommended):
   ```bash
   # Use appimage-builder or similar tools
   appimagetool StayAwake.AppDir StayAwake-v1.0.0-Linux.AppImage
   ```

2. **Tarball**:
   ```bash
   tar -czf StayAwake-v1.0.0-Linux.tar.gz dist/StayAwake dist/stay-awake-cli README.md LICENSE
   ```

3. **Debian Package**:
   - Create `.deb` using `dpkg-deb`
   - Include in package manager repositories

## GitHub Releases

### Creating a Release

1. Tag the version:
   ```bash
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

2. Build for all platforms (requires separate machines or CI/CD)

3. Create release on GitHub:
   - Go to Releases → Create New Release
   - Select the tag
   - Add release notes
   - Upload executables:
     - `StayAwake-v1.0.0-Windows.zip`
     - `StayAwake-v1.0.0-macOS.dmg`
     - `StayAwake-v1.0.0-Linux.AppImage`

### Release Notes Template

```markdown
## Stay Awake v1.0.0

### Features
- GUI application for easy configuration
- CLI for advanced users and automation
- 4 activity modes: Minimal, Mouse, Keyboard, Full
- 3 mouse patterns: Linear, Circle, Random
- Configuration save/load
- Real-time statistics

### Downloads

**Windows**
- [StayAwake-v1.0.0-Windows.zip](link) - Includes GUI and CLI

**macOS**
- [StayAwake-v1.0.0-macOS.dmg](link) - GUI application

**Linux**
- [StayAwake-v1.0.0-Linux.AppImage](link) - Portable application

### Installation

#### Windows
1. Download and extract ZIP
2. Run `StayAwake.exe`

#### macOS
1. Download DMG
2. Drag to Applications folder
3. First time: Right-click → Open (to bypass Gatekeeper)

#### Linux
1. Download AppImage
2. `chmod +x StayAwake-v1.0.0-Linux.AppImage`
3. Run: `./StayAwake-v1.0.0-Linux.AppImage`

### Checksums

```
SHA256 (Windows): ...
SHA256 (macOS): ...
SHA256 (Linux): ...
```
```

## Continuous Integration (CI/CD)

### GitHub Actions Example

Create `.github/workflows/build.yml`:

```yaml
name: Build Executables

on:
  push:
    tags:
      - 'v*'

jobs:
  build-windows:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - run: pip install pyinstaller pyautogui
      - run: python build_exe.py
      - uses: actions/upload-artifact@v2
        with:
          name: windows-build
          path: dist/*

  build-macos:
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - run: pip install pyinstaller pyautogui
      - run: python build_exe.py
      - uses: actions/upload-artifact@v2
        with:
          name: macos-build
          path: dist/*

  build-linux:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - run: pip install pyinstaller pyautogui
      - run: python build_exe.py
      - uses: actions/upload-artifact@v2
        with:
          name: linux-build
          path: dist/*
```

## Troubleshooting Build Issues

### Import Errors

If PyInstaller can't find modules:
```bash
pyinstaller --hidden-import=config --hidden-import=modes --hidden-import=core gui.py
```

### Missing DLLs (Windows)

Include system DLLs if needed:
```bash
pyinstaller --add-binary="C:\path\to\dll;." gui.py
```

### Large File Size

Reduce size:
```bash
# Use UPX compression
pyinstaller --upx-dir=/path/to/upx --onefile gui.py

# Exclude unnecessary modules
pyinstaller --exclude-module=matplotlib --exclude-module=numpy gui.py
```

### Antivirus False Positives

- Submit executables to antivirus vendors
- Code sign executables (requires certificate)
- Provide checksums for verification

## Support

For build issues, check:
- PyInstaller documentation
- Project GitHub issues
- PyInstaller GitHub issues

---

**Happy Building! 🚀**
