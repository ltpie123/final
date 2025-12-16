use clap::Parser;
use hyperpuzzle::{catalog, load_global_catalog};
use hyperpuzzle_core::Puzzle;

/// Orbit Explorer for Hyperspeedcube puzzles across dimensions
#[derive(Parser, Debug)]
#[command(name = "ctrl")]
#[command(about = "Explore move orbits on N-dimensional Rubik's cubes", long_about = None)]
struct Args {
    /// Puzzle ID to analyze (e.g., ft_cube:3, ft_hypercube:3)
    #[arg(short, long, default_value = "ft_hypercube:3")]
    puzzle: String,

    /// Move set to explore (comma-separated, e.g., "R,U")
    #[arg(short, long, default_value = "R,U")]
    moves: String,

    /// Maximum search depth (limits orbit size)
    #[arg(short = 'd', long, default_value_t = 6)]
    max_depth: usize,

    /// Output file path (JSON format)
    #[arg(short, long, default_value = "orbit_stats.json")]
    output: String,
}

fn main() {
    let args = Args::parse();

    println!("🧊 Hyperspeedcube Orbit Explorer");
    println!("=================================\n");

    // Step 1: Load the puzzle catalog (this includes all built-in puzzles)
    println!("Loading puzzle catalog...");
    load_global_catalog();

    // Step 2: Load the requested puzzle
    println!("Loading puzzle: {}...", args.puzzle);
    let puzzle = match catalog().build_blocking::<Puzzle>(&args.puzzle) {
        Ok(puz) => puz,
        Err(e) => {
            eprintln!("❌ Error loading puzzle '{}': {:?}", args.puzzle, e);
            eprintln!("\nAvailable puzzles:");
            eprintln!("  3D: ft_cube:2 (2x2x2), ft_cube:3 (3x3x3)");
            eprintln!("  4D: ft_hypercube:2 (2x2x2x2), ft_hypercube:3 (3x3x3x3)");
            return;
        }
    };

    println!("✅ Loaded puzzle: {}", puzzle.meta.name);
    println!("   Puzzle ID: {}", puzzle.meta.id);

    // Determine dimension from puzzle ID (simple heuristic)
    let dimension = if puzzle.meta.id.contains("hypercube") {
        4
    } else if puzzle.meta.id.contains("cube") {
        3
    } else {
        // Try to infer from number of axes (each dimension typically has 2 opposite axes)
        puzzle.axis_layers.len() / 2
    };
    println!("   Dimension: {}D", dimension);

    // Step 3: Create the initial (solved) state
    let initial_state = puzzle.new_solved_state();
    println!("\n✅ Created initial state");
    println!("   Is solved: {}", initial_state.is_solved());

    println!("\n📋 Configuration:");
    println!("   Move set: {}", args.moves);
    println!("   Max depth: {}", args.max_depth);
    println!("   Output: {}", args.output);

    // Next steps (TODO):
    // - Parse move notation
    // - Apply moves to explore the orbit
    // - Track visited states
    // - Export results

    println!("\n🎉 Basic setup working! Ready to implement orbit exploration.");
}
