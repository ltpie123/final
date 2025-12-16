# Presentation Notes: Person 1 (Introduction & Theory) - STREAMLINED VERSION

**Your Slides**: 1-8 (Title → Computational Approach)  
**Duration**: ~8-9 minutes  
**Role**: Set up the problem, explain dynamical systems framework, describe methods

---

## Slide 1: Title Slide

**Talking Points**:
- Good [morning/afternoon], everyone. Today we'll be presenting our final project on chaos theory in 4-dimensional Rubik's cubes.
- This project applies discrete dynamical systems and chaos theory to hyperdimensional puzzles computationally.
- I'll cover the mathematical framework, then [Person 2's name] will present our results.

**Timing**: 30 seconds

---

## Slide 2: Overview

**Talking Points**:
- Here's our roadmap
- I'll introduce 4D hypercubes and establish the dynamical systems framework
- Then explain our computational methods
- [Person 2's name] will present the key findings and conclusions

**Timing**: 30 seconds

---

## Slide 3: What is a 4D Rubik's Cube?

**Talking Points**:
- Most of you know the 3×3×3 Rubik's Cube: 6 faces, ~43 quintillion states
- A 4D hypercube extends this concept to four dimensions

**KEY POINTS**:
- **8 cells** (think 3D "faces" rather than 2D faces)
- **State space** (point to formula):
  - "This formula accounts for all possible permutations and orientations of pieces"
  - Result: **~1.76 × 10^120 states**
  - "That's 10^100 times larger than the 3D cube!"

**Move notation**:
- Two-letter notation: FR = "Front cell toward Right cell"
- UO = "Up toward Outside" (the 4th dimension)
- "If visualizing is hard, don't worry—the computer handles the actual geometry"

**Timing**: 2 minutes

---

## Slide 4: Research Question

**Talking Points**:
- Our question: What happens when you repeat the same move sequence over and over?

**Three key concepts**:
1. **Orbit/Period**: Since there are finitely many states, we must eventually return—how many iterations?
2. **Chaos**: Sensitivity to perturbations, measured by Lyapunov exponent
3. **Discrete Dynamics**: Deterministic maps on finite state space

**Transition**: "Let me formalize this as a dynamical system..."

**Timing**: 1 minute

---

## Slide 5: Discrete Dynamical System

**Talking Points**:
- Here's the rigorous framework

**Walk through definitions**:
- **S** = state space (all ~10^120 configurations)
- **M** = move sequence, like (FR, UF)
- **T_M** = composite map: "We compose the moves in order"
  - Example: T_M(s) means "apply FR to state s, then apply UF to the result"
- **Trajectory**: Starting from solved state s₀, iterate repeatedly

**Period p**: 
- "The minimum n such that applying the sequence n times returns to solved"
- Example: "On a 3×3×3 cube, (R,U) has period 840"

**Key property**:
- "Since the state space is finite, every trajectory must eventually repeat"
- "We always return to solved—the question is how long it takes"

**Mathematical note**: "This is a deterministic discrete-time dynamical system on a finite state space"

**Timing**: 2 minutes

---

## Slide 6: Lyapunov Exponents

**Talking Points**:
- How do we measure chaos in this setting?

**Perturbation approach**:
- Take base sequence M with period p
- Perturb it: insert, delete, or replace a move → get M'
- Compute new period p'
- "Lyapunov exponent averages the log of these period ratios"

**Formula**: 
- λ = (1/N) Σ ln|p'ᵢ/p|
- "We test N perturbations (typically 15) and average"

**Formal definition** (blue block):
- "In continuous systems, Lyapunov measures how nearby trajectories diverge exponentially"
- Point to continuous formula: λ = lim (1/t) ln(δ(t)/δ(0))
- "We adapt this: instead of trajectory distance, we use period ratios"
- "This quantifies sensitivity in sequence space"

**Classification thresholds**:
- λ < 0.1: **Regular** — perturbations barely affect period
- 0.1 ≤ λ < ln(2) ≈ 0.69: **Sensitive** — moderate changes
- λ ≥ 0.69: **Chaotic** — small changes cause massive period differences

**Example**: "If λ = 3, perturbed sequences have periods differing by factor of e³ ≈ 20 on average"

**Timing**: 2.5 minutes

---

## Slide 7: Chaos in Finite Systems

**Talking Points**:
- This addresses a fundamental theoretical challenge

**The problem**:
- "Classical chaos theory was developed for infinite or continuous state spaces"
- "Requires sensitive dependence, topological mixing, dense periodic orbits"
- "Our system is finite—only 10^120 states"
- "All trajectories are periodic! No strange attractors, no continuous divergence"

**Our solution**:
- "We shift focus from state space to sequence space"
- Three-step approach (walk through):
  1. "Perturb the move sequence M → M', not the initial state"
  2. "Measure how orbit structure changes (period, cycle length)"
  3. "Compute Lyapunov on these period ratios"

**Key insight** (blue block):
- Read: "Chaos manifests as sensitivity of dynamical properties to small sequence perturbations"
- "This is structural chaos: how the dynamics change, not how trajectories diverge"
- "It's a genuine adaptation of chaos theory to finite discrete systems"

**Why this matters**: 
- "Validates that chaos is meaningful even without infinity"
- "Opens up finite discrete systems to rigorous chaos analysis"

**Timing**: 2 minutes

---

## Slide 8: Computational Approach

**Talking Points**:
- Now let me describe our implementation

**Tool Stack** (briefly):
- Rust: fast trajectory analysis
- Python: Lyapunov computation and statistics
- Octave: visualization

**Systematic Testing**:
- Tested all 64 two-move combinations
- Computed periods using cycle detection
- For interesting sequences: Lyapunov analysis with 15 perturbations

**Cycle Detection Algorithm** (blue block):
- "This is the core algorithm for finding periods"
- **Walk through pseudocode**:
  - "Start with solved state, mark it as visited"
  - "Apply move sequence repeatedly"
  - "Hash each resulting state with SHA256"
  - "If we've seen this hash before, we've found the cycle"
  - "Period = current iteration minus when we first saw this state"
- **Complexity**: "O(p) space for hash table, O(p·T_M) time where T_M is sequence application time"
- "For periods up to 10,000, this runs in milliseconds to seconds"

**Technical detail**: "SHA256 gives collision-resistant hashing—extremely unlikely to mistake different states"

**Transition**: "With this framework and methodology established, let's see what we discovered. [Person 2's name]?"

**Timing**: 2.5 minutes

---

## Handoff to Person 2

**Smooth transition**: "So we've established a rigorous dynamical systems framework adapted for finite state spaces. The computational tools can efficiently explore these systems. Now let's see what the data reveals. [Person 2's name]?"

**Total Time for Person 1**: ~8-9 minutes

---

## Quick Reference Card

**Key numbers**:
- State space: |S| ≈ 1.76 × 10^120
- Period example: (R,U) on 3D = 840
- Classification: λ < 0.1 (regular), 0.1-0.69 (sensitive), ≥0.69 (chaotic)
- Perturbations: N = 15 per sequence

**Key concepts**:
- Finite state space → all trajectories periodic
- T_M = composite map (iterate sequence)
- Period p = iterations to return to solved
- Discrete Lyapunov: λ = E[ln|p'/p|]
- Sequence space (not state space) for chaos

**Key formulas**:
- |S| = (16!/2) · 12^15 · 4 · 32! · 6^31 · 3 · (24!/2) · 2^23
- λ = (1/N) Σ ln|p'ᵢ/p|
- Algorithm: O(p·T_M) time, O(p) space

---

## Anticipated Questions (During Your Section)

**Q: Why is the state space so large?**
- A: "It factors in all permutations and orientations of 72 movable pieces. Corners alone contribute 16!/2 · 12^15 ≈ 10^25. Combine with faces and edges, you get 10^120."

**Q: How do you know SHA256 doesn't collide?**
- A: "SHA256 has 2^256 possible outputs—astronomically larger than our 10^120 state space. We tested millions of states with zero collisions. Collision probability is negligible."

**Q: Is this really chaos or just variance?**
- A: "It's genuine sensitivity. Small, controlled perturbations (one move change) produce large, systematic changes in period. The Lyapunov exponent quantifies this rigorously. It's not random variance—it's deterministic sensitivity."

**Q: Why measure chaos in sequence space instead of state space?**
- A: "In state space, all trajectories are periodic—there's no divergence. But different sequences produce wildly different orbits. Sequence space is where the complexity lives in finite systems."

**Q: How does this relate to classical chaos?**
- A: "Classical chaos measures trajectory divergence in phase space. We adapt this: measure how orbit structure (period, cycle length) changes in parameter space (sequence space). Same principle, different locus of sensitivity."

**Q: What about transients?**
- A: "In our experiments, all trajectories from solved state are purely periodic (no transient). This is expected since moves preserve puzzle structure."

---

## Mathematical Depth Notes

**For Math 538 audience**:
- Emphasize adaptation of continuous chaos theory to finite discrete systems
- Connect to discrete-time dynamical systems (Poincaré maps, iterates)
- Highlight novelty: sequence-space Lyapunov exponents
- Show computational validation of theoretical framework

**Theoretical contributions**:
1. Discrete Lyapunov exponents adapted to finite systems
2. Sequence space as locus of chaos (parameter space, not phase space)
3. Computational framework for systematic exploration
4. Empirical validation with reproducible results

**If asked about rigor**:
- "We're using well-defined mathematical structures: deterministic maps on finite sets"
- "Lyapunov exponent has clear statistical interpretation"
- "Results are reproducible—no randomness in dynamics, only in perturbations"
- "Validated across 126+ sequences with consistent methodology"

---

## Key Messages to Emphasize

1. **Finite ≠ simple**: "Even with finite state space, complexity emerges"
2. **Adaptation, not approximation**: "This is rigorous chaos theory for discrete systems"
3. **Computational validation**: "Theory guided experiments, experiments validated theory"
4. **Surprising results ahead**: "Person 2 will show counterintuitive findings that challenge our intuition"

---

**Total Time**: 8-9 minutes  
**Slide Count**: 8 (streamlined from 10)  
**Focus**: Dynamical systems and chaos theory (minimal group theory)

**Good luck! The framework is solid—present with confidence!**
