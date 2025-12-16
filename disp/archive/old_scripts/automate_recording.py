#!/usr/bin/env python3
"""
Automated recording of Hyperspeedcube sequences using GUI automation.

This script:
1. Launches Hyperspeedcube
2. Uses the Puzzle Controls tab to click move buttons
3. Records the screen during the sequence
4. Saves video output

Requirements: pyautogui, xdotool, ffmpeg
"""

import time
import subprocess
import sys
import os
from pathlib import Path

# Try to import pyautogui, install if needed
try:
    import pyautogui
    pyautogui.FAILSAFE = True  # Move mouse to corner to abort
except ImportError:
    print("pyautogui not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", "pyautogui", "python3-xlib"])
    import pyautogui
    pyautogui.FAILSAFE = True


class HyperspeedcubeAutomator:
    def __init__(self):
        self.window_id = None
        self.recording_process = None
        self.hyperspeedcube_process = None
        
    def launch_hyperspeedcube(self):
        """Launch Hyperspeedcube in background."""
        print("🚀 Launching Hyperspeedcube...")
        
        self.hyperspeedcube_process = subprocess.Popen(
            ["hyperspeedcube"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
        # Wait for window to appear
        print("   Waiting for window...")
        time.sleep(4)
        
    def find_and_focus_window(self):
        """Find Hyperspeedcube window and focus it."""
        print("🔍 Finding Hyperspeedcube window...")
        
        try:
            result = subprocess.run(
                ["xdotool", "search", "--name", "Hyperspeedcube"],
                capture_output=True,
                text=True,
                check=True
            )
            self.window_id = result.stdout.strip().split()[0]
            print(f"   ✓ Found window ID: {self.window_id}")
            
            # Focus and raise window
            subprocess.run(["xdotool", "windowactivate", self.window_id], check=True)
            subprocess.run(["xdotool", "windowraise", self.window_id], check=True)
            time.sleep(0.5)
            
            # Click center of window to ensure focus
            geometry = subprocess.run(
                ["xdotool", "getwindowgeometry", "--shell", self.window_id],
                capture_output=True,
                text=True,
                check=True
            ).stdout
            
            # Parse geometry
            width = int([l for l in geometry.split('\n') if l.startswith('WIDTH=')][0].split('=')[1])
            height = int([l for l in geometry.split('\n') if l.startswith('HEIGHT=')][0].split('=')[1])
            x = int([l for l in geometry.split('\n') if l.startswith('X=')][0].split('=')[1])
            y = int([l for l in geometry.split('\n') if l.startswith('Y=')][0].split('=')[1])
            
            center_x = x + width // 2
            center_y = y + height // 2
            
            pyautogui.moveTo(center_x, center_y)
            pyautogui.click()
            time.sleep(0.3)
            
            return width, height, x, y
            
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Could not find Hyperspeedcube window: {e}")
    
    def reset_puzzle(self):
        """Reset puzzle to solved state using Ctrl+R."""
        print("🔄 Resetting puzzle...")
        pyautogui.keyDown('ctrl')
        pyautogui.press('r')
        pyautogui.keyUp('ctrl')
        time.sleep(1.5)
    
    def set_rkt_keybinds(self):
        """Navigate to Settings and set keybinds to RKT."""
        print("⚙️  Setting keybinds to RKT...")
        
        # Open settings with Ctrl+comma or click Settings tab
        # This is a bit fragile - may need manual setup
        print("   Please manually set Settings → Puzzle → Keybinds → RKT")
        print("   (Automation for UI navigation is complex)")
        time.sleep(0.5)
    
    def navigate_to_puzzle_controls(self):
        """Navigate to Puzzle Controls tab."""
        print("📑 Navigating to Puzzle Controls tab...")
        # Tab through interface or click location if we can find it
        # For now, assume it's accessible - may need adjustment
        time.sleep(0.5)
    
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
        
        # Give ffmpeg time to start
        time.sleep(2)
    
    def stop_recording(self):
        """Stop ffmpeg recording."""
        if self.recording_process:
            print("⏹️  Stopping recording...")
            self.recording_process.terminate()
            self.recording_process.wait(timeout=5)
            self.recording_process = None
            time.sleep(0.5)
    
    def execute_move_sequence(self, moves, cycles=4, delay_between_moves=1.5):
        """
        Execute move sequence by typing move notation (requires RKT keybinds).
        
        With RKT keybinds: Type "FR" + Enter to execute the move.
        
        Args:
            moves: List of move names, e.g., ["FR", "UF"]
            cycles: Number of times to repeat the sequence
            delay_between_moves: Seconds to wait between moves
        """
        print(f"🎮 Executing sequence: {' → '.join(moves)} × {cycles} cycles")
        
        for cycle in range(1, cycles + 1):
            print(f"   Cycle {cycle}/{cycles}")
            for move in moves:
                print(f"      → {move}")
                
                # Type the move notation
                for char in move:
                    pyautogui.press(char.lower())
                    time.sleep(0.05)
                
                # Press Enter to execute
                pyautogui.press('enter')
                
                # Wait for animation
                time.sleep(delay_between_moves)
    
    def record_sequence(self, sequence_name, moves, cycles=4, delay_between_moves=1.5):
        """
        Complete recording workflow for a sequence.
        
        Args:
            sequence_name: Name for output file (e.g., "FR_FR")
            moves: List of move names (e.g., ["FR", "FR"])
            cycles: Number of complete cycles to record
            delay_between_moves: Wait time between moves
        """
        print()
        print("=" * 60)
        print(f"Recording: {sequence_name}")
        print(f"Moves: {' → '.join(moves)}")
        print(f"Cycles: {cycles}")
        print("=" * 60)
        print()
        
        # Focus window (may have lost focus during pause)
        print("🔍 Re-focusing Hyperspeedcube window...")
        width, height, x, y = self.find_and_focus_window()
        
        # Reset puzzle
        self.reset_puzzle()
        
        # Calculate duration
        move_count = len(moves) * cycles
        duration = move_count * delay_between_moves + 5
        
        # Start recording
        output_file = f"recordings/{sequence_name}.mp4"
        self.start_recording(output_file, width, height, x, y, duration)
        
        # Execute moves
        self.execute_move_sequence(moves, cycles, delay_between_moves)
        
        # Wait for recording to finish
        print("   Waiting for recording to complete...")
        if self.recording_process:
            self.recording_process.wait()
            self.recording_process = None
        
        # Check output
        if Path(output_file).exists():
            size = Path(output_file).stat().st_size
            print(f"✅ Recording complete: {output_file} ({size:,} bytes)")
        else:
            print(f"❌ Recording failed: {output_file} not found")
        
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
    # Create recordings directory
    Path("recordings").mkdir(exist_ok=True)
    
    # Define sequences to record
    sequences = [
        {
            "name": "FR_single",
            "moves": ["FR"],
            "cycles": 8,
            "description": "Baseline (λ≈0, period 8)"
        },
        {
            "name": "FO_FO",
            "moves": ["FO", "FO"],
            "cycles": 4,
            "description": "Most chaotic (λ=6.093, period 4)"
        },
        {
            "name": "FR_FR",
            "moves": ["FR", "FR"],
            "cycles": 4,
            "description": "Self-composition (λ=5.942, period 4)"
        },
    ]
    
    automator = HyperspeedcubeAutomator()
    
    try:
        print()
        print("╔═══════════════════════════════════════════════════════╗")
        print("║  Hyperspeedcube Automated Recording                  ║")
        print("╚═══════════════════════════════════════════════════════╝")
        print()
        
        # Launch Hyperspeedcube first
        automator.launch_hyperspeedcube()
        width, height, x, y = automator.find_and_focus_window()
        
        # Pause for user to confirm setup
        print()
        print("⚙️  SETUP CHECK:")
        print("=" * 60)
        print()
        print("The script will use DEFAULT keybinds (not RKT).")
        print("Make sure:")
        print("  • Hyperspeedcube window is visible")
        print("  • You're on the 3×3×3×3 (4D) puzzle")
        print("  • Default keybinds are active")
        print()
        print("The script will press keys like:")
        print("  FR = Press 'f' then 'r' (Front grip → rotate Right)")
        print("  FO = Press 'f' then 'o' (Front grip → rotate Outside)")
        print()
        input("Press ENTER when ready to start recording...")
        print()
        print("✅ Starting recording in 3 seconds...")
        time.sleep(3)
        print()
        
        # Now record all sequences
        for seq in sequences:
            print()
            automator.record_sequence(
                sequence_name=seq["name"],
                moves=seq["moves"],
                cycles=seq["cycles"]
            )
        
        print()
        print("=" * 60)
        print("✅ All recordings complete!")
        print("=" * 60)
        print()
        print("Next steps:")
        print("  1. Check recordings/ directory")
        print("  2. Convert to GIF:")
        for seq in sequences:
            print(f"     ./scripts/video_to_gif.sh recordings/{seq['name']}.mp4 figures/sequence_{seq['name']}.gif")
        print()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        automator.cleanup()


if __name__ == "__main__":
    main()
