#!/usr/bin/env python3
"""
Launch Hyperspeedcube and guide user to check Help → Keybinds Reference
"""
import subprocess
import time

print("╔═══════════════════════════════════════════════════════╗")
print("║  Check Official Keybinds in Hyperspeedcube           ║")
print("╚═══════════════════════════════════════════════════════╝")
print()
print("Launching Hyperspeedcube...")
print()

proc = subprocess.Popen(["hyperspeedcube"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(6)

print("In Hyperspeedcube:")
print("  1. Go to Help → Keybinds reference (or press a help key)")
print("  2. Look for the keybind mappings for the 3×3×3×3 puzzle")
print("  3. Find how to perform 'FR' and 'FO' moves")
print()
print("Tell me:")
print("  • What keys grip the F (Front) face?")
print("  • What keys rotate toward R (Right)?")
print("  • What keys rotate toward O (Outside)?")
print()
print("OR: Just manually perform FR and FO and tell me which keys you pressed!")
print()
print("Press Ctrl+C when done checking...")

try:
    proc.wait()
except KeyboardInterrupt:
    proc.terminate()
    proc.wait()
    print("\nDone!")
