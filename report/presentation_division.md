# Presentation Division: Two-Person Team

## Overview

**Total Time**: 16-18 minutes (leaves 2-4 min for Q&A in 20-min slot)  
**Slide Deck**: `/home/hi/School/math538/final/report/presentation.pdf`

---

## Person 1: Introduction & Mathematical Framework

**Slides**: 1-7  
**Duration**: ~8-9 minutes  
**Notes**: `presentation_notes_person1.md`

### Responsibilities:
1. **Title & Overview** (Slides 1-2) - Introduce project, give roadmap
2. **What is a 4D Rubik's Cube?** (Slide 3) - Explain 4D hypercube, move notation
3. **Research Question** (Slide 4) - Define orbit, period, chaos, discrete dynamics
4. **Discrete Dynamical System** (Slide 5) - Formal math framework, state space, map T_M
5. **Lyapunov Exponents** (Slide 6) - Chaos metric, perturbation approach, classification
6. **Computational Approach** (Slide 7) - Tool stack, systematic testing, methods
7. **Handoff to Person 2** - Smooth transition to results

### Key Concepts to Explain:
- 4D hypercube has 8 cells (3D "faces")
- Two-letter move notation (FR, UO, etc.)
- State space S, composite map T_M, period p
- Lyapunov λ: measure chaos via perturbations
- Classification: Regular (<0.1), Sensitive (0.1-0.69), Chaotic (≥0.69)

### Strengths Needed:
- Comfort with mathematical notation
- Ability to explain abstract concepts clearly
- Setting up the framework that Person 2 will validate

---

## Person 2: Results & Conclusions

**Slides**: 8-17  
**Duration**: ~8-9 minutes  
**Notes**: `presentation_notes_person2.md`

### Responsibilities:
1. **Key Findings** (Slide 8) - Present main results, self-compositions, surprise findings
2. **Period vs Chaos** (Slide 9) - Analyze scatter plot, explain counterintuitive relationship
3. **Classification Distribution** (Slide 10) - Pie chart, 46% chaotic
4. **Top Chaotic Sequences** (Slide 11) - Bar chart, emphasize self-compositions
5. **Lyapunov vs Sequence Length** (Slide 12) - Sweet spot at length 2
6. **Sequence Animations** (Slide 13) - Describe visualizations
7. **Key Takeaways** (Slide 14) - Summarize 4 main insights
8. **Future Directions** (Slide 15) - Open questions, applications
9. **References** (Slide 16) - Acknowledge sources
10. **Thank You / Questions** (Slide 17) - Closing, handle Q&A

### Key Messages:
- Self-compositions (FR→FR, FO→FO) are most chaotic despite short periods
- Period ≠ complexity (main counterintuitive finding)
- 46% of sequences are chaotic (surprisingly high)
- Two-move sequences show highest chaos

### Strengths Needed:
- Enthusiasm about surprising results
- Comfort interpreting graphs and data
- Strong closing and Q&A handling

---

## Division Rationale

### Person 1 (Theory-Heavy):
- Sets mathematical foundation
- Explains framework that makes results meaningful
- More abstract, formula-focused
- Builds anticipation for results

### Person 2 (Results-Heavy):
- Delivers the "payoff" of the project
- More visual (plots, charts)
- Emphasizes surprising/counterintuitive findings
- Stronger closing position

### Natural Transition Point:
After Slide 7 (Computational Approach), Person 1 says:
> "So we've established the mathematical framework and our systematic testing approach. Now let's see what we discovered. [Person 2's name]?"

Person 2 picks up:
> "Thanks, [Person 1's name]. So with that framework established, let's look at what we discovered."

---

## Coordination Tips

### Before Presentation:
1. **Practice together** - Run through full presentation at least once
2. **Time yourselves** - Each should aim for 8 minutes (gives 1-min buffer)
3. **Sync on transition** - Make handoff smooth and natural
4. **Divide Q&A** - Person 1 handles theory questions, Person 2 handles results/interpretation

### During Presentation:
- **Support each other** - Nod, show engagement during partner's section
- **Backup** - If partner forgets something, gently prompt
- **Q&A strategy**: 
  - Theory questions → Person 1
  - Results/data questions → Person 2
  - Implementation → Either (both know this)

### Slide Advancement:
- **Option A**: Person 1 controls slides for both (smoother)
- **Option B**: Each person advances their own slides (requires handoff)
- **Recommended**: Option A with clear signal when Person 2 wants next slide

---

## Quick Reference

### Person 1's Key Numbers:
- 8 cells in 4D hypercube
- 64 two-move combinations tested
- λ thresholds: 0.1 (regular), 0.69 (chaotic)
- Example: R,U on 3D = period 840

### Person 2's Key Numbers:
- **46%** chaotic sequences
- **FO→FO**: λ = 6.09, period 4 (most chaotic)
- **FR→UF**: period 10,080, λ = 3.95 (longest period)
- **50** sequences with Lyapunov analysis

---

## Emergency Scenarios

### If Person 1 Runs Over:
- Skip or shorten Slide 7 (Methods) to 1 minute
- Give Person 2 signal to accelerate

### If Person 2 Runs Over:
- Condense Slide 13 (Animations) to 30 sec
- Shorten Slide 15 (Future Directions) to 1 min
- Skip detailed References walkthrough

### If Either Person Gets Stuck:
- Partner can jump in: "Let me add to that..."
- Refer back to slide: "As shown here..."
- Move forward: "We can discuss details in Q&A"

---

## Files Created

1. **presentation_notes_person1.md** - Person 1's detailed notes (Slides 1-7)
2. **presentation_notes_person2.md** - Person 2's detailed notes (Slides 8-17)
3. **presentation_division.md** - This overview document
4. **presentation.pdf** - Compiled slide deck with references

---

## Final Checklist

**Both People**:
- [ ] Read your respective notes thoroughly
- [ ] Practice your section (aim for 8 minutes)
- [ ] Memorize key numbers
- [ ] Understand partner's section (for Q&A support)

**Person 1**:
- [ ] Practice transition handoff to Person 2
- [ ] Review mathematical formulas on slides 5-6
- [ ] Prepare to answer theory questions

**Person 2**:
- [ ] Have GIF files ready: `disp/figures/sequence_FO_FO.gif`
- [ ] Practice interpreting graphs
- [ ] Prepare closing and Q&A handling

**Equipment**:
- [ ] Laptop with HDMI adapter
- [ ] Backup: Presentation PDF on USB drive
- [ ] Pointer (if available)

---

**Good luck to both of you! This is strong work—present with confidence!**
