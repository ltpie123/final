# CTRL - Hypercube Trajectory Explorer

**Discrete Dynamical Systems & Chaos Analysis on N-Dimensional Rubik's Cubes**

A Rust-based tool for exploring trajectories of move sequences on hyperdimensional twisty puzzles, built for chaos theory and discrete dynamical systems analysis.

## Overview

This tool analyzes the behavior of iterated maps on puzzle state spaces by repeatedly applying a fixed move sequence and detecting periodic orbits. It's designed to explore how complexity and periodicity scale across dimensions (3D vs 4D Rubik's cubes).

### Mathematical Framework

Given a puzzle state space $S$ and a move sequence $M = (m_1, m_2, \ldots, m_k)$, we define a map:

$$T: S \to S$$

where $T(s) = m_k \circ m_{k-1} \circ \cdots \circ m_1(s)$

We then follow the discrete trajectory:

$$s_0, s_1 = T(s_0), s_2 = T(s_1), \ldots$$

The tool detects:
- **Period**: Length of the cycle when the trajectory repeats
- **Transient length**: Number of iterations before entering the cycle
- **Unique states**: Total distinct states visited

## Installation

### Prerequisites

- Rust 1.70+ (install from [rustup.rs](https://rustup.rs/))
- Git with submodule support

### Setup

```bash
# Clone the repository (already done if you're reading this)
git clone --recurse-submodules <your-repo-url>
cd math538/final/ctrl

# Build the project
cargo build --release
```

## Usage

### Basic Command

```bash
cargo run --release -- \
  --puzzle <puzzle-id> \
  --moves <move-sequence> \
  --max-iterations <limit> \
  --output <output-file.json>
```

### Examples

#### 3D Rubik's Cube (3x3x3) with R,U moves
```bash
cargo run --release -- \
  --puzzle ft_cube:3 \
  --moves R,U \
  --max-iterations 1000 \
  --output results_3x3x3_RU.json
```

#### 4D Hypercube (3x3x3x3) with OF,OU moves
```bash
cargo run --release -- \
  --puzzle ft_hypercube:3 \
  --moves OF,OU \
  --max-iterations 100000 \
  --output results_3x3x3x3_OFOU.json
```

### Supported Puzzles

| Puzzle ID | Dimension | Description | Move Notation |
|-----------|-----------|-------------|---------------|
| `ft_cube:2` | 3D | 2x2x2 Pocket Cube | R, U, F, L, B, D |
| `ft_cube:3` | 3D | 3x3x3 Rubik's Cube | R, U, F, L, B, D |
| `ft_hypercube:2` | 4D | 2x2x2x2 4D Pocket Cube | OF, OU, OR, OL, etc. |
| `ft_hypercube:3` | 4D | 3x3x3x3 4D Rubik's Cube | OF, OU, OR, OL, etc. |

**Note**: Prime moves (inverses) are supported with apostrophe notation: `R'`, `U'`, `OF'`, etc.

## Cross-Dimensional Results

### Experiment 1: R,U Moves on 3D Cubes

| Puzzle | Dimension | Move Sequence | Period | Unique States | Time |
|--------|-----------|---------------|--------|---------------|------|
| 2x2x2 | 3D | R → U | 30 | 30 | <0.01s |
| 3x3x3 | 3D | R → U | 840 | 840 | 0.04s |

**Observation**: Period scales dramatically with puzzle complexity. The 3x3x3 has 28× longer period than the 2x2x2.

### Experiment 2: OF,OU Moves on 4D Cubes

| Puzzle | Dimension | Move Sequence | Period | Unique States | Time |
|--------|-----------|---------------|--------|---------------|------|
| 2x2x2x2 | 4D | OF → OU | 6 | 6 | <0.01s |
| 3x3x3x3 | 4D | OF → OU | 6 | 6 | <0.01s |

**Observation**: The OF,OU move combination creates a remarkably simple 6-cycle regardless of puzzle size! This suggests OF and OU have a special geometric relationship (possibly commute or nearly-commute).

### Key Findings

1. **Dimension vs Complexity**: Moving from 3D to 4D doesn't automatically increase period - the choice of moves matters more
2. **Move Selection**: Some move pairs (like OF,OU) create simple periodic behavior, while others (like R,U) create complex trajectories
3. **No Transients**: All tested trajectories returned directly to the solved state (transient length = 0), indicating all moves preserve the group structure

## Output Format

Results are exported as JSON:

```json
{
  "puzzle_id": "ft_cube:3",
  "puzzle_name": "3x3x3",
  "dimension": 3,
  "move_sequence": ["R", "U"],
  "period": 840,
  "transient_length": 0,
  "unique_states_visited": 840,
  "max_iterations": 1000,
  "reached_cycle": true,
  "exploration_time_ms": 42
}
```

## Implementation Details

### State Hashing

Puzzle states are hashed by extracting piece transforms from render data:
```rust
fn hash_state(state: &BoxDynPuzzleState) -> String {
    let render_data = state.render_data();
    let nd_render = render_data.downcast_ref::<NdEuclidPuzzleStateRenderData>()?;
    sha256(format!("{:?}", nd_render.piece_transforms))
}
```

This ensures that states are compared based on actual piece positions/orientations, not memory addresses.

### Cycle Detection

Uses a HashMap to track visited states:
```rust
for iteration in 1..=max_iterations {
    state = apply_move_sequence(state, moves);
    let hash = hash_state(&state);

    if let Some(&first_visit) = visited.get(&hash) {
        period = iteration - first_visit;
        break; // Cycle detected!
    }

    visited.insert(hash, iteration);
}
```

## Future Work

### Finding Chaotic Behavior

To demonstrate chaos emergence in higher dimensions, we need to:
1. Test longer move sequences (3+ moves)
2. Try non-commuting move pairs
3. Analyze move combinations that maximize period
4. Compare Lyapunov exponents across dimensions

### Suggested Experiments

- **3D Cube**: Try `R,U,F` or `R,U,R',U'` sequences
- **4D Cube**: Try `OF,OR,OU` or longer chains
- **Mixed Layers**: Test move sequences that affect multiple layers

## References

- **Hyperspeedcube**: [HactarCE/Hyperspeedcube](https://github.com/HactarCE/Hyperspeedcube)
- **Discrete Dynamical Systems**: Iterating maps on finite state spaces
- **Group Theory**: Rubik's cube group structure and orbits

## License

See [LICENSE](../LICENSE) for details.

## Contributing

This is a student project for Math 538 (Discrete Dynamical Systems & Chaos). The focus is on educational exploration of chaos theory concepts in unusual state spaces (hyperdimensional puzzles).

---

**Course**: Math 538 - Discrete Dynamical Systems & Chaos
**Institution**: [Your University]
**Semester**: [Current Semester]
