# Presentation Division: Two-Person Team (STREAMLINED VERSION)

## Overview

**Total Slides**: 18 (down from 20 math-heavy, 17 original)  
**Total Time**: 17-19 minutes  
**Slide Deck**: `/home/hi/School/math538/final/report/presentation.pdf` (518 KB)  
**Course**: Math 538 - Discrete Dynamical Systems & Chaos Theory  
**Version**: Streamlined (math-heavy with minimal group theory)

---

## What Changed from Math-Heavy Version

**Removed**:
- ❌ "Puzzle Structure & Symmetry" slide (B₄, wreath products, Coxeter notation)
- ❌ "Permutation Theory & Constraints" slide (A₁₆, parity, monoflip)
- ❌ Group-theoretic subsection in "Discrete Dynamical System" slide

**Kept**:
- ✅ State space formula (concrete and impressive: 1.76 × 10^120)
- ✅ Discrete Lyapunov formal definition (core chaos theory)
- ✅ "Chaos in Finite Systems" slide (important theoretical justification)
- ✅ Cycle detection algorithm (computational rigor)
- ✅ All results slides (unchanged)

**Focus**: Dynamical systems and chaos theory over abstract algebra

---

## Person 1: Introduction & Dynamical Systems Framework

**Slides**: 1-8  
**Duration**: ~8-9 minutes  
**Notes**: `presentation_notes_person1_streamlined.md`

### Slide Breakdown:
1. **Title Slide** - Introduction
2. **Overview** - Roadmap
3. **What is a 4D Rubik's Cube?** - Setup + state space formula (1.76 × 10^120)
4. **Research Question** - Key concepts (orbit, chaos, discrete dynamics)
5. **Discrete Dynamical System** - Framework (T_M, trajectories, period)
6. **Lyapunov Exponents** - Chaos metric + discrete adaptation
7. **Chaos in Finite Systems** - Theoretical justification (sequence space)
8. **Computational Approach** - Methods + cycle detection algorithm

### Key Mathematical Content:
- **State space formula**: |S| ≈ 1.76 × 10^120
- **Dynamical system**: T_M: S → S, periodic orbits
- **Discrete Lyapunov**: λ = E[ln|p'/p|] adapted from continuous
- **Finite-system chaos**: Sensitivity in sequence space, not state space
- **Cycle detection algorithm**: O(p·T_M) with pseudocode

### Focus:
- Discrete-time dynamical systems
- Adaptation of chaos theory to finite systems
- Computational methodology
- Theoretical rigor without heavy algebra

---

## Person 2: Results & Conclusions

**Slides**: 9-18  
**Duration**: ~9-10 minutes  
**Notes**: `presentation_notes_person2_streamlined.md`

### Slide Breakdown:
9. **Key Findings** - Main results, self-compositions
10. **Period vs Chaos** - Scatter plot, no correlation
11. **Classification Distribution** - 46% chaotic
12. **Top Chaotic Sequences** - Self-compositions dominate
13. **Lyapunov vs Sequence Length** - Length 2 sweet spot
14. **Sequence Animations** - Visual demonstrations
15. **Key Takeaways** - Four main insights
16. **Future Directions** - Open questions, applications
17. **References** - Citations
18. **Thank You / Questions** - Closing

### Key Results:
- **Self-compositions (FR→FR, FO→FO)** most chaotic
- **Period ≠ complexity**: Main counterintuitive finding
- **46% chaotic**: High proportion validates framework
- **Length 2 sweet spot**: Highest chaos at 2-move sequences

---

## Division Rationale

### Person 1 (Theory):
- Establishes dynamical systems framework
- Explains discrete chaos adaptation
- Focuses on methodology and theory
- **8 slides, ~8-9 minutes**
- Minimal group theory, maximum chaos theory

### Person 2 (Results):
- Delivers empirical findings
- Emphasizes surprising discoveries (self-compositions)
- Visual data interpretation
- **10 slides, ~9-10 minutes**
- More engaging, data-driven

### Natural Transition:
**Person 1 ends (Slide 8):**
> "With this framework and methodology established, let's see what we discovered. [Person 2's name]?"

**Person 2 begins (Slide 9):**
> "Thanks, [Person 1's name]. So with that framework, let's look at what we discovered."

---

## Mathematical Content Summary

### What's Included (Math Focus):

**Slide 3 - State Space Formula:**
$$|S| = \frac{16!}{2} \cdot 12^{15} \cdot 4 \cdot 32! \cdot 6^{31} \cdot 3 \cdot \frac{24!}{2} \cdot 2^{23} \approx 1.76 \times 10^{120}$$

**Slide 5 - Dynamical System:**
- Composite map: $T_M(s) = m_k \circ \cdots \circ m_1(s)$
- Trajectory: $s_0 \xrightarrow{T_M} s_1 \xrightarrow{T_M} s_2 \xrightarrow{T_M} \cdots$
- Period: $T_M^p(s_0) = s_0$
- Key property: Finite $|S|$ → eventually periodic

**Slide 6 - Discrete Lyapunov:**
- Continuous: $\lambda = \lim_{t \to \infty} \frac{1}{t} \ln \frac{||\delta(t)||}{||\delta(0)||}$
- Discrete adaptation: $\lambda_{\text{discrete}} = \mathbb{E}[\ln|p'/p|]$
- Classification: <0.1 (regular), 0.1-0.69 (sensitive), ≥0.69 (chaotic)

**Slide 7 - Finite-System Chaos:**
- Challenge: Classical chaos needs infinite/continuous spaces
- Solution: Measure sensitivity in sequence space
- Key insight: Sensitivity of dynamical properties to perturbations

**Slide 8 - Algorithm:**
- Cycle detection pseudocode
- Complexity: O(p·T_M) time, O(p) space
- SHA256 hashing for state comparison

### What's Excluded (Group Theory):
- ❌ Hyperoctahedral group B₄
- ❌ Wreath products S₂ ≀ S₄
- ❌ Alternating group A₁₆
- ❌ Parity constraints
- ❌ Monoflip invariant
- ❌ Cyclic subgroups ⟨T_M⟩

---

## Coordination Strategy

### Before Presentation:
1. **Practice together** - Full run-through twice
2. **Time yourselves** - Person 1: 8 min, Person 2: 9 min
3. **Sync on math** - Both understand all equations
4. **Divide Q&A**:
   - Person 1: Framework, Lyapunov, algorithm, finite chaos
   - Person 2: Results, self-compositions, comparisons
   - Either: Implementation, why 4D

### During Presentation:
- **Support each other** - Engage, nod during partner's section
- **Backup**: Help if partner struggles
- **Q&A strategy**: Theory→P1, Data→P2, discuss together when appropriate

### Mathematical Depth:
- **For Math 538**: Emphasize chaos theory adaptation
- **Don't avoid equations** - audience expects rigor
- **Connect to course**: Devaney, discrete systems, Lyapunov
- **Emphasize novelty**: Sequence-space framework

---

## Time Management

### If Running Long:
- **Person 1**: Shorten Slide 7 (Chaos in Finite Systems) to 1.5 min
- **Person 2**: Skip Slide 14 (Animations) or 30 sec only
- **Person 2**: Condense Slide 16 (Future) to 1 min

### If Running Short:
- **Person 1**: Expand on why finite systems are challenging
- **Person 2**: Show animations during main talk
- **Both**: Invite questions during presentation

### Ideal Timing:
- Person 1: 8 minutes
- Person 2: 9 minutes
- Total: 17 minutes
- Q&A: 3 min (20-min slot) or 8 min (25-min slot)

---

## Q&A Preparation

### Person 1 Should Handle:
- Lyapunov formal definition
- Why sequence space not state space?
- Algorithm and SHA256 hashing
- Finite-system chaos justification
- Computational complexity

### Person 2 Should Handle:
- Results interpretation
- Self-composition phenomenon
- Chaos classification thresholds
- 3D vs 4D comparison
- Why 46% is high

### Both Should Know:
- All mathematical content (support each other)
- Why 4D is interesting
- Course connections (Devaney, discrete dynamics)
- Validation approach

### Quick Answers:
- **State space size?** "Accounts for all piece permutations and orientations"
- **SHA256 collisions?** "Negligible probability, tested millions of states"
- **Really chaos?** "Yes—deterministic sensitivity, not random variance"
- **Why sequence space?** "State space all periodic; complexity is in parameter space"

---

## Comparison of Versions

| Aspect | Original | Math-Heavy | Streamlined |
|--------|----------|------------|-------------|
| Slides | 17 | 20 | 18 |
| Duration | 16-18 min | 19-21 min | 17-19 min |
| Group Theory | Minimal | Heavy | Minimal |
| Chaos Theory | Good | Excellent | Excellent |
| Formulas | ~5 | ~15 | ~10 |
| Abstract Algebra | Light | B₄, A₁₆, wreath | None |
| Dynamical Systems | Good | Excellent | Excellent |
| **Best For** | General | Pure math | Math 538 |

---

## Files Created

### This Version (Streamlined):
1. **presentation.pdf** (518 KB) - 18-slide deck
2. **presentation_notes_person1_streamlined.md** - Person 1 notes
3. **presentation_notes_person2_streamlined.md** - Person 2 notes
4. **presentation_division_streamlined.md** - This coordination guide

### Also Available (Other Versions):
- Original: presentation_notes_person1.md, presentation_notes_person2.md
- Math-Heavy: presentation_notes_person1_mathheavy.md, presentation_notes_person2_mathheavy.md

---

## Final Checklist

**Both People:**
- [ ] Read respective streamlined notes
- [ ] Understand all equations (both sections)
- [ ] Practice your section (time it!)
- [ ] Rehearse transition
- [ ] Prepare Q&A strategy

**Person 1 Specific:**
- [ ] Comfortable with discrete Lyapunov definition
- [ ] Can explain finite-system chaos adaptation
- [ ] Understand cycle detection algorithm
- [ ] Know state space formula components

**Person 2 Specific:**
- [ ] Memorize: 46%, λ=6.09, period 10,080
- [ ] Interpret scatter plots confidently
- [ ] Articulate self-composition surprise
- [ ] Have GIF files ready

**Equipment:**
- [ ] Laptop with PDF
- [ ] HDMI adapter
- [ ] Backup USB
- [ ] Pointer (optional)
- [ ] Animations accessible

---

## Summary

**Version**: Streamlined math-heavy (chaos theory focus, minimal group theory)  
**Slides**: 18 (removed 2 algebra slides from 20)  
**Time**: 17-19 minutes  
**Best For**: Math 538 audience wanting rigor without heavy abstract algebra  

**Key Advantages**:
- ✅ Strong chaos theory foundation
- ✅ Formal discrete Lyapunov definition
- ✅ Theoretical justification (finite systems)
- ✅ Computational rigor (algorithm with complexity)
- ✅ No distracting group theory
- ✅ Faster pacing (fits 20-min slot comfortably)

**Mathematical Depth**: Graduate-level dynamical systems without advanced algebra

**Status**: ✅ Ready for Math 538 presentation

---

**This is rigorous work with surprising results. Present with confidence!**
