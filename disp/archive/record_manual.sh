#!/usr/bin/env bash
# FINAL MANUAL RECORDING - You type, we record
# This is the most reliable method

SEQUENCE_NAME=${1:-"test"}
DURATION=${2:-15}

cd "$(dirname "$0")"
OUTPUT="recordings/${SEQUENCE_NAME}.mp4"

cat << EOF

🎥 MANUAL RECORDING: $SEQUENCE_NAME
===================================

WHAT YOU NEED TO DO:
  1. Have Hyperspeedcube window open and visible
  2. Press Ctrl+R in Hyperspeedcube to reset puzzle NOW
  3. When countdown ends, TYPE MOVES in Hyperspeedcube window

SEQUENCE GUIDE:
  FR_single: Type "FR" Enter, wait 2 sec, repeat 4 times
  FO_FO:     Type "FO" Enter, "FO" Enter, wait 2 sec, repeat 4 times  
  FR_FR:     Type "FR" Enter, "FR" Enter, wait 2 sec, repeat 4 times

Animation speed should be 0.25x (Settings > Animation > Speed)

Recording will start in 5 seconds...

EOF

sleep 1; echo "5..."
sleep 1; echo "4..."
sleep 1; echo "3..."
sleep 1; echo "2..."
sleep 1; echo "1..."

echo ""
echo "🔴 RECORDING NOW - TYPE MOVES IN HYPERSPEEDCUBE!"
echo ""

nix develop --command ffmpeg -f x11grab -framerate 30 -video_size 1920x1080 \
    -i :0.0 -t "$DURATION" -y "$OUTPUT" 2>&1 | tail -1

echo ""
if [ -f "$OUTPUT" ]; then
    echo "✅ Recording saved: $OUTPUT"
    ls -lh "$OUTPUT"
else
    echo "❌ Recording failed"
fi
