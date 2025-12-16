# Presentation Notes: Person 1 (Introduction & Theory)

**Your Slides**: 1-7 (Title → Computational Approach)  
**Duration**: ~8-9 minutes  
**Role**: Set up the problem, explain mathematical framework, describe methods

---

## Slide 1: Title Slide

**Talking Points**:
- Good [morning/afternoon], everyone. Today we'll be presenting our final project on chaos theory in 4-dimensional Rubik's cubes.
- This project explores discrete dynamical systems on hyperdimensional puzzles—a fascinating intersection of group theory, chaos theory, and computational mathematics.
- I'll cover the introduction and mathematical framework, then [Person 2's name] will present our results.

**Timing**: 30 seconds

---

## Slide 2: Overview

**Talking Points**:
- Here's a quick roadmap of what we'll cover today
- I'll start with an introduction to 4D hypercubes and the mathematical framework
- Then explain our computational methods
- [Person 2's name] will present our key findings, visualizations, and conclusions

**Timing**: 30 seconds

---

## Slide 3: What is a 4D Rubik's Cube?

**Talking Points**:
- Most of you are familiar with the classic 3×3×3 Rubik's Cube
- It has 6 faces—front, up, right, left, back, and down
- About 43 quintillion possible states
- A 4D hypercube takes this concept to the next dimension

**KEY POINT**: A 4D hypercube has 8 cells—think of these as 3D "faces" rather than 2D faces
- The state space is exponentially larger than the 3D version
- Instead of single-letter moves like R or U, we use two-letter notation
  - FR means "rotate the Front cell toward the Right cell"
  - UO means "rotate Up toward Outside" (the 4th dimension)
  
**Visual Aid**: Point to the table showing move notation

**Engagement**: "If visualizing 4D is challenging, don't worry—even mathematicians struggle with this! The computer handles the actual rotations."

**Timing**: 2 minutes

---

## Slide 4: Research Question

**Talking Points**:
- Our central question is deceptively simple: What happens when you repeat the same move sequence over and over on a 4D hypercube?

**Three key concepts**:
1. **Orbit/Period**: Since there are finitely many states, eventually you must return to where you started. The period is how many iterations this takes.
2. **Chaos**: We measure sensitivity to small changes using the Lyapunov exponent—a standard metric from chaos theory
3. **Discrete Dynamics**: Unlike continuous systems (pendulums, weather), we're dealing with discrete time steps and finite states

**Transition**: "Let me formalize this mathematically..."

**Timing**: 1.5 minutes

---

## Slide 5: Discrete Dynamical System

**Talking Points**:
- Here's the formal mathematical framework
- S is our state space—all possible puzzle configurations
- We choose a move sequence M, like (FR, UF)
- This defines a composite map T_M that takes any state s to a new state
- **Walk through the formula**: "We apply move 1, then move 2, then move 3, and so on"

**Key concept**: Starting from the solved state s₀, we iterate this map
- After n iterations, we've applied the sequence n times
- The period p is when we first return to the solved state

**Example**: "On a 3×3×3 cube, the sequence (R,U) has period 840—meaning you'd have to repeat those two moves 840 times to return to solved!"

**Technical note**: This is deterministic—no randomness involved

**Timing**: 2 minutes

---

## Slide 6: Lyapunov Exponents

**Talking Points**:
- Now, how do we measure chaos in a discrete, finite system?
- Classical Lyapunov exponents measure how nearby trajectories diverge in continuous systems
- We adapt this to our finite puzzle setting

**Our approach**:
1. Take a base sequence M with period p
2. Perturb it slightly—insert a random move, delete one, or swap one
3. Compute the new period p'
4. The Lyapunov exponent λ averages how much these periods change

**Walk through the formula**: 
- "We take the natural log of the period ratio"
- "Average over N perturbations—we used N=15 in most experiments"

**Classification thresholds**:
- λ < 0.1: **Regular/Trivial** — perturbations barely matter
- 0.1 ≤ λ < ln(2) ≈ 0.69: **Sensitive** — noticeable but moderate changes
- λ ≥ 0.69: **Chaotic** — small changes produce drastically different orbits

**Key insight**: "This is a discrete analogue of continuous Lyapunov exponents, adapted for finite state spaces"

**Timing**: 2.5 minutes

---

## Slide 7: Computational Approach

**Talking Points**:
- This project required building a complete analysis pipeline

**Tool Stack** (briefly):
- **Rust** for the core engine—fast trajectory tracking with cycle detection
- **Python** for statistical analysis and Lyapunov computation
- **Octave** for publication-quality visualizations

**Systematic Testing**:
- We tested all 64 possible two-move combinations
- "Why 64? There are 8 basic 4D moves we focused on, giving 8×8 = 64 pairs"
- Used SHA256 hashing to detect when we've returned to a previous state
- For interesting sequences, we computed 15-20 perturbations each

**Technical detail**: The Hyperspeedcube library (by Andrew Farkas) provided the underlying puzzle engine—we built analysis tools on top of it

**Transition to Person 2**: "Now I'll hand it over to [Person 2's name] to present our findings..."

**Timing**: 2 minutes

---

## Handoff to Person 2

**Smooth transition**: "So we've established the mathematical framework and our systematic testing approach. Now let's see what we discovered. [Person 2's name]?"

**Total Time for Person 1**: ~8-9 minutes

---

## Quick Reference Card

**Key numbers to remember**:
- 4D hypercube: 8 cells (3D faces)
- 64 two-move combinations tested
- Classification: λ < 0.1 (regular), 0.1-0.69 (sensitive), ≥0.69 (chaotic)
- Period example: R,U on 3D cube = 840

**Key concepts**:
- State space S = all configurations
- T_M = composite map (apply sequence)
- Period p = iterations to return to solved
- Lyapunov λ = measure of chaos via perturbations

**Backup info if asked**:
- SHA256 used for state hashing (collision-resistant)
- Perturbations: insert/delete/replace moves
- N=15 perturbations per sequence (convergence tested)

---

## Anticipated Questions (During Your Section)

**Q: Why 4D specifically?**
- A: "It's the first dimension beyond our intuition but still computationally tractable. 5D+ becomes much more expensive."

**Q: What does 'Outside' mean in 4D?**
- A: "It's the direction along the 4th spatial axis—perpendicular to all three dimensions we can visualize. Think of it as 'ana/kata' in 4D geometry."

**Q: Why use Lyapunov exponents for discrete systems?**
- A: "Standard chaos metrics like sensitive dependence don't apply directly to finite systems. Lyapunov exponents adapted to period changes give us a quantitative chaos measure."

**Q: How long do computations take?**
- A: "Single sequences: milliseconds to seconds. Full 64-pair systematic test: about 10 minutes. Lyapunov computations took about 2 hours total."

---

**Confidence Boosters**:
- You've done rigorous mathematical work—present with confidence
- If stuck, refer back to the formulas on slides
- Math framework is solid—Devaney, Strogatz use similar approaches
- The results [Person 2] will show validate the theory beautifully

**Good luck with your half!**
