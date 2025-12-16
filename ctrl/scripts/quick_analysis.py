#!/usr/bin/env python3
"""
Quick statistical analysis of collected trajectory data
"""

import json
import glob
from pathlib import Path
from collections import defaultdict, Counter
import sys

def prime_factorization(n):
    """Return prime factorization as dict {prime: power}"""
    if n <= 1:
        return {}

    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def analyze_results():
    """Analyze all JSON result files"""

    results_dir = Path(__file__).parent.parent
    json_files = list(results_dir.glob("results_*.json"))

    if not json_files:
        print("No results files found!")
        return

    print(f"Found {len(json_files)} result files\n")

    # Collect data
    by_length = defaultdict(list)
    all_periods = []
    all_factorizations = []

    for file in json_files:
        try:
            with open(file) as f:
                data = json.load(f)

            period = data.get('period')
            if period:
                moves = data.get('move_sequence', [])
                length = len(moves)

                by_length[length].append({
                    'moves': ' → '.join(moves),
                    'period': period,
                    'states': data.get('unique_states_visited', 0),
                    'time': data.get('exploration_time_ms', 0) / 1000
                })

                all_periods.append(period)
                all_factorizations.append(prime_factorization(period))
        except Exception as e:
            print(f"Error reading {file}: {e}")

    # Statistics
    print("="*70)
    print("OVERALL STATISTICS")
    print("="*70)
    print(f"Total sequences analyzed: {len(all_periods)}")
    print(f"Min period: {min(all_periods)}")
    print(f"Max period: {max(all_periods)}")
    print(f"Mean period: {sum(all_periods) / len(all_periods):.1f}")
    print(f"Median period: {sorted(all_periods)[len(all_periods)//2]}")
    print()

    # By sequence length
    print("="*70)
    print("BY SEQUENCE LENGTH")
    print("="*70)
    for length in sorted(by_length.keys()):
        sequences = by_length[length]
        periods = [s['period'] for s in sequences]

        print(f"\n{length}-move sequences: {len(sequences)} tested")
        print(f"  Max period: {max(periods)}")
        print(f"  Min period: {min(periods)}")
        print(f"  Mean: {sum(periods)/len(periods):.1f}")

        # Top 5
        top5 = sorted(sequences, key=lambda x: x['period'], reverse=True)[:5]
        print(f"  Top 5:")
        for seq in top5:
            print(f"    {seq['period']:>8,} | {seq['moves']}")

    # Period distribution
    print("\n" + "="*70)
    print("PERIOD DISTRIBUTION")
    print("="*70)

    ranges = [
        (1, 10, "1-10"),
        (11, 100, "11-100"),
        (101, 1000, "101-1,000"),
        (1001, 10000, "1,001-10,000"),
        (10001, 100000, "10,001+")
    ]

    for low, high, label in ranges:
        count = sum(1 for p in all_periods if low <= p <= high)
        pct = 100 * count / len(all_periods)
        print(f"  {label:15s}: {count:3d} sequences ({pct:5.1f}%)")

    # Common periods
    print("\n" + "="*70)
    print("MOST COMMON PERIODS")
    print("="*70)

    period_counts = Counter(all_periods)
    for period, count in period_counts.most_common(10):
        print(f"  {period:>8,}: appears {count:3d} times")

    # Prime factorization analysis
    print("\n" + "="*70)
    print("PRIME FACTORIZATION ANALYSIS")
    print("="*70)

    all_primes = set()
    for factors in all_factorizations:
        all_primes.update(factors.keys())

    print(f"Primes appearing in factorizations: {sorted(all_primes)}")
    print()

    # Prime frequency
    prime_freq = defaultdict(int)
    for factors in all_factorizations:
        for prime in factors:
            prime_freq[prime] += 1

    print("Prime frequency:")
    for prime in sorted(prime_freq.keys()):
        count = prime_freq[prime]
        pct = 100 * count / len(all_factorizations)
        print(f"  {prime:3d}: {count:3d} occurrences ({pct:5.1f}%)")

    # Example factorizations
    print("\n" + "="*70)
    print("EXAMPLE FACTORIZATIONS")
    print("="*70)

    interesting_periods = [6, 8, 16, 48, 105, 504, 840, 1680, 2160, 7920, 10080, 41496]
    for p in interesting_periods:
        if p in [seq['period'] for length in by_length.values() for seq in length]:
            factors = prime_factorization(p)
            factor_str = " × ".join(f"{prime}^{power}" if power > 1 else str(prime)
                                    for prime, power in sorted(factors.items()))
            print(f"  {p:>8,} = {factor_str}")

    # Performance analysis
    print("\n" + "="*70)
    print("PERFORMANCE METRICS")
    print("="*70)

    all_sequences = [seq for length in by_length.values() for seq in length]

    # Time per iteration
    time_per_iter = []
    for seq in all_sequences:
        if seq['period'] > 0 and seq['time'] > 0:
            time_per_iter.append(seq['time'] / seq['period'] * 1000)  # ms per iteration

    if time_per_iter:
        print(f"Time per iteration: {sum(time_per_iter)/len(time_per_iter):.3f} ms (average)")
        print(f"Fastest: {min(time_per_iter):.3f} ms")
        print(f"Slowest: {max(time_per_iter):.3f} ms")

    print("\n" + "="*70)
    print("Analysis complete!")
    print("="*70)

if __name__ == "__main__":
    analyze_results()