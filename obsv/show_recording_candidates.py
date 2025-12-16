#!/usr/bin/env python3
import csv

print("Sequences Good for Recording (by period)")
print("=" * 70)

with open('logs/lyapunov_data.csv') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Group by period
by_period = {}
for row in data:
    period = int(float(row['base_period']))
    if period not in by_period:
        by_period[period] = []
    by_period[period].append(row)

# Show interesting categories
print("\n1. BASIC ROTATIONS (period 8, trivial):")
for row in by_period.get(8, []):
    if row['classification'] == 'trivial':
        print(f"   {row['sequence']}")

print("\n2. SHORT ORBITS (period 6-20, chaotic):")
for period in [6, 12]:
    if period in by_period:
        for row in sorted(by_period[period], key=lambda x: float(x['lyapunov_exponent']), reverse=True)[:3]:
            print(f"   {row['sequence']} (period {period}, λ={float(row['lyapunov_exponent']):.2f})")

print("\n3. MODERATE ORBITS (period 48-105):")
for period in [48, 105]:
    if period in by_period:
        for row in by_period[period][:2]:
            print(f"   {row['sequence']} (period {period}, λ={float(row['lyapunov_exponent']):.2f})")

print("\n4. INTERESTING PAIRS (period 840-10080):")
for period in [840, 10080]:
    if period in by_period:
        for row in sorted(by_period[period], key=lambda x: float(x['lyapunov_exponent']), reverse=True)[:2]:
            print(f"   {row['sequence']} (period {period}, λ={float(row['lyapunov_exponent']):.2f})")

print("\n" + "=" * 70)
