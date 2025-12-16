#!/usr/bin/env python3
"""Verify specific moves we need for recording"""
import time
import subprocess
import pyautogui

print("Move Verification Test")
print("=" * 60)
print()
print("Testing our 3 sequences with 1.5 second delays:")
print("  1. FR (single move)")
print("  2. FO → FO (self-composition)")
print("  3. FR → FR (self-composition)")
print()

# Launch hyperspeedcube
print("Launching Hyperspeedcube...")
proc = subprocess.Popen(["hyperspeedcube"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(8)

# Find and focus window
result = subprocess.run(["xdotool", "search", "--name", "Hyper"], capture_output=True, text=True, check=True)
window_id = result.stdout.strip().split()[0]
subprocess.run(["xdotool", "windowactivate", window_id], check=True)
time.sleep(1)

# Click to focus
geometry = subprocess.run(["xdotool", "getwindowgeometry", "--shell", window_id], capture_output=True, text=True, check=True).stdout
width = int([l for l in geometry.split('\n') if l.startswith('WIDTH=')][0].split('=')[1])
height = int([l for l in geometry.split('\n') if l.startswith('HEIGHT=')][0].split('=')[1])
x = int([l for l in geometry.split('\n') if l.startswith('X=')][0].split('=')[1])
y = int([l for l in geometry.split('\n') if l.startswith('Y=')][0].split('=')[1])
pyautogui.moveTo(x + width // 2, y + height // 2)
pyautogui.click()
time.sleep(0.5)

def reset():
    print("  Resetting...")
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(2)

def do_move(move):
    grip = move[0].lower()
    direction = move[1].lower()
    pyautogui.keyDown(grip)
    time.sleep(0.1)
    pyautogui.press(direction)
    time.sleep(0.1)
    pyautogui.keyUp(grip)

# Test 1: FR single
print()
print("TEST 1: FR (repeat 3 times)")
reset()
for i in range(3):
    print(f"  Cycle {i+1}: FR")
    do_move("FR")
    time.sleep(1.5)
time.sleep(1)

# Test 2: FO → FO
print()
print("TEST 2: FO → FO (repeat 2 times)")
reset()
for i in range(2):
    print(f"  Cycle {i+1}: FO → FO")
    do_move("FO")
    time.sleep(1.5)
    do_move("FO")
    time.sleep(1.5)
time.sleep(1)

# Test 3: FR → FR
print()
print("TEST 3: FR → FR (repeat 2 times)")
reset()
for i in range(2):
    print(f"  Cycle {i+1}: FR → FR")
    do_move("FR")
    time.sleep(1.5)
    do_move("FR")
    time.sleep(1.5)
time.sleep(1)

print()
print("=" * 60)
print("✅ Verification complete!")
print()
print("Questions:")
print("  1. Were the moves smooth at 1.5 second intervals?")
print("  2. Could you distinguish each move clearly?")
print("  3. Did the sequences look correct?")
print()
print("If YES to all → run: ./record_with_nix.sh")
print("If NO → adjust delay and re-test")
print()
print("Press Ctrl+C to close...")

try:
    proc.wait()
except KeyboardInterrupt:
    proc.terminate()
    proc.wait()
