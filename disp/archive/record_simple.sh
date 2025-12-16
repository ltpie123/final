#!/usr/bin/env bash
# Simple screen recording - records full screen or you select region
# Usage: ./record_simple.sh SEQUENCE_NAME DURATION

set -e

SEQUENCE_NAME=${1:-"test"}
DURATION=${2:-15}
OUTPUT_FILE="recordings/${SEQUENCE_NAME}.mp4"

echo "🎥 Recording: $SEQUENCE_NAME"
echo "Duration: ${DURATION} seconds"
echo "Output: $OUTPUT_FILE"
echo ""
echo "MAKE SURE:"
echo "  ✓ Hyperspeedcube window is visible on screen"
echo "  ✓ Puzzle is reset (Ctrl+R in Hyperspeedcube)"
echo "  ✓ Animation speed is 0.25x (Settings > Animation > Speed)"
echo ""
echo "Recording will start in 5 seconds..."
echo "Get ready to type moves in Hyperspeedcube window!"
echo ""

sleep 1; echo "5..."
sleep 1; echo "4..."
sleep 1; echo "3..."
sleep 1; echo "2..."
sleep 1; echo "1..."

echo ""
echo "🔴 RECORDING NOW!"
echo "Type your moves in Hyperspeedcube window"
echo "Recording for ${DURATION} seconds..."
echo ""

# Simple full-screen recording with ffmpeg
ffmpeg -f x11grab -framerate 30 -video_size 1920x1080 -i :0.0 \
    -t "$DURATION" -y "$OUTPUT_FILE" 2>&1 | \
    grep -E "frame=|time=" | tail -20 || true

echo ""
echo "✅ Recording complete!"
ls -lh "$OUTPUT_FILE"
echo ""
echo "Next: Convert to GIF"
echo "  ./scripts/video_to_gif.sh $OUTPUT_FILE figures/sequence_${SEQUENCE_NAME}.gif"
echo ""
echo "Or trim if needed:"
echo "  ffmpeg -i $OUTPUT_FILE -ss 0 -t 10 recordings/${SEQUENCE_NAME}_trimmed.mp4"
