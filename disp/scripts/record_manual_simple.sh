#!/usr/bin/env bash
# Simple manual recording script
# Usage: ./record_manual_simple.sh <name> "<moves>" <cycles> <duration>
# Example: ./record_manual_simple.sh FR_single "F R" 8 24

set -e

if [ $# -lt 4 ]; then
    echo "Usage: $0 <name> '<moves>' <cycles> <duration>"
    echo "Example: $0 FR_single 'F R' 8 24"
    exit 1
fi

NAME="$1"
MOVES="$2"
CYCLES="$3"
DURATION="$4"

cd "$(dirname "$0")/.."

echo "📹 MANUAL RECORDING: $NAME"
echo "=========================================="
echo "Moves: $MOVES"
echo "Cycles: $CYCLES"
echo "Duration: ${DURATION}s"
echo ""
echo "⚠️  Make sure:"
echo "   - Hyperspeedcube window is VISIBLE"
echo "   - You're in RTK keybind mode"
echo "   - Window is focused and ready"
echo ""

OUTPUT="recordings/${NAME}.mp4"
mkdir -p recordings

# Get window info
WINDOW_ID=$(xdotool search --name "Hyperspeedcube" 2>/dev/null | head -1 || echo "")

if [ -z "$WINDOW_ID" ]; then
    echo "⚠️  Cannot detect Hyperspeedcube window automatically"
    echo "   You'll need to click it manually after countdown"
    read -p "Press Enter when window is ready..."
    
    # Record whole screen
    echo ""
    echo "🔴 Recording starts in:"
    for i in 3 2 1; do
        echo "   $i..."
        sleep 1
    done
    echo "   GO! Start typing: $MOVES (repeat $CYCLES times)"
    echo ""
    
    ffmpeg -f x11grab -framerate 30 -video_size 1920x1080 \
        -i :0.0 -t "$DURATION" -y "$OUTPUT" 2>&1 | grep -E "(frame=|error|Error)" || true
else
    echo "✓ Found window: $WINDOW_ID"
    eval $(xdotool getwindowgeometry --shell "$WINDOW_ID")
    echo "✓ Position: ${X},${Y}  Size: ${WIDTH}x${HEIGHT}"
    
    # Focus window
    xdotool windowactivate "$WINDOW_ID"
    xdotool windowraise "$WINDOW_ID"
    sleep 1
    
    # Reset puzzle
    echo "Resetting puzzle (Ctrl+R)..."
    xdotool key --window "$WINDOW_ID" ctrl+r
    sleep 2
    
    echo ""
    echo "🔴 Recording starts in:"
    for i in 3 2 1; do
        echo "   $i..."
        sleep 1
    done
    echo "   GO! Start typing: $MOVES (repeat $CYCLES times)"
    echo ""
    
    # Record just the window
    ffmpeg -f x11grab -framerate 30 -video_size "${WIDTH}x${HEIGHT}" \
        -i ":0.0+${X},${Y}" -t "$DURATION" -y "$OUTPUT" 2>&1 | grep -E "(frame=|error|Error)" || true
fi

echo ""
if [ -f "$OUTPUT" ] && [ -s "$OUTPUT" ]; then
    SIZE=$(du -h "$OUTPUT" | cut -f1)
    echo "✅ Recording complete: $OUTPUT ($SIZE)"
    echo ""
    echo "Verify with: ffplay $OUTPUT"
    echo "Convert to GIF: ./scripts/video_to_gif.sh $OUTPUT figures/sequence_${NAME}.gif"
else
    echo "❌ Recording failed or empty"
    exit 1
fi
