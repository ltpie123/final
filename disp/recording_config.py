#!/usr/bin/env python3
"""
Configuration for sequences to record
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
    'OU': ('v', 'j'),  # Outside → Up (y) - verify
    'OD': ('v', 'l'),  # Outside → Down (y') - verify
    
    # Grip F (Right face)
    'RF': ('f', 'j'),  # Right → Front (y)
    'RB': ('f', 'l'),  # Right → Back (y')
    'RU': ('f', 'j'),  # Right → Up (y)
    'RD': ('f', 'l'),  # Right → Down (y')
    'RO': ('f', 'o'),  # Right → Outside (z)
    'RI': ('f', 'u'),  # Right → Inside (z')
}

# Sequences to record, organized by category
SEQUENCES = {
    "basic": [
        {"name": "FR_single", "moves": ["FR"], "cycles": 2, "desc": "Basic FR rotation (period 8)"},
        {"name": "UF_single", "moves": ["UF"], "cycles": 2, "desc": "Basic UF rotation (period 8)"},
        {"name": "OR_single", "moves": ["OR"], "cycles": 2, "desc": "Basic OR rotation (period 8)"},
    ],
    
    "self_comp": [
        {"name": "FR_FR", "moves": ["FR", "FR"], "cycles": 2, "desc": "Self-composition (λ=5.94, period 4)"},
        {"name": "FO_FO", "moves": ["FO", "FO"], "cycles": 2, "desc": "Most chaotic (λ=6.09, period 4)"},
    ],
    
    "short_orbits": [
        {"name": "OF_OU_OB_OD", "moves": ["OF", "OU", "OB", "OD"], "cycles": 2, "desc": "Extremely chaotic (λ=5.64, period 6)"},
        {"name": "FR_OR_FL_OL", "moves": ["FR", "OR", "FL", "OL"], "cycles": 2, "desc": "4-move orbit (λ=4.65, period 12)"},
    ],
    
    "interesting_pairs": [
        {"name": "FR_UF_short", "moves": ["FR", "UF"], "cycles": 1, "desc": "Huge period sample (period 10080, 2 moves only)"},
        {"name": "FR_UO", "moves": ["FR", "UO"], "cycles": 1, "desc": "High chaos (λ=2.81, period 840, 2 moves)"},
    ],
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
    print("Recording Sequences Configuration")
    print("=" * 70)
    for cat_name, seqs in SEQUENCES.items():
        print(f"\n{cat_name.upper()}:")
        for seq in seqs:
            moves_str = " → ".join(seq['moves'])
            print(f"  {seq['name']}: {moves_str} × {seq['cycles']}")
            print(f"    {seq['desc']}")
    
    print(f"\nTotal sequences: {sum(len(s) for s in SEQUENCES.values())}")
    print(f"Total recordings: ~{sum(len(s['moves']) * s['cycles'] for cat in SEQUENCES.values() for s in cat)} moves")
