#!/bin/bash
# Automate Hyperspeedcube recording with xdotool
# Run from nix shell: nix develop
# Usage: ./scripts/automate_hyperspeedcube.sh 'FO FO' recordings/fo_fo.mp4 [duration]

set -e

SEQUENCE=$1
OUTPUT=$2
DURATION=${3:-15}  # Default 15 seconds

if [ -z "$SEQUENCE" ] || [ -z "$OUTPUT" ]; then
    echo "Usage: $0 'MOVE1 MOVE2' output.mp4 [duration]"
    echo "Example: $0 'FO FO' recordings/fo_fo.mp4 15"
    exit 1
fi

echo "🎬 Automating Hyperspeedcube recording"
echo "Sequence: $SEQUENCE"
echo "Output: $OUTPUT"
echo "Duration: ${DURATION}s"
echo ""

# Check if Hyperspeedcube is already running
if xdotool search --name "Hyperspeedcube" > /dev/null 2>&1; then
    echo "✓ Hyperspeedcube already running"
    WINDOW=$(xdotool search --name "Hyperspeedcube" | head -1)
    KILL_HSC=false
else
    echo "Starting Hyperspeedcube..."
    hyperspeedcube &
    HSC_PID=$!
    KILL_HSC=true
    sleep 4  # Wait for launch

    WINDOW=$(xdotool search --name "Hyperspeedcube" | head -1)
    if [ -z "$WINDOW" ]; then
        echo "❌ Error: Could not find Hyperspeedcube window"
        [ "$KILL_HSC" = true ] && kill $HSC_PID 2>/dev/null || true
        exit 1
    fi
    echo "✓ Hyperspeedcube launched (window: $WINDOW)"
fi

# Get window position and size
eval $(xdotool getwindowgeometry --shell $WINDOW)
echo "Window geometry: ${WIDTH}x${HEIGHT} at +${X}+${Y}"

# Focus and raise window
xdotool windowactivate --sync $WINDOW
xdotool windowraise $WINDOW
sleep 0.5

# Reset puzzle (Ctrl+R)
echo "Resetting puzzle..."
xdotool key --window $WINDOW ctrl+r
sleep 1.5

# Create output directory
mkdir -p "$(dirname "$OUTPUT")"

# Start recording
echo "▶ Recording for ${DURATION}s..."
ffmpeg -f x11grab -framerate 30 -video_size ${WIDTH}x${HEIGHT} \
    -i :0.0+${X},${Y} -t $DURATION -y "$OUTPUT" 2>/dev/null &
FFMPEG_PID=$!

sleep 1

# Type sequence (repeat to show multiple cycles)
IFS=' ' read -ra MOVES <<< "$SEQUENCE"
NUM_MOVES=${#MOVES[@]}
MOVE_DELAY=2.5  # Seconds per move

# Calculate how many repetitions we can fit
REPS=$((DURATION / (NUM_MOVES * MOVE_DELAY)))
REPS=$((REPS > 1 ? REPS : 2))  # At least 2 full cycles

echo "Performing $REPS cycles of ${NUM_MOVES}-move sequence..."

for ((cycle=0; cycle<$REPS; cycle++)); do
    for move in "${MOVES[@]}"; do
        xdotool type --window $WINDOW "$move"
        sleep $MOVE_DELAY
    done
done

# Wait for recording to finish
wait $FFMPEG_PID

# Clean up
if [ "$KILL_HSC" = true ]; then
    echo "Closing Hyperspeedcube..."
    kill $HSC_PID 2>/dev/null || true
fi

echo "✓ Recording complete: $OUTPUT"
echo ""

# Show file info
if [ -f "$OUTPUT" ]; then
    SIZE=$(du -h "$OUTPUT" | cut -f1)
    echo "File size: $SIZE"
    echo "Next: ./scripts/video_to_gif.sh $OUTPUT figures/sequence_$(echo $SEQUENCE | tr ' ' '_').gif"
fi