#!/usr/bin/env bash
# Automated recording - finds Hyperspeedcube, types moves, records video
# Usage: ./auto_record.sh SEQUENCE_NAME "MOVE1 MOVE2" CYCLES

set -e

SEQUENCE_NAME=${1:-"test"}
MOVES=${2:-"FR"}
CYCLES=${3:-4}

cd "$(dirname "$0")"

echo "🎬 AUTOMATED RECORDING"
echo "======================"
echo "Sequence: $SEQUENCE_NAME"
echo "Moves: $MOVES"
echo "Cycles: $CYCLES"
echo ""

# Calculate duration (each move ~2.5 seconds at 0.25x speed)
MOVE_COUNT=$(echo "$MOVES" | wc -w)
DURATION=$((CYCLES * MOVE_COUNT * 3 + 3))  # 3 sec per move + 3 sec buffer

OUTPUT_FILE="recordings/${SEQUENCE_NAME}.mp4"

echo "Estimated duration: ${DURATION} seconds"
echo ""
echo "Checking Hyperspeedcube..."

# Run automation in Nix shell (has xdotool and ffmpeg)
nix develop --command bash << EOF
set -e

# Find Hyperspeedcube window
WINDOW_ID=\$(xdotool search --name "Hyperspeedcube" 2>/dev/null | head -1 || echo "")

if [ -z "\$WINDOW_ID" ]; then
    echo "❌ Cannot find Hyperspeedcube window!"
    echo "Make sure Hyperspeedcube is running: hyperspeedcube &"
    exit 1
fi

echo "✓ Found Hyperspeedcube window: \$WINDOW_ID"

# Get window geometry for recording
eval \$(xdotool getwindowgeometry --shell \$WINDOW_ID)
echo "✓ Window: \${WIDTH}x\${HEIGHT} at +\${X}+\${Y}"

# Focus window and reset puzzle BEFORE recording
echo "Preparing puzzle..."
xdotool windowactivate --sync \$WINDOW_ID
xdotool windowraise \$WINDOW_ID
sleep 0.5

# Reset puzzle
echo "Resetting puzzle (Ctrl+R)..."
xdotool key --window \$WINDOW_ID ctrl+r
sleep 2

echo ""
echo "🔴 STARTING RECORDING"
echo ""

# Start recording in background
ffmpeg -f x11grab -framerate 30 -video_size \${WIDTH}x\${HEIGHT} \\
    -i :0.0+\${X},\${Y} -t $DURATION -y $OUTPUT_FILE 2>&1 >/dev/null &
FFMPEG_PID=\$!

# Wait for recording to stabilize
sleep 2

# Make sure window is still focused
xdotool windowactivate --sync \$WINDOW_ID

# Type moves AFTER recording started
echo "Typing moves..."
for ((cycle=1; cycle<=$CYCLES; cycle++)); do
    echo "  Cycle \$cycle/$CYCLES"
    for move in $MOVES; do
        echo "    → \$move"
        xdotool type --window \$WINDOW_ID "\$move"
        xdotool key --window \$WINDOW_ID Return
        sleep 2.8  # Time for animation at 0.25x speed
    done
done

# Wait for recording to finish
echo ""
echo "Waiting for recording to complete..."
wait \$FFMPEG_PID

echo "✅ Recording complete!"
EOF

if [ -f "$OUTPUT_FILE" ]; then
    echo ""
    ls -lh "$OUTPUT_FILE"
    echo ""
    echo "Next step: Convert to GIF"
    echo "  nix develop --command ./scripts/video_to_gif.sh $OUTPUT_FILE figures/sequence_${SEQUENCE_NAME}.gif"
else
    echo "❌ Recording failed - file not created"
    exit 1
fi
