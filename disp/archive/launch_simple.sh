#!/usr/bin/env bash
# Alternative launcher - tries different graphics backends

set -e

cd "$(dirname "$0")/../hyper/Hyperspeedcube"

echo "🎮 Launching Hyperspeedcube with graphics backend..."
echo ""

# Method 1: Try Vulkan (most compatible)
echo "Trying Vulkan backend..."
export WGPU_BACKEND=vulkan
export WGPU_POWER_PREF=high

./target/release/hyperspeedcube 2>&1 &
HYPER_PID=$!

sleep 3

# Check if it's still running
if ps -p $HYPER_PID > /dev/null; then
    echo "✅ Hyperspeedcube launched successfully with Vulkan!"
    echo "Process ID: $HYPER_PID"
    echo ""
    echo "Setup:"
    echo "  1. In Hyperspeedcube: Load 3^4 puzzle (should be default)"
    echo "  2. Press Ctrl+R to reset"
    echo "  3. Settings > Animation Speed > 0.25x"
    echo ""
    echo "To record, open another terminal and run:"
    echo "  cd disp && ./record_sequence.sh SEQUENCE_NAME DURATION"
    wait $HYPER_PID
else
    echo "❌ Vulkan backend failed"
    echo ""
    echo "Try manually with OpenGL:"
    echo "  cd hyper/Hyperspeedcube"
    echo "  WGPU_BACKEND=gl ./target/release/hyperspeedcube"
fi
