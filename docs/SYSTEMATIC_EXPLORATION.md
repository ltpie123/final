# Systematic Exploration Strategy for 4D Hypercube

## Goals

1. **Catalog all available moves** and understand their structure
2. **Find individual move orders** (period of single repeated move)
3. **Map commutator relationships** between key moves
4. **Systematically test 2-move combinations** from a representative set
5. **Identify patterns** in period values and group structure

---

## Phase 1: Understanding Move Structure

### Available Moves on 3×3×3×3

Total moves: **208**

### Move Taxonomy (Hypothesis)

Based on observed moves, the 4D hypercube appears to use **two-axis notation**:

- **First letter**: Primary axis (R, L, U, D, F, B, O, I)
- **Second letter**: Secondary axis (creates a rotation in the plane formed by both axes)

Examples:
- `FR` = rotation in the Front-Right plane
- `UO` = rotation in the Up-Out plane
- `OR` = rotation in the Out-Right plane

### Coordinate System (Hypothesis)

Assuming standard 4D coordinate system:
- **R/L**: Right/Left (x-axis)
- **U/D**: Up/Down (y-axis)
- **F/B**: Front/Back (z-axis)
- **O/I**: Out/In (w-axis, 4th dimension)

### Plane Classification

Moves can be classified by which dimensional subspace they affect:

1. **3D-only planes** (both axes in x,y,z):
   - FR, FL, UF, UD, RL, etc.
   - Affect pieces in standard 3D space

2. **3D-4D mixed planes** (one axis in x,y,z, one in w):
   - OR, OL, OU, OD, OF, OB
   - IR, IL, IU, ID, IF, IB
   - Bridge 3D and 4D spaces

3. **4D plane** (if it exists):
   - OI, IO
   - Pure 4th-dimensional rotation

---

## Phase 2: Single Move Analysis

### Experiment: Find Individual Move Orders

Test each basic move type to find its order (smallest n where M^n = identity).

**Script**:
```bash
# Test single moves
for move in OF OU OR FR UF UR FU RF RO; do
    cargo run --release -- \
        --puzzle ft_hypercube:3 \
        --moves "$move" \
        --max-iterations 100 \
        --output "results_single_${move}.json"
done
```

**Expected Results**:
- Most single moves should have order 4 (90° rotations)
- Some might have order 2 (180° rotations)
- Helps identify move symmetries

---

## Phase 3: Commutator Analysis

### Key Question: Which Moves Commute?

For moves A and B:
- If [A,B] = ABA'B' = identity, then A and B **commute perfectly**
- If [A,B] has small order, they **nearly commute**
- If [A,B] has large order, they **don't commute** (high complexity)

### Priority Tests

Test commutators of promising move pairs:

```bash
# Test if OF and OU commute
cargo run --release -- --puzzle ft_hypercube:3 --moves "OF,OU,OF',OU'" --max-iterations 10000

# Test if FR and UF commute
cargo run --release -- --puzzle ft_hypercube:3 --moves "FR,UF,FR',UF'" --max-iterations 50000
```

**Interpretation**:
- Period 1: Perfect commutation
- Period ≤ 10: Nearly commute (explains why OF,OU has period 6!)
- Period > 1000: Don't commute (explains high complexity)

---

## Phase 4: Systematic 2-Move Combinations

### Approach: Representative Sampling

Instead of testing all ~200×200 = 40,000 pairs, test a representative subset.

### Curated Move Set (16 moves)

**3D-only moves** (6):
- FR, FL, UF, UD, RU, RL

**3D-4D mixed moves** (8):
- OF, OB, OR, OL, OU, OD
- IR, IU (if distinct from O-moves)

**Test Matrix**: 16 × 16 = 256 combinations

### Prioritization Strategy

1. **High priority** (likely complex):
   - Different plane types: FR + OR, UF + OU, etc.
   - Non-shared axes: FR + UO (no common axis)

2. **Medium priority**:
   - Same plane type: FR + UF (both 3D)
   - One shared axis: FR + FU (both use F)

3. **Low priority**:
   - Same move repeated: FR + FR
   - Likely simple: OF + OU (known period 6)

---

## Phase 5: Pattern Recognition

### Metrics to Track

For each 2-move sequence (A,B), record:

1. **Period P**
2. **Factorization** of P
3. **Axes involved**: {x,y,z,w} subsets
4. **Commutator order**: period of [A,B]
5. **Plane types**: 3D-only, mixed, or 4D

### Hypotheses to Test

**H1: Period scales with non-commutation**
- Prediction: Period of (A,B) correlates with period of [A,B]

**H2: Cross-dimensional moves have higher periods**
- Prediction: (3D move, 4D move) pairs have larger periods than (3D, 3D) or (4D, 4D)

**H3: Disjoint axes maximize period**
- Prediction: Moves sharing no axes have longest periods

**H4: There exists a universal maximum period**
- Prediction: Some upper bound on period for all 2-move sequences

**H5: Period divisibility pattern**
- Prediction: All periods divide some universal constant (like lcm of all periods)

---

## Phase 6: Higher-Order Sequences

### Optimal 3-Move Strategy

Based on 2-move results, construct 3-move sequences:
- Choose A,B,C that pairwise don't commute
- Ensure all three use different planes
- Maximize dimensional coverage

### Optimal 4-Move Strategy

Our current best: FR,UF,OR,RO (period 41,496)

**Can we beat this?** Try:
1. **More dimensions per move**: Use all available plane types
2. **Balanced coverage**: Each of {x,y,z,w} appears exactly twice
3. **No shared planes**: All moves affect different 2D subspaces

Candidates:
- FR, UD, OL, IB (if I-moves exist)
- FR, UO, RL, FI

---

## Implementation Plan

### Script 1: Single Move Orders

```bash
#!/bin/bash
# single_move_analysis.sh

moves="OF OU OR OL OD OB FR FL FU FD FB UR UL UO UI UF UB"

for move in $moves; do
    echo "Testing move: $move"
    cargo run --release -- \
        --puzzle ft_hypercube:3 \
        --moves "$move" \
        --max-iterations 100 \
        --output "results_order_${move}.json"
done
```

### Script 2: Representative 2-Move Matrix

```bash
#!/bin/bash
# systematic_2move_test.sh

set1="FR UF OR UO"
set2="FR UF OR UO RL FU OL UD"

# Test all combinations
for m1 in $set2; do
    for m2 in $set2; do
        if [ "$m1" != "$m2" ]; then
            echo "Testing: $m1,$m2"
            cargo run --release -- \
                --puzzle ft_hypercube:3 \
                --moves "$m1,$m2" \
                --max-iterations 50000 \
                --output "results_2mov_${m1}_${m2}.json" \
                > logs/${m1}_${m2}.log 2>&1 &

            # Limit parallel jobs
            if [ $(jobs -r | wc -l) -ge 8 ]; then
                wait -n
            fi
        fi
    done
done

wait
echo "All tests complete!"
```

### Script 3: Commutator Tests

```bash
#!/bin/bash
# commutator_analysis.sh

pairs="OF,OU FR,UF OR,OU FR,OR UF,OU"

for pair in $pairs; do
    m1=$(echo $pair | cut -d, -f1)
    m2=$(echo $pair | cut -d, -f2)

    echo "Testing commutator [$m1,$m2]"
    cargo run --release -- \
        --puzzle ft_hypercube:3 \
        --moves "$m1,$m2,${m1}',${m2}'" \
        --max-iterations 10000 \
        --output "results_comm_${m1}_${m2}.json"
done
```

---

## Data Analysis Plan

### Aggregate Results

Create a summary table from all JSON files:

```python
import json
import glob

results = []
for file in glob.glob("results_*.json"):
    with open(file) as f:
        data = json.load(f)
        results.append({
            'moves': data['move_sequence'],
            'period': data['period'],
            'states': data['unique_states_visited'],
            'time': data['exploration_time_ms']
        })

# Sort by period
results.sort(key=lambda x: x['period'] if x['period'] else float('inf'), reverse=True)

# Top 20 longest periods
for r in results[:20]:
    print(f"{r['period']:>8} | {' → '.join(r['moves'])}")
```

### Visualization Ideas

1. **Heat map**: Period matrix for all tested 2-move pairs
2. **Scatter plot**: Period vs sequence length
3. **Histogram**: Period distribution
4. **Tree diagram**: Period hierarchy
5. **Network graph**: Move commutation relationships

---

## Expected Outcomes

1. **Move taxonomy**: Complete classification of 208 moves
2. **Period bounds**: Upper/lower bounds for n-move sequences
3. **Optimal sequences**: Best known sequences for each length
4. **Group structure**: Commutation patterns and subgroups
5. **Theoretical insights**: Conjectures about period patterns

---

**Status**: Planning phase
**Next**: Implement Script 1 (single move orders)
**Goal**: Comprehensive understanding of 4D hypercube dynamics