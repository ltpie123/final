#!/usr/bin/env python3
"""
Run Lyapunov exponent analysis on trajectory sequences.

This script computes discrete Lyapunov exponents to measure sensitivity
to perturbations in move sequences.
"""

import sys
from pathlib import Path

# Add parent directory to path so we can import obsv
sys.path.insert(0, str(Path(__file__).parent.parent))

from obsv.lyapunov import main

if __name__ == "__main__":
    main()