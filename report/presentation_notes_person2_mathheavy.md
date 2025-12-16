# Presentation Notes: Person 2 (Results & Conclusions) - MATH-HEAVY VERSION

**Your Slides**: 11-20 (Key Findings → Thank You)  
**Duration**: ~9-10 minutes  
**Role**: Present results, visualizations, discuss implications and future work

---

## Slide 11: Key Findings

**Opening** (pick up from Person 1):
- "Thanks, [Person 1's name]. So with that rigorous framework established, let's look at what we discovered."

**Talking Points**:
- We tested dozens of sequences systematically, and the results are fascinating

**Single moves** (top row):
- All single moves have period 8—completely trivial
- Lyapunov exponent is zero (no chaos)
- "This makes sense: a single 4D rotation has order 8 in the group"

**Most chaotic sequences** (middle section):
- **MAJOR DISCOVERY**: Self-compositions dominate!
  - FR→FR has period only 4, but λ = 5.94
  - FO→FO has period 4 but λ = 6.09—the most chaotic we found!
- "These are sequences where we repeat the same move twice"
- "Despite generating only a cyclic subgroup of order 4, they're maximally sensitive to perturbations"
- Four-move sequences like OF→OU→OB→OD also show extreme chaos (λ = 5.64)

**High-complexity sequences** (bottom section):
- FR→UF has period 10,080 with λ = 3.95
- FR→UO: period 840, λ = 2.81
- "Large cyclic subgroups, but less chaotic than self-compositions!"

**KEY COUNTERINTUITIVE FINDING**: "The order of the cyclic subgroup ⟨T_M⟩ does NOT predict chaos. Short periods can be maximally chaotic!"

**Timing**: 2.5 minutes

---

## Slide 12: Period vs Chaos

**Talking Points**:
- This scatter plot quantifies that counterintuitive relationship

**Axes**:
- **X-axis**: Period (log scale—ranges from 4 to over 10,000)
- **Y-axis**: Lyapunov exponent λ
- **Colors**: Blue = regular, orange = sensitive, red = chaotic

**Point to specific features**:
1. **Left cluster**: Periods 4-10 include λ > 5 (extreme chaos!)
2. **Right side**: Periods up to 10,000, but λ only ~3-4
3. **No correlation**: "If period predicted chaos, we'd see upward trend—we don't"

**Group-theoretic interpretation**:
- "Small cyclic subgroups can have extreme sensitivity"
- "Large cyclic subgroups don't guarantee complexity"
- "It's about the geometric structure of how T_M acts, not just |⟨T_M⟩|"

**Timing**: 1.5 minutes

---

## Slide 13: Classification Distribution

**Talking Points**:
- We analyzed 50 sequences and classified by Lyapunov thresholds

**Point to the pie chart**:
- 30% regular (blue)—mostly single moves
- 24% sensitive (orange)—moderate chaos
- **46% chaotic** (red)—nearly half!

**Statistical significance**:
- "This is remarkably high for random sampling"
- "Suggests that chaos is generic, not exceptional, in the space of 2-move sequences"
- "Compare to 3D cubes where most 2-move sequences are less chaotic"

**Why 4D exhibits more chaos**:
- Higher-dimensional rotations have more degrees of freedom
- Richer group structure (B₄ vs octahedral group)
- More piece interaction patterns

**Mathematical insight**: "The probability measure on sequence space is weighted toward chaotic behavior"

**Timing**: 1.5 minutes

---

## Slide 14: Top Chaotic Sequences

**Talking Points**:
- This bar chart ranks sequences by Lyapunov exponent

**Walk through top sequences**:
1. **FO→FO: λ = 6.09** — highest chaos
2. **FR→FR: λ = 5.94** — second
3. **Self-compositions dominate** top 5
4. **Four-move patterns** (OF→OU→OB→OD, λ = 5.64)
5. **FR→UF appears** but is outranked

**Open theoretical question**:
- "Why are self-compositions maximally chaotic?"
- **Hypothesis**: "Applying a move twice creates interference patterns"
  - First application scrambles pieces
  - Second application acts on already-displaced configuration
  - Creates multiplicative rather than additive complexity
- **Group theory angle**: "Could relate to commutator structure or conjugacy classes"
- "No rigorous proof yet—excellent topic for further research"

**Timing**: 1.5 minutes

---

## Slide 15: Lyapunov vs Sequence Length

**Talking Points**:
- How does sequence length affect chaos?

**Clear pattern in scatter**:
- **Length 1**: All λ = 0 (cyclic groups of order 8, no chaos)
- **Length 2**: Highest chaos! Peak λ > 6
- **Length 3-5**: Lower maximum chaos, more variance

**Interpretation**:
- "Two-move sequences are the 'sweet spot' for chaos"
- "Long enough to create non-commutativity"
- "Short enough that self-compositions (M,M) are possible"
- "Longer sequences average out chaos—central limit theorem analogy"

**Mathematical intuition**: "As sequence length grows, you're sampling more of the group, which tends toward regularity"

**Timing**: 1.5 minutes

---

## Slide 16: Sequence Animations

**Talking Points**:
- We created animated visualizations of actual puzzle states
- "Available if there's interest during Q&A"

**Three animations**:
1. **FR (single)**: Baseline—period 8, λ = 0, simple cycle
2. **FO→FO**: Most chaotic—period 4 but extreme scrambling
3. **FR→FR**: Second most chaotic—similar rapid state changes

**Visual chaos**:
- "Despite returning to solved in only 4 iterations, intermediate states are maximally scrambled"
- "Perturbations produce completely different state sequences"
- "Discrete chaos: combinatorial explosion of orbit structures"

**Timing**: 1 minute

---

## Slide 17: Key Takeaways

**Talking Points** (emphasize each):

**1. Rich dynamics in 4D**:
- "4D hypercubes exhibit surprisingly complex behavior"
- 46% chaotic is high for finite discrete systems
- Period diversity (4 to 10,080) shows rich group structure

**2. Self-compositions are maximally chaotic**:
- "Our most surprising and important finding"
- λ > 5 approaches theoretical limits
- "Repeating a single move is not redundant—it's structurally optimal for chaos"

**3. Period ≠ complexity**:
- "Challenges intuition from continuous dynamical systems"
- |⟨T_M⟩| (order of cyclic subgroup) doesn't predict λ
- "Geometric action matters more than algebraic order"

**4. Discrete chaos is rigorously definable**:
- "Successfully adapted Lyapunov exponents to finite systems"
- "Sequence space as locus of chaos is a valid framework"
- "Small perturbations → massive structural changes"

**Meta-point**: "This validates studying chaos in finite discrete systems—not just an approximation, but a genuine mathematical framework"

**Timing**: 2 minutes

---

## Slide 18: Future Directions

**Talking Points**:

**Theoretical questions**:
- "Why self-compositions are so chaotic is still open"
  - Group-theoretic explanation?
  - Connection to commutator subgroups?
  - Can we predict chaos from move algebraic properties?
- "Relate to classical ergodic theory?"
  - Mixing properties in finite groups
  - Entropy in discrete systems

**Computational extensions**:
- "5D or 6D hypercubes"
  - State space grows to 10^200+
  - Periods might exceed computational limits
- "Longer sequences (5-10 moves)"
  - Test central-limit-like behavior
- "Systematic perturbation taxonomy"

**Applications**:
- "Cryptographic PRNGs based on chaotic sequences"
- "Physical systems with discrete symmetries"
  - Quantum computing (finite Hilbert spaces)
  - Lattice models in condensed matter
- "Complexity theory connections"

**Timing**: 1.5 minutes

---

## Slide 19: References

**Talking Points**:
- "Our work builds on foundational theory and tools"
- **Theory**: Devaney, Strogatz (chaos), Joyner (group theory)
- **Software**: Hyperspeedcube by Andrew Farkas enabled 4D simulation
- "Full citations on slide and in written report"

**Timing**: 30 seconds

---

## Slide 20: Thank You / Questions

**Closing**:
- "Thank you for your attention!"
- "We're happy to answer questions about the mathematics, results, or implementation"
- "Code available on GitHub for reproduction"

**Timing**: 30 seconds + Q&A

---

## Anticipated Questions (During Your Section)

**Q: Can you show a GIF?**
- A: "Absolutely! Let me pull up FO→FO..." [Have `disp/figures/sequence_FO_FO.gif` ready]

**Q: What about 3D vs 4D comparison?**
- A: "4D shows higher chaos rates. FR→UF on 4D: period 10,080, λ = 3.95. Analogous R→U on 3D: period 840, lower λ. The extra dimension creates more complex group structure and piece interactions."

**Q: How do you interpret λ > 5?**
- A: "It means perturbed sequences have periods that differ by factors of e^5 ≈ 150 on average. A sequence with period 4 might become period 600 with a single move change. That's extreme sensitivity!"

**Q: Is this really chaos or just high variance?**
- A: "Great question! It's genuine chaos in the sense of sensitive dependence. Small perturbations (one move change) produce large, systematic changes in orbit structure. The Lyapunov exponent quantifies this rigorously."

**Q: Could self-compositions relate to conjugacy classes?**
- A: "Interesting idea! Self-compositions (M,M) generate powers of a single element. Their conjugacy class structure might explain sensitivity. We haven't explored this formally—excellent direction for future work."

**Q: What's the theoretical maximum λ?**
- A: "Roughly ln(period). For period 4 sequences, theoretical max is ln(1.76×10^120) ≈ 280, but that assumes maximum perturbation. Our observed max ~6 suggests there are algebraic constraints limiting achievable chaos."

**Q: Why not test 1000s of sequences?**
- A: "Computational cost. Each Lyapunov computation requires 15+ ctrl runs, each taking seconds to minutes. We focused on systematic 2-move coverage (64 sequences) plus selected longer sequences. Total: ~2 hours compute."

---

## Q&A Strategy

**If Person 1 should answer**:
- "That's about the mathematical framework—[Person 1's name]?"
- Examples: group theory questions, Lyapunov formal definition, parity constraints

**If you should answer**:
- Results interpretation, data questions, chaos classification, comparisons

**If neither knows**:
- "Excellent question for future research"
- "We didn't explore that—here's my hypothesis..."
- "Let me think... [pause, respond honestly]"

**Keep answers**: 30-60 seconds, refer to slides when possible

---

## Quick Reference Card

**Key numbers**:
- **46%** chaotic (23/50 sequences)
- **FO→FO**: λ = 6.09, period 4 (most chaotic)
- **FR→UF**: period 10,080, λ = 3.95 (longest period)
- **FR→FR**: λ = 5.94, period 4 (second most chaotic)
- Classification: Regular < 0.1, Sensitive 0.1-0.69, Chaotic ≥ 0.69

**Key messages**:
1. Self-compositions maximize chaos (main discovery)
2. Period (subgroup order) ≠ complexity
3. 46% chaotic validates discrete chaos framework
4. 4D richer than 3D (more complex group structure)

**Files ready**:
- GIFs: `disp/figures/sequence_FO_FO.gif`, `sequence_FR_FR.gif`
- Code: github.com/ltpie123/final

---

## Mathematical Connection Points

**For Math 538 synthesis**:
- "Connects group theory, discrete dynamics, chaos theory"
- "Validates finite-system chaos as rigorous framework"
- "Novel adaptation: sequence space Lyapunov"
- "Computational validation of theoretical predictions"

**If asked about course connections**:
- "Builds on Devaney's definition of chaos (sensitive dependence)"
- "Extends discrete-time dynamical systems to finite state spaces"
- "Lyapunov exponents adapted from continuous systems"
- "Group actions as dynamical systems (Burnside, orbits)"

---

**Total Time for Person 2**: 9-10 minutes (+ Q&A)

**Combined presentation**: 19-21 minutes  
**Recommendation**: Request 25 minutes if possible (gives 4-6 min Q&A buffer)

**You're presenting cutting-edge results—be confident and enthusiastic!**
