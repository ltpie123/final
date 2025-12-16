#!/usr/bin/env bash
# Start recording session with Nix environment

set -e

echo "🎬 Hyperspeedcube Recording Session"
echo "==================================="
echo ""
echo "Entering Nix development environment..."
echo "This provides: ffmpeg, gifsicle, xdotool, and X11 libraries"
echo ""
echo "Once in the shell, run:"
echo "  cd ../hyper/Hyperspeedcube"
echo "  ./target/release/hyperspeedcube &"
echo ""
echo "Then follow RECORDING_GUIDE.md for step-by-step instructions"
echo ""
echo "Priority sequences: See sequences_to_record.txt"
echo ""

cd "$(dirname "$0")"
exec nix develop
