#!/usr/bin/env python3
"""
Random sequence testing suite for chaos detection and statistical analysis.
"""

import json
import time
import random
from pathlib import Path
from typing import List, Dict, Tuple
from collections import defaultdict
import numpy as np

from .ctrl_runner import CtrlRunner, MoveGenerator


class RandomSequenceTester:
    """Test suite for random sequence analysis."""

    def __init__(self, output_dir: Path = None):
        """Initialize tester.

        Args:
            output_dir: Directory to save results
        """
        if output_dir is None:
            output_dir = Path(__file__).parent / "logs"
        self.output_dir = output_dir
        self.output_dir.mkdir(exist_ok=True, parents=True)

        self.runner = CtrlRunner()
        self.generator = MoveGenerator()

    def test_random_batch(
        self,
        count: int = 100,
        min_length: int = 2,
        max_length: int = 6,
        max_iterations: int = 50000,
        save_results: bool = True
    ) -> List[Dict]:
        """Run a batch of random sequences.

        Args:
            count: Number of random sequences to test
            min_length: Minimum sequence length
            max_length: Maximum sequence length
            max_iterations: Max iterations per sequence
            save_results: Save individual JSON results

        Returns:
            List of result dictionaries
        """
        print(f"Generating {count} random sequences...")
        sequences = self.generator.generate_random_batch(
            count, min_length, max_length,
            allow_repeats=False  # More interesting sequences
        )

        results = []
        start_time = time.time()

        for i, seq in enumerate(sequences, 1):
            print(f"[{i}/{count}] Testing: {' → '.join(seq)}", end=" ... ")

            try:
                # Generate unique filename
                seq_name = "_".join(seq)
                if save_results:
                    output_file = self.output_dir / f"results_random_{i:03d}_{seq_name}.json"
                else:
                    output_file = self.output_dir / "temp_random.json"

                result = self.runner.run_sequence(
                    seq,
                    max_iterations=max_iterations,
                    output_file=output_file
                )

                print(f"period={result['period']:,}")
                results.append(result)

            except Exception as e:
                print(f"FAILED: {e}")
                continue

        elapsed = time.time() - start_time
        print(f"\nCompleted {len(results)}/{count} sequences in {elapsed:.1f}s")

        return results

    def analyze_chaos(self, sequences: List[List[str]], perturbation_size: int = 1,
                     max_iterations: int = 50000) -> Dict:
        """Test for chaotic behavior via sensitivity analysis.

        For each sequence, perturb it slightly and measure divergence.

        Args:
            sequences: Base sequences to test
            perturbation_size: How many moves to change
            max_iterations: Max iterations per test

        Returns:
            Dictionary with chaos metrics
        """
        print("Testing for chaotic behavior...")

        divergences = []
        sensitivity_scores = []

        for seq in sequences:
            # Run original sequence
            result_orig = self.runner.run_sequence(seq, max_iterations)

            # Perturb: change one random move
            perturbed = seq.copy()
            idx = random.randint(0, len(seq) - 1)
            perturbed[idx] = random.choice(self.generator.COMMON_MOVES)

            # Run perturbed sequence
            result_pert = self.runner.run_sequence(perturbed, max_iterations)

            # Measure divergence
            period_diff = abs(result_orig['period'] - result_pert['period'])
            period_ratio = max(result_orig['period'], result_pert['period']) / \
                          min(result_orig['period'], result_pert['period'])

            divergences.append(period_diff)
            sensitivity_scores.append(period_ratio)

            print(f"  {' → '.join(seq)}: {result_orig['period']} → {result_pert['period']} "
                  f"(ratio: {period_ratio:.2f})")

        return {
            'mean_divergence': np.mean(divergences),
            'std_divergence': np.std(divergences),
            'mean_sensitivity': np.mean(sensitivity_scores),
            'max_sensitivity': np.max(sensitivity_scores),
            'chaotic_sequences': sum(1 for s in sensitivity_scores if s > 2.0),
            'total_tested': len(sequences)
        }

    def compare_strategic_vs_random(self, random_results: List[Dict],
                                   strategic_file: Path = None) -> Dict:
        """Compare random sequences vs strategically chosen ones.

        Args:
            random_results: Results from random testing
            strategic_file: Path to curated results (default: analyze existing logs)

        Returns:
            Comparison statistics
        """
        print("Comparing random vs strategic sequences...")

        # Load strategic results
        if strategic_file is None:
            strategic_results = []
            for json_file in self.output_dir.glob("results_[!r]*.json"):  # Exclude random_
                try:
                    with open(json_file) as f:
                        strategic_results.append(json.load(f))
                except:
                    continue

        random_periods = [r['period'] for r in random_results]
        strategic_periods = [r['period'] for r in strategic_results]

        comparison = {
            'random': {
                'count': len(random_periods),
                'mean': np.mean(random_periods),
                'median': np.median(random_periods),
                'std': np.std(random_periods),
                'max': np.max(random_periods),
                'min': np.min(random_periods),
            },
            'strategic': {
                'count': len(strategic_periods),
                'mean': np.mean(strategic_periods),
                'median': np.median(strategic_periods),
                'std': np.std(strategic_periods),
                'max': np.max(strategic_periods),
                'min': np.min(strategic_periods),
            }
        }

        # Statistical test
        from scipy import stats
        t_stat, p_value = stats.ttest_ind(random_periods, strategic_periods)
        comparison['statistical_test'] = {
            't_statistic': t_stat,
            'p_value': p_value,
            'significantly_different': p_value < 0.05
        }

        # Calculate percentile of max strategic in random distribution
        max_strategic = comparison['strategic']['max']
        percentile = sum(1 for p in random_periods if p < max_strategic) / len(random_periods) * 100
        comparison['max_strategic_percentile'] = percentile

        return comparison

    def analyze_period_distribution(self, results: List[Dict]) -> Dict:
        """Analyze statistical properties of period distribution.

        Args:
            results: List of trajectory results

        Returns:
            Statistical analysis dictionary
        """
        periods = [r['period'] for r in results]

        # Group by sequence length
        by_length = defaultdict(list)
        for r in results:
            length = len(r['move_sequence'])
            by_length[length].append(r['period'])

        analysis = {
            'overall': {
                'count': len(periods),
                'mean': np.mean(periods),
                'median': np.median(periods),
                'std': np.std(periods),
                'min': np.min(periods),
                'max': np.max(periods),
                'percentiles': {
                    '25': np.percentile(periods, 25),
                    '50': np.percentile(periods, 50),
                    '75': np.percentile(periods, 75),
                    '90': np.percentile(periods, 90),
                    '95': np.percentile(periods, 95),
                    '99': np.percentile(periods, 99),
                }
            },
            'by_length': {}
        }

        for length, length_periods in sorted(by_length.items()):
            analysis['by_length'][length] = {
                'count': len(length_periods),
                'mean': np.mean(length_periods),
                'median': np.median(length_periods),
                'max': np.max(length_periods),
            }

        return analysis

    def print_summary(self, results: List[Dict], comparison: Dict = None,
                     chaos: Dict = None):
        """Print formatted summary of results.

        Args:
            results: Test results
            comparison: Strategic vs random comparison
            chaos: Chaos analysis results
        """
        print("\n" + "="*70)
        print("RANDOM SEQUENCE ANALYSIS SUMMARY")
        print("="*70)

        periods = [r['period'] for r in results]

        print(f"\nTotal sequences tested: {len(results)}")
        print(f"Mean period: {np.mean(periods):,.1f}")
        print(f"Median period: {np.median(periods):,.0f}")
        print(f"Std deviation: {np.std(periods):,.1f}")
        print(f"Range: [{np.min(periods)} - {np.max(periods):,}]")

        print("\nPercentiles:")
        for p in [25, 50, 75, 90, 95, 99]:
            print(f"  {p:2d}th: {np.percentile(periods, p):>10,.0f}")

        if comparison:
            print("\n" + "-"*70)
            print("RANDOM vs STRATEGIC COMPARISON")
            print("-"*70)
            print(f"\nRandom sequences:")
            print(f"  Mean period: {comparison['random']['mean']:,.1f}")
            print(f"  Max period:  {comparison['random']['max']:,}")

            print(f"\nStrategic sequences:")
            print(f"  Mean period: {comparison['strategic']['mean']:,.1f}")
            print(f"  Max period:  {comparison['strategic']['max']:,}")

            print(f"\nStatistical significance: p={comparison['statistical_test']['p_value']:.4f}")
            if comparison['statistical_test']['significantly_different']:
                print("  ✓ Strategic selection produces significantly different periods")
            else:
                print("  ✗ No significant difference detected")

            print(f"\nOur record of {comparison['strategic']['max']:,} is at the "
                  f"{comparison['max_strategic_percentile']:.1f}th percentile of random sequences")

        if chaos:
            print("\n" + "-"*70)
            print("CHAOS ANALYSIS")
            print("-"*70)
            print(f"\nMean sensitivity ratio: {chaos['mean_sensitivity']:.2f}")
            print(f"Max sensitivity ratio: {chaos['max_sensitivity']:.2f}")
            print(f"Sequences with >2x sensitivity: {chaos['chaotic_sequences']}/{chaos['total_tested']}")
            if chaos['mean_sensitivity'] > 2.0:
                print("  ✓ System shows chaotic behavior (high sensitivity)")
            else:
                print("  ○ System shows moderate sensitivity")

        print("\n" + "="*70)


def main():
    """Main entry point for random sequence testing."""
    import argparse

    parser = argparse.ArgumentParser(description="Random sequence testing suite")
    parser.add_argument("--count", type=int, default=100,
                       help="Number of random sequences to test")
    parser.add_argument("--min-length", type=int, default=2,
                       help="Minimum sequence length")
    parser.add_argument("--max-length", type=int, default=6,
                       help="Maximum sequence length")
    parser.add_argument("--chaos", action="store_true",
                       help="Run chaos sensitivity analysis")
    parser.add_argument("--compare", action="store_true",
                       help="Compare with strategic sequences")
    parser.add_argument("--max-iterations", type=int, default=50000,
                       help="Max iterations per sequence")

    args = parser.parse_args()

    tester = RandomSequenceTester()

    # Run random batch
    results = tester.test_random_batch(
        count=args.count,
        min_length=args.min_length,
        max_length=args.max_length,
        max_iterations=args.max_iterations
    )

    # Analyze distribution
    distribution = tester.analyze_period_distribution(results)

    # Optional analyses
    comparison = None
    if args.compare:
        comparison = tester.compare_strategic_vs_random(results)

    chaos = None
    if args.chaos:
        # Test a subset for chaos (expensive)
        test_sequences = [r['move_sequence'] for r in results[:10]]
        chaos = tester.analyze_chaos(test_sequences)

    # Print summary
    tester.print_summary(results, comparison, chaos)

    # Save summary (convert numpy types to native Python)
    def convert_numpy(obj):
        """Recursively convert numpy types to Python native types."""
        if isinstance(obj, dict):
            return {k: convert_numpy(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_numpy(item) for item in obj]
        elif isinstance(obj, (np.integer, np.floating)):
            return obj.item()
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return obj

    summary_file = tester.output_dir / "random_test_summary.json"
    with open(summary_file, 'w') as f:
        json.dump(convert_numpy({
            'distribution': distribution,
            'comparison': comparison,
            'chaos': chaos,
        }), f, indent=2)
    print(f"\nSummary saved to: {summary_file}")


if __name__ == "__main__":
    main()
