use hyperpuzzle_core::{BoxDynPuzzleState, LayeredTwist, Puzzle};
use hyperpuzzle_impl_nd_euclid::NdEuclidPuzzleStateRenderData;
use serde::Serialize;
use sha2::{Digest, Sha256};
use std::collections::HashMap;
use std::fs;
use std::sync::Arc;
use std::time::Instant;

/// Statistics about trajectory exploration (discrete dynamical systems)
#[derive(Debug, Serialize)]
pub struct TrajectoryStats {
    pub puzzle_id: String,
    pub puzzle_name: String,
    pub dimension: usize,
    pub move_sequence: Vec<String>,

    // Dynamical systems metrics
    pub period: Option<usize>,           // Period of the cycle (None if not found)
    pub transient_length: usize,         // States before entering cycle
    pub unique_states_visited: usize,   // Total unique states in trajectory
    pub max_iterations: usize,           // How far we explored
    pub reached_cycle: bool,             // Did we find a repeating state?

    // Timing
    pub exploration_time_ms: u128,
}

/// Explore trajectory by repeatedly applying a move sequence
/// This is for discrete dynamical systems / chaos analysis
pub fn explore_trajectory(
    puzzle: &Arc<Puzzle>,
    initial_state: BoxDynPuzzleState,
    move_sequence: &[LayeredTwist],
    max_iterations: usize,
    dimension: usize,
) -> TrajectoryStats {
    let start_time = Instant::now();

    println!("\n🌀 Following trajectory (discrete dynamical system)...");
    println!("   Initial state: solved");
    println!("   Move sequence: applying {} moves per iteration", move_sequence.len());

    let mut state = initial_state;
    let mut visited: HashMap<String, usize> = HashMap::new();

    // Hash initial state
    let initial_hash = hash_state(&state);
    visited.insert(initial_hash, 0);

    let mut period = None;
    let mut transient_length = 0;
    let mut reached_cycle = false;

    let mut last_report = Instant::now();

    for iteration in 1..=max_iterations {
        // Apply entire move sequence once (one iteration of the map T)
        for layered_twist in move_sequence {
            match state.do_twist_dyn(*layered_twist) {
                Ok(new_state) => {
                    state = new_state;
                }
                Err(_) => {
                    println!("   ⚠️  Move blocked at iteration {}!", iteration);
                    break;
                }
            }
        }

        // Hash the new state
        let state_hash = hash_state(&state);

        // Check if we've seen this state before (cycle detected!)
        if let Some(&first_visit) = visited.get(&state_hash) {
            period = Some(iteration - first_visit);
            transient_length = first_visit;
            reached_cycle = true;

            println!("   🔄 CYCLE DETECTED at iteration {}!", iteration);
            println!("   First saw this state at iteration {}", first_visit);
            println!("   Period = {} iterations", period.unwrap());
            break;
        }

        visited.insert(state_hash, iteration);

        // Progress reporting
        if iteration % 1000 == 0 || last_report.elapsed().as_secs() >= 2 {
            println!("   Iteration {}: {} unique states visited, solved={}",
                     iteration, visited.len(), state.is_solved());
            last_report = Instant::now();
        }
    }

    let exploration_time = start_time.elapsed();
    let unique_states = visited.len();

    if !reached_cycle {
        println!("   ⏸️  Reached max iterations ({}) without finding cycle", max_iterations);
        println!("   Visited {} unique states", unique_states);
    }

    println!("✅ Trajectory exploration complete!");
    println!("   Unique states visited: {}", unique_states);
    if let Some(p) = period {
        println!("   Period: {} iterations", p);
        println!("   Transient: {} iterations", transient_length);
    }
    println!("   Time: {:.2}s", exploration_time.as_secs_f64());

    // Get move names
    let move_names: Vec<String> = move_sequence
        .iter()
        .map(|twist| {
            puzzle.twists.names.get(twist.transform)
                .map(|ns| ns.preferred.clone())
                .unwrap_or_else(|_| format!("?{}", twist.transform.0))
        })
        .collect();

    TrajectoryStats {
        puzzle_id: puzzle.meta.id.clone(),
        puzzle_name: puzzle.meta.name.clone(),
        dimension,
        move_sequence: move_names,
        period,
        transient_length,
        unique_states_visited: unique_states,
        max_iterations,
        reached_cycle,
        exploration_time_ms: exploration_time.as_millis(),
    }
}

impl TrajectoryStats {
    /// Export trajectory statistics to a JSON file
    pub fn export_json(&self, path: &str) -> Result<(), Box<dyn std::error::Error>> {
        let json = serde_json::to_string_pretty(self)?;
        fs::write(path, json)?;
        Ok(())
    }
}

/// Hash a puzzle state by extracting piece transforms from render data
fn hash_state(state: &BoxDynPuzzleState) -> String {
    // Get render data which contains the actual piece positions/orientations
    let render_data = state.render_data();

    // Try to downcast to NdEuclidPuzzleStateRenderData
    if let Some(nd_render) = render_data.downcast_ref::<NdEuclidPuzzleStateRenderData>() {
        // Hash the piece transforms (Motors) which represent the actual puzzle state
        let piece_data = format!("{:?}", nd_render.piece_transforms);

        // Use SHA256 for consistent hashing
        let mut hasher = Sha256::new();
        hasher.update(piece_data.as_bytes());
        let hash = hasher.finalize();
        format!("{:x}", hash)
    } else {
        // Fallback: use debug format of the full render data
        let mut hasher = Sha256::new();
        hasher.update(format!("{:?}", render_data).as_bytes());
        let hash = hasher.finalize();
        format!("{:x}", hash)
    }
}