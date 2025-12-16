#!/usr/bin/env python3
"""
Manual recording guide - simplest approach that will definitely work
"""
import subprocess
from pathlib import Path

sequences = [
    {
        "name": "FR_single",
        "moves": ["FR"],
        "cycles": 8,
        "total": 8,
    },
    {
        "name": "FO_FO",
        "moves": ["FO", "FO"],
        "cycles": 4,
        "total": 8,
    },
    {
        "name": "FR_FR",
        "moves": ["FR", "FR"],
        "cycles": 4,
        "total": 8,
    },
]

print()
print("╔═══════════════════════════════════════════════════════╗")
print("║  Manual Recording Guide (Quick & Easy!)              ║")
print("╚═══════════════════════════════════════════════════════╝")
print()
print("Since keybind automation is tricky, let's do it manually.")
print("This will take ~5 minutes total and definitely work!")
print()
print("Setup:")
print("  1. Open Hyperspeedcube in one window")
print("  2. Open SimpleScreenRecorder (or use your recording tool)")
print("  3. Set it to record the Hyperspeedcube window")
print()

for i, seq in enumerate(sequences, 1):
    print()
    print(f"{'='*60}")
    print(f"SEQUENCE {i}/3: {seq['name']}")
    print(f"{'='*60}")
    print()
    print(f"Moves to perform: {' → '.join(seq['moves'])}")
    print(f"Repeat: {seq['cycles']} times")
    print(f"Total moves: {seq['total']}")
    print()
    print("Steps:")
    print("  1. In Hyperspeedcube: Press Ctrl+R to reset")
    print("  2. Start screen recording")
    print("  3. Click the twist buttons in Puzzle Controls tab:")
    
    move_list = []
    for cycle in range(seq['cycles']):
        for move in seq['moves']:
            move_list.append(move)
    
    print(f"     {', '.join(move_list)}")
    print("     (Click each button, wait for animation)")
    print()
    print("  4. Stop recording")
    print(f"  5. Save as: recordings/{seq['name']}.mp4")
    print()
    input(f"Press Enter when {seq['name']} recording is saved...")

print()
print(f"{'='*60}")
print("✅ All recordings complete!")
print(f"{'='*60}")
print()
print("Convert to GIFs:")
print()
print("cd disp")
print("nix develop --command bash -c \"")
for seq in sequences:
    print(f"  ./scripts/video_to_gif.sh recordings/{seq['name']}.mp4 figures/sequence_{seq['name']}.gif 640 20")
print("\"")
print()
