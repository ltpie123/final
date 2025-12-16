# Orbit Exploration Tool for Hyperspeedcube (4D Rubik's Cube)

## Goal
Create a Rust-based orbit exploration tool to analyze move sequences (like RU combinations) on a 3x3x3x3 (4D Rubik's cube) for a math class project.

## Approach: Rust Binary Using Hyperspeedcube as Library

### Why Rust over Python?
- **Faster development**: Writing Rust code using the existing library is faster than creating Python bindings
- **Performance critical**: 4D cube state spaces are enormous; Rust's speed is essential
- **Simple integration**: Hyperspeedcube's crates are designed to be used as libraries
- **Export results**: Generate JSON/CSV files that can be analyzed with Python/matplotlib later if needed

## Implementation Plan

### 1. Create Rust workspace in `ctrl/` directory
- **File**: `ctrl/Cargo.toml`
  - Create workspace with dependency on `../hyper/Hyperspeedcube/crates/hyperpuzzle`
  - Add dependencies: `serde`, `serde_json` for exports, `clap` for CLI args

### 2. Create main orbit exploration binary
- **File**: `ctrl/src/main.rs`
  - Load 3x3x3x3 puzzle from catalog: `catalog().build_puzzle_blocking("ft_tesseract:3")`
  - Implement orbit generation using BFS:
    - Start from solved state
    - Apply move sequences (configurable, e.g., "R", "U", "RU", "R'", "U'")
    - Track visited states (using hash set)
    - Record transitions for graph export
  - Calculate orbit statistics (size, depth distribution)
  - Export results to JSON files

### 3. State representation and tracking
- **File**: `ctrl/src/orbit.rs`
  - Wrapper around `BoxDynPuzzleState` for hashing/equality
  - BFS/DFS exploration logic
  - State encoding for efficient storage
  - Orbit graph structure (nodes = states, edges = moves)

### 4. Output formats
- **File**: `ctrl/src/export.rs`
  - JSON export: orbit graph with nodes (state IDs) and edges (move labels)
  - CSV export: statistics (orbit size, max depth, state counts by depth)
  - DOT format: for Graphviz visualization (optional, for small orbits)

### 5. CLI interface
- Parse arguments:
  - Puzzle spec (default: "ft_tesseract:3")
  - Move set (default: ["R", "U"])
  - Max depth limit (safety for large orbits)
  - Output directory
  - Verbosity level

## Critical Files from Hyperspeedcube

### Core API to use:
- `hyper/Hyperspeedcube/crates/hyperpuzzle/src/lib.rs` - Loading puzzles
- `hyper/Hyperspeedcube/crates/hyperpuzzle_core/src/traits/state.rs` - `PuzzleState::do_twist()`
- `hyper/Hyperspeedcube/crates/hyperpuzzle_core/src/puzzle/twist.rs` - `LayeredTwist` struct
- `hyper/Hyperspeedcube/crates/hyperpuzzle_core/src/puzzle/dev_data/orbits.rs` - Existing orbit types (for reference)

### Key structs/traits:
- `Puzzle` - puzzle type definition
- `BoxDynPuzzleState` - puzzle state instance
- `LayeredTwist` - represents a move (axis + layers + transform)
- `PuzzleState::do_twist()` - applies a move, returns new state or blocking pieces

## Files to Create

1. `ctrl/Cargo.toml` - Rust project manifest
2. `ctrl/src/main.rs` - CLI entry point
3. `ctrl/src/orbit.rs` - Orbit exploration logic
4. `ctrl/src/export.rs` - Output formatters
5. `ctrl/src/moves.rs` - Move notation parser (convert "R", "U" strings to twists)
6. `ctrl/README.md` - Usage documentation

## Example Usage (after implementation)

```bash
cd ctrl
cargo run --release -- \
  --puzzle "ft_tesseract:3" \
  --moves "R,U" \
  --max-depth 8 \
  --output ../results/ru_orbit.json
```

## Expected Outputs

1. **orbit_stats.json**: Orbit size, depth distribution, timing
2. **orbit_graph.json**: Full graph structure (state IDs + transitions)
3. **states_by_depth.csv**: Count of states at each depth
4. **Console output**: Progress updates, final statistics

## Phase 1: Initial Implementation TODO

### Must Have (MVP)
- [ ] Set up Rust workspace in `ctrl/` with Hyperspeedcube dependency
- [ ] Load 3x3x3x3 puzzle from catalog
- [ ] Parse move notation (convert "R", "U" strings to LayeredTwist)
- [ ] Implement basic BFS orbit exploration
- [ ] Add state deduplication (hashing)
- [ ] Export orbit size and basic stats to JSON
- [ ] Add CLI arguments (moves, max-depth, output path)
- [ ] Test with small move set (depth limit ~5-6 initially)

### Nice to Have (Phase 1)
- [ ] Progress bar / status updates during search
- [ ] CSV export for state counts by depth
- [ ] Handle puzzle load errors gracefully
- [ ] Add time elapsed tracking

### Deferred to Phase 2
- [ ] Graph export (full transition graph)
- [ ] DOT format for visualization
- [ ] Parallel processing optimization
- [ ] Multiple puzzle support
- [ ] Advanced symmetry analysis
- [ ] Python visualization scripts

## Phase 2: Post-Bug-Fix Improvements

After Phase 1 is working and bugs are resolved, we'll add:

### 2.1 Performance Optimization
- **File**: `ctrl/src/orbit.rs`
  - Implement parallel BFS using `rayon`
  - Add state canonicalization (reduce equivalent states under symmetry)
  - Memory-efficient state encoding
  - Benchmark different hash algorithms

### 2.2 Enhanced Exports
- **File**: `ctrl/src/export.rs`
  - Full orbit graph export (JSON with state IDs + edges)
  - DOT format generation for Graphviz
  - GraphML format for network analysis tools
  - SQLite database export for large orbits

### 2.3 Visualization Integration
- **Directory**: `disp/` (Python scripts)
  - Read JSON outputs from `ctrl/`
  - Generate orbit graphs using networkx + matplotlib
  - Create state space diagrams
  - Interactive visualization with plotly
  - Statistics dashboards

### 2.4 Advanced Analysis
- **File**: `ctrl/src/analysis.rs`
  - Orbit decomposition (find sub-orbits)
  - Compute stabilizer subgroups
  - Calculate God's number for the move set
  - Find diameter of the orbit graph
  - Detect interesting patterns/symmetries

### 2.5 Documentation and Report Generation
- **File**: `report/` (LaTeX or Markdown)
  - Auto-generate sections from computed results
  - Include orbit statistics tables
  - Embed generated visualizations
  - Mathematical analysis writeup

## Notes

- For 3x3x3x3 with RU moves, the orbit might be huge - may need to implement depth limits
- State hashing: need efficient serialization of puzzle states for deduplication
- Consider using parallel processing (rayon) if performance is an issue
- Can add visualization generation later using Python scripts that read the JSON output
- Start with depth limit of 5-6 to ensure fast iteration during development
- Once Phase 1 works, we can gradually increase depth and add Phase 2 features
