# Contributing to NJStayAwake

Thank you for your interest in contributing to NJStayAwake! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/jjnanthakumar/stay-awake.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate it:
   - Windows: `venv\Scripts\activate`
   - Unix/Mac: `source venv/bin/activate`
5. Install dependencies: `pip install -e .[dev]`

## Development Workflow

1. Create a new branch: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Test your changes thoroughly
4. Commit with clear messages: `git commit -m "Add: feature description"`
5. Push to your fork: `git push origin feature/your-feature-name`
6. Create a Pull Request

## Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Add docstrings to all functions and classes
- Keep functions focused and modular

## Testing

Before submitting a PR:
- Test on your target platform
- Verify all modes work correctly
- Check that configuration loading/saving works
- Ensure graceful shutdown (Ctrl+C) functions properly

## Feature Requests and Bug Reports

Please use GitHub Issues to report bugs or suggest features. Include:
- Clear description
- Steps to reproduce (for bugs)
- Expected vs actual behavior
- System information (OS, Python version)

## Areas for Contribution

- Additional mouse movement patterns
- System tray icon support
- GUI interface
- More comprehensive testing
- Documentation improvements
- Platform-specific optimizations

## Questions?

Feel free to open an issue for any questions about contributing!
