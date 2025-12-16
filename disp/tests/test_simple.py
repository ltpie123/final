#!/usr/bin/env python3
"""
Minimal test: Can we type into Hyperspeedcube?
"""
import time
import subprocess
import sys
import pyautogui

print("🧪 Testing Hyperspeedcube Keyboard Input")
print("=" * 50)

# Launch Hyperspeedcube (using installed version)
print("Launching Hyperspeedcube...")
proc = subprocess.Popen(["hyperspeedcube"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("Waiting for window to appear (8 seconds)...")
time.sleep(8)

# Find and focus window
print("Finding window...")
window_id = None
for attempt in range(5):
    try:
        result = subprocess.run(
            ["xdotool", "search", "--name", "Hyper"],
            capture_output=True, text=True, check=True
        )
        window_id = result.stdout.strip().split()[0]
        print(f"✓ Found window: {window_id}")
        break
    except:
        if attempt < 4:
            print(f"  Attempt {attempt + 1}/5 failed, retrying...")
            time.sleep(2)
        else:
            raise Exception("Could not find Hyperspeedcube window after 5 attempts")

try:
    if not window_id:
        raise Exception("Window ID not found")
    
    # Focus it
    subprocess.run(["xdotool", "windowactivate", window_id], check=True)
    subprocess.run(["xdotool", "windowraise", window_id], check=True)
    time.sleep(1)
    
    # Click center to ensure focus
    geometry = subprocess.run(
        ["xdotool", "getwindowgeometry", "--shell", window_id],
        capture_output=True, text=True, check=True
    ).stdout
    
    width = int([l for l in geometry.split('\n') if l.startswith('WIDTH=')][0].split('=')[1])
    height = int([l for l in geometry.split('\n') if l.startswith('HEIGHT=')][0].split('=')[1])
    x = int([l for l in geometry.split('\n') if l.startswith('X=')][0].split('=')[1])
    y = int([l for l in geometry.split('\n') if l.startswith('Y=')][0].split('=')[1])
    
    center_x = x + width // 2
    center_y = y + height // 2
    
    pyautogui.moveTo(center_x, center_y)
    pyautogui.click()
    time.sleep(0.5)
    
    print("\n🎹 Testing keyboard input...")
    print("Watch the Hyperspeedcube window!")
    print()
    
    # Reset puzzle
    print("1. Pressing Ctrl+R (reset)...")
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(2)
    
    # Try typing a move
    print("2. Typing 'FR' + Enter...")
    pyautogui.typewrite('FR', interval=0.1)
    pyautogui.press('enter')
    time.sleep(3)
    
    print("3. Typing 'UF' + Enter...")
    pyautogui.typewrite('UF', interval=0.1)
    pyautogui.press('enter')
    time.sleep(3)
    
    print()
    print("=" * 50)
    print("Test complete!")
    print()
    print("DID THE CUBE MOVE?")
    print("  [YES] → automation works! Run: uv run python3 automate_recording.py")
    print("  [NO]  → need manual recording (see RECORDING_GUIDE.md)")
    print()
    
except Exception as e:
    print(f"❌ Error: {e}")
finally:
    print("Press Ctrl+C to close Hyperspeedcube...")
    try:
        proc.wait()
    except KeyboardInterrupt:
        proc.terminate()
        proc.wait()
