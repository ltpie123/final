#!/usr/bin/env python3
"""Test 4D move keybinds"""
import time
import subprocess
import pyautogui

print("Testing 4D move keybinds")
print("=" * 60)
print()

# Launch hyperspeedcube
print("Launching Hyperspeedcube...")
proc = subprocess.Popen(["hyperspeedcube"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(8)

# Find and focus
result = subprocess.run(["xdotool", "search", "--name", "Hyper"], capture_output=True, text=True, check=True)
window_id = result.stdout.strip().split()[0]
subprocess.run(["xdotool", "windowactivate", window_id], check=True)
time.sleep(1)

# Click center
geometry = subprocess.run(["xdotool", "getwindowgeometry", "--shell", window_id], capture_output=True, text=True, check=True).stdout
width = int([l for l in geometry.split('\n') if l.startswith('WIDTH=')][0].split('=')[1])
height = int([l for l in geometry.split('\n') if l.startswith('HEIGHT=')][0].split('=')[1])
x = int([l for l in geometry.split('\n') if l.startswith('X=')][0].split('=')[1])
y = int([l for l in geometry.split('\n') if l.startswith('Y=')][0].split('=')[1])
pyautogui.moveTo(x + width // 2, y + height // 2)
pyautogui.click()
time.sleep(0.5)

# Reset
print("Resetting puzzle (Ctrl+R)...")
pyautogui.hotkey('ctrl', 'r')
time.sleep(2)

# Test our 3 moves
test_moves = [
    ("FR", "Front grip → rotate Right"),
    ("FO", "Front grip → rotate Outside"),
]

print()
print("Testing moves (1.5 sec between):")
print()

for move, desc in test_moves:
    print(f"{move} ({desc})")
    grip = move[0].lower()
    direction = move[1].lower()
    
    # Press grip, then direction
    pyautogui.press(grip)
    time.sleep(0.05)
    pyautogui.press(direction)
    
    time.sleep(1.5)

print()
print("=" * 60)
print("✅ Test complete!")
print()
print("Did you see 2 distinct moves?")
print("  1. FR (Front → Right)")
print("  2. FO (Front → Outside)")
print()
print("If YES → run: ./record_with_nix.sh")
print("If NO → describe what happened")
print()
print("Press Ctrl+C to close...")

try:
    proc.wait()
except KeyboardInterrupt:
    proc.terminate()
    proc.wait()
