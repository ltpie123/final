# Experiment Log - 4D Hypercube Trajectory Exploration

**Project**: Math 538 Final - Discrete Dynamical Systems
**Date Started**: December 16, 2025
**Status**: Active Exploration

---

## Experiment Series 1: Single Move Orders

**Date**: 2025-12-16 03:35 UTC
**Hypothesis**: All basic moves have the same order
**Method**: Test 12 representative moves individually

### Results
- **ALL moves have order 8** ✓
- Tested: OF, OU, OR, OL, FR, UF, UR, FU, RF, RO, UO, FO
- Conclusion: Universal property of 3×3×3×3 puzzle structure

---

## Experiment Series 2: Commutator Analysis

**Date**: 2025-12-16 03:36 UTC
**Hypothesis**: Commutator period predicts 2-move period
**Method**: Test [A,B] = A,B,A',B' for key pairs

### Results

| Commutator | Period | Interpretation |
|------------|--------|----------------|
| [OF,OU] | 6 | Nearly commute |
| [OR,OU] | 6 | Nearly commute |
| [FR,OR] | 12 | Slight non-commutation |
| [FR,UO] | 105 | Moderate |
| [UF,OR] | 105 | Moderate |
| [FR,UF] | **504** | **Strong non-commutation** |
| [UF,OU] | **504** | **Strong non-commutation** |

**Key Insight**: Commutator period is a strong predictor of complexity!

---

## Experiment Series 3: 2-Move Exploration

**Status**: Partial (10/64 tested from systematic matrix)

### Confirmed Maximum: FR → UF = 10,080

Other high-complexity pairs:
- OR → UF = 840
- FR → UO = 840
- RF → UF = 840
- FU → RO = 840

**Pattern**: "840 attractor" - most generic pairs settle here

---

## Experiment Series 4: 3-Move Sequences

**Hypothesis**: Longer sequences → higher periods
**Result**: REJECTED! Period can decrease with more moves

### Results

| Sequence | Period | Complexity |
|----------|--------|------------|
| FR → OR → UF | 7,920 | High |
| UF → FR → OR | 7,920 | High (order variation) |
| FR → UF → OR | 2,160 | Medium |
| FR → UF → UF | 48 | Low (repeated move) |
| FR → FR → UF | 16 | Low (repeated move) |

**Key Finding**: Order matters! Permuting the same moves changes period.

---

## Experiment Series 5: 4-Move Sequences

**NEW RECORD**: FR → UF → OR → RO = **41,496**

### All 4-Move Results

| Sequence | Period | Notes |
|----------|--------|-------|
| FR → UF → OR → RO | 41,496 | **MAXIMUM FOUND** |
| FR → UF → FU → RF | 1,680 | Symmetric pattern |

**Insight**: All-distinct-planes strategy works!
- FR: (F,R) plane
- UF: (U,F) plane
- OR: (O,R) plane
- RO: (R,O) plane
- No two moves share both axes!

---

## Experiment Series 6: 5-Move Sequences

**Date**: 2025-12-16 04:15 UTC
**Goal**: Beat 41,496
**Strategy**: Maximize dimensional coverage and non-commutation
**Result**: FAILED - No improvement over 4-move record

### Results

| Sequence | Period | Notes |
|----------|--------|-------|
| FR → UO → UF → OR → RO | 27,720 | Best 5-move (still < 41,496) |
| FR → UF → OR → RO → UO | 1,440 | Adding 5th plane to winner reduced period |
| FR → UF → UR → FO → LU | 720 | All different axes gave low period |

**Key Finding**: More moves ≠ Higher period!
- Best 5-move sequence (27,720) is 33% LOWER than best 4-move (41,496)
- Adding moves can actually reduce period
- Confirms that move selection and geometric relationships matter more than length

---

## Experiment Series 7: (PLANNED) Systematic 2-Move Matrix

**Goal**: Complete the 8×8 = 64 combination matrix
**Moves**: [FR, UF, OR, UO, RL, FU, OL, UD]

**Status**: Script created, ready to launch
**Estimated time**: ~2 hours (64 tests × 2min avg)

---

## Key Discoveries

### 1. Universal Order-8 Property
Every basic move generates Z₈ subgroup.

### 2. O-Axis Anomaly
Moves with O prefix form small subgroup (period ≤ 6).

### 3. The 840 Phenomenon
Most "generic" 2-move pairs have period exactly 840.

### 4. Commutator Prediction Rule
Large Period([A,B]) → Large Period(A,B)

### 5. Repeated Moves Kill Complexity
Adding repeated move can reduce period by 100×+

### 6. Distinct-Planes Principle
Maximum periods require moves on different 2D planes.

---

## Next Experiments

### High Priority
- [x] Test 5-move sequences (attempting to beat 41,496) - COMPLETED: Failed to beat record
- [ ] Complete systematic 2-move matrix (64 combinations)
- [ ] Test move inverses: Period(A,B) vs Period(A',B)
- [ ] Test conjugacy: Period(MAM⁻¹, MBM⁻¹) = Period(A,B)?

### Medium Priority
- [ ] Test longer repeated sequences: (FR,UF)ⁿ
- [ ] Explore 6+ move sequences
- [ ] Test random sequences for chaos detection
- [ ] Compare with 3×3×3 analogues

### Lower Priority
- [ ] Test all 208 moves individually
- [ ] Exhaustive 3-move testing
- [ ] State space coverage estimation
- [ ] Trajectory visualization

---

**Last Updated**: 2025-12-16 04:15 UTC
**Total Experiments**: 41 sequences tested
**Maximum Period Found**: 41,496 (FR,UF,OR,RO)