#!/usr/bin/env bash
#
# Convert video to optimized GIF for report figures
#
# Usage:
#   ./video_to_gif.sh input.mp4 output.gif [width] [fps]
#
# Examples:
#   ./video_to_gif.sh recording.mp4 sequence_FR_UF.gif
#   ./video_to_gif.sh recording.mp4 sequence.gif 640 20

set -euo pipefail

# Check dependencies
for cmd in ffmpeg gifsicle; do
    if ! command -v "$cmd" &> /dev/null; then
        echo "Error: $cmd is not installed"
        echo "Install with:"
        echo "  sudo pacman -S $cmd  # Arch"
        echo "  sudo apt install $cmd  # Ubuntu/Debian"
        echo "  brew install $cmd  # macOS"
        exit 1
    fi
done

# Parse arguments
INPUT="${1:-}"
OUTPUT="${2:-}"
WIDTH="${3:-480}"
FPS="${4:-15}"

if [[ -z "$INPUT" || -z "$OUTPUT" ]]; then
    echo "Usage: $0 <input_video> <output.gif> [width] [fps]"
    echo ""
    echo "Arguments:"
    echo "  input_video  Input video file (mp4, mov, avi, etc.)"
    echo "  output.gif   Output GIF file"
    echo "  width        Output width in pixels (default: 480)"
    echo "  fps          Framerate (default: 15)"
    echo ""
    echo "Examples:"
    echo "  $0 recording.mp4 sequence_FR_UF.gif"
    echo "  $0 recording.mp4 sequence.gif 640 20"
    exit 1
fi

if [[ ! -f "$INPUT" ]]; then
    echo "Error: Input file not found: $INPUT"
    exit 1
fi

# Create temp directory for palette
TMPDIR=$(mktemp -d)
trap "rm -rf $TMPDIR" EXIT

PALETTE="$TMPDIR/palette.png"

echo "Converting $INPUT to $OUTPUT..."
echo "  Width: ${WIDTH}px"
echo "  FPS: ${FPS}"

# Generate optimized palette
echo "  [1/3] Generating color palette..."
ffmpeg -v warning -i "$INPUT" -vf "fps=$FPS,scale=$WIDTH:-1:flags=lanczos,palettegen=stats_mode=diff" -y "$PALETTE"

# Generate GIF with palette
echo "  [2/3] Creating GIF..."
ffmpeg -v warning -i "$INPUT" -i "$PALETTE" -lavfi "fps=$FPS,scale=$WIDTH:-1:flags=lanczos [x]; [x][1:v] paletteuse=dither=bayer:bayer_scale=5:diff_mode=rectangle" -y "$OUTPUT"

# Optimize GIF
echo "  [3/3] Optimizing with gifsicle..."
gifsicle -O3 --colors 256 --lossy=80 -i "$OUTPUT" -o "${OUTPUT}.tmp"
mv "${OUTPUT}.tmp" "$OUTPUT"

# Show file size
SIZE=$(du -h "$OUTPUT" | cut -f1)
echo ""
echo "Done! Output: $OUTPUT ($SIZE)"

# Warning if > 5MB
SIZE_BYTES=$(stat -c%s "$OUTPUT" 2>/dev/null || stat -f%z "$OUTPUT")
if (( SIZE_BYTES > 5242880 )); then
    echo ""
    echo "Warning: GIF is larger than 5MB. Consider:"
    echo "  - Reducing width: $0 $INPUT $OUTPUT 320 $FPS"
    echo "  - Reducing FPS: $0 $INPUT $OUTPUT $WIDTH 10"
    echo "  - Trimming video length"
fi
