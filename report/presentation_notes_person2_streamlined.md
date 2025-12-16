# Presentation Notes: Person 2 (Results & Conclusions) - STREAMLINED VERSION

**Your Slides**: 9-18 (Key Findings → Thank You)  
**Duration**: ~9-10 minutes  
**Role**: Present results, visualizations, discuss implications and future work

---

## Slide 9: Key Findings

**Opening** (pick up from Person 1):
- "Thanks, [Person 1's name]. So with that framework, let's look at what we discovered."

**Talking Points**:
- We systematically tested sequences, and the results are fascinating

**Single moves** (top row):
- All single moves: period 8, λ = 0 (no chaos)
- "Makes sense: a single rotation returns quickly"

**Most chaotic sequences** (middle section):
- **MAJOR DISCOVERY**: Self-compositions!
  - FR→FR: period 4, λ = 5.94
  - FO→FO: period 4, λ = 6.09 — **most chaotic**
- "Repeating the same move twice creates extreme chaos"
- "Despite returning in only 4 iterations!"
- Four-move patterns (OF→OU→OB→OD): λ = 5.64

**High-period sequences** (bottom):
- FR→UF: period 10,080, λ = 3.95
- FR→UO: period 840, λ = 2.81
- "Long periods but LESS chaotic than self-compositions"

**KEY FINDING**: "Period does NOT predict chaos. The shortest orbits can be the most chaotic!"

**Timing**: 2.5 minutes

---

## Slide 10: Period vs Chaos

**Talking Points**:
- This plot quantifies that surprising relationship

**Point to features**:
- **X-axis**: Period (log scale, 4 to 10,000+)
- **Y-axis**: Lyapunov λ
- **Colors**: Blue/orange/red = regular/sensitive/chaotic

**Observations**:
1. **Left side**: Short periods (4-10) have λ > 5 (extreme chaos!)
2. **Right side**: Long periods (10,000+) only λ ≈ 3-4
3. **No correlation**: "If period predicted chaos, we'd see upward trend—we don't!"

**Interpretation**:
- "It's not about how long the orbit is"
- "It's about the structure of how the sequence acts on the puzzle"
- "Short, simple orbits can be highly sensitive to perturbations"

**Timing**: 1.5 minutes

---

## Slide 11: Classification Distribution

**Talking Points**:
- We classified 50 sequences by Lyapunov threshold

**Pie chart breakdown**:
- 30% regular (blue) — mostly single moves
- 24% sensitive (orange) — moderate
- **46% chaotic** (red) — nearly HALF!

**Why this matters**:
- "46% chaotic is surprisingly high"
- "Suggests chaos is common, not exceptional, in 4D sequence space"
- "Compared to 3D cubes, 4D exhibits richer chaotic behavior"

**Reason**: "Higher dimensions allow more complex interactions between pieces"

**Timing**: 1.5 minutes

---

## Slide 12: Top Chaotic Sequences

**Talking Points**:
- Bar chart ranks by λ

**Walk through**:
1. **FO→FO (λ = 6.09)** — highest
2. **FR→FR (λ = 5.94)** — second
3. **Self-compositions dominate** top 5
4. **Four-move cycles** also high
5. **FR→UF appears** but lower

**Open question**:
- "Why are self-compositions so chaotic?"
- **Hypothesis**: "First application scrambles, second application acts on displaced state"
- "Creates interference or resonance effects"
- "No formal proof yet—excellent for future research"

**Timing**: 1.5 minutes

---

## Slide 13: Lyapunov vs Sequence Length

**Talking Points**:
- How does length affect chaos?

**Pattern**:
- **Length 1**: All λ = 0
- **Length 2**: Peak chaos (λ > 6)
- **Length 3-5**: Lower max, more variance

**Interpretation**:
- "Two moves is the 'sweet spot'"
- "Long enough to create complexity"
- "Short enough for self-compositions"
- "Longer sequences tend to average out—like a random walk reaching equilibrium"

**Timing**: 1.5 minutes

---

## Slide 14: Sequence Animations

**Talking Points**:
- We created visualizations of actual puzzle states
- "Available during Q&A if interested"

**Three types**:
1. **FR (single)**: Period 8, λ = 0, simple cycle
2. **FO→FO**: Period 4, λ = 6.09, rapid scrambling
3. **FR→FR**: Period 4, λ = 5.94, similar chaos

**Key insight**:
- "Even with period 4, intermediate states are maximally scrambled"
- "Perturbations produce completely different orbit structures"
- "This is discrete chaos: combinatorial explosion, not continuous divergence"

**Timing**: 1 minute

---

## Slide 15: Key Takeaways

**Talking Points** (emphasize each):

**1. Rich dynamics in 4D**:
- "4D systems are not just bigger 3D systems"
- 46% chaotic shows genuine complexity
- Period diversity (4 to 10,080)

**2. Self-compositions maximize chaos**:
- "Most surprising finding"
- λ > 5 is extreme
- "Repeating a move is structurally optimal for chaos"

**3. Period ≠ complexity**:
- "Challenges intuition from continuous systems"
- "Short orbits can be maximally chaotic"
- "Structure matters more than length"

**4. Discrete chaos is rigorous**:
- "Successfully adapted Lyapunov to finite systems"
- "Sequence space framework is valid"
- "Small perturbations → large structural changes"

**Meta-point**: "This validates chaos theory in finite discrete systems as rigorous mathematics, not just approximation"

**Timing**: 2 minutes

---

## Slide 16: Future Directions

**Talking Points**:

**Theoretical**:
- "Why self-compositions are chaotic—open question"
- "Can we predict chaos from sequence properties?"
- "Connection to ergodic theory in finite systems?"

**Computational**:
- "5D or 6D hypercubes (if feasible)"
- "Longer sequences (test averaging hypothesis)"
- "Systematic perturbation taxonomy"

**Applications**:
- "Cryptographic PRNGs from chaotic sequences"
- "Physical systems with discrete symmetries"
  - Quantum computing (finite state spaces)
  - Lattice models
- "Complexity theory connections"

**Timing**: 1.5 minutes

---

## Slide 17: References

**Talking Points**:
- "Built on foundational theory and tools"
- Devaney, Strogatz (chaos), Joyner (puzzles)
- Hyperspeedcube enabled 4D simulation
- "Citations on slide and in report"

**Timing**: 30 seconds

---

## Slide 18: Thank You / Questions

**Closing**:
- "Thank you!"
- "Happy to answer questions"
- "Code on GitHub for reproduction"

**Timing**: 30 seconds + Q&A

---

## Anticipated Questions

**Q: Can you show a GIF?**
- A: "Yes! Let me show FO→FO..." [Open `disp/figures/sequence_FO_FO.gif`]

**Q: 3D vs 4D comparison?**
- A: "4D shows higher chaos. FR→UF on 4D: period 10,080, λ = 3.95. Analogous R→U on 3D: period 840, lower λ. Extra dimension creates more complexity."

**Q: What does λ = 6 mean practically?**
- A: "Period changes by factor e^6 ≈ 400 on average. A period-4 sequence might become period-1600 with one move change. That's extreme sensitivity!"

**Q: Is this really chaos or variance?**
- A: "Genuine chaos. Small, systematic perturbations (one move) produce large, consistent changes. Not randomness—deterministic sensitivity."

**Q: Why self-compositions?**
- A: "Hypothesis: First application displaces pieces, second acts on already-displaced configuration. Creates multiplicative complexity. No proof yet—great research direction."

**Q: Theoretical max λ?**
- A: "Roughly ln(state space) ≈ 280, but algebraic constraints limit achievable values. Our max ~6 suggests strong constraints."

**Q: Why not test 1000s of sequences?**
- A: "Computational cost. Each Lyapunov needs 15+ runs, taking minutes. We did systematic 2-move coverage (64) plus selected longer ones. ~2 hours total compute."

---

## Q&A Strategy

**Person 1 handles**:
- Framework, Lyapunov definition, algorithm, finite-system chaos

**Person 2 handles**:
- Results interpretation, chaos classification, self-compositions, comparisons

**Both can discuss**:
- Why 4D, implementation, future work

**If unsure**:
- "Excellent question for future research"
- "We didn't explore that—here's speculation..."
- "Let me think... [honest response]"

**Keep answers**: 30-60 seconds, refer to slides

---

## Quick Reference

**Key numbers**:
- **46%** chaotic (23/50)
- **FO→FO**: λ = 6.09, period 4 (most chaotic)
- **FR→UF**: period 10,080, λ = 3.95 (longest)
- **FR→FR**: λ = 5.94, period 4 (second)
- Thresholds: <0.1, 0.1-0.69, ≥0.69

**Key messages**:
1. Self-compositions = maximum chaos
2. Period ≠ complexity (main surprise)
3. 46% chaotic validates framework
4. 4D richer than 3D

**Files ready**:
- GIFs: `disp/figures/sequence_*.gif`
- Code: github.com/ltpie123/final

---

## Mathematical Connection Points

**For Math 538**:
- Builds on Devaney's chaos definition (adapted)
- Discrete-time dynamical systems on finite sets
- Lyapunov exponents (discrete version)
- Computational validation approach

**Novel contribution**:
- Sequence-space Lyapunov for finite systems
- Empirical discovery: self-composition phenomenon
- Period-chaos independence

---

**Total Time**: 9-10 minutes (+ Q&A)  
**Combined**: 17-19 minutes  
**Leaves**: 1-3 min buffer in 20-min slot, or 6-8 min in 25-min slot

**Present with confidence—strong results!**
