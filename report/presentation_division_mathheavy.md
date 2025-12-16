# Presentation Division: Two-Person Team (MATH-HEAVY VERSION)

## Overview

**Total Slides**: 20 (was 17, added 3 math slides)  
**Total Time**: 19-21 minutes (recommend requesting 25 min slot for Q&A buffer)  
**Slide Deck**: `/home/hi/School/math538/final/report/presentation.pdf`  
**Course**: Math 538 - Discrete Dynamical Systems & Chaos Theory

---

## Person 1: Introduction & Mathematical Framework

**Slides**: 1-10  
**Duration**: ~10-11 minutes  
**Notes**: `presentation_notes_person1_mathheavy.md`

### Slide Breakdown:
1. **Title Slide** - Introduction
2. **Overview** - Roadmap
3. **What is a 4D Rubik's Cube?** - Basic setup + state space formula
4. **Puzzle Structure & Symmetry** - NEW: Piece types, B₄ group, order 384
5. **Research Question** - Key concepts
6. **Discrete Dynamical System** - Framework + group theory
7. **Permutation Theory & Constraints** - NEW: Parity, monoflip, A₁₆
8. **Lyapunov Exponents** - Chaos metric + discrete adaptation
9. **Chaos in Finite Systems** - NEW: Why sequence space not state space
10. **Computational Approach** - Methods + cycle detection algorithm

### Key Mathematical Content Added:
- **State space formula**: $|S| = \frac{16!}{2} \cdot 12^{15} \cdot 4 \cdot 32! \cdot 6^{31} \cdot 3 \cdot \frac{24!}{2} \cdot 2^{23} \approx 1.76 \times 10^{120}$
- **Symmetry group**: Hyperoctahedral group $B_4$, order 384
- **Cyclic subgroups**: $\langle T_M \rangle$ with order $p$ (the period)
- **Parity constraints**: Corners in $A_{16}$, orientation sums mod 3 and mod 2
- **Monoflip invariant**: Unique 4D phenomenon from $A_4$ structure
- **Discrete Lyapunov**: Formal adaptation from continuous systems
- **Cycle detection algorithm**: Pseudocode with complexity analysis

### Mathematical Depth:
- Group theory throughout (puzzle group, cyclic subgroups, symmetry groups)
- Permutation theory (alternating groups, parity)
- Formal chaos definitions adapted to finite systems
- Algorithmic complexity analysis

---

## Person 2: Results & Conclusions

**Slides**: 11-20  
**Duration**: ~9-10 minutes  
**Notes**: `presentation_notes_person2_mathheavy.md`

### Slide Breakdown:
11. **Key Findings** - Main results, self-compositions discovery
12. **Period vs Chaos** - Scatter plot, no correlation
13. **Classification Distribution** - 46% chaotic pie chart
14. **Top Chaotic Sequences** - Bar chart, self-compositions dominate
15. **Lyapunov vs Sequence Length** - Sweet spot at length 2
16. **Sequence Animations** - Visual demonstrations
17. **Key Takeaways** - Four main insights
18. **Future Directions** - Open questions, applications
19. **References** - Citations
20. **Thank You / Questions** - Closing

### Key Results to Emphasize:
- **Self-compositions (FR→FR, FO→FO)** most chaotic despite short periods
- **Period ≠ complexity**: Subgroup order doesn't predict chaos
- **46% chaotic**: Validates discrete chaos framework
- **Length 2 sweet spot**: Highest chaos at 2-move sequences

---

## Division Rationale

### Person 1 (Theory-Heavy):
- Establishes rigorous mathematical foundation
- Group theory, permutation theory, symmetry groups
- Formal chaos definitions for finite systems
- More abstract, formula-focused
- **Strength needed**: Comfort with mathematical notation and abstract algebra

### Person 2 (Results-Heavy):
- Delivers empirical validation of framework
- Emphasizes surprising/counterintuitive findings
- More visual (plots, charts, animations)
- Connects results back to group theory
- **Strength needed**: Data interpretation and enthusiasm about discoveries

### Natural Transition:
**Person 1 ends:** "With this rigorous mathematical framework and computational approach established, let's see what the data reveals. [Person 2's name]?"

**Person 2 begins:** "Thanks, [Person 1's name]. So with that framework established, let's look at what we discovered."

---

## New Mathematical Content Summary

### Slide 4: Puzzle Structure & Symmetry
- **72 movable pieces**: 16 corners (12 orientations), 32 faces (6 orientations), 24 edges (2 orientations)
- **Symmetry group B₄**: Order 384 = 2^4 × 4!
- **Structure**: Wreath product S₂ ≀ S₄
- **Coxeter notation**: [4,3,3]

### Slide 7: Permutation Theory & Constraints
- **State representation**: s = (π, o)
- **Corner parity**: π₄c ∈ A₁₆ (even permutations only)
- **Edge-Face parity**: sgn(π₂c) = sgn(π₃c)
- **Orientation sums**: Σo₃c ≡ 0 (mod 3), Σo₂c ≡ 0 (mod 2)
- **Monoflip invariant**: Unique to 4D, related to A₄ and Klein four-group

### Slide 9: Chaos in Finite Systems
- **Challenge**: Classical chaos requires infinite/continuous spaces
- **Solution**: Measure chaos in sequence space, not state space
- **Key insight**: Sensitivity of dynamical properties (period, orbit structure) to perturbations
- **Theoretical contribution**: Rigorous chaos framework for finite discrete systems

### Slide 10: Cycle Detection Algorithm
- **Pseudocode**: Full algorithmic description
- **Complexity**: O(p·(T_M + H)) time, O(p) space
- **SHA256 hashing**: Collision-resistant state fingerprinting

---

## Coordination Strategy

### Before Presentation:
1. **Practice together** - Full run-through at least twice
2. **Time yourselves** - Person 1: 10-11 min, Person 2: 9-10 min
3. **Sync on mathematical depth** - Both should understand all equations
4. **Divide Q&A**:
   - **Person 1**: Group theory, Lyapunov definitions, parity, algorithm
   - **Person 2**: Results interpretation, chaos classification, comparisons
   - **Either**: Implementation, why 4D, general methodology

### During Presentation:
- **Support each other** - Nod, show engagement
- **Backup**: If partner struggles with math, gently assist
- **Q&A strategy**:
  - Theory/framework → Person 1
  - Results/data → Person 2
  - Open questions → Either, discuss together

### Mathematical Rigor:
- **For Math 538**: This is your chance to show depth
- **Don't shy away** from equations—the audience expects rigor
- **Connect to course**: Devaney's chaos definition, discrete-time systems, group actions
- **Emphasize novelty**: Sequence-space Lyapunov is a genuine contribution

---

## Time Management

### If Running Long:
- **Person 1**: Shorten Slide 4 (Symmetry) to 1.5 min
- **Person 2**: Skip Slide 16 (Animations) or reduce to 30 sec
- **Person 2**: Condense Slide 18 (Future Directions) to 1 min

### If Running Short:
- **Person 1**: Expand on monoflip invariant (fascinating 4D property)
- **Person 2**: Show animations during main presentation
- **Both**: Invite questions during presentation (interactive style)

### Ideal Timing:
- Person 1: 10 minutes
- Person 2: 9 minutes
- Total: 19 minutes
- Q&A: 6 minutes (in 25-min slot)

---

## Mathematical Talking Points for Q&A

### If Asked About Rigor:
- "We're working in well-defined algebraic structures: puzzle groups as subgroups of S_n"
- "Lyapunov exponent is a computable real number with statistical interpretation"
- "Results are reproducible—deterministic system, no randomness in dynamics"

### If Asked About Connections to Course Material:
- "Extends Devaney's definition of chaos to finite discrete systems"
- "Group actions as dynamical systems—orbits are group-theoretic orbits"
- "Discrete Lyapunov exponents analogous to continuous case"
- "Finite-state Markov chains as limiting case when trajectories aren't purely periodic"

### If Asked About Theoretical Contributions:
1. **Discrete Lyapunov in finite spaces**: Adapted from continuous, validated computationally
2. **Sequence-space chaos**: Locus of sensitivity shifts from state space to parameter space
3. **Group-theoretic chaos**: Subgroup order (period) doesn't predict sensitivity
4. **Self-composition phenomenon**: Empirical discovery with open theoretical explanation

---

## Quick Reference: Key Math

**Person 1 Should Know:**
- $|S| \approx 1.76 \times 10^{120}$ (state space)
- $|B_4| = 384$ (symmetry group order)
- $\langle T_M \rangle$ = cyclic subgroup of period $p$
- Parity: $\pi_{4c} \in A_{16}$
- Monoflip: Unique to 4D, $A_4$ structure
- Discrete Lyapunov: $\lambda = \mathbb{E}[\ln|p'/p|]$

**Person 2 Should Know:**
- 46% chaotic (23/50 sequences)
- FO→FO: λ = 6.09, period 4 (highest)
- FR→UF: period 10,080, λ = 3.95
- Classification: <0.1, 0.1-0.69, ≥0.69
- No correlation between period and λ

---

## Emergency Scenarios

### Person 1 Forgets a Formula:
- Refer to slide: "As shown here..."
- Key formulas are on slides—read them if needed
- Person 2 can prompt: "The state space formula?"

### Person 2 Forgets a Number:
- Refer to plot: "As we can see in this graph..."
- Key numbers in table on Slide 11
- Person 1 can prompt: "46% chaotic, right?"

### Technical Question Neither Can Answer:
- "That's an excellent question for future investigation"
- "Our framework could be extended to address that"
- "We focused on 2-move sequences—your question about longer sequences is interesting"

### Audience Seems Lost:
- **Person 1**: Pause, ask "Should I clarify the group theory?"
- **Person 2**: Use analogies: "Think of it like..."
- **Both**: Offer to discuss details after presentation

---

## Files & Resources

**Created Files:**
1. `presentation.pdf` - 20-slide deck with math enhancements
2. `presentation_notes_person1_mathheavy.md` - Person 1 detailed notes
3. `presentation_notes_person2_mathheavy.md` - Person 2 detailed notes
4. `presentation_division_mathheavy.md` - This coordination guide
5. `math_enhancements.md` - Documentation of math content added

**Original Files (still valid):**
- `presentation_notes_person1.md` - Original version (lighter on math)
- `presentation_notes_person2.md` - Original version
- `presentation_division.md` - Original coordination guide

**Data Files Ready:**
- GIF animations: `disp/figures/sequence_*.gif`
- All plots referenced in slides
- Code repository: github.com/ltpie123/final

---

## Final Checklist

**Both People:**
- [ ] Read your respective notes thoroughly
- [ ] Understand all mathematical content (both sections)
- [ ] Practice your section (time it!)
- [ ] Rehearse transition handoff
- [ ] Prepare for Q&A (divide by topic)

**Person 1 Specific:**
- [ ] Comfortable explaining B₄, wreath products, A₁₆
- [ ] Can walk through state space formula if asked
- [ ] Understand monoflip invariant (unique 4D property)
- [ ] Know cycle detection algorithm

**Person 2 Specific:**
- [ ] Memorize key numbers (46%, λ=6.09, period 10,080)
- [ ] Can interpret scatter plots and distributions
- [ ] Articulate why self-compositions are surprising
- [ ] Have GIF files ready to show

**Equipment:**
- [ ] Laptop with presentation.pdf
- [ ] HDMI adapter for projector
- [ ] Backup: USB drive with PDF
- [ ] Pointer (if available)
- [ ] Animations accessible (for Q&A)

---

## Summary of Enhancements

**Math content added**: 3 new slides + enhancements to 4 existing slides  
**New equations**: 10+ mathematical formulas and definitions  
**Depth increase**: Suitable for graduate-level Math 538 final presentation  
**Time impact**: +3 minutes total (19-21 min from 16-18 min)

**Recommended**: Request 25-minute time slot (if typically 20 min) to accommodate mathematical depth and Q&A

---

**This is rigorous, novel work. Present with confidence! The mathematical framework is sound, and the results are genuinely surprising. Good luck!**
