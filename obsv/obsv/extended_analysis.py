#!/usr/bin/env python3
"""
Extended Lyapunov Analysis Tools

Additional analyses beyond basic Lyapunov computation:
- Perturbation sensitivity distributions
- Divergence correlations
- Move pattern analysis
- Self-composition studies
"""

import json
from pathlib import Path
from typing import Dict, List, Tuple
from collections import Counter
import csv


def load_all_results(logs_dir: Path) -> List[Dict]:
    """Load all Lyapunov JSON results."""
    results = []

    json_files = list(logs_dir.glob("lyapunov_*.json"))
    json_files = [f for f in json_files if f.name != "lyapunov_summary.json"]

    for json_file in json_files:
        with open(json_file) as f:
            data = json.load(f)
            results.append(data)

    return results


def analyze_perturbation_distribution(results: List[Dict]) -> Dict:
    """
    Analyze the distribution of period ratios across all perturbations.

    Shows the "spectrum" of sensitivity - some perturbations cause massive
    period increases (2520×!) while others are mild.
    """
    all_ratios = []

    for result in results:
        sequence = " → ".join(result['move_sequence'])
        ratios = result['period_ratios']

        # Skip trivial sequences (ratio = 1.0 always)
        if result['classification'] != 'trivial':
            all_ratios.extend(ratios)

    # Statistics
    all_ratios.sort()
    n = len(all_ratios)

    analysis = {
        'total_perturbations': n,
        'min_ratio': min(all_ratios) if all_ratios else 0,
        'max_ratio': max(all_ratios) if all_ratios else 0,
        'median_ratio': all_ratios[n//2] if all_ratios else 0,
        'mean_ratio': sum(all_ratios) / n if all_ratios else 0,
        'ratios_over_100': sum(1 for r in all_ratios if r > 100),
        'ratios_over_1000': sum(1 for r in all_ratios if r > 1000),
        'all_ratios': all_ratios
    }

    # Histogram bins
    bins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
    histogram = {}
    for i in range(len(bins)):
        if i == 0:
            count = sum(1 for r in all_ratios if r <= bins[i])
            histogram[f"≤{bins[i]}"] = count
        else:
            count = sum(1 for r in all_ratios if bins[i-1] < r <= bins[i])
            histogram[f"{bins[i-1]}-{bins[i]}"] = count
    histogram[f">{bins[-1]}"] = sum(1 for r in all_ratios if r > bins[-1])

    analysis['histogram'] = histogram

    return analysis


def analyze_divergence_correlation(results: List[Dict]) -> Dict:
    """
    Analyze correlation between state space divergence and Lyapunov exponent.

    Does max divergence in state space predict sensitivity to perturbations?
    """
    data_points = []

    for result in results:
        sequence = " → ".join(result['move_sequence'])
        lam = result['lyapunov_exponent']
        max_div = result['statistics']['max_divergence']
        mean_div = result['statistics']['mean_divergence']
        classification = result['classification']

        data_points.append({
            'sequence': sequence,
            'lambda': lam,
            'max_divergence': max_div,
            'mean_divergence': mean_div,
            'classification': classification
        })

    return {'data_points': data_points}


def analyze_move_patterns(results: List[Dict]) -> Dict:
    """
    Analyze which moves appear most frequently in chaotic sequences.

    Identifies "chaos-inducing" moves and patterns.
    """
    # Count moves by classification
    move_counts = {
        'trivial': Counter(),
        'weakly_chaotic': Counter(),
        'strongly_chaotic': Counter(),
        'extremely_chaotic': Counter()
    }

    # Count move pairs
    pair_counts = {
        'trivial': Counter(),
        'weakly_chaotic': Counter(),
        'strongly_chaotic': Counter(),
        'extremely_chaotic': Counter()
    }

    for result in results:
        moves = result['move_sequence']
        classification = result['classification']

        # Individual moves
        for move in moves:
            move_counts[classification][move] += 1

        # Move pairs
        for i in range(len(moves) - 1):
            pair = f"{moves[i]}→{moves[i+1]}"
            pair_counts[classification][pair] += 1

    # Self-composition detection
    self_compositions = []
    for result in results:
        moves = result['move_sequence']
        if len(moves) == 2 and moves[0] == moves[1]:
            self_compositions.append({
                'move': moves[0],
                'lambda': result['lyapunov_exponent'],
                'classification': result['classification']
            })

    return {
        'move_counts': {k: dict(v.most_common()) for k, v in move_counts.items()},
        'pair_counts': {k: dict(v.most_common(5)) for k, v in pair_counts.items()},
        'self_compositions': self_compositions
    }


def export_for_octave(analysis_type: str, data: Dict, output_file: Path):
    """Export analysis data in format Octave can easily read (CSV)."""

    if analysis_type == "perturbation_distribution":
        # Export all ratios for histogram
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['period_ratio'])
            for ratio in data['all_ratios']:
                writer.writerow([ratio])

    elif analysis_type == "divergence_correlation":
        # Export divergence vs lambda points
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['sequence', 'lambda', 'max_divergence', 'mean_divergence', 'classification'])
            for point in data['data_points']:
                writer.writerow([
                    point['sequence'],
                    point['lambda'],
                    point['max_divergence'],
                    point['mean_divergence'],
                    point['classification']
                ])


def print_analysis_summary(results: List[Dict]):
    """Print comprehensive analysis summary."""

    print("\n" + "="*70)
    print("EXTENDED LYAPUNOV ANALYSIS")
    print("="*70)

    # Perturbation distribution
    print("\n1. PERTURBATION SENSITIVITY DISTRIBUTION")
    print("-" * 70)
    pert_analysis = analyze_perturbation_distribution(results)
    print(f"Total perturbations tested: {pert_analysis['total_perturbations']}")
    print(f"Period ratio range: {pert_analysis['min_ratio']:.1f} to {pert_analysis['max_ratio']:.1f}")
    print(f"Median ratio: {pert_analysis['median_ratio']:.1f}")
    print(f"Mean ratio: {pert_analysis['mean_ratio']:.1f}")
    print(f"Ratios > 100×: {pert_analysis['ratios_over_100']} ({100*pert_analysis['ratios_over_100']/pert_analysis['total_perturbations']:.1f}%)")
    print(f"Ratios > 1000×: {pert_analysis['ratios_over_1000']} ({100*pert_analysis['ratios_over_1000']/pert_analysis['total_perturbations']:.1f}%)")

    print("\nHistogram:")
    for bin_label, count in pert_analysis['histogram'].items():
        bar = '█' * (count // 2)
        print(f"  {bin_label:>10}: {count:3d} {bar}")

    # Divergence correlation
    print("\n2. DIVERGENCE vs LYAPUNOV CORRELATION")
    print("-" * 70)
    div_analysis = analyze_divergence_correlation(results)

    # Find extremes
    by_div = sorted(div_analysis['data_points'], key=lambda x: x['max_divergence'], reverse=True)
    print(f"Highest divergence: {by_div[0]['sequence']}")
    print(f"  λ={by_div[0]['lambda']:.3f}, max_div={by_div[0]['max_divergence']}")

    # Move patterns
    print("\n3. MOVE PATTERN ANALYSIS")
    print("-" * 70)
    pattern_analysis = analyze_move_patterns(results)

    print("\nMost common moves in extremely chaotic sequences:")
    if pattern_analysis['move_counts']['extremely_chaotic']:
        for move, count in sorted(pattern_analysis['move_counts']['extremely_chaotic'].items(),
                                   key=lambda x: x[1], reverse=True)[:5]:
            print(f"  {move}: {count}")

    print("\nMost common pairs in extremely chaotic sequences:")
    if pattern_analysis['pair_counts']['extremely_chaotic']:
        for pair, count in sorted(pattern_analysis['pair_counts']['extremely_chaotic'].items(),
                                   key=lambda x: x[1], reverse=True)[:5]:
            print(f"  {pair}: {count}")

    print("\nSelf-compositions detected:")
    if pattern_analysis['self_compositions']:
        for sc in sorted(pattern_analysis['self_compositions'], key=lambda x: x['lambda'], reverse=True):
            print(f"  {sc['move']}→{sc['move']}: λ={sc['lambda']:.3f} ({sc['classification']})")
    else:
        print("  (Run self-composition analysis to collect this data)")

    return {
        'perturbation': pert_analysis,
        'divergence': div_analysis,
        'patterns': pattern_analysis
    }


if __name__ == "__main__":
    import sys

    # Load data
    logs_dir = Path(__file__).parent.parent / "logs"
    results = load_all_results(logs_dir)

    print(f"Loaded {len(results)} Lyapunov results")

    # Run analysis
    analyses = print_analysis_summary(results)

    # Export for Octave
    print("\n" + "="*70)
    print("EXPORTING DATA FOR OCTAVE")
    print("="*70)

    export_for_octave("perturbation_distribution",
                      analyses['perturbation'],
                      logs_dir / "perturbation_distribution.csv")
    print(f"Saved: {logs_dir / 'perturbation_distribution.csv'}")

    export_for_octave("divergence_correlation",
                      analyses['divergence'],
                      logs_dir / "divergence_correlation.csv")
    print(f"Saved: {logs_dir / 'divergence_correlation.csv'}")
