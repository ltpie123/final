#!/usr/bin/env python3
"""
Automated sequence execution with manual recording control.

This script:
1. Launches Hyperspeedcube
2. Sets up the puzzle
3. Prompts you to start your screen recorder
4. Executes the sequence automatically
5. Prompts you to stop recording
6. Repeats for each sequence

You control the screen recorder, it controls the moves.
"""

import pyautogui
import time
import subprocess
import sys
from pathlib import Path

# Import corrected config
from recording_config_CORRECTED import MOVE_KEYBINDS, get_category, SEQUENCES

class SequenceAutomator:
    def __init__(self):
        self.window_id = None
        pyautogui.PAUSE = 0.1
    
    def launch_hyperspeedcube(self):
        """Launch Hyperspeedcube."""
        print("🚀 Launching Hyperspeedcube...")
        subprocess.Popen(["hyperspeedcube"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(3)
    
    def find_and_focus_window(self):
        """Find and focus the Hyperspeedcube window."""
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
            
            # Click center to ensure focus
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
            
            center_x = x + width // 2
            center_y = y + height // 2
            pyautogui.click(center_x, center_y)
            time.sleep(0.3)
            
            return True
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
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
    
    def execute_move(self, move_name):
        """Execute a single move."""
        if move_name not in MOVE_KEYBINDS:
            print(f"⚠️  Unknown move: {move_name}")
            return False
        
        grip_key, twist_key = MOVE_KEYBINDS[move_name]
        
        # Hold grip, tap twist, release grip
        pyautogui.keyDown(grip_key)
        time.sleep(0.1)
        pyautogui.press(twist_key)
        time.sleep(0.1)
        pyautogui.keyUp(grip_key)
        
        return True
    
    def execute_sequence(self, moves, cycles, delay=1.5):
        """Execute a sequence multiple times."""
        total_moves = len(moves) * cycles
        move_count = 0
        
        print(f"\n{'='*60}")
        print(f"🎬 EXECUTING: {' → '.join(moves)} × {cycles}")
        print(f"   Total moves: {total_moves}")
        print(f"{'='*60}\n")
        
        for cycle in range(cycles):
            print(f"Cycle {cycle + 1}/{cycles}: ", end='', flush=True)
            for move in moves:
                self.execute_move(move)
                move_count += 1
                print(f"{move} ", end='', flush=True)
                time.sleep(delay)
            print(f"  [{move_count}/{total_moves}]")
        
        print(f"\n✅ Sequence complete!")
    
    def prompt_start_recording(self, seq_name, desc):
        """Prompt user to start their screen recorder."""
        print("\n" + "="*70)
        print(f"📹 SEQUENCE: {seq_name}")
        print(f"   {desc}")
        print("="*70)
        print("\n🎬 ACTION REQUIRED:")
        print("   1. Start your screen recorder (SimpleScreenRecorder, OBS, etc.)")
        print("   2. Focus the Hyperspeedcube window")
        print("   3. Press ENTER when ready to begin sequence execution")
        print()
        
        input("Press ENTER to start... ")
        print("\n⏱️  Starting in 3 seconds...")
        time.sleep(1)
        print("   3...")
        time.sleep(1)
        print("   2...")
        time.sleep(1)
        print("   1...")
        time.sleep(1)
        print("   GO!\n")
    
    def prompt_stop_recording(self, seq_name):
        """Prompt user to stop their screen recorder."""
        print("\n" + "="*70)
        print(f"✅ SEQUENCE COMPLETE: {seq_name}")
        print("="*70)
        print("\n🛑 ACTION REQUIRED:")
        print("   1. Stop your screen recorder")
        print(f"   2. Save as: recordings/{seq_name}.mp4")
        print("   3. Press ENTER when ready for next sequence")
        print()
        
        input("Press ENTER to continue... ")
    
    def run_sequence(self, seq_config):
        """Run a single sequence with manual recording control."""
        name = seq_config['name']
        moves = seq_config['moves']
        cycles = seq_config['cycles']
        desc = seq_config['desc']
        
        # Focus window
        self.find_and_focus_window()
        
        # Reset puzzle
        self.reset_puzzle()
        
        # Prompt to start recording
        self.prompt_start_recording(name, desc)
        
        # Execute sequence
        self.execute_sequence(moves, cycles)
        
        # Prompt to stop recording
        self.prompt_stop_recording(name)
    
    def run_category(self, category_name):
        """Run all sequences in a category."""
        sequences = get_category(category_name)
        
        if not sequences:
            print(f"❌ Unknown category: {category_name}")
            print(f"Available: {', '.join(SEQUENCES.keys())}")
            return
        
        print(f"\n{'='*70}")
        print(f"📋 CATEGORY: {category_name}")
        print(f"   Sequences: {len(sequences)}")
        print(f"{'='*70}\n")
        
        for i, seq in enumerate(sequences):
            print(f"\n{'#'*70}")
            print(f"# SEQUENCE {i+1}/{len(sequences)}")
            print(f"{'#'*70}\n")
            
            self.run_sequence(seq)
            
            if i < len(sequences) - 1:
                print("\n⏸️  Brief pause before next sequence...")
                time.sleep(2)
        
        print("\n" + "="*70)
        print("🎉 ALL SEQUENCES COMPLETE!")
        print("="*70)

def main():
    if len(sys.argv) < 2:
        print("Usage: python automate_sequences.py <category>")
        print("\nAvailable categories:")
        for cat in SEQUENCES.keys():
            seqs = SEQUENCES[cat]
            print(f"  {cat:20s} - {len(seqs)} sequences")
        print("\nRecommended: demo_friendly")
        sys.exit(1)
    
    category = sys.argv[1]
    
    automator = SequenceAutomator()
    
    # Launch and setup
    automator.launch_hyperspeedcube()
    
    if not automator.find_and_focus_window():
        print("❌ Could not find Hyperspeedcube window")
        sys.exit(1)
    
    automator.load_3x3x3x3()
    
    # Initial instructions
    print("\n" + "="*70)
    print("🎬 AUTOMATED SEQUENCE EXECUTION WITH MANUAL RECORDING")
    print("="*70)
    print("\nHow this works:")
    print("  1. You'll be prompted before each sequence")
    print("  2. Start your screen recorder (SimpleScreenRecorder recommended)")
    print("  3. Press ENTER - the script executes the moves automatically")
    print("  4. Stop your recorder when sequence completes")
    print("  5. Save the video and repeat for next sequence")
    print("\nReady to begin?")
    input("Press ENTER to start... ")
    
    # Run sequences
    automator.run_category(category)
    
    print("\n📁 Remember to save your recordings to:")
    print("   disp/recordings/<sequence_name>.mp4")
    print("\n💡 Convert to GIFs with:")
    print("   cd disp")
    print("   nix develop --command ./scripts/video_to_gif.sh \\")
    print("     recordings/<name>.mp4 figures/sequence_<name>.gif 640 20")

if __name__ == "__main__":
    main()
