#!/usr/bin/env bash
# Record sequences with nix environment

cd "$(dirname "$0")"

echo "🎬 Hypercube Sequence Recording"
echo ""
echo "Categories available:"
echo "  basic          - Single rotations (3 sequences)"
echo "  self_comp      - Self-compositions (2 sequences)"
echo "  short_orbits   - Short period orbits (2 sequences)"
echo "  interesting_pairs - Long period samples (2 sequences)"
echo "  all            - Record everything (9 sequences)"
echo ""

# Default to all if no argument
CATEGORY=${1:-all}

echo "Recording category: $CATEGORY"
echo ""

nix develop --command bash -c "uv run python3 record_sequences.py --category $CATEGORY"
