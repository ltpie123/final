#!/usr/bin/env bash
# FINAL AUTOMATION - Using RTK keybinds (direct key press = twist)

set -e

SEQUENCE_NAME=${1:-"test"}
MOVES=${2:-"FR"}
CYCLES=${3:-4}

cd "$(dirname "$0")"

echo "🎬 AUTOMATED RECORDING (RTK Mode): $SEQUENCE_NAME"
echo "================================================="
echo "Moves: $MOVES"
echo "Cycles: $CYCLES"
echo ""
echo "⚠️  IMPORTANT: Hyperspeedcube must be in RTK keybind mode!"
echo ""

MOVE_COUNT=$(echo "$MOVES" | wc -w)
DURATION=$((CYCLES * MOVE_COUNT * 3 + 5))
OUTPUT_FILE="recordings/${SEQUENCE_NAME}.mp4"

nix develop --command bash << EOF
set -e

WINDOW_ID=\$(xdotool search --name "Hyperspeedcube" 2>/dev/null | head -1)

if [ -z "\$WINDOW_ID" ]; then
    echo "❌ Cannot find Hyperspeedcube window!"
    exit 1
fi

echo "✓ Found window: \$WINDOW_ID"
eval \$(xdotool getwindowgeometry --shell \$WINDOW_ID)
echo "✓ Geometry: \${WIDTH}x\${HEIGHT} at +\${X}+\${Y}"

# Focus window
echo "Focusing Hyperspeedcube..."
xdotool windowactivate \$WINDOW_ID
xdotool windowraise \$WINDOW_ID
sleep 1

# Click center to ensure input focus
CENTER_X=\$((X + WIDTH / 2))
CENTER_Y=\$((Y + HEIGHT / 2))
xdotool mousemove \$CENTER_X \$CENTER_Y
xdotool click 1
sleep 0.5

# Reset puzzle
echo "Resetting puzzle (Ctrl+R)..."
xdotool key ctrl+r
sleep 2

echo "🔴 STARTING RECORDING"
echo ""

# Start recording
ffmpeg -f x11grab -framerate 30 -video_size \${WIDTH}x\${HEIGHT} \\
    -i :0.0+\${X},\${Y} -t $DURATION -y $OUTPUT_FILE 2>&1 >/dev/null &
FFMPEG_PID=\$!

sleep 2

# Type moves WITHOUT Enter - each key press executes immediately in RTK mode
echo "Sending key presses (RTK mode - no Enter needed)..."
for ((cycle=1; cycle<=$CYCLES; cycle++)); do
    echo "  Cycle \$cycle/$CYCLES"
    for move in $MOVES; do
        echo "    → \$move"
        # Send each character as a single key press
        for ((i=0; i<\${#move}; i++)); do
            char="\${move:\$i:1}"
            case "\$char" in
                [A-Z]) xdotool key shift+\${char,,} ;;
                [a-z]) xdotool key \$char ;;
                *) xdotool key \$char ;;
            esac
            sleep 0.1  # Small delay between keypresses
        done
        sleep 2.5  # Wait for animation
    done
done

echo ""
echo "Waiting for recording to finish..."
wait \$FFMPEG_PID
echo "✅ Recording complete!"
EOF

if [ -f "$OUTPUT_FILE" ]; then
    echo ""
    ls -lh "$OUTPUT_FILE"
    echo ""
    echo "Next: Convert to GIF"
    echo "  nix develop --command ./scripts/video_to_gif.sh $OUTPUT_FILE figures/sequence_${SEQUENCE_NAME}.gif"
else
    echo "❌ Recording failed"
    exit 1
fi
