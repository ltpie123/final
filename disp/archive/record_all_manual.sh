#!/usr/bin/env bash
# BATCH MANUAL RECORDING - Record all 3 sequences with manual input

cd "$(dirname "$0")"

cat << 'EOF'
🎬 MANUAL BATCH RECORDING
==========================

You'll record 3 sequences. For each one:
  1. Script counts down
  2. You TYPE the moves in Hyperspeedcube
  3. Recording auto-stops
  4. Script converts to GIF

SEQUENCES TO RECORD:
  1. FR_single - Type "FR" Enter (repeat 4 times, 25 sec)
  2. FO_FO     - Type "FO" Enter, "FO" Enter (repeat 4 times, 30 sec)
  3. FR_FR     - Type "FR" Enter, "FR" Enter (repeat 4 times, 30 sec)

MAKE SURE:
  ✓ Hyperspeedcube window is visible
  ✓ Animation speed is 0.25x (Settings > Animation > Speed)
  ✓ You're ready to type quickly!

EOF

read -p "Press Enter to start recording sequence 1/3 (FR_single)..."

echo ""
echo "========================================="
echo "SEQUENCE 1/3: FR_single"
echo "========================================="
./record_manual.sh FR_single 25

echo ""
echo "Converting to GIF..."
nix develop --command ./scripts/video_to_gif.sh recordings/FR_single.mp4 figures/sequence_FR_single.gif
echo ""

read -p "Press Enter for sequence 2/3 (FO_FO)..."

echo ""
echo "========================================="
echo "SEQUENCE 2/3: FO_FO"  
echo "========================================="
./record_manual.sh FO_FO 30

echo ""
echo "Converting to GIF..."
nix develop --command ./scripts/video_to_gif.sh recordings/FO_FO.mp4 figures/sequence_FO_FO.gif
echo ""

read -p "Press Enter for sequence 3/3 (FR_FR)..."

echo ""
echo "========================================="
echo "SEQUENCE 3/3: FR_FR"
echo "========================================="
./record_manual.sh FR_FR 30

echo ""
echo "Converting to GIF..."
nix develop --command ./scripts/video_to_gif.sh recordings/FR_FR.mp4 figures/sequence_FR_FR.gif

echo ""
echo "✅ ALL SEQUENCES RECORDED!"
echo ""
ls -lh figures/sequence_*.gif
echo ""
echo "View them:"
echo "  xdg-open figures/sequence_FR_single.gif"
echo "  xdg-open figures/sequence_FO_FO.gif"
echo "  xdg-open figures/sequence_FR_FR.gif"
