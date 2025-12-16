use eyre::Result;

fn main() -> Result<()> {
    println!("Hypercube Renderer - Checking dependencies");
    
    // Load puzzle catalog
    let catalog = hyperpuzzle::catalog();
    
    // Try to load 3^4 puzzle
    let puzzle_id = "ft_hypercube:3";
    println!("Loading puzzle: {}", puzzle_id);
    
    match catalog.get_puzzle(puzzle_id) {
        Ok(puzzle_spec) => {
            println!("✓ Loaded puzzle: {}", puzzle_spec.meta.name);
            println!("  ID: {}", puzzle_spec.meta.id);
            println!("  Version: {}.{}.{}", 
                puzzle_spec.meta.version.major,
                puzzle_spec.meta.version.minor, 
                puzzle_spec.meta.version.patch
            );
        }
        Err(e) => {
            println!("✗ Failed to load puzzle: {}", e);
            return Err(e.into());
        }
    }
    
    println!("\nNote: Full rendering requires graphics context (WGPU)");
    println!("This would need to be integrated with the full Hyperspeedcube app.");
    
    Ok(())
}
