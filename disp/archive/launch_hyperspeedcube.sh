#!/usr/bin/env bash
# Launch Hyperspeedcube with proper GUI display

set -e

cd "$(dirname "$0")"

echo "🎮 Launching Hyperspeedcube..."
echo ""

# Check if binary exists
if [ ! -f "../hyper/Hyperspeedcube/target/release/hyperspeedcube" ]; then
    echo "❌ Hyperspeedcube binary not found!"
    echo "Build it first:"
    echo "  cd ../hyper/Hyperspeedcube"
    echo "  nix develop --command cargo build --release"
    exit 1
fi

# Launch with Nix environment (for proper libraries)
echo "Starting in Nix shell (for X11 libraries)..."
echo "Hyperspeedcube window should appear shortly..."
echo ""
echo "Once loaded:"
echo "  1. Set up 3^4 puzzle (should be default)"
echo "  2. Press Ctrl+R to reset to solved state"
echo "  3. Settings > Animation Speed > 0.25x"
echo "  4. Settings > Stickers > High Contrast"
echo ""
echo "Then use record_sequence.sh to capture!"
echo ""

cd ../hyper/Hyperspeedcube

# Try different WGPU backends (Vulkan is usually most stable)
echo "Attempting to launch with Vulkan backend..."
export WGPU_BACKEND=vulkan
export WGPU_POWER_PREF=high

# Try to launch
nix develop ../../disp --command ./target/release/hyperspeedcube

# If that fails, the script will show the error
# User can try manually with: WGPU_BACKEND=gl ./target/release/hyperspeedcube
