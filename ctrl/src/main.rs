use clap::Parser;
use hyperpuzzle::{catalog, load_global_catalog};
use hyperpuzzle_core::Puzzle;

mod moves;
mod orbit;

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

    /// Maximum iterations to follow trajectory
    #[arg(short = 'i', long, default_value_t = 100000)]
    max_iterations: usize,

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
    println!("   Move sequence: {}", args.moves);
    println!("   Max iterations: {}", args.max_iterations);
    println!("   Output: {}", args.output);

    // Step 4: Parse moves
    println!("\n🔄 Parsing move sequence...");
    let moves = match moves::parse_moves(&puzzle, &args.moves) {
        Ok(m) => m,
        Err(e) => {
            eprintln!("❌ Error parsing moves: {}", e);
            eprintln!("\nAvailable moves for this puzzle:");
            eprintln!("  First few twists:");
            for (twist_id, name_spec) in puzzle.twists.names.iter().take(10) {
                eprintln!("    {}: {}", twist_id.0, &name_spec.preferred);
            }
            eprintln!("  ... and {} more", puzzle.twists.names.len().saturating_sub(10));
            return;
        }
    };

    println!("✅ Parsed move sequence: {} moves per iteration", moves.len());
    for (i, layered_twist) in moves.iter().enumerate() {
        let name_spec = puzzle.twists.names.get(layered_twist.transform)
            .expect("Invalid twist ID");
        println!("   {}: {} (layers: {})", i + 1, &name_spec.preferred, layered_twist.layers.0);
    }

    // Step 5: Follow trajectory (discrete dynamical system)
    let stats = orbit::explore_trajectory(&puzzle, initial_state, &moves, args.max_iterations, dimension);

    // Step 6: Display summary
    println!("\n📊 Dynamical Systems Summary:");
    println!("   Puzzle: {} ({}D)", stats.puzzle_name, stats.dimension);
    println!("   Map T: {}", stats.move_sequence.join(" → "));
    println!("   Unique states visited: {}", stats.unique_states_visited);

    if stats.reached_cycle {
        println!("\n   🔄 Periodic Behavior:");
        println!("     Period: {} iterations", stats.period.unwrap());
        println!("     Transient: {} iterations", stats.transient_length);
        println!("     Total trajectory: {} states", stats.unique_states_visited);
    } else {
        println!("\n   ⏸️  Non-periodic (or period > {} iterations)", stats.max_iterations);
        println!("     This suggests complex/chaotic behavior!");
    }

    // Step 7: Export to JSON
    println!("\n💾 Exporting results...");
    match stats.export_json(&args.output) {
        Ok(_) => {
            println!("✅ Results exported to: {}", args.output);
        }
        Err(e) => {
            eprintln!("❌ Failed to export results: {}", e);
        }
    }

    println!("\n✅ Trajectory analysis complete!");
}
