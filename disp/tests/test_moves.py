#!/usr/bin/env python3
"""Quick test of move key combinations with longer delays"""
import time
import subprocess
import pyautogui

print("Testing move key combinations...")
print("Watch for FR → UF → FO moves (with 4 second delays)")
print()

# Launch hyperspeedcube
print("Launching Hyperspeedcube...")
proc = subprocess.Popen(["hyperspeedcube"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(8)

# Find window
result = subprocess.run(["xdotool", "search", "--name", "Hyper"], capture_output=True, text=True, check=True)
window_id = result.stdout.strip().split()[0]
print(f"Found window: {window_id}")

# Focus it
subprocess.run(["xdotool", "windowactivate", window_id], check=True)
time.sleep(1)

# Get window center and click
geometry = subprocess.run(["xdotool", "getwindowgeometry", "--shell", window_id], capture_output=True, text=True, check=True).stdout
width = int([l for l in geometry.split('\n') if l.startswith('WIDTH=')][0].split('=')[1])
height = int([l for l in geometry.split('\n') if l.startswith('HEIGHT=')][0].split('=')[1])
x = int([l for l in geometry.split('\n') if l.startswith('X=')][0].split('=')[1])
y = int([l for l in geometry.split('\n') if l.startswith('Y=')][0].split('=')[1])

pyautogui.moveTo(x + width // 2, y + height // 2)
pyautogui.click()
time.sleep(0.5)

# Reset
print("Resetting puzzle...")
pyautogui.hotkey('ctrl', 'r')
time.sleep(2)

# Test moves with longer delay
test_moves = ["FR", "UF", "FO"]
for move in test_moves:
    print(f"Executing {move}...")
    grip = move[0].lower()
    direction = move[1].lower()
    
    pyautogui.keyDown(grip)
    time.sleep(0.1)
    pyautogui.press(direction)
    time.sleep(0.1)
    pyautogui.keyUp(grip)
    
    print(f"  Waiting 4 seconds for animation...")
    time.sleep(4.0)

print()
print("✅ Test complete!")
print("Did you see 3 distinct moves: FR, then UF, then FO?")
print("Press Ctrl+C to close...")

try:
    proc.wait()
except KeyboardInterrupt:
    proc.terminate()
    proc.wait()
