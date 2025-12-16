#!/usr/bin/env python3
"""
Generate Hyperspeedcube .hsc log files for visualization sequences.
"""

from datetime import datetime, timezone

def generate_hsc_log(puzzle_id: str, moves: list[str], cycles: int, output_file: str):
    """
    Generate a .hsc log file for Hyperspeedcube.
    
    Args:
        puzzle_id: Puzzle identifier (e.g., "ft_hypercube:3")
        moves: List of move names (e.g., ["FR", "FO"])
        cycles: Number of times to repeat the sequence
        output_file: Path to output .hsc file
    """
    timestamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    
    # Build twist sequence
    twist_sequence = " ".join(moves * cycles)
    
    # Calculate mock duration (500ms per move)
    duration_ms = len(moves) * cycles * 500
    
    hsc_content = f"""// Hyperspeedcube puzzle log
// Generated for visualization sequence
version 2

program name="Generated" version="1.0.0"

solve {{
    puzzle id="{puzzle_id}" version="1.0.0"
    solved #false
    duration {duration_ms}
    
    scramble "none" time="{timestamp}" seed="0" {{
        twists ""
    }}
    
    log {{
        scramble
        start-solve time="{timestamp}" duration=0
        twists "{twist_sequence}"
    }}
}}
"""
    
    with open(output_file, 'w') as f:
        f.write(hsc_content)
    
    print(f"✓ Generated: {output_file}")
    print(f"  Puzzle: {puzzle_id}")
    print(f"  Moves: {' '.join(moves)} × {cycles} cycles")
    print(f"  Total moves: {len(moves) * cycles}")
    print()


def main():
    """Generate .hsc files for the three priority sequences."""
    
    # 4D Rubik's cube (3^4)
    puzzle_id = "ft_hypercube:3"
    
    sequences = [
        {
            "name": "FR_single",
            "moves": ["FR"],
            "cycles": 8,
            "description": "Baseline sequence (period 8)"
        },
        {
            "name": "FO_FO",
            "moves": ["FO", "FO"],
            "cycles": 4,
            "description": "Most chaotic (λ=6.093, period 4)"
        },
        {
            "name": "FR_FR",
            "moves": ["FR", "FR"],
            "cycles": 4,
            "description": "Self-composition (λ=5.942, period 4)"
        }
    ]
    
    print("Generating Hyperspeedcube log files")
    print("=" * 50)
    print()
    
    for seq in sequences:
        print(f"# {seq['name']}: {seq['description']}")
        output_file = f"logs/{seq['name']}.hsc"
        generate_hsc_log(
            puzzle_id=puzzle_id,
            moves=seq['moves'],
            cycles=seq['cycles'],
            output_file=output_file
        )
    
    print("=" * 50)
    print("✅ All log files generated!")
    print()
    print("Next steps:")
    print("1. Open Hyperspeedcube: hyperspeedcube &")
    print("2. Load log file: File → Open Log")
    print("3. Step through moves: Use arrow keys or playback controls")
    print("4. Export frames: Image Generator tab → Set resolution → Save images")
    print()


if __name__ == "__main__":
    main()
