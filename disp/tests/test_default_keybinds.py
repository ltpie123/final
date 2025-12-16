#!/usr/bin/env python3
"""Test with actual default keybinds"""
import time
import subprocess
import pyautogui

print("Testing Default Rubiks4D Keybinds")
print("=" * 60)
print()

# Launch
print("Launching Hyperspeedcube...")
proc = subprocess.Popen(["hyperspeedcube"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(8)

# Focus
result = subprocess.run(["xdotool", "search", "--name", "Hyper"], capture_output=True, text=True, check=True)
window_id = result.stdout.strip().split()[0]
subprocess.run(["xdotool", "windowactivate", window_id], check=True)
time.sleep(1)

geometry = subprocess.run(["xdotool", "getwindowgeometry", "--shell", window_id], capture_output=True, text=True, check=True).stdout
width = int([l for l in geometry.split('\n') if l.startswith('WIDTH=')][0].split('=')[1])
height = int([l for l in geometry.split('\n') if l.startswith('HEIGHT=')][0].split('=')[1])
x = int([l for l in geometry.split('\n') if l.startswith('X=')][0].split('=')[1])
y = int([l for l in geometry.split('\n') if l.startswith('Y=')][0].split('=')[1])
pyautogui.moveTo(x + width // 2, y + height // 2)
pyautogui.click()
time.sleep(0.5)

# Make sure we're on 3x3x3x3
print("Pressing F4 to load 3×3×3×3...")
pyautogui.press('f4')
time.sleep(2)

# Reset
print("Resetting puzzle (Ctrl+R)...")
pyautogui.hotkey('ctrl', 'r')
time.sleep(2)

print()
print("Testing moves with default keybinds:")
print()

# Test FR: Hold S (Front), press I (+x)
print("1. FR move: Hold S (Front), press I")
pyautogui.keyDown('s')
time.sleep(0.1)
pyautogui.press('i')
time.sleep(0.1)
pyautogui.keyUp('s')
time.sleep(1.5)

# Test FO: Hold S (Front), press O (+z toward Outside)
print("2. FO move: Hold S (Front), press O")
pyautogui.keyDown('s')
time.sleep(0.1)
pyautogui.press('o')
time.sleep(0.1)
pyautogui.keyUp('s')
time.sleep(1.5)

print()
print("=" * 60)
print("✅ Test complete!")
print()
print("Did you see 2 moves: FR then FO?")
print("If YES → ./record_with_nix.sh")
print()
print("Press Ctrl+C to close...")

try:
    proc.wait()
except KeyboardInterrupt:
    proc.terminate()
    proc.wait()
