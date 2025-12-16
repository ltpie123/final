# Additional Analyses for 4D Hypercube Dynamics

## Analyses We Can Implement

### 1. **Statistical Analysis of Period Distribution**

Create a histogram showing the distribution of all discovered periods:

**Questions**:
- Is there a power law distribution?
- Are periods normally distributed (on log scale)?
- What's the mean, median, variance?

**Implementation**:
```python
import json, glob, matplotlib.pyplot as plt
import numpy as np

periods = []
for file in glob.glob("results_*.json"):
    with open(file) as f:
        data = json.load(f)
        if data.get('period'):
            periods.append(data['period'])

# Log-scale histogram
plt.hist(np.log10(periods), bins=30)
plt.xlabel('log₁₀(Period)')
plt.ylabel('Frequency')
plt.title('Period Distribution')
```

---

### 2. **2-Move Period Heatmap**

Create a matrix showing period for every (A,B) pair tested:

```
      FR   UF   OR   UO   RL   FU   OL   UD
FR  [ 16  10080  840  840  ???  6   ???  ??? ]
UF  [10080  48  840  ???  ???  ??? 840  ??? ]
OR  [ 840  840   16  ???  ???  ???  6   ??? ]
...
```

**Visual**: Heatmap with colors representing period magnitude.

---

### 3. **Move Similarity Clustering**

Group moves by similarity using period data:

**Method**:
- Distance(A,B) = |log(Period(A,C)) - log(Period(B,C))|
- Average over all C
- Use hierarchical clustering

**Output**: Dendrogram showing move "families"

---

### 4. **Lyapunov-like Exponent**

Measure sensitivity to small changes:

For move sequence S, compute:
```
λ(S) = lim (1/n) Σ log|Period(S_perturbed) / Period(S)|
```

Where S_perturbed differs by one move.

**Interpretation**:
- λ > 0: Chaotic-like (high sensitivity)
- λ ≈ 0: Regular
- λ < 0: Stable

---

### 5. **State Space Coverage Analysis**

Calculate what fraction of state space is visited:

```
Coverage(S, n) = UniqueStates(S, n) / TotalStates
```

For 3×3×3×3, TotalStates ≈ 10¹⁷⁵ (way too large!)

**Better metric**: Coverage relative to accessible subset
- Compare to known orbit sizes from group theory

---

### 6. **Recurrence Analysis**

Track how long before trajectory returns "near" starting point:

**Method**:
1. Define distance metric on states
2. Track dist(s₀, sₙ) over time
3. Plot recurrence times

**Output**: Recurrence plot showing when trajectory revisits regions

---

### 7. **Prime Factorization Patterns**

Analyze the prime factorizations of all periods:

```
Periods:
6      = 2 × 3
8      = 2³
840    = 2³ × 3 × 5 × 7
10,080 = 2⁴ × 3² × 5 × 7
41,496 = 2³ × 3 × 7 × 13 × 19
```

**Questions**:
- Is there a maximum prime that appears?
- Do certain primes appear more frequently?
- Is there a universal period that all divide?

---

### 8. **Comparison with 3D Cube**

Direct comparison table:

| Property | 3×3×3 | 3×3×3×3 | Ratio |
|----------|-------|---------|-------|
| Single move order | 4 | 8 | 2× |
| (R,U) period | 105 | N/A | - |
| Analogous pair period | 105 | 840 | 8× |
| Maximum 2-move | ??? | 10,080 | ??? |

**Goal**: Show how complexity scales with dimension

---

### 9. **Entropy Calculation**

Shannon entropy of state visits:

```
H = -Σ p(state) log p(state)
```

Where p(state) = frequency of visiting that state in trajectory

**Interpretation**:
- H ≈ 0: Regular, visits few states
- H large: Chaotic, visits many states uniformly

---

### 10. **Conjugacy Class Analysis**

Test if some move sequences are equivalent under conjugation:

For sequences S₁, S₂, test if ∃M such that:
```
S₂ = M S₁ M⁻¹
```

**Method**: Compare periods and structures

---

### 11. **Move Algebra Predictions**

Test algebraic rules like:
```
Period(A,B,C) ≈ f(Period(A,B), Period(B,C), Period(A,C))
```

Try different functions f (lcm, product, sum, etc.)

---

### 12. **Reversibility Analysis**

Compare move M with its inverse M':

| Pair | Period(M,N) | Period(M',N) | Ratio |
|------|-------------|--------------|-------|
| FR,UF | 10,080 | ??? | ??? |
| OF,OU | 6 | ??? | ??? |

**Hypothesis**: Period(M,N) = Period(M',N) (group symmetry)

---

### 13. **Trajectory Visualization**

Project high-dimensional trajectory onto 2D/3D:

**Methods**:
- PCA on state feature vectors
- t-SNE embedding
- UMAP projection

**Output**: Animated trajectory showing complex motion

---

### 14. **Bifurcation-like Diagram**

Vary a parameter and plot resulting periods:

**Example**: For (FR, UF^k), plot period as function of k:
```
k=1: Period(FR,UF) = 10,080
k=2: Period(FR,UF,UF) = 48
k=3: Period(FR,UF,UF,UF) = ???
```

**Output**: Graph showing how period changes

---

### 15. **Group Generator Testing**

Test if small move sets generate the full puzzle group:

**Method**:
- Apply random sequences of {FR, UO, OR}
- Count unique states reached
- Estimate group size generated

**Goal**: Find minimal generating set

---

## Priority Rankings

### High Priority (Educational Value)
1. **Statistical distribution** - Shows mathematical patterns
2. **Heatmap** - Visual understanding of period landscape
3. **3D comparison** - Demonstrates dimensional scaling
4. **Entropy calculation** - Quantifies chaos
5. **Commutator prediction** - Tests group theory

### Medium Priority (Interesting)
6. Prime factorization patterns
7. Lyapunov-like exponent
8. Reversibility analysis
9. Trajectory visualization
10. Clustering analysis

### Lower Priority (Advanced)
11. Recurrence plots
12. Conjugacy testing
13. State space coverage
14. Bifurcation diagrams
15. Group generator testing

---

## Implementation Plan

### Phase 1: Data Collection (Complete)
- ✅ Single move orders
- ✅ Key commutators
- ✅ Multiple sequence lengths
- 🔄 Complete 2-move matrix (in progress)

### Phase 2: Statistical Analysis
- [ ] Period distribution histogram
- [ ] Mean, median, variance calculations
- [ ] Prime factorization catalog
- [ ] Correlation matrix

### Phase 3: Visualization
- [ ] 2-move period heatmap
- [ ] Move similarity dendrogram
- [ ] Period vs sequence length plot
- [ ] Factorization tree diagram

### Phase 4: Theoretical Comparison
- [ ] 3D vs 4D comparison table
- [ ] Entropy calculations
- [ ] Lyapunov-like exponents
- [ ] Predictive formulas

### Phase 5: Advanced Topics
- [ ] Conjugacy classes
- [ ] Trajectory embeddings
- [ ] Group structure analysis

---

## Tools Needed

### For Python Analysis
```bash
pip install numpy scipy matplotlib seaborn pandas scikit-learn
```

### For Octave/MATLAB
```octave
% Read JSON
data = jsondecode(fileread('results.json'));
% Plot histogram
histogram(log10([data.period]));
```

### For LaTeX Report
- TikZ for diagrams
- pgfplots for graphs
- Algorithm package for pseudocode

---

**Next Step**: Choose 3-5 high-priority analyses to implement for the final report.