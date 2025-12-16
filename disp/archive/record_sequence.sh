#!/usr/bin/env bash
# Quick recording helper for Hyperspeedcube sequences
# Usage: ./record_sequence.sh SEQUENCE_NAME DURATION

set -e

SEQUENCE_NAME=${1:-"test"}
DURATION=${2:-15}
OUTPUT_FILE="recordings/${SEQUENCE_NAME}.mp4"

echo "🎥 Recording: $SEQUENCE_NAME"
echo "Duration: ${DURATION} seconds"
echo "Output: $OUTPUT_FILE"
echo ""
echo "INSTRUCTIONS:"
echo "1. Make sure Hyperspeedcube window is visible"
echo "2. Reset puzzle (Ctrl+R in Hyperspeedcube)"
echo "3. Adjust view and animation speed (Settings > 0.25x recommended)"
echo ""
echo "Recording will start in 3 seconds..."
echo "Press Ctrl+C to stop early"
echo ""

sleep 1; echo "3..."
sleep 1; echo "2..."
sleep 1; echo "1..."
echo "🔴 RECORDING NOW - Perform your sequence!"
echo ""

# Find Hyperspeedcube window
WINDOW_ID=$(xdotool search --name "Hyperspeedcube" 2>/dev/null | head -1 || echo "")

if [ -z "$WINDOW_ID" ]; then
    echo "⚠ Could not find Hyperspeedcube window"
    echo "Recording full screen instead..."
    ffmpeg -f x11grab -framerate 30 -i :0.0 -t "$DURATION" -y "$OUTPUT_FILE" 2>&1 | grep -E "frame=|Duration|time=" || true
else
    # Get window geometry
    eval $(xdotool getwindowgeometry --shell "$WINDOW_ID")
    echo "Found Hyperspeedcube window: ${WIDTH}x${HEIGHT} at +${X}+${Y}"
    
    ffmpeg -f x11grab -framerate 30 -video_size ${WIDTH}x${HEIGHT} \
        -i :0.0+${X},${Y} -t "$DURATION" -y "$OUTPUT_FILE" 2>&1 | \
        grep -E "frame=|Duration|time=" || true
fi

echo ""
echo "✅ Recording complete: $OUTPUT_FILE"
ls -lh "$OUTPUT_FILE"
echo ""
echo "Next step: Convert to GIF"
echo "  ./scripts/video_to_gif.sh $OUTPUT_FILE figures/sequence_${SEQUENCE_NAME}.gif"
