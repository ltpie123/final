#!/usr/bin/env bash
# Test different ways of sending moves to Hyperspeedcube

cd "$(dirname "$0")"

nix develop --command bash << 'EOF'
set -e

WINDOW=$(xdotool search --name "Hyperspeedcube" | head -1)

if [ -z "$WINDOW" ]; then
    echo "❌ No Hyperspeedcube window found"
    exit 1
fi

echo "Found window: $WINDOW"
echo ""
echo "Testing different input methods..."
echo "Watch the Hyperspeedcube window to see which works!"
echo ""

# Method 1: Type characters directly
echo "Test 1: Type 'F' then 'R' separately"
xdotool windowactivate --sync $WINDOW
sleep 0.5
xdotool key --window $WINDOW f
sleep 0.2
xdotool key --window $WINDOW r
sleep 0.5
xdotool key --window $WINDOW Return
echo "  → Did the cube move?"
sleep 3

# Method 2: Type string all at once
echo "Test 2: Type 'FR' as string"
xdotool windowactivate --sync $WINDOW
sleep 0.5
xdotool type --window $WINDOW "FR"
sleep 0.5
xdotool key --window $WINDOW Return
echo "  → Did the cube move?"
sleep 3

# Method 3: Type with clearmodifiers (in case modifiers stuck)
echo "Test 3: Type with clearmodifiers"
xdotool windowactivate --sync $WINDOW
sleep 0.5
xdotool key --clearmodifiers --window $WINDOW shift+f shift+r
sleep 0.5
xdotool key --window $WINDOW Return
echo "  → Did the cube move?"
sleep 3

# Method 4: Just simulate keypresses for F, R, Enter
echo "Test 4: Individual keypresses F R Enter"
xdotool windowactivate --sync $WINDOW
sleep 0.5
xdotool key --window $WINDOW F R Return
echo "  → Did the cube move?"
sleep 3

echo ""
echo "Tests complete!"
echo "Which method worked? (if any)"
EOF
