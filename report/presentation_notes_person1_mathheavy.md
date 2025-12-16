# Presentation Notes: Person 1 (Introduction & Theory) - MATH-HEAVY VERSION

**Your Slides**: 1-10 (Title → Computational Approach)  
**Duration**: ~10-11 minutes  
**Role**: Set up the problem, explain mathematical framework in depth, describe methods

---

## Slide 1: Title Slide

**Talking Points**:
- Good [morning/afternoon], everyone. Today we'll be presenting our final project on chaos theory in 4-dimensional Rubik's cubes.
- This project explores discrete dynamical systems on hyperdimensional puzzles—a rigorous application of group theory, chaos theory, and computational mathematics.
- I'll cover the mathematical foundations and framework, then [Person 2's name] will present our results.

**Timing**: 30 seconds

---

## Slide 2: Overview

**Talking Points**:
- Here's our roadmap today
- I'll establish the 4D hypercube structure and mathematical framework
- Then explain our computational methods
- [Person 2's name] will present our key findings and conclusions

**Timing**: 30 seconds

---

## Slide 3: What is a 4D Rubik's Cube?

**Talking Points**:
- Most of you are familiar with the classic 3×3×3 Rubik's Cube
- It has 6 faces and about 43 quintillion possible states
- A 4D hypercube extends this to the fourth dimension

**KEY POINT**: A 4D hypercube has 8 cells—think of these as 3D "faces"
- **State space formula**: Point to the formula at bottom
- "This product accounts for corner permutations and orientations, face pieces, and edge pieces"
- The result: approximately **1.76 × 10^120 states**
- That's 10^100 times larger than the 3D cube!

**Move notation**:
- Two-letter notation: FR means "rotate Front cell toward Right cell"
- UO means "rotate Up toward Outside" (the 4th dimension)

**Timing**: 2 minutes

---

## Slide 4: Puzzle Structure & Symmetry

**Talking Points**:
- Let's break down the mathematical structure

**Left column - Piece Types**:
- 72 movable pieces total: 16 corners, 32 faces, 24 edges
- Each has different orientation counts
- "Corners can be placed in 12 different orientations—much richer than 3D where corners have only 3 orientations"
- Each quarter turn affects 8 corners, 12 faces, and 4 edges

**Right column - Symmetry**:
- The tesseract's symmetry group is B₄, the hyperoctahedral group
- **Order 384** = 2^4 × 4! 
- "This is the wreath product S₂ ≀ S₄"
- Coxeter notation [4,3,3] indicates the reflection structure
- Rotational symmetry is order 192 (index 2 subgroup)

**Key point**: "This rich group structure with 384 symmetries enables the complex dynamics we'll explore"

**Timing**: 2 minutes

---

## Slide 5: Research Question

**Talking Points**:
- Our central question: What happens when you repeat the same move sequence over and over?

**Three key concepts**:
1. **Orbit/Period**: Eventually must return to solved state—how many iterations?
2. **Chaos**: Sensitivity to perturbations measured by Lyapunov exponent
3. **Discrete Dynamics**: Finite state space, deterministic maps

**Transition**: "Now let me formalize this mathematically..."

**Timing**: 1 minute

---

## Slide 6: Discrete Dynamical System

**Talking Points**:
- Here's the rigorous framework

**Main definitions**:
- S is our state space—all 10^120 configurations
- M is a move sequence, like (FR, UF)
- T_M is the composite map: "We compose the moves in order"
- Starting from solved state s₀, we iterate

**Group-theoretic view** (bottom block):
- "Each move is a bijection in the puzzle group G"
- "The sequence generates a cyclic subgroup ⟨T_M⟩"
- "The order of this subgroup is precisely the period p"
- **Example**: "If FR→UF has period 10,080, then ⟨T_M⟩ is a cyclic group of order 10,080"

**Mathematical rigor**: "This connects our computational results to abstract algebra—every trajectory is an orbit of a cyclic group action"

**Timing**: 2 minutes

---

## Slide 7: Permutation Theory & Constraints

**Talking Points**:
- Not all permutations are reachable—the puzzle has algebraic constraints

**State representation**:
- Each state is a permutation π plus orientations o
- "This is how we mathematically encode where each piece is and how it's rotated"

**Parity constraints** (walk through each):
1. **Corner parity**: "Corners must form an even permutation—they're in the alternating group A₁₆, not the full symmetric group S₁₆"
2. **Edge-Face parity**: "The permutation signatures of edges and faces must match"
3. **Orientation sums**: "Face orientations sum to 0 mod 3, edge orientations sum to 0 mod 2"

**Monoflip invariant**:
- "This is unique to 4D! A single corner can be 'flipped in place' with all others solved"
- "Related to the A₄ orientation group—doesn't happen in 3D or 5D+"
- "This is a beautiful example of how dimensionality affects group-theoretic structure"

**Timing**: 2 minutes

---

## Slide 8: Lyapunov Exponents

**Talking Points**:
- How do we measure chaos in a finite system?

**Perturbation approach**:
- Take base sequence M with period p
- Perturb it: insert, delete, or replace a move
- Compute new period p'
- "The Lyapunov exponent averages the log of these period ratios"

**Formal definition** (blue block):
- "In continuous systems, Lyapunov measures trajectory divergence"
- **Show formula**: λ = limit of (1/t) ln(δ(t)/δ(0))
- "We adapt this: instead of state space divergence, we measure period ratio changes"
- "This is λ_discrete = expected value of ln|p'/p|"

**Classification thresholds**:
- λ < 0.1: Regular—perturbations barely change period
- 0.1 ≤ λ < ln(2) ≈ 0.69: Sensitive—moderate changes
- λ ≥ 0.69: Chaotic—small changes cause massive period differences

**Key insight**: "This discrete Lyapunov exponent quantifies sensitivity in sequence space, not state space"

**Timing**: 2.5 minutes

---

## Slide 9: Chaos in Finite Systems

**Talking Points**:
- This slide addresses a fundamental challenge

**The problem**:
- "Classical chaos theory assumes infinite or continuous state spaces"
- "Our system is finite—only 10^120 states"
- "All trajectories are periodic! No strange attractors, no continuous divergence"

**Our solution**:
- "We move from state space to sequence space"
- "Instead of perturbing initial conditions, we perturb the move sequence itself"
- "Chaos manifests as sensitivity of orbit properties—period, structure—not trajectory divergence"

**Key insight** (blue block):
- Read this: "Chaos manifests as sensitivity of dynamical properties to small sequence perturbations"
- "This is a genuine adaptation of chaos theory to finite discrete systems"
- "We're measuring structural chaos, not metric chaos"

**Theoretical significance**: "This validates discrete dynamical systems as a rigorous framework for complexity, even without infinity"

**Timing**: 2 minutes

---

## Slide 10: Computational Approach

**Talking Points**:
- Now let me describe our implementation

**Tool Stack** (briefly):
- Rust for fast cycle detection
- Python for Lyapunov analysis
- Octave for visualization

**Systematic Testing**:
- Tested all 64 two-move combinations
- Used SHA256 hashing for state comparison

**Cycle Detection Algorithm** (blue block):
- "This is the core algorithm"
- **Walk through**:
  1. "Initialize with solved state, mark it as visited"
  2. "For each iteration, apply the move sequence"
  3. "Hash the resulting state with SHA256"
  4. "If we've seen this hash before, we've found the cycle"
  5. "Return the period as current iteration minus when we first saw this state"
- **Complexity**: "O(p) space and O(p·(T_M + H)) time"
- "For our periods up to 10,000, this runs in milliseconds to seconds"

**Technical detail**: "SHA256 gives us collision-resistant hashing—no false positives across millions of states"

**Transition to Person 2**: "With this mathematical foundation and computational framework established, let's see what we discovered. [Person 2's name]?"

**Timing**: 2.5 minutes

---

## Handoff to Person 2

**Smooth transition**: "So we've built a rigorous mathematical framework connecting group theory, discrete dynamical systems, and chaos theory. Now let's see what the data reveals. [Person 2's name]?"

**Total Time for Person 1**: ~10-11 minutes

---

## Quick Reference Card

**Key equations to know**:
- State space: $|S| \approx 1.76 \times 10^{120}$
- Symmetry: $|B_4| = 384$
- Lyapunov: $\lambda = \frac{1}{N} \sum \ln|p'/p|$
- Period: $T_M^p(s_0) = s_0$

**Key concepts**:
- Hyperoctahedral group B₄
- Cyclic subgroup ⟨T_M⟩
- Parity constraints (A₁₆, orientation sums)
- Monoflip invariant (unique to 4D)
- Discrete Lyapunov (sequence space not state space)

**Backup info**:
- 72 movable pieces (16+32+24)
- SHA256 for collision-resistant hashing
- Complexity: O(p·(T_M + H))
- N=15 perturbations per sequence

---

## Anticipated Questions (During Your Section)

**Q: Why is the state space formula so complicated?**
- A: "It factors in corner permutations (16!/2), their orientations (12^15), face piece arrangements (32!), their orientations (6^31), edges (24!/2), and edge orientations (2^23). Each term comes from the group theory of that piece type."

**Q: What is the hyperoctahedral group B₄?**
- A: "It's the symmetry group of the 4D hypercube, consisting of all signed permutations of 4 coordinates. Think of it as the 4D analogue of the octahedral group (symmetries of a 3D octahedron)."

**Q: Why does monoflip only exist in 4D?**
- A: "It's related to the structure of the alternating group A₄ and its commutator subgroup, the Klein four-group. In 3D (A₃ = ℤ₃) and 5D+ (larger alternating groups), this particular algebraic structure doesn't arise."

**Q: How is this different from classical chaos?**
- A: "Classical chaos requires infinite or continuous state spaces. We adapt the concept by measuring sensitivity in sequence space rather than state space—how much does the orbit structure change when you perturb the sequence?"

**Q: Why SHA256 instead of direct state comparison?**
- A: "Puzzle states are complex objects (piece transforms in SE(4)). SHA256 gives us a canonical fingerprint that's collision-resistant and fast to compute."

---

## Mathematical Depth Notes

**For Math 538 audience**:
- Emphasize the group theory throughout
- Connect to classical dynamical systems (Poincaré maps, discrete-time systems)
- Highlight the novelty of sequence-space Lyapunov exponents
- Show how finite systems require adaptation, not abandonment, of chaos theory

**Theoretical contributions**:
1. Discrete Lyapunov exponents on finite state spaces
2. Sequence space as locus of chaos (not state space)
3. Computational validation of theoretical framework
4. Connection between group structure and dynamical complexity

**If asked about rigor**:
- "We're working in well-defined algebraic structures (puzzle groups, permutation groups)"
- "Our Lyapunov exponent is a computable real number with statistical interpretation"
- "Results are reproducible and validated across 126+ sequences"

---

**Total Time for Person 1**: 10-11 minutes  
**Combined presentation**: 19-21 minutes → May need to extend time request or trim Person 2's section slightly

**Good luck! The mathematical depth is impressive—own it!**
