#!/usr/bin/env python3
"""
Reclassify existing Lyapunov results with new data-driven thresholds.

This script updates the classification in existing lyapunov_*.json files
without rerunning the expensive analysis.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

def classify_lambda(lam: float) -> str:
    """Apply new data-driven classification."""
    if lam == 0.0:
        return "trivial"
    elif lam < 2.0:
        return "weakly_chaotic"
    elif lam < 4.0:
        return "strongly_chaotic"
    else:
        return "extremely_chaotic"

def main():
    logs_dir = Path(__file__).parent.parent / "logs"

    # Find all lyapunov JSON files
    lyapunov_files = list(logs_dir.glob("lyapunov_*.json"))
    lyapunov_files = [f for f in lyapunov_files if f.name != "lyapunov_summary.json"]

    print(f"Found {len(lyapunov_files)} Lyapunov result files")
    print("Reclassifying with new thresholds...")

    updated_count = 0

    for json_file in lyapunov_files:
        try:
            # Read
            with open(json_file) as f:
                data = json.load(f)

            # Get lambda
            lam = data.get('lyapunov_exponent', 0.0)
            old_class = data.get('classification', 'unknown')

            # Reclassify
            new_class = classify_lambda(lam)

            # Update if changed
            if old_class != new_class:
                data['classification'] = new_class

                # Write back
                with open(json_file, 'w') as f:
                    json.dump(data, f, indent=2)

                updated_count += 1
                print(f"  {json_file.name}: {old_class} → {new_class} (λ={lam:.3f})")

        except Exception as e:
            print(f"  ERROR processing {json_file.name}: {e}")

    print(f"\nUpdated {updated_count}/{len(lyapunov_files)} files")

    # Now regenerate summary and CSV
    print("\nRegenerating summary and CSV...")
    from obsv.lyapunov import LyapunovAnalyzer

    analyzer = LyapunovAnalyzer()

    # Load all results
    from obsv.lyapunov import LyapunovResult
    results = []

    for json_file in lyapunov_files:
        with open(json_file) as f:
            data = json.load(f)

        result = LyapunovResult(
            sequence=data['move_sequence'],
            base_period=data['base_period'],
            lyapunov_exponent=data['lyapunov_exponent'],
            perturbations_tested=data['perturbations_tested'],
            period_ratios=data['period_ratios'],
            divergence_scores=data['divergence_scores'],
            classification=data['classification']
        )
        results.append(result)

    # Generate new summary
    analyzer.print_summary(results)

    print("\nDone! New classifications:")
    print("  - trivial: λ = 0.0 (single moves)")
    print("  - weakly_chaotic: 0 < λ < 2.0")
    print("  - strongly_chaotic: 2.0 ≤ λ < 4.0")
    print("  - extremely_chaotic: λ ≥ 4.0")

if __name__ == "__main__":
    main()