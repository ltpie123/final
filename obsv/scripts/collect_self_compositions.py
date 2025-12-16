#!/usr/bin/env python3
"""
Collect Self-Composition Sequences

Tests all 12 self-compositions (X→X) to understand how repeating
a single move affects chaotic behavior.

Key question: Is FR→FR's extreme chaos (λ=5.94) unique, or do other
self-compositions also exhibit high sensitivity?
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from obsv.lyapunov import LyapunovAnalyzer


def main():
    # All 12 base moves (6 faces × 2 directions)
    moves = ["FR", "FL", "FU", "FO", "RF", "RO", "UR", "UF", "UO", "UL", "OR", "OL"]

    print("="*70)
    print("SELF-COMPOSITION ANALYSIS")
    print("="*70)
    print(f"\nCollecting Lyapunov data for all {len(moves)} self-compositions")
    print("(X→X for each move X)\n")

    # Create sequences
    sequences = [[move, move] for move in moves]

    print("Sequences to analyze:")
    for i, seq in enumerate(sequences, 1):
        print(f"  {i:2d}. {' → '.join(seq)}")

    # Run analysis
    print(f"\n{'='*70}")
    print("Starting parallel analysis...")
    print(f"{'='*70}\n")

    analyzer = LyapunovAnalyzer()
    results = analyzer.analyze_sequence_batch(sequences, n_perturbations=10, parallel=True, max_workers=4)

    # Print results
    print(f"\n{'='*70}")
    print("RESULTS: Self-Composition Sensitivity")
    print(f"{'='*70}\n")

    # Sort by Lyapunov exponent
    sorted_results = sorted(results, key=lambda r: r.lyapunov_exponent, reverse=True)

    print(f"{'Sequence':<20} {'λ':<10} {'Period':<10} {'Classification':<20}")
    print("-" * 70)

    for result in sorted_results:
        seq_str = " → ".join(result.sequence)
        print(f"{seq_str:<20} {result.lyapunov_exponent:>8.3f}  "
              f"{result.base_period:>8}  {result.classification:<20}")

    # Analysis summary
    print(f"\n{'='*70}")
    print("KEY FINDINGS")
    print(f"{'='*70}\n")

    chaotic_count = sum(1 for r in results if r.classification != 'trivial')
    print(f"Chaotic self-compositions: {chaotic_count}/{len(results)}")

    if chaotic_count > 0:
        max_lambda = max(r.lyapunov_exponent for r in results)
        min_lambda = min(r.lyapunov_exponent for r in results if r.lyapunov_exponent > 0)
        print(f"Lyapunov range: {min_lambda:.3f} to {max_lambda:.3f}")

    # Identify patterns
    print("\nMove patterns:")

    # Group by first letter (face)
    face_groups = {}
    for result in results:
        face = result.sequence[0][0]  # First letter of move
        if face not in face_groups:
            face_groups[face] = []
        face_groups[face].append(result)

    for face in sorted(face_groups.keys()):
        group = face_groups[face]
        avg_lambda = sum(r.lyapunov_exponent for r in group) / len(group)
        print(f"  {face}-face moves: {len(group)} sequences, avg λ={avg_lambda:.3f}")

    print("\nData saved to obsv/logs/")
    print("Run extended_analysis.py again to see updated self-composition results")


if __name__ == "__main__":
    main()