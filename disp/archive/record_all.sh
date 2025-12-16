#!/usr/bin/env bash
# Batch record all priority sequences automatically

set -e

cd "$(dirname "$0")"

echo "🎬 BATCH RECORDING ALL PRIORITY SEQUENCES"
echo "=========================================="
echo ""
echo "This will record 3 sequences automatically:"
echo "  1. FR_single (baseline)"
echo "  2. FO_FO (most chaotic)"
echo "  3. FR_FR (self-composition)"
echo ""
echo "Make sure:"
echo "  ✓ Hyperspeedcube is running: hyperspeedcube &"
echo "  ✓ Animation speed set to 0.25x (Settings > Animation > Speed)"
echo "  ✓ Window is visible on screen"
echo ""
read -p "Ready? Press Enter to start or Ctrl+C to cancel..."

echo ""
echo "================================"
echo "SEQUENCE 1/3: FR single (baseline)"
echo "================================"
./auto_record.sh FR_single "FR" 4

echo ""
echo "Waiting 3 seconds before next recording..."
sleep 3

echo ""
echo "================================"
echo "SEQUENCE 2/3: FO→FO (most chaotic)"
echo "================================"
./auto_record.sh FO_FO "FO FO" 4

echo ""
echo "Waiting 3 seconds before next recording..."
sleep 3

echo ""
echo "================================"
echo "SEQUENCE 3/3: FR→FR (self-composition)"
echo "================================"
./auto_record.sh FR_FR "FR FR" 4

echo ""
echo "✅ ALL RECORDINGS COMPLETE!"
echo ""
echo "Recordings saved:"
ls -lh recordings/*.mp4
echo ""
echo "================================"
echo "CONVERTING TO GIFS"
echo "================================"
echo ""

nix develop --command bash << 'EOF'
for video in recordings/FR_single.mp4 recordings/FO_FO.mp4 recordings/FR_FR.mp4; do
    basename=$(basename "$video" .mp4)
    echo "Converting: $basename..."
    ./scripts/video_to_gif.sh "$video" "figures/sequence_${basename}.gif"
done
EOF

echo ""
echo "✅ ALL DONE!"
echo ""
echo "GIFs created:"
ls -lh figures/sequence_*.gif
echo ""
echo "View them:"
echo "  xdg-open figures/sequence_FR_single.gif"
echo "  xdg-open figures/sequence_FO_FO.gif"
echo "  xdg-open figures/sequence_FR_FR.gif"
