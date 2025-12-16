#!/usr/bin/env bash
# Run automated sequence execution with manual recording

cd "$(dirname "$0")"

echo "🎬 Automated Sequence Execution"
echo ""
echo "Categories available:"
echo "  basic_single       - Single move orbits (3 sequences, 8 moves each)"
echo "  self_compositions  - FR→FR, FO→FO (2 sequences, 8 moves each)"
echo "  short_complex      - 4-move orbits (2 sequences, 24-48 moves)"
echo "  long_period_samples - FR→UF, FR→UO samples (2 sequences, 50-60 moves)"
echo "  demo_friendly      - Best for presentation (4 sequences, 16-48 moves) ⭐"
echo ""
echo "Recommended: demo_friendly"
echo ""

# Default to demo_friendly if no argument
CATEGORY=${1:-demo_friendly}

echo "Recording category: $CATEGORY"
echo ""

# Make sure recordings directory exists
mkdir -p recordings

echo "💡 SETUP INSTRUCTIONS:"
echo "  1. Make sure your screen recorder is ready (SimpleScreenRecorder, OBS, etc.)"
echo "  2. Position the recorder to capture the Hyperspeedcube window"
echo "  3. The script will prompt you before each sequence"
echo "  4. When prompted, start recording, press ENTER, and it executes moves"
echo ""

read -p "Press ENTER when ready... "

nix develop --command bash -c "uv run python3 automate_sequences.py $CATEGORY"
