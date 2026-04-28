
"""
Stay Awake - Prevent your computer from going to sleep.

This is a simple wrapper that maintains backward compatibility with the original script.
For advanced features, use cli.py instead.

Example usage:
    python main.py
    
For advanced usage:
    python cli.py --help
"""

import sys
from cli import main

if __name__ == '__main__':
    sys.exit(main())