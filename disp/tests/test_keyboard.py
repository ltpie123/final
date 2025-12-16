#!/usr/bin/env python3
"""
Test keyboard automation for Hyperspeedcube.
This will help us figure out what keyboard controls actually work.
"""

import time
import subprocess
import sys

try:
    import pyautogui
except ImportError:
    print("Installing pyautogui...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", "pyautogui"])
    import pyautogui

print("Keyboard Automation Test")
print("=" * 50)
print()
print("Instructions:")
print("1. This script will launch Hyperspeedcube")
print("2. Make sure the Hyperspeedcube window is visible")
print("3. The script will try various keyboard inputs")
print("4. Watch what happens in the window")
print()
print("Starting in 3 seconds...")
time.sleep(3)

# Launch Hyperspeedcube
print("Launching Hyperspeedcube...")
proc = subprocess.Popen(
    ["../hyper/Hyperspeedcube/target/release/hyperspeedcube"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

print("Waiting 5 seconds for window to appear...")
time.sleep(5)

# Try to find and focus the window
print("Attempting to focus Hyperspeedcube window...")
try:
    subprocess.run(["xdotool", "search", "--name", "Hyperspeedcube", "windowactivate"], check=True)
    print("✓ Window focused")
except:
    print("⚠ Could not focus window automatically - please click on Hyperspeedcube")
    print("  You have 3 seconds...")
    time.sleep(3)

print()
print("Testing keyboard inputs...")
print("-" * 50)

# Test various keys that might control the puzzle
test_keys = [
    ("Ctrl+R", "ctrl+r", "Reset puzzle"),
    ("R key", "r", "R face move?"),
    ("U key", "u", "U face move?"),
    ("F key", "f", "F face move?"),
    ("Space", "space", "Action/confirm?"),
    ("Arrow Right", "right", "Navigate/rotate?"),
    ("Arrow Left", "left", "Navigate/rotate?"),
    ("Tab", "tab", "Switch tabs?"),
]

for name, key, description in test_keys:
    print(f"Pressing {name} ({description})...")
    pyautogui.press(key)
    time.sleep(1)

print()
print("-" * 50)
print("Test complete!")
print()
print("Did you see any cube movements?")
print("If yes, tell me which keys worked and we'll build the automation!")
print()
print("Press Ctrl+C to exit Hyperspeedcube...")

try:
    proc.wait()
except KeyboardInterrupt:
    print("\nTerminating...")
    proc.terminate()
    proc.wait()
