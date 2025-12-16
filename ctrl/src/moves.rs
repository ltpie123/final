use hyperpuzzle_core::{LayerMask, LayeredTwist, Puzzle};
use std::sync::Arc;

/// Parse a move string like "R", "U", "R'", "U2" into a LayeredTwist
pub fn parse_move(puzzle: &Arc<Puzzle>, move_str: &str) -> Result<LayeredTwist, String> {
    let move_str = move_str.trim();
    if move_str.is_empty() {
        return Err("Empty move string".to_string());
    }

    // Parse the base move and any modifiers
    let (base_name, is_prime) = if move_str.ends_with('\'') || move_str.ends_with('\u{2019}') {
        // Handle prime moves (R', U')
        (&move_str[..move_str.len() - 1], true)
    } else {
        (move_str, false)
    };

    // TODO: Handle move repetition (e.g., "R2" means apply R twice)
    // For now, we'll ignore numbers

    // Look up the twist by name
    let twist = puzzle
        .twists
        .names
        .id_from_name(base_name)
        .ok_or_else(|| format!("Unknown move: '{}'", base_name))?;

    // If this is a prime move, get the reverse twist
    let final_twist = if is_prime {
        puzzle.twists.twists.get(twist)
            .map_err(|_| format!("Invalid twist ID"))?
            .reverse
    } else {
        twist
    };

    // For basic moves, use the outer layer (bit 0 = layer 0)
    let layers = LayerMask::default(); // LayerMask(1) = outer layer

    Ok(LayeredTwist {
        layers,
        transform: final_twist,
    })
}

/// Parse a comma-separated list of moves
pub fn parse_moves(puzzle: &Arc<Puzzle>, moves_str: &str) -> Result<Vec<LayeredTwist>, String> {
    moves_str
        .split(',')
        .map(|s| parse_move(puzzle, s.trim()))
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;
    use hyperpuzzle::{catalog, load_global_catalog};
    use hyperpuzzle_core::Puzzle;

    #[test]
    fn test_parse_basic_moves() {
        load_global_catalog();
        let puzzle = catalog()
            .build_blocking::<Puzzle>("ft_cube:3")
            .expect("Failed to load puzzle");

        // Test parsing basic moves
        let r_move = parse_move(&puzzle, "R").expect("Failed to parse R");
        let u_move = parse_move(&puzzle, "U").expect("Failed to parse U");

        // Verify they're different twists
        assert_ne!(r_move.transform, u_move.transform);
    }

    #[test]
    fn test_parse_prime_moves() {
        load_global_catalog();
        let puzzle = catalog()
            .build_blocking::<Puzzle>("ft_cube:3")
            .expect("Failed to load puzzle");

        let r_move = parse_move(&puzzle, "R").expect("Failed to parse R");
        let r_prime = parse_move(&puzzle, "R'").expect("Failed to parse R'");

        // R and R' should have different twist IDs (R' is the reverse)
        assert_ne!(r_move.transform, r_prime.transform);
    }
}
