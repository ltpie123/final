#!/usr/bin/env python3
"""
CORRECTED Configuration for sequences to record FULL ORBITS
Key insight: period = number of times to repeat the move sequence to return to solved
"""

# Keybind mapping: move_name -> (grip_key, twist_key)
# Based on default Rubiks4D keybinds
MOVE_KEYBINDS = {
    # Grip S (Front face)
    'FR': ('s', 'i'),  # Front → Right (x)
    'FL': ('s', 'k'),  # Front → Left (x')
    'FU': ('s', 'j'),  # Front → Up (y)
    'FD': ('s', 'l'),  # Front → Down (y')
    'FO': ('s', 'o'),  # Front → Outside (z)
    'FI': ('s', 'u'),  # Front → Inside (z')
    
    # Grip E (Up face)
    'UF': ('e', 'j'),  # Up → Front (y)
    'UB': ('e', 'l'),  # Up → Back (y')
    'UR': ('e', 'i'),  # Up → Right (x)
    'UL': ('e', 'k'),  # Up → Left (x')
    'UO': ('e', 'o'),  # Up → Outside (z)
    'UI': ('e', 'u'),  # Up → Inside (z')
    
    # Grip V (Outside face)
    'OR': ('v', 'i'),  # Outside → Right (x)
    'OL': ('v', 'k'),  # Outside → Left (x')
    'OF': ('v', 'j'),  # Outside → Front (y)
    'OB': ('v', 'l'),  # Outside → Back (y')
    'OU': ('v', 'o'),  # Outside → Up (z) - using o instead of j
    'OD': ('v', 'u'),  # Outside → Down (z') - using u instead of l
    
    # Grip F (Right face)
    'RF': ('f', 'j'),  # Right → Front (y)
    'RB': ('f', 'l'),  # Right → Back (y')
    'RU': ('f', 'j'),  # Right → Up (y)
    'RD': ('f', 'l'),  # Right → Down (y')
    'RO': ('f', 'o'),  # Right → Outside (z)
    'RI': ('f', 'u'),  # Right → Inside (z')
}

# Sequences to record - CORRECTED TO SHOW FULL ORBITS
# cycles = period (number of times to repeat the move sequence)
SEQUENCES = {
    "basic_single": [
        {"name": "FR_orbit", "moves": ["FR"], "cycles": 8, "desc": "FR single move, period 8 (full orbit)"},
        {"name": "UF_orbit", "moves": ["UF"], "cycles": 8, "desc": "UF single move, period 8 (full orbit)"},
        {"name": "OR_orbit", "moves": ["OR"], "cycles": 8, "desc": "OR single move, period 8 (full orbit)"},
    ],
    
    "self_compositions": [
        {"name": "FR_FR_orbit", "moves": ["FR", "FR"], "cycles": 4, "desc": "FR→FR, period 4, λ=5.94 (full orbit = 8 moves)"},
        {"name": "FO_FO_orbit", "moves": ["FO", "FO"], "cycles": 4, "desc": "FO→FO, period 4, λ=6.09 MOST CHAOTIC (full orbit = 8 moves)"},
    ],
    
    "short_complex": [
        {"name": "OF_OU_OB_OD_orbit", "moves": ["OF", "OU", "OB", "OD"], "cycles": 6, "desc": "4-move sequence, period 6, λ=5.64 (full orbit = 24 moves)"},
        {"name": "FR_OR_FL_OL_orbit", "moves": ["FR", "OR", "FL", "OL"], "cycles": 12, "desc": "4-move sequence, period 12, λ=4.65 (full orbit = 48 moves)"},
    ],
    
    "long_period_samples": [
        # These have huge periods - can't show full orbit, but show enough to see pattern
        {"name": "FR_UF_sample", "moves": ["FR", "UF"], "cycles": 30, "desc": "FR→UF, period 10,080, λ=3.95 (60 moves shows pattern)"},
        {"name": "FR_UO_sample", "moves": ["FR", "UO"], "cycles": 25, "desc": "FR→UO, period 840, λ=2.81 (50 moves shows pattern)"},
    ],
    
    # For presentation - shorter versions that are still meaningful
    "demo_friendly": [
        {"name": "FR_orbit_demo", "moves": ["FR"], "cycles": 16, "desc": "FR × 2 orbits for clarity"},
        {"name": "FO_FO_demo", "moves": ["FO", "FO"], "cycles": 8, "desc": "FO→FO × 2 orbits (most chaotic)"},
        {"name": "OF_OU_OB_OD_demo", "moves": ["OF", "OU", "OB", "OD"], "cycles": 12, "desc": "4-move × 2 orbits"},
        {"name": "FR_UF_demo", "moves": ["FR", "UF"], "cycles": 15, "desc": "FR→UF 15 iterations (30 moves)"},
    ]
}

def get_all_sequences():
    """Get flattened list of all sequences."""
    result = []
    for category, seqs in SEQUENCES.items():
        result.extend(seqs)
    return result

def get_category(category_name):
    """Get sequences from a specific category."""
    return SEQUENCES.get(category_name, [])

if __name__ == "__main__":
    print("CORRECTED Recording Sequences - Full Orbits")
    print("=" * 80)
    for cat_name, seqs in SEQUENCES.items():
        print(f"\n{cat_name.upper()}:")
        for seq in seqs:
            moves_str = " → ".join(seq['moves'])
            total_moves = len(seq['moves']) * seq['cycles']
            print(f"  {seq['name']}: [{moves_str}] × {seq['cycles']} = {total_moves} moves")
            print(f"    {seq['desc']}")
    
    print(f"\nTotal sequences: {sum(len(s) for s in SEQUENCES.values())}")
    print(f"\nRECOMMENDED FOR PRESENTATION (demo_friendly):")
    print("  - Short enough for GIFs (15-32 moves)")
    print("  - Show at least 1-2 complete orbits")
    print("  - Include most chaotic (FO→FO)")
