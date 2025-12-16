# Discrete Dynamical Systems on Hyperdimensional Rubik's Cubes

**Math 538 Final Project - Chaos Theory & N-Dimensional Puzzles**

## Project Overview

This project explores discrete dynamical systems on N-dimensional Rubik's cubes by analyzing trajectories of move sequences. We investigate how periodic behavior scales across dimensions (3D vs 4D) and which move combinations exhibit complex vs. simple dynamics.

### Key Findings

1. **Move geometry matters more than dimension** - Some 4D sequences are simpler than 3D
2. **FR,UO on 4D has same period (840) as R,U on 3D** - Equal complexity achieved
3. **O-axis moves form small subgroup** - Period ≤ 6 regardless of puzzle size
4. **Demonstrates concepts**: Orbit analysis, period detection, group structure, finite dynamical systems

## Repository Structure

```
.
├── ctrl/                   # Main Rust trajectory analysis tool
│   ├── src/
│   │   ├── main.rs        # CLI interface
│   │   ├── orbit.rs       # Trajectory exploration & cycle detection
│   │   └── moves.rs       # Move notation parser
│   ├── README.md          # Detailed usage documentation
│   └── RESULTS_SUMMARY.md # Comprehensive experimental results
│
├── docs/                   # Mathematical documentation
│   └── mathematical_framework.md  # Formal theory & algorithms
│
├── hyper/                  # Hyperspeedcube submodule (puzzle engine)
│   └── Hyperspeedcube/    # HactarCE's 4D puzzle library
│
├── TODO.md                 # Project planning & implementation notes
└── LICENSE                 # MIT License with educational notice
```

## Quick Start

### Prerequisites

- Rust 1.70+ ([install from rustup.rs](https://rustup.rs/))
- Git with submodule support

### Installation

```bash
# Clone with submodules
git clone --recurse-submodules <repo-url>
cd math538/final

# Build the tool
cd ctrl
cargo build --release
```

### Run Analysis

```bash
# 3D Rubik's Cube with R,U moves
cargo run --release -- --puzzle ft_cube:3 --moves R,U --max-iterations 1000

# 4D Hypercube with FR,UO moves (complex behavior)
cargo run --release -- --puzzle ft_hypercube:3 --moves FR,UO --max-iterations 1000

# Export results to JSON
cargo run --release -- --puzzle ft_cube:3 --moves R,U --output results.json
```

## Results Summary

| Puzzle | Dimension | Moves | Period | Complexity |
|--------|-----------|-------|--------|------------|
| 2×2×2 | 3D | R,U | 30 | Simple |
| 3×3×3 | 3D | R,U | 840 | Complex |
| 2×2×2×2 | 4D | OF,OU | 6 | Very Simple |
| 3×3×3×3 | 4D | OF,OU | 6 | Very Simple |
| 3×3×3×3 | 4D | FR,UO | **840** | **Complex** |

**Key Insight**: The 3×3×3×3 with FR,UO achieves the same complexity as the 3×3×3 with R,U, demonstrating that 4D puzzles can exhibit equally complex behavior with proper move selection.

## Documentation

### For Users
- **[ctrl/README.md](ctrl/README.md)**: Detailed tool usage, command-line options, examples
- **[ctrl/RESULTS_SUMMARY.md](ctrl/RESULTS_SUMMARY.md)**: Complete experimental results and analysis

### For Mathematicians
- **[docs/mathematical_framework.md](docs/mathematical_framework.md)**: Formal definitions, theorems, algorithms
  - Discrete dynamical systems on finite groups
  - Trajectory analysis and cycle detection
  - State space hashing via piece transforms
  - Connections to classical chaos theory

### For Developers
- **[TODO.md](TODO.md)**: Project planning, implementation notes, architecture decisions
- **Source Code**: Well-commented Rust implementation in `ctrl/src/`

## Mathematical Framework

Given a puzzle state space $S$ and move sequence $M = (m_1, m_2, \ldots, m_k)$, we define:

$$T_M: S \to S, \quad T_M(s) = m_k \circ \cdots \circ m_1(s)$$

The trajectory starting from $s_0$ (solved state) is:

$$s_0, s_1 = T_M(s_0), s_2 = T_M(s_1), \ldots$$

We detect when $s_n = s_0$, finding:
- **Period** $p$: length of cycle
- **Transient** $\tau$: iterations before cycle (always 0 for solved start)
- **Orbit size**: total unique states visited

## Key Contributions

### 1. Cross-Dimensional Analysis
First systematic comparison of trajectory complexity between 3D and 4D Rubik's cubes.

### 2. Move Geometry Discovery
Identified that O-axis moves form a small subgroup with period ≤ 6, independent of puzzle size.

### 3. State Hashing Algorithm
Developed robust state comparison via SHA256 hashing of piece transforms, enabling efficient cycle detection.

### 4. Educational Tool
Created accessible Rust CLI for exploring discrete dynamical systems on hyperdimensional puzzles.

## Future Work

1. **Find maximum period** on 3×3×3×3 by testing all move pairs
2. **Analyze commutators** $[A,B] = ABA'B'$ for complex behavior
3. **Test non-solved initial states** to find non-zero transients
4. **Compute God's number** for specific move sets
5. **Extend to 5D+** hypercubes

## References

- **Hyperspeedcube**: [HactarCE/Hyperspeedcube](https://github.com/HactarCE/Hyperspeedcube) - 4D puzzle simulator
- **Rubik's Cube Group**: Joyner, D. (2008). *Adventures in Group Theory*
- **Discrete Dynamics**: Devaney, R. L. (2003). *An Introduction to Chaotic Dynamical Systems*
- **Chaos Theory**: Strogatz, S. H. (2015). *Nonlinear Dynamics and Chaos*

## License

MIT License with educational use notice. See [LICENSE](LICENSE) for details.

## Acknowledgments

- **HactarCE** for the Hyperspeedcube library
- **Math 538** course for motivation and theoretical foundation
- **Rust Community** for excellent tooling and documentation

---

**Course**: Math 538 - Discrete Dynamical Systems & Chaos
**Semester**: Fall 2025
**Project**: Orbit Exploration on N-Dimensional Twisty Puzzles
