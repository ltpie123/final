#!/usr/bin/env bash
# FINAL AUTOMATION ATTEMPT - Focus window then send global keystrokes

set -e

SEQUENCE_NAME=${1:-"test"}
MOVES=${2:-"FR"}
CYCLES=${3:-4}

cd "$(dirname "$0")"

echo "🎬 FINAL AUTOMATION ATTEMPT: $SEQUENCE_NAME"
echo "============================================"
echo "Moves: $MOVES"
echo "Cycles: $CYCLES"
echo ""

MOVE_COUNT=$(echo "$MOVES" | wc -w)
DURATION=$((CYCLES * MOVE_COUNT * 3 + 5))
OUTPUT_FILE="recordings/${SEQUENCE_NAME}.mp4"

nix develop --command bash << EOF
set -e

# Find and focus Hyperspeedcube
WINDOW_ID=\$(xdotool search --name "Hyperspeedcube" 2>/dev/null | head -1)

if [ -z "\$WINDOW_ID" ]; then
    echo "❌ Cannot find Hyperspeedcube window!"
    exit 1
fi

echo "✓ Found window: \$WINDOW_ID"

# Get window geometry
eval \$(xdotool getwindowgeometry --shell \$WINDOW_ID)
echo "✓ Geometry: \${WIDTH}x\${HEIGHT} at +\${X}+\${Y}"

# Focus and raise window
echo "Focusing Hyperspeedcube..."
xdotool windowactivate \$WINDOW_ID
xdotool windowraise \$WINDOW_ID
sleep 1

# Click on the window center to ensure it has input focus
CENTER_X=\$((X + WIDTH / 2))
CENTER_Y=\$((Y + HEIGHT / 2))
echo "Clicking center of window to ensure focus..."
xdotool mousemove \$CENTER_X \$CENTER_Y
xdotool click 1
sleep 0.5

# Reset puzzle
echo "Resetting puzzle (sending Ctrl+R globally)..."
xdotool key ctrl+r
sleep 2

echo ""
echo "🔴 STARTING RECORDING"
echo ""

# Start recording
ffmpeg -f x11grab -framerate 30 -video_size \${WIDTH}x\${HEIGHT} \\
    -i :0.0+\${X},\${Y} -t $DURATION -y $OUTPUT_FILE 2>&1 >/dev/null &
FFMPEG_PID=\$!

sleep 2

# Type moves WITHOUT window specification (go to focused window)
echo "Typing moves globally..."
for ((cycle=1; cycle<=$CYCLES; cycle++)); do
    echo "  Cycle \$cycle/$CYCLES"
    for move in $MOVES; do
        echo "    → \$move"
        # Send each character as a key press
        for ((i=0; i<\${#move}; i++)); do
            char="\${move:\$i:1}"
            # Convert to uppercase key name
            case "\$char" in
                [A-Z]) xdotool key shift+\${char,,} ;;  # Lowercase for key, use shift
                *) xdotool key \$char ;;
            esac
            sleep 0.05
        done
        xdotool key Return
        sleep 2.8
    done
done

echo "Waiting for recording to finish..."
wait \$FFMPEG_PID
echo "✅ Recording complete!"
EOF

if [ -f "$OUTPUT_FILE" ]; then
    echo ""
    ls -lh "$OUTPUT_FILE"
    echo ""
    echo "Check if cube moved! If YES, continue with:"
    echo "  nix develop --command ./scripts/video_to_gif.sh $OUTPUT_FILE figures/sequence_${SEQUENCE_NAME}.gif"
    echo ""
    echo "If NO, we'll go manual: ./record_all_manual.sh"
else
    echo "❌ Recording failed"
    exit 1
fi
