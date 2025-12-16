#!/usr/bin/env bash
# Simple manual recording - YOU type the moves
# Usage: ./manual_record.sh SEQUENCE_NAME DURATION

SEQUENCE_NAME=${1:-"test"}
DURATION=${2:-15}
OUTPUT="recordings/${SEQUENCE_NAME}.mp4"

cd "$(dirname "$0")"

echo "🎥 MANUAL RECORDING: $SEQUENCE_NAME"
echo "Duration: ${DURATION} seconds"
echo ""
echo "INSTRUCTIONS:"
echo "  1. Make sure Hyperspeedcube window is visible and IN FOCUS"
echo "  2. Reset puzzle in Hyperspeedcube: Ctrl+R"
echo "  3. When recording starts, YOU type the moves"
echo ""
echo "Recording will start in 5 seconds..."
echo "Get ready!"
echo ""

sleep 1; echo "5..."
sleep 1; echo "4..."
sleep 1; echo "3..."
sleep 1; echo "2..."
sleep 1; echo "1..."

echo ""
echo "🔴 RECORDING NOW - Type moves in Hyperspeedcube!"
echo "Recording for ${DURATION} seconds..."
echo ""

# Simple screen recording
nix develop --command bash -c "
    ffmpeg -f x11grab -framerate 30 -video_size 1920x1080 \
        -i :0.0 -t $DURATION -y $OUTPUT 2>&1 | tail -5
"

echo ""
if [ -f "$OUTPUT" ]; then
    echo "✅ Recording saved!"
    ls -lh "$OUTPUT"
    echo ""
    echo "Convert to GIF:"
    echo "  nix develop --command ./scripts/video_to_gif.sh $OUTPUT figures/sequence_${SEQUENCE_NAME}.gif"
else
    echo "❌ Recording failed"
fi
