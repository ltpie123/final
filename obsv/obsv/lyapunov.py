#!/usr/bin/env python3
"""
Lyapunov-like Exponent Analysis for Discrete Puzzle Dynamics

Implements a discrete analog of the Lyapunov exponent to measure sensitivity
to perturbations in move sequences. Positive exponents indicate chaotic-like
behavior (high sensitivity), while near-zero exponents indicate regular dynamics.

Reference: docs/ADDITIONAL_ANALYSES.md, Section 4
"""

import json
import numpy as np
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from collections import defaultdict
import random
from dataclasses import dataclass

from .ctrl_runner import CtrlRunner, MoveGenerator


@dataclass
class LyapunovResult:
    """Result of Lyapunov exponent calculation."""
    sequence: List[str]
    base_period: int
    lyapunov_exponent: float
    perturbations_tested: int
    period_ratios: List[float]
    divergence_scores: List[float]
    classification: str  # "chaotic", "regular", or "stable"


class LyapunovAnalyzer:
    """Compute discrete Lyapunov-like exponents for puzzle dynamics."""

    def __init__(self, output_dir: Path = None):
        """Initialize analyzer.

        Args:
            output_dir: Directory for logs and results
        """
        if output_dir is None:
            output_dir = Path(__file__).parent.parent / "logs"
        self.output_dir = output_dir
        self.output_dir.mkdir(exist_ok=True, parents=True)

        self.runner = CtrlRunner()
        self.generator = MoveGenerator()

    def compute_lyapunov_exponent(
        self,
        sequence: List[str],
        n_perturbations: int = 10,
        max_iterations: int = 50000,
        perturbation_type: str = "substitute"
    ) -> LyapunovResult:
        """Compute discrete Lyapunov exponent for a sequence.

        The discrete Lyapunov exponent is defined as:
            λ(S) = (1/n) Σ log|Period(S_perturbed) / Period(S)|

        where S_perturbed differs from S by a small perturbation.

        Args:
            sequence: Base move sequence
            n_perturbations: Number of perturbations to test
            max_iterations: Max iterations per trajectory
            perturbation_type: Type of perturbation ('substitute', 'swap', 'insert', 'delete')

        Returns:
            LyapunovResult with exponent and diagnostics
        """
        print(f"\nComputing Lyapunov exponent for: {' → '.join(sequence)}")

        # Run base sequence
        print(f"  Base sequence...", end=" ")
        base_result = self.runner.run_sequence(sequence, max_iterations)
        base_period = base_result['period']
        print(f"period={base_period:,}")

        # Generate and test perturbations
        period_ratios = []
        divergence_scores = []

        for i in range(n_perturbations):
            perturbed = self._perturb_sequence(sequence, perturbation_type)

            print(f"  Perturbation {i+1}/{n_perturbations}: {' → '.join(perturbed)}", end=" ... ")

            try:
                result = self.runner.run_sequence(perturbed, max_iterations)
                pert_period = result['period']

                # Compute ratio (always >= 1)
                ratio = max(pert_period, base_period) / min(pert_period, base_period)
                period_ratios.append(ratio)

                # Compute divergence
                divergence = abs(pert_period - base_period)
                divergence_scores.append(divergence)

                print(f"period={pert_period:,}, ratio={ratio:.2f}")

            except Exception as e:
                print(f"FAILED: {e}")
                continue

        if not period_ratios:
            raise ValueError("All perturbations failed!")

        # Compute Lyapunov exponent: λ = (1/n) Σ log(ratio)
        log_ratios = [np.log(r) for r in period_ratios]
        lyapunov = np.mean(log_ratios)

        # Classify behavior
        if lyapunov > 0.69:  # log(2) ≈ 0.69
            classification = "chaotic"
        elif lyapunov > 0.1:
            classification = "sensitive"
        else:
            classification = "regular"

        print(f"  → Lyapunov exponent: λ = {lyapunov:.3f} ({classification})")

        return LyapunovResult(
            sequence=sequence,
            base_period=base_period,
            lyapunov_exponent=lyapunov,
            perturbations_tested=len(period_ratios),
            period_ratios=period_ratios,
            divergence_scores=divergence_scores,
            classification=classification
        )

    def _perturb_sequence(
        self,
        sequence: List[str],
        perturbation_type: str = "substitute"
    ) -> List[str]:
        """Apply a single perturbation to the sequence.

        Args:
            sequence: Original move sequence
            perturbation_type: Type of perturbation

        Returns:
            Perturbed sequence
        """
        perturbed = sequence.copy()

        if perturbation_type == "substitute":
            # Replace one move with a different move
            idx = random.randint(0, len(perturbed) - 1)
            candidates = [m for m in self.generator.COMMON_MOVES if m != perturbed[idx]]
            perturbed[idx] = random.choice(candidates)

        elif perturbation_type == "swap":
            # Swap two adjacent moves
            if len(perturbed) < 2:
                # Fall back to substitute for 1-move sequences
                idx = 0
                candidates = [m for m in self.generator.COMMON_MOVES if m != perturbed[idx]]
                perturbed[idx] = random.choice(candidates)
            else:
                idx = random.randint(0, len(perturbed) - 2)
                perturbed[idx], perturbed[idx + 1] = perturbed[idx + 1], perturbed[idx]

        elif perturbation_type == "insert":
            # Insert a random move
            idx = random.randint(0, len(perturbed))
            new_move = random.choice(self.generator.COMMON_MOVES)
            perturbed.insert(idx, new_move)

        elif perturbation_type == "delete":
            # Delete a move (if sequence length > 1)
            if len(perturbed) > 1:
                idx = random.randint(0, len(perturbed) - 1)
                perturbed.pop(idx)
            else:
                # Fall back to substitute for single moves
                perturbed[0] = random.choice([m for m in self.generator.COMMON_MOVES
                                             if m != perturbed[0]])

        else:
            raise ValueError(f"Unknown perturbation type: {perturbation_type}")

        return perturbed

    def analyze_sequence_batch(
        self,
        sequences: List[List[str]],
        n_perturbations: int = 10,
        perturbation_type: str = "substitute",
        save_results: bool = True
    ) -> List[LyapunovResult]:
        """Analyze multiple sequences.

        Args:
            sequences: List of move sequences
            n_perturbations: Perturbations per sequence
            perturbation_type: Type of perturbation
            save_results: Save individual results to JSON

        Returns:
            List of LyapunovResult objects
        """
        results = []

        print(f"Analyzing {len(sequences)} sequences...")

        for i, seq in enumerate(sequences, 1):
            print(f"\n[{i}/{len(sequences)}] " + "="*60)

            try:
                result = self.compute_lyapunov_exponent(
                    seq,
                    n_perturbations=n_perturbations,
                    perturbation_type=perturbation_type
                )
                results.append(result)

                if save_results:
                    self._save_result(result, i)

            except Exception as e:
                print(f"ERROR: Failed to analyze {' → '.join(seq)}: {e}")
                continue

        return results

    def analyze_from_logs(
        self,
        n_perturbations: int = 10,
        max_sequences: Optional[int] = None
    ) -> List[LyapunovResult]:
        """Analyze sequences from existing result logs.

        Args:
            n_perturbations: Perturbations per sequence
            max_sequences: Maximum number of sequences to analyze (None = all)

        Returns:
            List of LyapunovResult objects
        """
        print("Loading sequences from logs...")

        # Load existing results
        json_files = list(self.output_dir.glob("results_*.json"))

        # Exclude lyapunov results and random tests
        json_files = [f for f in json_files
                     if "lyapunov" not in f.name and "random" not in f.name]

        if max_sequences:
            json_files = json_files[:max_sequences]

        sequences = []
        for json_file in json_files:
            try:
                with open(json_file) as f:
                    data = json.load(f)
                    seq = data.get('move_sequence', [])
                    if seq:
                        sequences.append(seq)
            except Exception as e:
                print(f"Warning: Could not load {json_file}: {e}")

        print(f"Loaded {len(sequences)} sequences")

        return self.analyze_sequence_batch(
            sequences,
            n_perturbations=n_perturbations
        )

    def _save_result(self, result: LyapunovResult, index: int):
        """Save a single result to JSON."""
        seq_name = "_".join(result.sequence)
        filename = f"lyapunov_{index:03d}_{seq_name}.json"
        filepath = self.output_dir / filename

        data = {
            'move_sequence': result.sequence,
            'base_period': result.base_period,
            'lyapunov_exponent': result.lyapunov_exponent,
            'perturbations_tested': result.perturbations_tested,
            'period_ratios': result.period_ratios,
            'divergence_scores': result.divergence_scores,
            'classification': result.classification,
            'statistics': {
                'mean_ratio': float(np.mean(result.period_ratios)),
                'std_ratio': float(np.std(result.period_ratios)),
                'max_ratio': float(np.max(result.period_ratios)),
                'mean_divergence': float(np.mean(result.divergence_scores)),
                'max_divergence': float(np.max(result.divergence_scores)),
            }
        }

        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

    def generate_summary_report(
        self,
        results: List[LyapunovResult]
    ) -> Dict:
        """Generate summary statistics from results.

        Args:
            results: List of LyapunovResult objects

        Returns:
            Summary dictionary
        """
        if not results:
            return {}

        # Group by sequence length
        by_length = defaultdict(list)
        for r in results:
            by_length[len(r.sequence)].append(r)

        # Overall statistics
        exponents = [r.lyapunov_exponent for r in results]
        classifications = [r.classification for r in results]

        summary = {
            'total_sequences': len(results),
            'overall': {
                'mean_lambda': float(np.mean(exponents)),
                'median_lambda': float(np.median(exponents)),
                'std_lambda': float(np.std(exponents)),
                'min_lambda': float(np.min(exponents)),
                'max_lambda': float(np.max(exponents)),
            },
            'classifications': {
                'chaotic': classifications.count('chaotic'),
                'sensitive': classifications.count('sensitive'),
                'regular': classifications.count('regular'),
            },
            'by_length': {}
        }

        # By length statistics
        for length, length_results in sorted(by_length.items()):
            length_exponents = [r.lyapunov_exponent for r in length_results]
            summary['by_length'][length] = {
                'count': len(length_results),
                'mean_lambda': float(np.mean(length_exponents)),
                'median_lambda': float(np.median(length_exponents)),
                'max_lambda': float(np.max(length_exponents)),
                'most_chaotic': {
                    'sequence': ' → '.join(max(length_results,
                                             key=lambda r: r.lyapunov_exponent).sequence),
                    'lambda': float(max(length_exponents))
                }
            }

        return summary

    def export_to_csv(self, results: List[LyapunovResult],
                     output_file: Optional[Path] = None):
        """Export results to CSV for Octave/MATLAB analysis.

        Args:
            results: List of LyapunovResult objects
            output_file: Path to output CSV (default: logs/lyapunov_data.csv)
        """
        if output_file is None:
            output_file = self.output_dir / "lyapunov_data.csv"

        import csv

        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)

            # Header
            writer.writerow([
                'sequence',
                'sequence_length',
                'base_period',
                'lyapunov_exponent',
                'classification',
                'perturbations_tested',
                'mean_ratio',
                'std_ratio',
                'max_ratio',
                'mean_divergence',
                'max_divergence'
            ])

            # Data rows
            for r in results:
                writer.writerow([
                    ' → '.join(r.sequence),
                    len(r.sequence),
                    r.base_period,
                    r.lyapunov_exponent,
                    r.classification,
                    r.perturbations_tested,
                    float(np.mean(r.period_ratios)),
                    float(np.std(r.period_ratios)),
                    float(np.max(r.period_ratios)),
                    float(np.mean(r.divergence_scores)),
                    float(np.max(r.divergence_scores))
                ])

        print(f"CSV data exported to: {output_file}")

    def print_summary(self, results: List[LyapunovResult]):
        """Print formatted summary of results."""
        summary = self.generate_summary_report(results)

        print("\n" + "="*70)
        print("LYAPUNOV EXPONENT ANALYSIS SUMMARY")
        print("="*70)

        print(f"\nTotal sequences analyzed: {summary['total_sequences']}")

        print("\nOverall Statistics:")
        print(f"  Mean λ:   {summary['overall']['mean_lambda']:.3f}")
        print(f"  Median λ: {summary['overall']['median_lambda']:.3f}")
        print(f"  Std λ:    {summary['overall']['std_lambda']:.3f}")
        print(f"  Range:    [{summary['overall']['min_lambda']:.3f}, "
              f"{summary['overall']['max_lambda']:.3f}]")

        print("\nClassifications:")
        for cls, count in summary['classifications'].items():
            pct = 100 * count / summary['total_sequences']
            print(f"  {cls:10s}: {count:3d} sequences ({pct:5.1f}%)")

        print("\nBy Sequence Length:")
        for length, stats in sorted(summary['by_length'].items()):
            print(f"\n  {length}-move sequences: {stats['count']} tested")
            print(f"    Mean λ:   {stats['mean_lambda']:.3f}")
            print(f"    Median λ: {stats['median_lambda']:.3f}")
            print(f"    Max λ:    {stats['max_lambda']:.3f}")
            print(f"    Most chaotic: {stats['most_chaotic']['sequence']} "
                  f"(λ={stats['most_chaotic']['lambda']:.3f})")

        print("\n" + "="*70)

        # Save summary
        summary_file = self.output_dir / "lyapunov_summary.json"
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2)
        print(f"\nSummary saved to: {summary_file}")

        # Export CSV for Octave
        self.export_to_csv(results)


def main():
    """Main entry point for Lyapunov analysis."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Lyapunov exponent analysis for puzzle dynamics"
    )
    parser.add_argument("--from-logs", action="store_true",
                       help="Analyze sequences from existing logs")
    parser.add_argument("--sequences", type=str, nargs="+",
                       help="Specific sequences to analyze (comma-separated moves)")
    parser.add_argument("--n-perturbations", type=int, default=10,
                       help="Number of perturbations per sequence")
    parser.add_argument("--perturbation-type",
                       choices=["substitute", "swap", "insert", "delete"],
                       default="substitute",
                       help="Type of perturbation to apply")
    parser.add_argument("--max-sequences", type=int,
                       help="Maximum sequences to analyze from logs")

    args = parser.parse_args()

    analyzer = LyapunovAnalyzer()

    if args.from_logs:
        # Analyze from existing logs
        results = analyzer.analyze_from_logs(
            n_perturbations=args.n_perturbations,
            max_sequences=args.max_sequences
        )
    elif args.sequences:
        # Analyze specific sequences
        sequences = [seq.split(',') for seq in args.sequences]
        results = analyzer.analyze_sequence_batch(
            sequences,
            n_perturbations=args.n_perturbations,
            perturbation_type=args.perturbation_type
        )
    else:
        # Default: analyze a few interesting sequences
        print("No input specified. Analyzing default sequences...")
        sequences = [
            ["FR", "UF"],           # High period (10,080)
            ["FR", "UF", "OR"],     # Medium period (2,160)
            ["OF", "OU"],           # Low period (6)
            ["FR", "UF", "OR", "RO"],  # Record period (41,496)
        ]
        results = analyzer.analyze_sequence_batch(
            sequences,
            n_perturbations=args.n_perturbations
        )

    # Print summary
    analyzer.print_summary(results)


if __name__ == "__main__":
    main()
