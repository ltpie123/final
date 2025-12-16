# Presentation Notes: Person 2 (Results & Conclusions)

**Your Slides**: 8-17 (Key Findings → Thank You)  
**Duration**: ~8-9 minutes  
**Role**: Present results, visualizations, discuss implications and future work

---

## Slide 8: Key Findings

**Opening** (pick up from Person 1):
- "Thanks, [Person 1's name]. So with that framework established, let's look at what we discovered."

**Talking Points**:
- We tested dozens of sequences systematically, and the results are fascinating

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

**KEY COUNTERINTUITIVE FINDING**: "Short periods do NOT imply simple behavior! The most chaotic sequences have the shortest orbits."

**Timing**: 2.5 minutes

---

## Slide 9: Period vs Chaos

**Talking Points**:
- This plot really drives home that surprising relationship
- **X-axis**: Period (log scale—notice it ranges from 4 to over 10,000)
- **Y-axis**: Lyapunov exponent (chaos measure)
- **Colors**: Blue = regular, orange = sensitive, red = chaotic

**Point to specific features**:
1. **Left side of plot**: Short periods (4-10) include the MOST chaotic sequences (top red points)
2. **Right side**: Long periods don't guarantee high chaos—many are only moderately sensitive
3. **No clear correlation**: Period and chaos are nearly independent

**Why this matters**: 
- "Classical intuition says complex should mean long orbits"
- "Reality: Geometric structure of the move matters more than orbit length"
- "Self-compositions create rapid scrambling despite returning quickly"

**Timing**: 1.5 minutes

---

## Slide 10: Classification Distribution

**Talking Points**:
- We analyzed 50 sequences total and classified each by Lyapunov exponent

**Point to the pie chart**:
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
- This bar chart ranks the top 10 most chaotic sequences by Lyapunov exponent

**Walk through the chart**:
1. **Self-compositions dominate**: FO→FO, FR→FR, FL→FL all in top 5
2. **Four-move patterns**: OF→OU→OB→OD and FR→OR→FL→OL show extreme chaos
3. **Classic pairs**: FR→UF appears but is outranked by self-compositions

**Open question**: 
- "Why are self-compositions so chaotic?"
- "Our hypothesis: Repeating the same rotation might create resonance-like effects"
- "The second application interferes with the partially scrambled state from the first"
- "This is still an open theoretical question—no formal proof yet"

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
- "Two-move sequences hit a 'sweet spot' for chaos"
- "Long enough to create complexity"
- "Short enough that self-compositions are possible"
- "Longer sequences tend to average out chaos—they explore more of the state space uniformly"

**Counterintuitive**: "More moves does NOT equal more chaos"

**Timing**: 1.5 minutes

---

## Slide 13: Sequence Animations

**Talking Points**:
- We also created animated GIFs showing actual puzzle states during these sequences
- "I can show these during Q&A if there's interest"

**Available animations**:
1. **FR (single)**: Baseline—simple rotation, period 8, no chaos
2. **FO→FO**: The most chaotic—pieces scatter rapidly despite returning in just 4 iterations
3. **FR→FR**: Second most chaotic—similar rapid scrambling

**Visual insight**:
- "Even though these return to solved quickly, intermediate states are highly scrambled"
- "Perturbations produce radically different intermediate patterns"
- "This is what chaos looks like in discrete systems—not continuous divergence, but combinatorial explosion"

**Timing**: 1 minute

---

## Slide 14: Key Takeaways

**Talking Points** (walk through each deliberately):

**1. Rich dynamics**:
- "4D hypercubes are not simple extensions of 3D cubes"
- 46% chaotic is surprisingly high
- Period range (4 to 10,080) shows incredible diversity

**2. Self-compositions are extreme**:
- "This is our most surprising finding"
- Repeating a single move is not redundant—it creates maximal chaos
- Highest λ > 5, approaching theoretical limits

**3. Period ≠ complexity**:
- "This challenges our intuition about dynamical systems"
- Short orbits can be highly chaotic
- Long periods don't guarantee interesting behavior
- "It's about the geometry of how moves interact, not just how many states you visit"

**4. Discrete chaos is real**:
- "We successfully adapted continuous chaos theory to finite systems"
- Lyapunov exponents work in discrete settings
- Small perturbations → massive behavioral shifts
- "This validates discrete dynamical systems as a lens for studying complexity"

**Timing**: 2 minutes

---

## Slide 15: Future Directions

**Talking Points**:

**Theoretical questions** (point to each):
- "The self-composition phenomenon needs mathematical explanation"
  - Is there a group-theoretic reason? 
  - Connection to conjugacy classes or commutator structure?
- "Can we predict chaos from move properties alone?"

**Computational extensions**:
- "5D or 6D hypercubes—if computationally feasible"
  - Our tools can handle it, but periods might be very long
- "Longer sequences (5-10 moves)"
  - See if chaos persists or averages out
- "Different perturbation strategies"

**Applications** (speculative but interesting):
- "Cryptographic pseudo-random number generators based on chaotic sequences?"
  - High Lyapunov means good mixing
- "Physical systems with discrete symmetries"
  - Crystallography, quantum systems
  - Puzzles as toy models

**Timing**: 1.5 minutes

---

## Slide 16: References

**Talking Points**:
- "Our work builds on several foundational texts and tools"
- **Briefly highlight**:
  - Devaney and Strogatz for chaos theory framework
  - Joyner for group theory of puzzles
  - Hyperspeedcube (Andrew Farkas) made the 4D simulation possible
- "Full references are on the slide and in our written report"

**Timing**: 30 seconds

---

## Slide 17: Thank You / Questions

**Closing**:
- "Thank you for your attention!"
- "We're happy to answer questions about the mathematics, implementation, or findings"
- "Code is available on GitHub if you want to explore further"

**Timing**: 30 seconds + Q&A

---

## Anticipated Questions (During Your Section)

**Q: Can you show a GIF?**
- A: "Absolutely! Let me pull up FO→FO..." [Have `disp/figures/sequence_FO_FO.gif` ready]

**Q: What about 3D vs 4D comparison?**
- A: "Great question! 4D has higher chaos rates. FR→UF on 4D has period 10,080, while R→U on 3D has period 840. The 4D version also has a higher Lyapunov exponent—extra dimension creates more complex interactions."

**Q: Could this be used for scrambling?**
- A: "Yes! FO→FO scrambles efficiently despite short period. Though for serious scrambling, you'd want longer sequences to explore more of the state space."

**Q: What's the theoretical maximum Lyapunov?**
- A: "For our perturbation scheme, roughly ln(period). Self-compositions achieve near-maximum values—they're close to maximally chaotic for their period length."

**Q: Why focus on two-move sequences?**
- A: "Computational tractability—64 combinations is exhaustive. Also, two moves showed the highest chaos. We tested some longer sequences, but they didn't exceed the two-move chaos peaks."

**Q: How do you know SHA256 doesn't have collisions?**
- A: "We tested across millions of states—no collisions found. SHA256's 256-bit output space is astronomically larger than our puzzle state space, so collision probability is negligible."

---

## Q&A Strategy

**If you don't know**:
- "That's a great question—[Person 1's name], do you want to take that?" (if it's theory)
- "We didn't explore that in this project, but it's an excellent direction for future work"
- "Let me think... [pause, think, respond]"

**If technical detail needed**:
- Refer to specific slides: "As shown on the Period vs Chaos plot..."
- Cite numbers: "46% chaotic, λ_max = 6.09"

**Keep answers concise**:
- 30-60 seconds per answer
- If complex, offer to discuss after presentation

---

## Quick Reference Card

**Key numbers**:
- **46%** of sequences are chaotic
- **FO→FO** most chaotic (λ = 6.09, period 4)
- **FR→UF** longest period (10,080) with high chaos (λ = 3.95)
- **50** sequences analyzed with Lyapunov
- Classification: Regular < 0.1, Sensitive 0.1-0.69, Chaotic ≥ 0.69

**Key messages**:
1. Self-compositions are surprisingly chaotic
2. Period ≠ complexity
3. 4D exhibits rich chaos (46%)
4. Discrete Lyapunov exponents work!

**Files to have ready**:
- GIFs in `disp/figures/`: sequence_FO_FO.gif, sequence_FR_FR.gif
- Code link: github.com/ltpie123/final

---

## Presentation Tips

**Energy level**:
- Match excitement to the surprising results
- Emphasize "counterintuitive" findings
- Show enthusiasm about the self-composition discovery

**Pacing**:
- Don't rush the Key Findings slide (your most important one)
- Pause after stating surprising results to let them sink in
- Point to specific data on graphs

**Body language**:
- Gesture toward high points on bar chart
- Trace the scatter plot pattern with your hand
- Make eye contact when stating key takeaways

**If running long**:
- Shorten Slide 13 (Animations) to 30 seconds
- Condense Future Directions to 1 minute
- Skip detailed explanation of References slide

**If running short**:
- Expand on self-composition phenomenon
- Discuss specific examples in more detail
- Offer to show animations during main presentation

---

## Closing Thought (Optional, if time permits)

"This project shows that even completely deterministic finite systems—like a 4D Rubik's cube—can exhibit complex, chaotic behavior. The fact that repeating a single move creates more chaos than complex combinations reminds us that chaos isn't just about randomness or size. It's about how simple rules interact in unexpected ways."

---

**Total Time for Person 2**: ~8-9 minutes (+ Q&A)

**Combined presentation**: 16-18 minutes → Leaves 2-4 minutes for questions in a 20-minute slot

**Good luck! Your results are impressive—present with confidence!**
