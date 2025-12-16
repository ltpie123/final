#!/usr/bin/env python3
"""
Collect All 2-Move Sequences for Heat Map

Systematically collects Lyapunov data for all 12×12 = 144 possible
2-move combinations to create a complete heat map showing which move
pairs exhibit chaotic behavior.

This will take approximately 30-60 minutes with parallel execution.
"""

import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from obsv.lyapunov import LyapunovAnalyzer


def get_existing_2move_sequences(logs_dir: Path) -> set:
    """Get set of already-analyzed 2-move sequences."""
    existing = set()

    json_files = list(logs_dir.glob("lyapunov_*.json"))
    json_files = [f for f in json_files if f.name != "lyapunov_summary.json"]

    for json_file in json_files:
        try:
            with open(json_file) as f:
                data = json.load(f)

            if len(data['move_sequence']) == 2:
                seq_tuple = tuple(data['move_sequence'])
                existing.add(seq_tuple)
        except Exception as e:
            print(f"Warning: Error reading {json_file}: {e}")

    return existing


def main():
    # All 12 base moves
    moves = ["FR", "FL", "FU", "FO", "RF", "RO", "UR", "UF", "UO", "UL", "OR", "OL"]

    # Generate all 12×12 = 144 combinations
    all_sequences = [[m1, m2] for m1 in moves for m2 in moves]

    print("="*70)
    print("2-MOVE SEQUENCE HEAT MAP DATA COLLECTION")
    print("="*70)
    print(f"\nTotal possible 2-move sequences: {len(all_sequences)}")

    # Check what we already have
    logs_dir = Path(__file__).parent.parent / "logs"
    existing = get_existing_2move_sequences(logs_dir)

    print(f"Already analyzed: {len(existing)}")
    print(f"Remaining to collect: {len(all_sequences) - len(existing)}")

    # Filter to only sequences we don't have yet
    missing_sequences = [
        seq for seq in all_sequences
        if tuple(seq) not in existing
    ]

    if not missing_sequences:
        print("\n✓ All 2-move sequences already collected!")
        print("  You can generate the heat map now.")
        return

    # Show sample of what we'll collect
    print(f"\nSample of sequences to collect:")
    for seq in missing_sequences[:10]:
        print(f"  {' → '.join(seq)}")
    if len(missing_sequences) > 10:
        print(f"  ... and {len(missing_sequences) - 10} more")

    # Estimate time
    est_time_min = len(missing_sequences) * 3 / 60  # ~3 sec per sequence with parallelism
    est_time_max = len(missing_sequences) * 6 / 60  # ~6 sec worst case
    print(f"\nEstimated time: {est_time_min:.1f}-{est_time_max:.1f} minutes")

    # Confirm
    response = input("\nProceed with collection? [y/N]: ")
    if response.lower() != 'y':
        print("Cancelled.")
        return

    # Run analysis
    print(f"\n{'='*70}")
    print("Starting parallel analysis...")
    print(f"{'='*70}\n")

    analyzer = LyapunovAnalyzer()
    results = analyzer.analyze_sequence_batch(missing_sequences, n_perturbations=10, parallel=True, max_workers=6)

    # Quick summary
    print(f"\n{'='*70}")
    print("COLLECTION COMPLETE")
    print(f"{'='*70}\n")

    print(f"Analyzed {len(results)} new sequences")
    print(f"Total 2-move sequences now: {len(existing) + len(results)}/{len(all_sequences)}")

    # Classification breakdown
    from collections import Counter
    classifications = Counter(r.classification for r in results)

    print("\nNew sequences by classification:")
    for cls in ['trivial', 'weakly_chaotic', 'strongly_chaotic', 'extremely_chaotic']:
        if cls in classifications:
            print(f"  {cls}: {classifications[cls]}")

    print("\nData saved to obsv/logs/")
    print("Run 'cd disp && octave plot_2move_heatmap.m' to generate heat map")


if __name__ == "__main__":
    main()