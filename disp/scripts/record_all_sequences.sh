#!/bin/bash
# Batch record all priority sequences for presentation
# Run from nix shell: nix develop

set -e

echo "🎬 BATCH RECORDING: Hypercube Sequences"
echo "========================================"
echo ""

# Priority sequences for 15-minute presentation
# Format: "SEQUENCE|output_name|duration"
SEQUENCES=(
    "FR|FR_single|10"
    "FO FO|FO_FO|15"
    "FR FR|FR_FR|15"
    "RO RO|RO_RO|15"
    "FR UF|FR_UF|20"
)

TOTAL=${#SEQUENCES[@]}
echo "Will record $TOTAL sequences"
echo ""

# Check if Hyperspeedcube is available
if ! command -v hyperspeedcube &> /dev/null; then
    echo "❌ Error: hyperspeedcube not found"
    echo "   Run: nix develop"
    exit 1
fi

if ! command -v xdotool &> /dev/null; then
    echo "❌ Error: xdotool not found"
    echo "   Run: nix develop"
    exit 1
fi

# Launch Hyperspeedcube once
echo "Launching Hyperspeedcube..."
hyperspeedcube &
HSC_PID=$!
sleep 4

# Check if it launched
if ! xdotool search --name "Hyperspeedcube" > /dev/null 2>&1; then
    echo "❌ Error: Hyperspeedcube failed to launch"
    kill $HSC_PID 2>/dev/null || true
    exit 1
fi

echo "✓ Hyperspeedcube running"
echo ""

# Record each sequence
for i in "${!SEQUENCES[@]}"; do
    IFS='|' read -r sequence name duration <<< "${SEQUENCES[$i]}"

    NUM=$((i+1))
    echo "[$NUM/$TOTAL] Recording: $sequence"
    echo "        Output: recordings/${name}.mp4"
    echo "        Duration: ${duration}s"

    ./scripts/automate_hyperspeedcube.sh "$sequence" "recordings/${name}.mp4" "$duration"

    echo ""
    sleep 2  # Pause between recordings
done

# Close Hyperspeedcube
echo "Closing Hyperspeedcube..."
kill $HSC_PID 2>/dev/null || true

echo ""
echo "✓ All recordings complete!"
echo ""
echo "Converting to GIFs..."
echo "====================="
echo ""

# Convert all to GIFs
for i in "${!SEQUENCES[@]}"; do
    IFS='|' read -r sequence name duration <<< "${SEQUENCES[$i]}"

    VIDEO="recordings/${name}.mp4"
    GIF="figures/sequence_${name}.gif"

    if [ -f "$VIDEO" ]; then
        echo "Converting: $VIDEO → $GIF"
        ./scripts/video_to_gif.sh "$VIDEO" "$GIF" 480 15
    fi
done

echo ""
echo "✨ COMPLETE! All sequences recorded and converted."
echo ""
echo "Files created:"
ls -lh recordings/*.mp4 2>/dev/null | awk '{print "  " $9 " (" $5 ")"}'
echo ""
ls -lh figures/sequence_*.gif 2>/dev/null | awk '{print "  " $9 " (" $5 ")"}'