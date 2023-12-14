from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import ctypes
import sys
import os

def run_script_as_admin(script_path):
    try:
        ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            sys.executable,
            script_path,
            None,
            0x1 | 0x08000000  # Use 0x08000000 to hide the console window
        )
    except ctypes.WinError as e:
        # Handle error (e.g., user canceled UAC prompt)
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    run_script_as_admin("app.py")
