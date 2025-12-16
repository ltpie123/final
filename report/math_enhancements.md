# Mathematical Equations to Add to Presentation

Based on the mathematical framework documentation and hypercubing.xyz, here are suggested additions:

---

## Slide 3 Enhancement: "What is a 4D Rubik's Cube?"

### Add State Space Formula:

**Current**: "State space exponentially larger"

**Enhanced**: Add this equation box at the bottom:

```latex
\begin{block}{State Space Size}
$$|S_{4D}| = \frac{16!}{2} \cdot 12^{15} \cdot 4 \cdot 32! \cdot 6^{31} \cdot 3 \cdot \frac{24!}{2} \cdot 2^{23}$$
$$\approx 1.76 \times 10^{120} \text{ states}$$
\end{block}
```

**Comparison**:
- 3×3×3: $|S_{3D}| \approx 4.3 \times 10^{19}$
- 4D is $\sim 10^{100}$ times larger!

---

## New Slide After Slide 3: "Puzzle Structure & Symmetry"

```latex
\begin{frame}{Puzzle Structure \& Symmetry}
\begin{columns}
\column{0.5\textwidth}
\textbf{Piece Types (72 movable):}
\begin{itemize}
    \item \textbf{8 corners} (4-color, 1c pieces)
    \item \textbf{24 edges} (2-color, 2c pieces)
    \item \textbf{32 faces} (3-color, 3c pieces)
    \item \textbf{8 cells} (centers, fixed)
\end{itemize}

\vspace{1em}

\textbf{Orientations:}
\begin{itemize}
    \item 4c: 12 orientations each
    \item 3c: 6 orientations each
    \item 2c: 2 orientations each
\end{itemize}

\column{0.5\textwidth}
\textbf{Symmetry Group:}

The 4D tesseract has symmetry group $B_4$ (hyperoctahedral group):

$$|B_4| = 2^4 \cdot 4! = 384$$

\vspace{1em}

\textbf{Structure:} $S_2 \wr S_4$ (wreath product)

\vspace{1em}

\textbf{Coxeter notation:} $[4,3,3]$

\vspace{1em}

\textbf{Rotational subgroup:} Order 192
\end{columns}
\end{frame}
```

---

## Slide 5 Enhancement: "Discrete Dynamical System"

### Add Group-Theoretic Framework:

**After the current content, add**:

```latex
\vspace{1em}

\textbf{Group-Theoretic View:}

Let $G$ be the puzzle group. Each move $m_i \in G$ is a bijection:
$$m_i: S \to S, \quad m_i^{-1} \circ m_i = \text{id}$$

The move sequence generates a cyclic subgroup:
$$\langle T_M \rangle = \{T_M^0, T_M^1, T_M^2, \ldots, T_M^{p-1}\} \subseteq G$$

where $|\langle T_M \rangle| = p$ (the period).
```

---

## New Slide After Slide 5: "Permutation Theory"

```latex
\begin{frame}{Permutation Theory \& Constraints}
\textbf{State Representation:}

Each configuration is a permutation + orientation:
$$s = (\pi, o) \in S$$
where $\pi$ permutes pieces, $o$ specifies orientations.

\vspace{1em}

\textbf{Parity Constraints:}
\begin{enumerate}
    \item \textbf{Corner parity}: 4c pieces must form \textit{even} permutations
    $$\pi_{4c} \in A_{16} \subset S_{16}$$
    
    \item \textbf{Edge-Face parity}: Linked permutation parity
    $$\text{sgn}(\pi_{2c}) = \text{sgn}(\pi_{3c})$$
    
    \item \textbf{Orientation sums}:
    $$\sum_{i=1}^{31} o_{3c,i} \equiv 0 \pmod{3}, \quad \sum_{i=1}^{23} o_{2c,i} \equiv 0 \pmod{2}$$
\end{enumerate}

\vspace{0.5em}

\textbf{Monoflip Invariant (unique to 4D):}
A single 4c piece can be "flipped" with all others solved. Related to $A_4$ orientation group and Klein four-group $\mathbb{Z}_2 \times \mathbb{Z}_2$.
\end{frame}
```

---

## Slide 6 Enhancement: "Lyapunov Exponents"

### Add Discrete Lyapunov Definition:

**After the perturbation description, add**:

```latex
\vspace{1em}

\textbf{Formal Definition (Discrete Lyapunov):}

For continuous systems, Lyapunov exponent measures trajectory divergence:
$$\lambda = \lim_{t \to \infty} \frac{1}{t} \ln \frac{||\delta(t)||}{||\delta(0)||}$$

\vspace{0.5em}

For our discrete finite system, we adapt this using period ratios:
$$\lambda_{\text{discrete}} = \mathbb{E}\left[\ln\left|\frac{p'}{p}\right|\right] = \frac{1}{N} \sum_{i=1}^{N} \ln\left|\frac{p'_i}{p}\right|$$

where $p$ = base period, $p'_i$ = perturbed period.
```

---

## New Slide After Slide 6: "Chaos in Finite Systems"

```latex
\begin{frame}{Chaos in Finite Systems}
\textbf{Challenge:} Classical chaos requires:
\begin{itemize}
    \item Sensitive dependence on initial conditions
    \item Topological mixing
    \item Dense periodic orbits
\end{itemize}

\vspace{1em}

\textbf{Problem:} Our system is finite ($|S| < \infty$), so all trajectories are periodic!

\vspace{1em}

\textbf{Solution:} Adapt chaos metrics to \textit{sequence space} rather than state space:
\begin{enumerate}
    \item Perturb the \textbf{move sequence} $M \to M'$ (not initial state)
    \item Measure change in \textbf{orbit structure} ($p \to p'$)
    \item Compute Lyapunov on period ratios
\end{enumerate}

\vspace{1em}

\begin{block}{Key Insight}
Chaos manifests as \textbf{sensitivity of dynamical properties} (period, orbit structure) to small sequence perturbations, not trajectory divergence in state space.
\end{block}
\end{frame}
```

---

## Slide 7 Enhancement: "Computational Approach"

### Add Cycle Detection Algorithm:

**After "Used SHA256 hashing...", add**:

```latex
\vspace{1em}

\textbf{Cycle Detection Algorithm:}

\begin{algorithmic}[1]
\STATE Initialize: $s \gets s_0$ (solved), $\text{visited} \gets \{h(s_0): 0\}$
\FOR{$n = 1, 2, 3, \ldots, N_{\max}$}
    \STATE $s \gets T_M(s)$ \COMMENT{Apply move sequence}
    \STATE $h \gets \text{SHA256}(s)$ \COMMENT{Hash state}
    \IF{$h \in \text{visited}$}
        \STATE \textbf{return} $n - \text{visited}[h]$ \COMMENT{Period found}
    \ENDIF
    \STATE $\text{visited}[h] \gets n$
\ENDFOR
\STATE \textbf{return} \texttt{NO\_CYCLE} \COMMENT{Exceeded max iterations}
\end{algorithmic}

\textbf{Complexity:} $O(p \cdot (T_M + H))$ where $p$ = period, $T_M$ = move time, $H$ = hash time
```

---

## Alternative: Condensed Math Reference Slide

If you don't want to add multiple slides, create one comprehensive "Mathematical Background" slide:

```latex
\begin{frame}{Mathematical Background}
\footnotesize

\textbf{State Space:}
$$|S| = \frac{16!}{2} \cdot 12^{15} \cdot 4 \cdot 32! \cdot 6^{31} \cdot 3 \cdot \frac{24!}{2} \cdot 2^{23} \approx 1.76 \times 10^{120}$$

\textbf{Puzzle Group $G$:}
\begin{itemize}
    \item Generated by basic moves $\{m_1, \ldots, m_k\}$
    \item Symmetry: Hyperoctahedral group $B_4$, $|B_4| = 384$
    \item Each $m_i: S \to S$ is a bijection (permutation)
\end{itemize}

\textbf{Dynamical System:}
$$T_M(s) = m_k \circ \cdots \circ m_1(s), \quad T_M^p(s_0) = s_0$$

\textbf{Lyapunov Exponent (Discrete):}
$$\lambda = \frac{1}{N} \sum_{i=1}^{N} \ln\left|\frac{p'_i}{p}\right|, \quad p' = \text{period of perturbed sequence}$$

\textbf{Parity Constraints:}
\begin{itemize}
    \item Corners: $\pi_{4c} \in A_{16}$ (even permutations)
    \item Edge-Face: $\text{sgn}(\pi_{2c}) = \text{sgn}(\pi_{3c})$
    \item Orientations: $\sum o_{3c} \equiv 0 \pmod{3}$, $\sum o_{2c} \equiv 0 \pmod{2}$
\end{itemize}
\end{frame}
```

---

## Recommended Approach

**Option A (More Math-Heavy):**
- Add 3 new slides:
  1. "Puzzle Structure & Symmetry" (after slide 3)
  2. "Permutation Theory & Constraints" (after slide 5)
  3. "Chaos in Finite Systems" (after slide 6)
- Enhance existing slides 5, 6, 7 with equations
- **Total slides**: 20 (from 17)
- **Presentation time**: +3-4 minutes (need to trim elsewhere or extend)

**Option B (Moderate):**
- Add 1 comprehensive "Mathematical Background" slide (after slide 5)
- Enhance slides 3, 5, 6 with key equations
- **Total slides**: 18 (from 17)
- **Presentation time**: +1-2 minutes

**Option C (Minimal):**
- Just enhance existing slides with equations:
  - Slide 3: Add state space formula
  - Slide 5: Add group structure
  - Slide 6: Add formal Lyapunov definition
- **Total slides**: 17 (unchanged)
- **Presentation time**: +30 seconds (minimal)

---

## My Recommendation

Go with **Option B** - it adds substantial mathematical rigor without overwhelming the results section. The comprehensive "Mathematical Background" slide can be Person 1's finale before handoff, showcasing the theoretical depth.

Would you like me to implement one of these options into the presentation.tex file?
