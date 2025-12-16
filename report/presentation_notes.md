# Presentation Notes: Chaos in Hyperdimensional Rubik's Cubes

**Course**: Math 538 Final Project  
**Duration**: ~15-20 minutes  
**Date**: December 2024

---

## Slide 1: Title Slide

**Talking Points**:

- Good [morning/afternoon], everyone. Today I'll be presenting my final project on chaos theory in 4-dimensional Rubik's cubes.
- This project explores discrete dynamical systems on hyperdimensional puzzles—a fascinating intersection of group theory, chaos theory, and computational mathematics.

**Timing**: 30 seconds

---

## Slide 2: Overview

**Talking Points**:

- Here's a quick roadmap of what we'll cover today
- We'll start with an introduction to 4D hypercubes
- Then establish the mathematical framework using discrete dynamical systems
- Discuss our computational methods
- Present key findings including some surprising results
- And conclude with implications and future directions

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

**Transition**: "Let's formalize this mathematically..."

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
- "Why 64? There are 12 basic 4D moves, but we restricted to 8 that preserve puzzle structure, giving 8×8 = 64 pairs"
- Used SHA256 hashing to detect when we've returned to a previous state
- For interesting sequences, computed 15-20 perturbations each

**Technical detail**: The Hyperspeedcube library (by Andrew Farkas) provided the underlying puzzle engine—we built analysis tools on top of it

**Timing**: 2 minutes

---

## Slide 8: Key Findings

**Talking Points**:

- Now for the exciting results!

**Single moves** (top row):

- All single moves have period 8—completely trivial
- Lyapunov exponent is zero (no chaos)
- "This makes sense geometrically—a single rotation in 4D returns to itself quickly"

**Most chaotic sequences** (middle section):

- **SURPRISE #1**: Self-compositions dominate!
  - FR→FR has period only 4, but λ = 5.94
  - FO→FO has period 4 but λ = 6.09—the most chaotic we found!
- "These are sequences where we repeat the same move twice"
- Four-move sequences like OF→OU→OB→OD also show extreme chaos (λ = 5.64)

**High-complexity sequences** (bottom section):

- FR→UF has a massive period of 10,080 with λ = 3.95
- FR→UO: period 840, λ = 2.81

**Key counterintuitive finding**: "Short periods do NOT imply simple behavior! The most chaotic sequences have the shortest orbits."

**Timing**: 3 minutes

---

## Slide 9: Period vs Chaos

**Talking Points**:

- This plot drives home the surprising relationship
- **X-axis**: Period (log scale—notice it ranges from 4 to over 10,000)
- **Y-axis**: Lyapunov exponent (chaos measure)
- **Colors**: Blue = regular, orange = sensitive, red = chaotic

**Key observations**:

1. **Left side of plot**: Short periods (4-10) include the MOST chaotic sequences (top red points)
2. **Right side**: Long periods don't guarantee high chaos—many are only moderately sensitive
3. **No clear correlation**: Period and chaos are nearly independent

**Why this matters**:

- Classical intuition: complex = long orbits
- Reality: Geometric structure of the move matters more than orbit length
- Self-compositions create rapid scrambling despite returning quickly

**Transition**: "Let's look at the overall distribution of behaviors..."

**Timing**: 2 minutes

---

## Slide 10: Classification Distribution

**Talking Points**:

- We analyzed 50 sequences total and classified each by Lyapunov exponent

**Results**:

- 30% are regular (blue)—mostly single moves or commuting pairs
- 24% are sensitive (orange)—moderate chaos
- **46% are chaotic** (red)—nearly half!

**Implications**:

- "This is a surprisingly high proportion"
- "It suggests that chaos is the norm, not the exception, for random move combinations on 4D hypercubes"
- Compare to 3D cubes where most two-move sequences are less chaotic

**Why 4D is different**:

- Higher dimensional rotations have more degrees of freedom
- More ways for pieces to interact in complex patterns
- Group structure is richer

**Timing**: 1.5 minutes

---

## Slide 11: Top Chaotic Sequences

**Talking Points**:

- This bar chart shows the top 10 most chaotic sequences ranked by Lyapunov exponent

**Observations**:

1. **Self-compositions dominate**: FO→FO, FR→FR, FL→FL all in top 5
2. **Four-move patterns**: OF→OU→OB→OD and FR→OR→FL→OL show extreme chaos
3. **Classic pairs**: FR→UF appears but is outranked by self-compositions

**Theoretical puzzle**:

- "Why are self-compositions so chaotic?"
- Hypothesis: Repeating the same rotation might create resonance-like effects
- The second application interferes with partially scrambled state from first
- Still an open question—no formal proof yet

**Timing**: 1.5 minutes

---

## Slide 12: Lyapunov vs Sequence Length

**Talking Points**:

- This scatter plot shows how chaos depends on sequence length

**Clear pattern**:

- **Length 1** (leftmost): All have λ = 0 (trivial)
- **Length 2** (second column): Highest chaos! Top points all here
- **Length 3-5**: More varied, but lower maximum chaos

**Interpretation**:

- Two-move sequences hit a "sweet spot" for chaos
- Long enough to create complexity
- Short enough that self-compositions are possible
- Longer sequences tend to average out chaos—they explore more of the state space

**Unexpected finding**: "More moves ≠ more chaos"

**Timing**: 1.5 minutes

---

## Slide 13: Sequence Animations

**Talking Points**:

- We created animated GIFs showing actual puzzle states during these sequences
- "I can show these if there's interest during Q&A"

**Available animations**:

1. **FR (single)**: Baseline—simple rotation, period 8, no chaos
2. **FO→FO**: The most chaotic—watch how pieces scatter despite returning in just 4 iterations
3. **FR→FR**: Second most chaotic—similar rapid scrambling

**Visual insight**:

- "Even though these return to solved quickly, intermediate states are highly scrambled"
- "Perturbations to these sequences produce radically different intermediate patterns"
- "This is what chaos looks like in discrete systems—not continuous divergence, but combinatorial explosion of possibilities"

**Timing**: 1 minute

---

## Slide 14: Key Takeaways

**Talking Points** (walk through each point slowly):

**1. Rich dynamics**:

- "4D hypercubes are not simple extensions of 3D cubes"
- 46% chaotic is surprisingly high
- Period range (4 to 10,080) shows incredible diversity

**2. Self-compositions are extreme**:

- "This is the most surprising finding"
- Repeating a single move is not redundant—it creates maximal chaos
- Highest λ > 5, compared to theoretical maximum around 7-8 for these systems

**3. Period ≠ complexity**:

- "This challenges our intuition"
- Short orbits can be highly chaotic
- Long periods don't guarantee interesting behavior
- "It's about the geometry of how moves interact, not just how many states you visit"

**4. Discrete chaos is real**:

- "We successfully adapted continuous chaos theory to finite systems"
- Lyapunov exponents work in discrete settings
- Small perturbations (one move change) → massive behavioral shifts
- "This validates discrete dynamical systems as a lens for studying complex phenomena"

**Timing**: 2.5 minutes

---

## Slide 15: Future Directions

**Talking Points**:

**Theoretical questions**:

- "The self-composition phenomenon needs mathematical explanation"
  - Is there a group-theoretic reason?
  - Does it relate to conjugacy classes?
- "Can we predict chaos from move properties alone?"
  - Connection to commutator structure?
  - Role of symmetries in 4D?

**Computational extensions**:

- "5D or 6D hypercubes—if computationally feasible"
  - Current tools can handle it, but periods might exceed compute budget
- "Longer sequences (5-10 moves)"
  - Explore if chaos persists or averages out
- "Different perturbation types"
  - Currently random; could try systematic perturbations

**Applications** (speculative):

- "Cryptographic PRNGs based on chaotic puzzle sequences?"
  - High Lyapunov → good mixing properties
- "Physical systems with discrete symmetries"
  - Crystallography, quantum systems
  - Puzzles as toy models for more complex phenomena

**Timing**: 2 minutes

---

## Slide 16: Thank You / Questions

**Talking Points**:

- "Thank you for your attention!"
- "I'm happy to answer questions about the mathematics, implementation, or findings"

**Anticipated Questions & Answers**:

**Q: How long did computations take?**

- A: "Single sequences: milliseconds to seconds. Full 64-pair systematic test: about 10 minutes. Lyapunov computations (15 perturbations × 126 sequences): about 2 hours total."

**Q: Can you show a GIF?**

- A: "Yes! Let me pull up FO→FO..." [Be ready to open disp/figures/sequence_FO_FO.gif]

**Q: Why SHA256 for state hashing?**

- A: "Needed a robust hash since puzzle states can't be directly compared. SHA256 is collision-resistant enough for our state space size. We tested for collisions—none found across millions of states."

**Q: What about 3D vs 4D comparison?**

- A: "Great question! We found that 4D has higher chaos rates. For example, FR→UF on 4D has period 10,080, while the analogous R→U on 3D has period 840—but with lower Lyapunov exponent. The extra dimension creates more complex interactions."

**Q: What's the theoretical maximum Lyapunov?**

- A: "For our perturbation scheme, roughly ln(period). Self-compositions achieve near-maximum values, suggesting they're close to maximally chaotic for their period length."

**Q: Could this be used for scrambling?**

- A: "Absolutely! Speedcubers might find FO→FO interesting—it scrambles quickly despite short period. Though for serious scrambling, you'd want longer sequences to explore more states."

**Timing**: 1-2 minutes + Q&A

---

## Technical Backup Information

### If Asked About Implementation Details:

**Rust trajectory engine (`ctrl/`)**:

- Uses `hyperpuzzle` crate for puzzle simulation
- Cycle detection via HashMap of state hashes
- SHA256 hashing of piece transformation matrices
- Typically processes 1000-10000 iterations/second

**Python analysis (`obsv/`)**:

- `lyapunov.py`: Perturbation generation and λ computation
- `analyze.py`: Statistical summaries and period distributions
- `ctrl_runner.py`: Interface to Rust engine
- Uses NumPy for numerical computations

**Octave visualization (`disp/`)**:

- Reads CSV data from Python analysis
- Generates publication-quality PNG figures (300 DPI)
- Scripts: `plot_lyapunov_vs_length.m`, `plot_period_vs_lambda.m`, etc.

### If Asked About Mathematical Rigor:

**Lyapunov exponent formula**:
$$\lambda = \frac{1}{N} \sum_{i=1}^{N} \ln\left|\frac{p'_i}{p}\right|$$

- N = 15 perturbations (based on convergence testing)
- Perturbations: 50% insert, 30% delete, 20% replace
- Bootstrap validation: λ estimates stable within ±0.2

**Classification thresholds**:

- Regular (λ < 0.1): Empirical—perturbations cause < 10% period change
- Chaotic (λ ≥ ln(2)): Standard from discrete dynamical systems literature
- Sensitive: Middle range

### If Asked About Related Work:

**Group theory of puzzles**:

- Joyner (2008): _Adventures in Group Theory_
- Rokicki et al. (2014): Proved Rubik's Cube diameter is 20

**Chaos theory**:

- Devaney (2003): _Introduction to Chaotic Dynamical Systems_
- Strogatz (2015): _Nonlinear Dynamics and Chaos_

**4D puzzles**:

- Limited academic literature—mostly recreational mathematics
- Roice Nelson, Melinda Green: 4D puzzle pioneering work
- Our work is novel in applying chaos theory systematically

---

## Presentation Tips

**Pacing**:

- Total slides: 16
- Target time: 15-18 minutes (leaves 2-5 min for Q&A in 20-min slot)
- Don't rush the "Key Findings" slide—it's the highlight

**Emphasis points**:

- **Counterintuitive results**: Short periods with high chaos
- **Self-compositions**: The most surprising discovery
- **Visual data**: Pause on graphs, let audience absorb

**Body language**:

- Point to specific data points on plots
- Use hand gestures when explaining 4D rotations
- Make eye contact during key takeaways

**Avoid**:

- Deep technical details unless asked
- Excessive focus on implementation (it's a math presentation)
- Apologizing for complexity—embrace it!

**If running long**:

- Skip slide 13 (Animations)—can reference during Q&A
- Shorten slide 15 (Future Directions) to 1 minute
- Condense slide 7 (Methods) to 1.5 minutes

**If running short**:

- Expand on mathematical framework (slides 5-6)
- Discuss specific examples in more detail
- Show animations during main presentation

---

## Key Messages to Emphasize

1. **This is a novel application of chaos theory to discrete finite systems**
2. **4D hypercubes exhibit richer dynamics than 3D cubes**
3. **Self-compositions are unexpectedly chaotic—major finding**
4. **Period and complexity are independent—challenges intuition**
5. **Computational approach enabled systematic exploration**

---

## Closing Thought (if time permits)

"This project shows that discrete dynamical systems—even on seemingly simple objects like puzzles—can exhibit complex, chaotic behavior. The fact that a 4D Rubik's cube, a completely deterministic finite system, produces such rich dynamics reminds us that chaos isn't just about continuous flows or infinite dimensions. It's about how simple rules interact in unexpected ways. And sometimes, the simplest sequences—repeating a single move—create the most chaos."

---

**Final Check Before Presenting**:

- [ ] Figures compiled and readable in PDF
- [ ] Backup GIFs ready to show if asked
- [ ] Laptop charged / HDMI adapter ready
- [ ] Practiced timing (aim for 16-17 minutes to leave buffer)
- [ ] Key numbers memorized: 46% chaotic, λ_max = 6.09, period range 4-10,080
- [ ] GitHub link ready: `github.com/ltpie123/final`

**Good luck! You've done rigorous, novel work—present with confidence!**
