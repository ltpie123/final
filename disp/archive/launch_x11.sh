#!/usr/bin/env bash
# Launch Hyperspeedcube with X11 backend (fixes Wayland library errors)

cd "$(dirname "$0")/../hyper/Hyperspeedcube"

echo "🎮 Launching Hyperspeedcube..."
echo "Session type: $XDG_SESSION_TYPE"
echo "Forcing X11 backend (avoids Wayland library issues)..."
echo ""

# Force X11 backend for winit (window library)
export WAYLAND_DISPLAY=""
export WINIT_UNIX_BACKEND=x11

# Use Vulkan for graphics
export WGPU_BACKEND=vulkan
export WGPU_POWER_PREF=high

echo "Starting Hyperspeedcube..."
./target/release/hyperspeedcube &
HYPER_PID=$!

echo "Process ID: $HYPER_PID"
echo ""
echo "Waiting for window to appear..."
sleep 3

if ps -p $HYPER_PID > /dev/null 2>&1; then
    echo "✅ Hyperspeedcube is running!"
    echo ""
    echo "Next steps:"
    echo "  1. In Hyperspeedcube window: Press Ctrl+R to reset puzzle"
    echo "  2. Settings > Animation Speed > 0.25x"
    echo "  3. Adjust view with mouse"
    echo ""
    echo "To record, open another terminal:"
    echo "  cd $(pwd)/../../disp"
    echo "  ./record_sequence.sh SEQUENCE_NAME DURATION"
    echo ""
    echo "Press Ctrl+C here to close Hyperspeedcube"
    wait $HYPER_PID
else
    echo "❌ Hyperspeedcube failed to start"
    echo ""
    echo "Check errors above or try:"
    echo "  WINIT_UNIX_BACKEND=x11 WGPU_BACKEND=gl ./target/release/hyperspeedcube"
fi
