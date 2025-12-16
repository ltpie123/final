#!/usr/bin/env bash
# Debug script - check window and recording setup

echo "Window Diagnostic"
echo "================="

# Check if Hyperspeedcube is running
if pgrep -x "hyperspeedcube" > /dev/null; then
    echo "✓ Hyperspeedcube is running"
else
    echo "✗ Hyperspeedcube is NOT running"
    echo "  Launch it: hyperspeedcube &"
    exit 1
fi

# Find window
WINDOW_ID=$(xdotool search --name "Hyper" 2>/dev/null | head -1)
if [ -z "$WINDOW_ID" ]; then
    echo "✗ Cannot find Hyperspeedcube window"
    exit 1
fi

echo "✓ Found window ID: $WINDOW_ID"

# Get geometry
eval $(xdotool getwindowgeometry --shell $WINDOW_ID)
echo "  Position: ($X, $Y)"
echo "  Size: ${WIDTH}x${HEIGHT}"

# Check if window is visible/mapped
IS_MAPPED=$(xdotool getwindowgeometry $WINDOW_ID 2>&1 | grep -c "Mapped")
echo "  Mapped: $IS_MAPPED"

# Get screen dimensions
SCREEN_GEOM=$(xdpyinfo 2>/dev/null | grep dimensions | awk '{print $2}')
echo "  Screen: $SCREEN_GEOM"

# Check if window is on screen
if [ $X -lt 0 ] || [ $Y -lt 0 ]; then
    echo "⚠ Warning: Window position is negative (off-screen?)"
fi

echo ""
echo "Recording test command:"
echo "ffmpeg -f x11grab -framerate 30 -video_size ${WIDTH}x${HEIGHT} -i :0.0+${X},${Y} -t 5 test.mp4"
echo ""
echo "Try this manually and check if video is not black"
