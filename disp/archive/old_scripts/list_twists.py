#!/usr/bin/env python3
"""List available twist names for 3×3×3×3 puzzle"""
import subprocess
import json

result = subprocess.run(
    ["hyperspeedcube", "puzzle", "ft_hypercube:3"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    data = json.loads(result.stdout)
    print("Available twists for 3×3×3×3:")
    print("="*60)
    if "twists" in data:
        for twist in data["twists"]:
            print(f"  {twist}")
    else:
        print(json.dumps(data, indent=2))
else:
    print("Error:", result.stderr)
