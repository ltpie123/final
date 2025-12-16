#!/usr/bin/env python3
"""Quick test - record just one move to verify it works"""
import time
import subprocess
from pathlib import Path
import pyautogui

print("Quick Recording Test")
print("=" * 60)

# Launch
print("Launching Hyperspeedcube...")
proc = subprocess.Popen(["hyperspeedcube"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(8)

# Find and focus
result = subprocess.run(["xdotool", "search", "--name", "Hyper"], capture_output=True, text=True, check=True)
window_id = result.stdout.strip().split()[0]
subprocess.run(["xdotool", "windowactivate", window_id], check=True)
time.sleep(1)

# Load 3x3x3x3
print("Loading 3×3×3×3...")
pyautogui.press('f4')
time.sleep(3)

# Reset
print("Resetting...")
pyautogui.hotkey('ctrl', 'r')
time.sleep(2)

# Get geometry RIGHT BEFORE recording
geometry = subprocess.run(
    ["xdotool", "getwindowgeometry", "--shell", window_id],
    capture_output=True, text=True, check=True
).stdout

width = int([l for l in geometry.split('\n') if l.startswith('WIDTH=')][0].split('=')[1])
height = int([l for l in geometry.split('\n') if l.startswith('HEIGHT=')][0].split('=')[1])
x = int([l for l in geometry.split('\n') if l.startswith('X=')][0].split('=')[1])
y = int([l for l in geometry.split('\n') if l.startswith('Y=')][0].split('=')[1])

print(f"Window geometry: {width}x{height} at position ({x}, {y})")

# Click center to ensure focus
center_x = x + width // 2
center_y = y + height // 2
pyautogui.moveTo(center_x, center_y)
pyautogui.click()
time.sleep(0.5)

# Start recording
output = "test_recording.mp4"
print(f"Starting ffmpeg recording...")

rec_proc = subprocess.Popen([
    "ffmpeg",
    "-f", "x11grab",
    "-framerate", "30",
    "-video_size", f"{width}x{height}",
    "-i", f":0.0+{x},{y}",
    "-t", "10",
    "-y",
    output
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

time.sleep(2)
print("Recording started, executing 2 FR moves...")

# Do 2 FR moves
for i in range(2):
    print(f"  Move {i+1}: FR")
    pyautogui.keyDown('s')  # Front grip
    time.sleep(0.1)
    pyautogui.press('i')     # x direction
    time.sleep(0.1)
    pyautogui.keyUp('s')
    time.sleep(1.5)

print("Waiting for recording to finish...")
rec_proc.wait()

if Path(output).exists():
    size = Path(output).stat().st_size
    print(f"✅ Recording saved: {output} ({size:,} bytes)")
    print()
    print("Test playback:")
    print(f"  ffplay {output}")
    print()
    print("Extract frame to check:")
    print(f"  ffmpeg -i {output} -vframes 1 test_frame.png")
else:
    print("❌ Recording failed!")

proc.terminate()
proc.wait()
