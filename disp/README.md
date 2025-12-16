# disp/ - Visualization & Recording

Clean, organized visualization and GIF generation for the hypercube dynamics project.

## Structure

```
disp/
├── octave/              # Octave plotting scripts (*.m)
├── scripts/             # Utilities (video_to_gif.sh)
├── tests/               # Test scripts (development)
├── figures/             # Output: Plots & GIFs
├── recordings/          # Output: MP4 videos
├── logs/                # Input: .hsc log files
├── final_record.py      # Main recording script ⭐
├── RECORD_NOW.sh        # Quick launcher ⭐
├── generate_hsc_logs.py # Generate .hsc files
└── README.md
```

## Quick Start

### 1. Record Sequences

```bash
./RECORD_NOW.sh
```

Records 3 sequences using default Rubiks4D keybinds:
- FR_single (8 moves)
- FO_FO (8 moves)
- FR_FR (8 moves)

### 2. Convert to GIFs

```bash
nix develop --command bash -c "
  ./scripts/video_to_gif.sh recordings/FR_single.mp4 figures/sequence_FR_single.gif 640 20
  ./scripts/video_to_gif.sh recordings/FO_FO.mp4 figures/sequence_FO_FO.gif 640 20
  ./scripts/video_to_gif.sh recordings/FR_FR.mp4 figures/sequence_FR_FR.gif 640 20
"
```

### 3. Generate Statistical Plots

```bash
cd octave
octave plot_all.m
```

## Files

**Active:**
- `final_record.py` - Automated recording (pyautogui)
- `RECORD_NOW.sh` - Launcher with nix shell
- `generate_hsc_logs.py` - Generate .hsc log files
- `RECORDING_GUIDE.md` - Complete workflow guide
- `QUICK_RECORD.md` - Quick reference

**Config:**
- `pyproject.toml` - Python dependencies
- `flake.nix` - Nix environment

**Octave:**
- `octave/plot_all.m` - Master plotting script
- `octave/plot_*.m` - Individual plot functions

## Dependencies

Install via uv: `uv sync`
- pyautogui
- python3-xlib

Via Nix: `nix develop`
- ffmpeg, gifsicle, xdotool

## Default Keybinds

Uses Rubiks4D default keybinds from `~/.config/hyperspeedcube/hyperspeedcube.yaml`:

**Grip + Twist:**
- FR = Hold S (Front), press I (x direction)
- FO = Hold S (Front), press O (z direction)

## Output

- `figures/*.png` - Statistical plots
- `figures/sequence_*.gif` - Puzzle animations
- `recordings/*.mp4` - Raw screen captures
