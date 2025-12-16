#!/usr/bin/env bash
# Recording script that runs ffmpeg from Nix shell
# Usage: ./record.sh SEQUENCE_NAME DURATION

set -e

SEQUENCE_NAME=${1:-"test"}
DURATION=${2:-15}
OUTPUT_FILE="recordings/${SEQUENCE_NAME}.mp4"

cd "$(dirname "$0")"

echo "🎥 Recording: $SEQUENCE_NAME"
echo "Duration: ${DURATION} seconds"
echo "Output: $OUTPUT_FILE"
echo ""
echo "READY?"
echo "  ✓ Hyperspeedcube window is visible"
echo "  ✓ Puzzle reset (Ctrl+R)"
echo "  ✓ Animation speed 0.25x"
echo ""
echo "Recording starts in 5 seconds..."
echo "Get ready to type moves!"
echo ""

sleep 1; echo "5..."
sleep 1; echo "4..."
sleep 1; echo "3..."
sleep 1; echo "2..."
sleep 1; echo "1..."

echo ""
echo "🔴 RECORDING - Type moves in Hyperspeedcube!"
echo ""

# Run ffmpeg in Nix shell (has ffmpeg available)
nix develop --command bash -c "
    ffmpeg -f x11grab -framerate 30 -video_size 1920x1080 -i :0.0 \
        -t $DURATION -y $OUTPUT_FILE 2>&1 | grep -E 'frame=|time=' || true
"

echo ""
if [ -f "$OUTPUT_FILE" ]; then
    echo "✅ Recording saved!"
    ls -lh "$OUTPUT_FILE"
    echo ""
    echo "Convert to GIF:"
    echo "  nix develop --command ./scripts/video_to_gif.sh $OUTPUT_FILE figures/sequence_${SEQUENCE_NAME}.gif"
else
    echo "❌ Recording failed - file not created"
fi
