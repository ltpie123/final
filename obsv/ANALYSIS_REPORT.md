# Trajectory Analysis Report - 4D Hypercube

**Generated**: $(date)
**Puzzle**: 3×3×3×3 Hypercube (ft_hypercube:3)
**Tool**: CTRL v0.1.0

---

## Quick Statistics

Found 34 result files

======================================================================
OVERALL STATISTICS
======================================================================
Total sequences analyzed: 34
Min period: 4
Max period: 41496
Mean period: 3135.9
Median period: 105

======================================================================
BY SEQUENCE LENGTH
======================================================================

1-move sequences: 12 tested
  Max period: 8
  Min period: 8
  Mean: 8.0
  Top 5:
           8 | RF
           8 | OU
           8 | UR
           8 | RO
           8 | OF

2-move sequences: 7 tested
  Max period: 10080
  Min period: 4
  Mean: 2040.6
  Top 5:
      10,080 | FR → UF
         840 | FU → RO
         840 | RF → UF
         840 | FR → UO
         840 | UF → OR

3-move sequences: 4 tested
  Max period: 7920
  Min period: 48
  Mean: 4512.0
  Top 5:
       7,920 | FR → OR → UF
       7,920 | UF → FR → OR
       2,160 | FR → UF → OR
          48 | FR → UF → UF

4-move sequences: 8 tested
  Max period: 41496
  Min period: 6
  Mean: 5539.1
  Top 5:
      41,496 | FR → UF → OR → RO
       1,680 | FR → UF → FU → RF
         504 | UF → OU → UB → OD
         504 | FR → UF → FL → UB
         105 | FR → UO → FL → UI

5-move sequences: 3 tested
  Max period: 27720
  Min period: 720
  Mean: 9960.0
  Top 5:
      27,720 | FR → UO → UF → OR → RO
       1,440 | FR → UF → OR → RO → UO
         720 | FR → UF → UR → FO → LU

======================================================================
PERIOD DISTRIBUTION
======================================================================
  1-10           :  15 sequences ( 44.1%)
  11-100         :   2 sequences (  5.9%)
  101-1,000      :   9 sequences ( 26.5%)
  1,001-10,000   :   5 sequences ( 14.7%)
  10,001+        :   3 sequences (  8.8%)

======================================================================
MOST COMMON PERIODS
======================================================================
         8: appears  12 times
       840: appears   5 times
       504: appears   2 times
         6: appears   2 times
     7,920: appears   2 times
     1,680: appears   1 times
       720: appears   1 times
    41,496: appears   1 times
    10,080: appears   1 times
     2,160: appears   1 times

======================================================================
PRIME FACTORIZATION ANALYSIS
======================================================================
Primes appearing in factorizations: [2, 3, 5, 7, 11, 13, 19]

Prime frequency:
    2:  33 occurrences ( 97.1%)
    3:  21 occurrences ( 61.8%)
    5:  14 occurrences ( 41.2%)
    7:  12 occurrences ( 35.3%)
   11:   3 occurrences (  8.8%)
   13:   1 occurrences (  2.9%)
   19:   1 occurrences (  2.9%)

======================================================================
EXAMPLE FACTORIZATIONS
======================================================================
         6 = 2 × 3
         8 = 2^3
        48 = 2^4 × 3
       105 = 3 × 5 × 7
       504 = 2^3 × 3^2 × 7
       840 = 2^3 × 3 × 5 × 7
     1,680 = 2^4 × 3 × 5 × 7
     2,160 = 2^4 × 3^3 × 5
     7,920 = 2^4 × 3^2 × 5 × 11
    10,080 = 2^5 × 3^2 × 5 × 7
    41,496 = 2^3 × 3 × 7 × 13 × 19

======================================================================
PERFORMANCE METRICS
======================================================================
Time per iteration: 0.317 ms (average)
Fastest: 0.125 ms
Slowest: 0.615 ms

======================================================================
Analysis complete!
======================================================================

---

## All Results (sorted by period)

| Period | Length | Move Sequence | States | Time (s) |
|--------|--------|---------------|--------|----------|
| 41496 | 4 | FR → UF → OR → RO | 41496 | 16.94 |
| 27720 | 5 | FR → UO → UF → OR → RO | 27720 | 13.59 |
| 10080 | 2 | FR → UF | 10080 | 2.70 |
| 7920 | 3 | UF → FR → OR | 7920 | 3.04 |
| 7920 | 3 | FR → OR → UF | 7920 | 2.97 |
| 2160 | 3 | FR → UF → OR | 2160 | 0.83 |
| 1680 | 4 | FR → UF → FU → RF | 1680 | 0.72 |
| 1440 | 5 | FR → UF → OR → RO → UO | 1440 | 0.80 |
| 840 | 2 | UF → OR | 840 | 0.26 |
| 840 | 2 | RF → UF | 840 | 0.28 |
| 840 | 2 | OR → UF | 840 | 0.27 |
| 840 | 2 | FU → RO | 840 | 0.28 |
| 840 | 2 | FR → UO | 840 | 0.28 |
| 720 | 5 | FR → UF → UR → FO → LU | 720 | 0.44 |
| 504 | 4 | UF → OU → UB → OD | 504 | 0.20 |
| 504 | 4 | FR → UF → FL → UB | 504 | 0.22 |
| 105 | 4 | FR → UO → FL → UI | 105 | 0.04 |
| 48 | 3 | FR → UF → UF | 48 | 0.02 |
| 12 | 4 | FR → OR → FL → OL | 12 | 0.00 |
| 8 | 1 | UR | 8 | 0.00 |
| 8 | 1 | UO | 8 | 0.00 |
| 8 | 1 | UF | 8 | 0.00 |
| 8 | 1 | RO | 8 | 0.00 |
| 8 | 1 | RF | 8 | 0.00 |
| 8 | 1 | OU | 8 | 0.00 |
| 8 | 1 | OR | 8 | 0.00 |
| 8 | 1 | OL | 8 | 0.00 |
| 8 | 1 | OF | 8 | 0.00 |
| 8 | 1 | FU | 8 | 0.00 |
| 8 | 1 | FR | 8 | 0.00 |
| 8 | 1 | FO | 8 | 0.00 |
| 6 | 4 | OR → OU → OL → OD | 6 | 0.00 |
| 6 | 4 | OF → OU → OB → OD | 6 | 0.00 |
| 4 | 2 | FR → FR | 4 | 0.00 |

---

