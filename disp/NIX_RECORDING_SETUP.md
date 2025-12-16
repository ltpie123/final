# Automated GIF Recording with Nix

Complete automated recording setup for Hyperspeedcube using Nix flakes.

## Prerequisites

- NixOS or Nix package manager with flakes enabled
- X11 display (not Wayland, due to xdotool limitations)

## Quick Start

### 1. Enter Nix Shell

```bash
cd /home/hi/School/math538/final/disp
nix develop
```

This will:
- Build Hyperspeedcube with all X11 dependencies
- Install xdotool, ffmpeg, gifsicle
- Set up proper library paths

### 2. Record All Priority Sequences (Automated)

```bash
./scripts/record_all_sequences.sh
```

This will automatically:
1. Launch Hyperspeedcube
2. Record 5 priority sequences (FR, FO→FO, FR→FR, RO→RO, FR→UF)
3. Convert all to optimized GIFs
4. Clean up

### 3. Record Individual Sequence

```bash
# Format: ./scripts/automate_hyperspeedcube.sh 'MOVES' output.mp4 [duration]

# Example: Record FO→FO for 15 seconds
./scripts/automate_hyperspeedcube.sh 'FO FO' recordings/fo_fo.mp4 15

# Convert to GIF
./scripts/video_to_gif.sh recordings/fo_fo.mp4 figures/sequence_FO_FO.gif
```

## Output

**Videos**: `recordings/*.mp4` (raw screen captures)
**GIFs**: `figures/sequence_*.gif` (optimized, ~5MB each)

## Priority Sequences

Based on Lyapunov analysis, these sequences demonstrate key findings:

1. **FR** (single) - Trivial baseline (λ=0.0, period=8)
2. **FO→FO** - Highest chaos (λ=6.093, period=4)
3. **FR→FR** - Self-composition chaos (λ=5.942, period=4)
4. **RO→RO** - O-face pattern (λ=5.850, period=4)
5. **FR→UF** - Long period (λ=3.949, period=10,080!)

## How It Works

### Automation Flow

```
1. Launch Hyperspeedcube
2. xdotool finds window
3. ffmpeg starts recording
4. xdotool types moves (Ctrl+R, then sequence)
5. ffmpeg stops after duration
6. Convert MP4 → GIF (optimized)
```

### Key Technologies

- **xdotool**: Simulates keyboard input to Hyperspeedcube
- **ffmpeg**: Screen capture (x11grab) and video encoding
- **gifsicle**: GIF optimization
- **Nix**: Reproducible build environment

## Troubleshooting

### Hyperspeedcube won't launch

```bash
# Check if X11 is available
echo $DISPLAY

# Try launching manually
hyperspeedcube
```

### xdotool can't find window

```bash
# List all windows
xdotool search --name ""

# Search specifically for Hyperspeedcube
xdotool search --name "Hyperspeedcube"
```

### Recording is black/corrupted

- Ensure Hyperspeedcube window is visible (not minimized)
- Check window geometry: `xdotool getwindowgeometry <window_id>`
- Try slower animation speed in Hyperspeedcube settings

### GIF file size too large

```bash
# More aggressive compression
./scripts/video_to_gif.sh input.mp4 output.gif 320 10
#                                                ^smaller ^slower
```

## Manual Recording (Alternative)

If automation fails, you can still record manually:

1. Launch: `hyperspeedcube`
2. Use screen recorder (SimpleScreenRecorder, OBS, etc.)
3. Manually perform moves
4. Convert with: `./scripts/video_to_gif.sh`

## Customization

### Add More Sequences

Edit `scripts/record_all_sequences.sh`:

```bash
SEQUENCES=(
    "FR|FR_single|10"
    "YOUR MOVES HERE|output_name|duration"
)
```

### Adjust Animation Speed

In Hyperspeedcube:
- Settings → Animation → Speed: 0.25× (slower)
- Settings → Animation → Speed: 0.5× (moderate)

### Change GIF Settings

Edit `scripts/video_to_gif.sh` defaults:
- Width: 480px (line with `WIDTH`)
- FPS: 15 (line with `FPS`)
- Optimize level: -O3 (gifsicle parameter)

## Clean Build

If something goes wrong with the Nix build:

```bash
nix flake update          # Update flake inputs
nix develop --rebuild     # Force rebuild
```

## Performance Notes

- Each sequence takes ~20-30 seconds to record
- Full batch (5 sequences) takes ~5 minutes
- GIF conversion adds ~1 minute per sequence
- Total automation time: ~10 minutes for all 5 sequences

## Next Steps

After generating GIFs:
1. Review in browser: `firefox figures/sequence_*.gif`
2. Include in presentation slides
3. Embed in LaTeX report

## Files Generated

```
disp/
├── recordings/
│   ├── FR_single.mp4         (~5MB, raw video)
│   ├── FO_FO.mp4
│   ├── FR_FR.mp4
│   ├── RO_RO.mp4
│   └── FR_UF.mp4
└── figures/
    ├── sequence_FR_single.gif     (~3-5MB, optimized)
    ├── sequence_FO_FO.gif
    ├── sequence_FR_FR.gif
    ├── sequence_RO_RO.gif
    └── sequence_FR_UF.gif
```

## Credits

- Hyperspeedcube: https://ajfarkas.dev/hyperspeedcube/
- xdotool: https://github.com/jordansissel/xdotool
- ffmpeg: https://ffmpeg.org/