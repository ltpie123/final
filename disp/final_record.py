#!/usr/bin/env python3
"""
FINAL automated recording script using default Rubiks4D keybinds
"""

import time
import subprocess
import sys
import os
from pathlib import Path

try:
    import pyautogui
    pyautogui.FAILSAFE = True
except ImportError:
    print("ERROR: pyautogui not found")
    sys.exit(1)


class HyperspeedcubeRecorder:
    def __init__(self):
        self.window_id = None
        self.recording_process = None
        self.hyperspeedcube_process = None
        
    def launch_hyperspeedcube(self):
        """Launch Hyperspeedcube."""
        print("🚀 Launching Hyperspeedcube...")
        self.hyperspeedcube_process = subprocess.Popen(
            ["hyperspeedcube"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print("   Waiting for window...")
        time.sleep(4)
        
    def find_and_focus_window(self):
        """Find and focus Hyperspeedcube window."""
        print("🔍 Finding Hyperspeedcube window...")
        
        try:
            result = subprocess.run(
                ["xdotool", "search", "--name", "Hyper"],
                capture_output=True,
                text=True,
                check=True
            )
            self.window_id = result.stdout.strip().split()[0]
            print(f"   ✓ Found window: {self.window_id}")
            
            # Focus and raise
            subprocess.run(["xdotool", "windowactivate", self.window_id], check=True)
            subprocess.run(["xdotool", "windowraise", self.window_id], check=True)
            time.sleep(0.5)
            
            # Get geometry
            geometry = subprocess.run(
                ["xdotool", "getwindowgeometry", "--shell", self.window_id],
                capture_output=True,
                text=True,
                check=True
            ).stdout
            
            width = int([l for l in geometry.split('\n') if l.startswith('WIDTH=')][0].split('=')[1])
            height = int([l for l in geometry.split('\n') if l.startswith('HEIGHT=')][0].split('=')[1])
            x = int([l for l in geometry.split('\n') if l.startswith('X=')][0].split('=')[1])
            y = int([l for l in geometry.split('\n') if l.startswith('Y=')][0].split('=')[1])
            
            # Click center to focus
            pyautogui.moveTo(x + width // 2, y + height // 2)
            pyautogui.click()
            time.sleep(0.3)
            
            return width, height, x, y
            
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Could not find Hyperspeedcube window: {e}")
    
    def load_3x3x3x3(self):
        """Load 3×3×3×3 puzzle."""
        print("📐 Loading 3×3×3×3...")
        pyautogui.press('f4')
        time.sleep(2)
    
    def reset_puzzle(self):
        """Reset puzzle to solved state."""
        print("🔄 Resetting puzzle...")
        pyautogui.hotkey('ctrl', 'r')
        time.sleep(1.5)
    
    def start_recording(self, output_file, width, height, x, y, duration):
        """Start ffmpeg screen recording."""
        print(f"🔴 Starting recording: {output_file}")
        
        cmd = [
            "ffmpeg",
            "-f", "x11grab",
            "-framerate", "30",
            "-video_size", f"{width}x{height}",
            "-i", f":0.0+{x},{y}",
            "-t", str(duration),
            "-y",
            output_file
        ]
        
        self.recording_process = subprocess.Popen(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
        time.sleep(2)
    
    def execute_moves(self, moves, cycles=4, delay=1.5):
        """
        Execute moves using default Rubiks4D keybinds.
        
        Default system: Hold grip key, press twist key
        - Grip: S=F(Front), V=O(Outside), F=R(Right), etc.
        - Twist: I=x(Right), O=z(Outside), J=y, etc.
        """
        # Move mappings based on default config
        move_map = {
            'FR': ('s', 'i'),  # Front grip, x twist (toward Right)
            'FO': ('s', 'o'),  # Front grip, z twist (toward Outside)
        }
        
        print(f"🎮 Executing: {' → '.join(moves)} × {cycles} cycles")
        
        for cycle in range(1, cycles + 1):
            print(f"   Cycle {cycle}/{cycles}")
            for move in moves:
                print(f"      → {move}")
                
                if move in move_map:
                    grip, twist = move_map[move]
                    # Hold grip, press twist, release grip
                    pyautogui.keyDown(grip)
                    time.sleep(0.1)
                    pyautogui.press(twist)
                    time.sleep(0.1)
                    pyautogui.keyUp(grip)
                else:
                    print(f"      ⚠️  Unknown move: {move}")
                
                time.sleep(delay)
    
    def record_sequence(self, name, moves, cycles=4, delay=1.5):
        """Record one sequence."""
        print()
        print("=" * 60)
        print(f"Recording: {name}")
        print(f"Moves: {' → '.join(moves)} × {cycles}")
        print("=" * 60)
        print()
        
        # Re-focus window
        width, height, x, y = self.find_and_focus_window()
        
        # Reset puzzle
        self.reset_puzzle()
        
        # Calculate duration
        duration = cycles * len(moves) * delay + 5
        
        # Start recording
        output = f"recordings/{name}.mp4"
        self.start_recording(output, width, height, x, y, duration)
        
        # Execute moves
        self.execute_moves(moves, cycles, delay)
        
        # Wait for recording to finish
        print("   Waiting for recording...")
        if self.recording_process:
            self.recording_process.wait()
            self.recording_process = None
        
        # Check output
        if Path(output).exists():
            size = Path(output).stat().st_size
            print(f"✅ Complete: {output} ({size:,} bytes)")
        else:
            print(f"❌ Failed: {output}")
        
        time.sleep(1)
    
    def cleanup(self):
        """Clean up processes."""
        if self.recording_process:
            self.recording_process.terminate()
            self.recording_process.wait(timeout=5)
        
        if self.hyperspeedcube_process:
            print("🛑 Stopping Hyperspeedcube...")
            self.hyperspeedcube_process.terminate()
            try:
                self.hyperspeedcube_process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                self.hyperspeedcube_process.kill()
                self.hyperspeedcube_process.wait()


def main():
    Path("recordings").mkdir(exist_ok=True)
    
    sequences = [
        {"name": "FR_single", "moves": ["FR"], "cycles": 8},
        {"name": "FO_FO", "moves": ["FO", "FO"], "cycles": 4},
        {"name": "FR_FR", "moves": ["FR", "FR"], "cycles": 4},
    ]
    
    recorder = HyperspeedcubeRecorder()
    
    try:
        print()
        print("╔═══════════════════════════════════════════════════════╗")
        print("║  Hyperspeedcube Automated Recording                  ║")
        print("╚═══════════════════════════════════════════════════════╝")
        print()
        
        # Launch and setup
        recorder.launch_hyperspeedcube()
        recorder.find_and_focus_window()
        recorder.load_3x3x3x3()
        
        print()
        print("⚠️  Ready to record!")
        print("   • Keep window visible")
        print("   • Don't touch mouse/keyboard")
        print()
        input("Press ENTER to start recording...")
        print()
        
        # Record all sequences
        for seq in sequences:
            recorder.record_sequence(seq["name"], seq["moves"], seq["cycles"])
        
        print()
        print("=" * 60)
        print("✅ All recordings complete!")
        print("=" * 60)
        print()
        print("Next: Convert to GIFs")
        for seq in sequences:
            print(f"  ./scripts/video_to_gif.sh recordings/{seq['name']}.mp4 figures/sequence_{seq['name']}.gif 640 20")
        print()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        recorder.cleanup()


if __name__ == "__main__":
    main()
