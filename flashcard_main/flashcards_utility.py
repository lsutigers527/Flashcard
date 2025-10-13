"""
These are utility functions with various use cases
"""

import os


def clear_console():
    """Clears the console screen based on the operating system."""
    if os.name == "nt":  # For Windows
        os.system("cls")
    else:  # For macOS and Linux
        os.system("clear")
