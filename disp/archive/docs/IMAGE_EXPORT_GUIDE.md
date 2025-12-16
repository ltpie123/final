# Hyperspeedcube Image Export Workflow

## Overview
Use Hyperspeedcube's built-in Image Generator to export sequence frames from log files.

## Prerequisites
- Hyperspeedcube installed (`hyperspeedcube` command available)
- Log files generated (`logs/*.hsc`)

## Step-by-Step Process

### 1. Launch Hyperspeedcube
```bash
cd disp
hyperspeedcube &
```

### 2. Load Log File
1. **File → Open Log** (or `Ctrl+O`)
2. Navigate to `logs/` directory
3. Select one of:
   - `FR_single.hsc` - Baseline (8 moves)
   - `FO_FO.hsc` - Most chaotic (8 moves)
   - `FR_FR.hsc` - Self-composition (8 moves)

### 3. Navigate Through Sequence
- **Right Arrow** - Next move
- **Left Arrow** - Previous move  
- **Home** - Reset to start
- **Playback controls** - Auto-play at desired speed

### 4. Export Frames

#### Using Image Generator Tab:
1. Switch to **"Image Generator"** tab in the sidebar
2. **Set output directory**: Click "Browse" → Select `figures/` directory
3. **Set resolution**: 800×800 (or higher for presentation quality)
4. **Export each frame**:
   - Reset to start (Home key)
   - For each move (0-8):
     - Set filename: `FR_single_frame_00.png`, `FR_single_frame_01.png`, etc.
     - Click "Save Image"
     - Press Right Arrow to advance
     - Repeat

#### Frame Naming Convention:
```
{sequence_name}_frame_{nn}.png
```
Examples:
- `FR_single_frame_00.png` - Initial state
- `FR_single_frame_01.png` - After FR move #1
- `FR_single_frame_08.png` - After FR move #8 (complete cycle)

### 5. Convert Frames to GIF

Once all frames exported:

```bash
# Using ImageMagick
convert -delay 100 -loop 0 figures/FR_single_frame_*.png figures/sequence_FR_single.gif

# Or using ffmpeg
ffmpeg -framerate 2 -pattern_type glob -i 'figures/FR_single_frame_*.png' \
    -vf "scale=800:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \
    figures/sequence_FR_single.gif

# Optimize with gifsicle
gifsicle -O3 --colors 256 figures/sequence_FR_single.gif -o figures/sequence_FR_single_opt.gif
```

## Sequences to Export

| Sequence | Moves per cycle | Cycles | Total frames | Description |
|----------|----------------|--------|--------------|-------------|
| FR_single | 1 | 8 | 9 | Baseline (λ~0, period 8) |
| FO_FO | 2 | 4 | 9 | Most chaotic (λ=6.093) |
| FR_FR | 2 | 4 | 9 | Self-composition (λ=5.942) |

*Note: Total frames = total moves + 1 (initial state)*

## Automation Alternative

If manual export is too tedious, consider:

1. **Python + pyautogui**: Script the GUI interactions
2. **Xdotool + scripting**: Automate key presses and button clicks
3. **Rust custom tool**: Build using Hyperspeedcube crates (complex)

## Tips

- **Higher resolution** (1200×1200 or 1600×1600) for presentation
- **Consistent camera angle**: Don't rotate view between frames
- **Verify each frame**: Quick visual check before moving to next
- **Batch export**: Do all frames for one sequence before starting another
- **Naming is critical**: Frames must sort alphabetically for GIF creation

## Troubleshooting

**"No active puzzle" error:**
- Make sure log file is loaded
- Try selecting the puzzle view tab

**Wrong camera angle:**
- Reset view with `Ctrl+R`
- Use same angle for entire sequence

**Export directory issues:**
- Use absolute paths if relative paths fail
- Verify `figures/` directory exists

## Expected Output

After completing all three sequences:
```
figures/
├── FR_single_frame_00.png through 08.png
├── FO_FO_frame_00.png through 08.png
├── FR_FR_frame_00.png through 08.png
├── sequence_FR_single.gif
├── sequence_FO_FO.gif
└── sequence_FR_FR.gif
```

## Next Steps

1. Start with FR_single (simplest, 8 identical moves)
2. Verify GIF creation works
3. Proceed to FO_FO and FR_FR
4. Include GIFs in presentation slides
