# disp/ Organization Complete ✓

## What Changed

### Archived
- 15 experimental shell scripts → `archive/`
- 4 redundant documentation files → `archive/docs/`

### Active Files (Clean!)

**Main Scripts:**
- `automate_recording.py` - Automated recording with pyautogui ⭐
- `test_simple.py` - Quick test to verify automation works
- `generate_hsc_logs.py` - Generate .hsc log files
- `plot_all.m` - Generate all statistical plots

**Octave Plotting:**
- `plot_*.m` - Individual plotting functions (7 files)

**Documentation:**
- `README.md` - Main documentation
- `RECORDING_GUIDE.md` - Complete recording workflow
- `QUICK_RECORD.md` - Quick reference

**Utilities:**
- `scripts/video_to_gif.sh` - MP4 to GIF conversion
- `sequences_to_record.txt` - Sequence checklist

**Config:**
- `pyproject.toml` + `uv.lock` - Python dependencies
- `flake.nix` + `flake.lock` - Nix environment

## Next Steps

### 1. Test Automation

```bash
cd disp
uv run python3 test_simple.py
```

Watch Hyperspeedcube window - does the cube move when it types FR and UF?

### 2a. If YES - Run Full Automation

```bash
uv run python3 automate_recording.py
```

### 2b. If NO - Manual Recording

See `RECORDING_GUIDE.md` for manual process.

### 3. Convert Videos to GIFs

```bash
./scripts/video_to_gif.sh recordings/FR_single.mp4 figures/sequence_FR_single.gif 640 20
./scripts/video_to_gif.sh recordings/FO_FO.mp4 figures/sequence_FO_FO.gif 640 20
./scripts/video_to_gif.sh recordings/FR_FR.mp4 figures/sequence_FR_FR.gif 640 20
```

### 4. Verify Output

```bash
ls -lh figures/sequence_*.gif
```

Each GIF should be < 5MB and show the cube animating.

## File Count

- Before: 15 shell scripts, 7 markdown files (messy!)
- After: 4 Python scripts, 3 markdown files, 1 utility script (clean!)
