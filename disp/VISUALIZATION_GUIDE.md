# Hyperspeedcube Visualization Guide

Guide for creating GIFs and videos of 4D hypercube sequences for the final report.

## Prerequisites

### 1. Install Hyperspeedcube

The Hyperspeedcube source is already in `../hyper/Hyperspeedcube/`. Build it:

```bash
cd ../hyper/Hyperspeedcube
cargo build --release
```

Binary will be at: `target/release/hyperspeedcube`

Or download pre-built binary from: https://ajfarkas.dev/hyperspeedcube/

### 2. Install Screen Recording Software

**Linux (recommended)**:
```bash
# SimpleScreenRecorder - best for GIF conversion
sudo pacman -S simplescreenrecorder  # Arch
sudo apt install simplescreenrecorder  # Ubuntu/Debian

# Or use OBS Studio
sudo pacman -S obs-studio
```

**macOS**:
- Built-in: Cmd+Shift+5 for screen recording
- Or use OBS Studio: `brew install --cask obs`

**Windows**:
- Built-in: Win+G (Xbox Game Bar)
- Or OBS Studio

### 3. Install GIF Conversion Tools

```bash
# FFmpeg (for video → GIF conversion)
sudo pacman -S ffmpeg    # Arch
sudo apt install ffmpeg  # Ubuntu/Debian
brew install ffmpeg      # macOS

# Gifsicle (for GIF optimization)
sudo pacman -S gifsicle
sudo apt install gifsicle
brew install gifsicle
```

## Workflow

### Step 1: Launch Hyperspeedcube

```bash
cd ../hyper/Hyperspeedcube
./target/release/hyperspeedcube
```

Or if using downloaded binary:
```bash
./hyperspeedcube
```

### Step 2: Set Up Puzzle

1. **Select puzzle**: `File > Open Puzzle` → Select `3^4` (3x3x3x3 hypercube)
2. **Reset to solved state**: `Ctrl+R` or `Puzzle > Reset`
3. **Adjust view**:
   - Rotate to a good viewing angle
   - Adjust camera distance (mouse wheel)
   - Consider using "Projection: Perspective" for better 4D visualization

### Step 3: Record Sequence

#### Option A: Manual Recording (Recommended for Reports)

1. **Start screen recording** (SimpleScreenRecorder or OBS)
2. **Perform the move sequence** manually or via macro
3. **Stop recording**
4. **Convert to GIF** (see conversion section below)

#### Option B: Hyperspeedcube Macro System

Hyperspeedcube has a built-in macro system:

1. **Create macro file** (`.hscm` format):
   ```
   # Example: FR_UF.hscm
   FR
   UF
   ```

2. **Load and run**:
   - `Macros > Load Macro`
   - Select your `.hscm` file
   - Click "Run" or press hotkey

3. **Record while macro runs**

### Step 4: Convert Video to GIF

Use our helper script:

```bash
# Convert video to optimized GIF
./scripts/video_to_gif.sh input_video.mp4 output.gif

# Custom settings
./scripts/video_to_gif.sh input.mp4 output.gif 480 15
#                                                ^width ^fps
```

## Recommended Sequences to Visualize

Based on our Lyapunov analysis, these are the most interesting sequences:

### High Priority (Most Chaotic)
1. **FR → UF** (period: 10,080, high λ)
2. **FR → UF → OR** (period: 2,160)
3. **FR → UF → OR → RO** (period: 41,496, record!)

### Comparison (Regular Behavior)
4. **OF → OU** (period: 6, low λ)
5. **Single move: FR** (period: 4)

### File Naming Convention

Save GIFs as:
```
figures/sequence_FR_UF.gif           # FR → UF
figures/sequence_FR_UF_OR.gif        # FR → UF → OR
figures/sequence_OF_OU.gif           # OF → OU
figures/sequence_FR_UF_OR_RO.gif     # Record sequence
```

## GIF Optimization

Our conversion script automatically:
- Scales to reasonable size (480px default)
- Reduces framerate (15 fps default)
- Optimizes palette
- Compresses with Gifsicle

Target GIF size: < 5MB for easy inclusion in LaTeX/Markdown reports

## Recording Tips

### Camera Angles
- **4D projection**: Use "Schlegel" or "Stereographic" for clearer 4D structure
- **Lighting**: Enable "Stickers > High Contrast" for better visibility
- **Background**: Use solid color background (white or black)

### Move Speed
- **Slow down**: Settings > Animation > Speed (0.5x or 0.25x)
- This makes the GIFs more comprehensible

### Loop Points
- **Start from solved state**
- **End after complete cycle** if showing periodicity
- For chaotic sequences, show 2-3 full periods

### Resolution
- Record at **1920x1080** or **1280x720**
- Will be scaled down to ~480px width for GIFs

## Alternative: Static Images

If GIF file sizes are too large, use static images:

1. Take screenshot at key points in sequence
2. Use `montage` (ImageMagick) to create composite:

```bash
montage step1.png step2.png step3.png step4.png \
  -tile 4x1 -geometry +5+5 sequence_FR_UF_composite.png
```

## Troubleshooting

### Hyperspeedcube won't build
```bash
# Update Rust toolchain
rustup update
cd ../hyper/Hyperspeedcube
cargo clean
cargo build --release
```

### GIF too large
```bash
# Reduce size more aggressively
./scripts/video_to_gif.sh input.mp4 output.gif 320 10
#                                                ^smaller ^slower

# Or optimize existing GIF
gifsicle -O3 --colors 128 input.gif -o optimized.gif
```

### Video quality issues
- Use lossless recording (H.264 with high bitrate)
- Record at higher resolution, scale down later
- Use good lighting in Hyperspeedcube settings

## Integration with Report

### LaTeX

```latex
\begin{figure}[h]
    \centering
    \animategraphics[width=0.6\textwidth]{15}{figures/sequence_FR_UF}{}{}
    \caption{Trajectory of FR → UF sequence (period = 10,080)}
\end{figure}
```

### Markdown

```markdown
![FR → UF sequence](figures/sequence_FR_UF.gif)
```

## Resources

- **Hyperspeedcube docs**: https://dev.hypercubing.xyz/hsc/
- **Hypercubing community**: https://hypercubing.xyz/
- **Move notation**: See our project's `docs/notation.md`
