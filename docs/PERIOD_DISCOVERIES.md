# Period Discovery Summary - 3x3x3x3 Hypercube

## MAXIMUM PERIOD FOUND: 41,496

**Move Sequence**: FR → UF → OR → RO (4 moves)
**Time**: 17.14 seconds
**Discovery**: December 2025

---

## Complete Results by Sequence Length

### 2-Move Sequences

| Rank | Moves | Period | Factor of 840 | Notes |
|------|-------|--------|---------------|-------|
| 1 | **FR → UF** | **10,080** | 840 × 12 | Maximum for 2-moves |
| 2 | FR → UO | 840 | 840 × 1 | Common period |
| 2 | OR → UF | 840 | 840 × 1 | |
| 2 | FU → RO | 840 | 840 × 1 | |
| 2 | FR → OR | 840 | 840 × 1 | |
| 2 | UF → OR | 840 | 840 × 1 | |
| 2 | RF → UF | 840 | 840 × 1 | Reverse of FR |
| 3 | FR → FU | 6 | - | Both share F axis |
| 3 | OF → OU | 6 | - | O-axis subgroup |
| 3 | OF → OR | 6 | - | O-axis subgroup |

### 3-Move Sequences

| Rank | Moves | Period | Factor of 840 | Notes |
|------|-------|--------|---------------|-------|
| 1 | **FR → OR → UF** | **7,920** | 840 × 9.43 | Maximum for 3-moves |
| 1 | **UF → FR → OR** | **7,920** | 840 × 9.43 | Order variation |
| 2 | FR → UF → OR | 2,160 | 840 × 2.57 | Different ordering |
| 3 | FR → UF → UF | 48 | - | Repeated move |
| 4 | FR → FR → UF | 16 | - | Repeated move |
| 5 | OF → OU → OR | 4 | - | O-axis only |

### 4-Move Sequences

| Rank | Moves | Period | Factor of 840 | Notes |
|------|-------|--------|---------------|-------|
| 1 | **FR → UF → OR → RO** | **41,496** | 840 × 49.4 | **MAXIMUM FOUND** |
| 2 | FR → UF → FU → RF | 1,680 | 840 × 2 | Symmetric sequence |

---

## Key Insights

### 1. Period Growth with Sequence Length

| Length | Max Period | Growth Factor vs 2-move |
|--------|------------|------------------------|
| 2 moves | 10,080 | 1.0× |
| 3 moves | 7,920 | 0.79× (decreases!) |
| 4 moves | 41,496 | **4.12×** |

**Observation**: Adding a 3rd move can actually *decrease* period! But 4 moves can create massive periods.

### 2. The "840 Attractor"

Most generic 2-move pairs have period exactly 840. This appears to be the "natural" period for non-special move combinations on the 3×3×3×3.

840 = 2³ × 3 × 5 × 7

### 3. What Makes High Periods?

**High complexity requires:**
- ✅ Moves affecting different planes
- ✅ No repeated moves
- ✅ No shared axes (e.g., FR and FU both use F)
- ✅ Mix of 3D and 4D axes

**FR,UF,OR,RO works because:**
- FR: Front-Right (x,z plane in 3D)
- UF: Up-Front (y,z plane in 3D)
- OR: Out-Right (w,x plane crossing 3D/4D)
- RO: Right-Out (x,w plane crossing 3D/4D)
- All four affect different dimensional subspaces!

### 4. Repeated Moves Kill Complexity

| Sequence | Period | Reduction |
|----------|--------|-----------|
| FR → UF | 10,080 | baseline |
| FR → FR → UF | 16 | 630× smaller! |
| FR → UF → UF | 48 | 210× smaller! |

**Why?** Repeating a move effectively reduces it to a power: FR² is simpler than FR·UF.

### 5. Shared Axes Create Trivial Periods

| Sequence | Shared Axis | Period |
|----------|-------------|--------|
| FR → FU | F (front) | 6 |
| OF → OU | O (out) | 6 |
| OF → OR | O (out) | 6 |

When two moves share an axis, they nearly commute, creating simple behavior.

---

## Mathematical Structure

### Period Factorizations

- 6 = 2 × 3
- 16 = 2⁴
- 48 = 2⁴ × 3
- 840 = 2³ × 3 × 5 × 7
- 1,680 = 2⁴ × 3 × 5 × 7
- 2,160 = 2⁴ × 3³ × 5
- 7,920 = 2⁴ × 3² × 5 × 11
- 10,080 = 2⁴ × 3² × 5 × 7
- 41,496 = 2³ × 3 × 7 × 13 × 19

**Hypothesis**: All periods are highly composite numbers with many small prime factors. This suggests deep group-theoretic structure.

### LCM Analysis

The least common multiple of interesting periods:
- lcm(840, 10080) = 10,080
- lcm(840, 7920) = 27,720
- lcm(10080, 41496) = 414,960

---

## Recommendations for Finding Even Higher Periods

### 1. Test 5+ Move Sequences
Hypothesis: Period continues to grow with more moves (if chosen carefully).

**Try:**
- FR,UF,OR,RO,UO
- FR,UF,UR,FO,RU

### 2. Test All-Distinct-Axis Combinations
Choose moves that each affect completely different dimensional subspaces.

### 3. Avoid Commutators
Commutator sequences like [A,B] = A,B,A',B' tend to have structure that reduces period.

### 4. Consider Prime Move Orders
Test moves with prime orders in the group.

---

## Period Hierarchy

```
         41,496 (FR,UF,OR,RO) [4-move MAX]
            ↑
        10,080 (FR,UF) [2-move MAX]
            ↑
         7,920 (FR,OR,UF) [3-move MAX]
            ↑
         2,160 (FR,UF,OR)
            ↑
         1,680 (FR,UF,FU,RF)
            ↑
          840 ← COMMON PERIOD
            ↑
           48 (FR,UF,UF)
            ↑
           16 (FR,FR,UF)
            ↑
            6 (O-axis, shared-axis)
            ↑
            4 (OF,OU,OR)
```

---

**Status**: Exploration ongoing
**Tool**: CTRL v0.1.0
**Max Tested**: 50,000 iterations
**Date**: December 2025
