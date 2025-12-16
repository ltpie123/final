# Quick Recording Guide - Automated Sequences

## The Hybrid Approach

✅ **Script automates**: Move execution (accurate, consistent, no counting)  
✅ **You control**: Screen recorder (SimpleScreenRecorder, OBS, whatever you trust)

## Quick Start

```bash
cd disp
./AUTOMATE.sh demo_friendly
```

## What Happens

1. Script launches Hyperspeedcube and loads 3×3×3×3
2. For each sequence:
   - Shows sequence info (name, moves, description)
   - **PROMPTS YOU** to start your screen recorder
   - You start recording, press ENTER
   - Script executes moves automatically (you watch)
   - **PROMPTS YOU** to stop recording
   - You stop recording, save file, press ENTER
3. Repeat for next sequence

## Recommended: demo_friendly Category

4 sequences perfect for presentation:

| Sequence | Moves | Duration | Why Include |
|----------|-------|----------|-------------|
| FR_orbit_demo | 16 | ~24s | Baseline (2 orbits) |
| FO_FO_demo | 16 | ~24s | Most chaotic (λ=6.09) |
| OF_OU_OB_OD_demo | 48 | ~72s | Complex 4-move orbit |
| FR_UF_demo | 30 | ~45s | Huge period (10,080) |

**Total recording time: ~3 minutes of video**

## All Categories

```bash
./AUTOMATE.sh basic_single        # Single moves (FR, UF, OR) × 8
./AUTOMATE.sh self_compositions   # FR→FR, FO→FO × 4 (most chaotic)
./AUTOMATE.sh short_complex       # 4-move orbits (24-48 moves)
./AUTOMATE.sh long_period_samples # FR→UF, FR→UO samples (50-60 moves)
./AUTOMATE.sh demo_friendly       # Best for presentation ⭐
```

## Screen Recorder Setup

### SimpleScreenRecorder (Recommended)
1. Launch: `simplescreenrecorder`
2. Continue → Continue
3. Record: Window → Select Hyperspeedcube window
4. Scale to: 1280×720 (good quality, reasonable size)
5. Frame rate: 30 fps
6. Container: MP4
7. Save to: `~/Videos/` (you'll move them later)
8. Continue → Continue
9. Keep window open, use Start/Stop button

### OBS Studio
1. Launch: `obs`
2. Scene → Add Source → Window Capture
3. Select Hyperspeedcube
4. Settings → Output → Recording Format: MP4
5. Keep OBS window open, use Start/Stop Recording

## During Recording

**You'll see:**
```
============================================================
📹 SEQUENCE: FO_FO_demo
   FO→FO × 2 orbits (most chaotic)
============================================================

🎬 ACTION REQUIRED:
   1. Start your screen recorder
   2. Focus the Hyperspeedcube window
   3. Press ENTER when ready to begin sequence execution

Press ENTER to start...
```

**Then:**
- Script counts down: 3... 2... 1... GO!
- Moves execute automatically (you watch the cube)
- Shows progress: `Cycle 1/8: FO FO [2/16]`
- When done, prompts you to stop recording

## After Each Recording

1. Stop your screen recorder
2. Save as: `recordings/<sequence_name>.mp4`
3. Press ENTER for next sequence

## File Naming

Match the sequence name exactly:
- `FR_orbit_demo.mp4`
- `FO_FO_demo.mp4`
- `OF_OU_OB_OD_demo.mp4`
- `FR_UF_demo.mp4`

## Converting to GIFs

After recording all sequences:

```bash
cd disp
nix develop --command bash -c '
  for mp4 in recordings/*.mp4; do
    name=$(basename "$mp4" .mp4)
    echo "Converting $name..."
    ./scripts/video_to_gif.sh "$mp4" "figures/sequence_$name.gif" 640 20
  done
'
```

**Parameters**: 640px width, 20fps (good quality, reasonable size)

## Verification

Check your GIFs:
```bash
ls -lh figures/sequence_*.gif
# Should be 2-8 MB each

# View them
firefox figures/sequence_FO_FO_demo.gif
```

## Troubleshooting

**"pyautogui not found"**
```bash
cd disp
uv sync  # Install Python dependencies
```

**"xdotool: command not found"**
```bash
# Should be available in nix shell, but if not:
nix-shell -p xdotool
```

**Moves not executing correctly**
- Make sure Hyperspeedcube window is focused
- Script clicks center of window automatically
- If still issues, manually click the cube before pressing ENTER

**Wrong keybinds**
- Check that Hyperspeedcube is using default "Rubiks4D" keybinds
- File: `~/.config/hyperspeedcube/hyperspeedcube.yaml`
- Look for `keybinds: Rubiks4D`

**Video quality poor**
- Record at higher resolution in your screen recorder settings
- Make sure to capture the full window
- Use 30fps minimum

## Tips

- **Dry run first**: Run with one sequence to test your workflow
- **Timing**: 1.5 seconds between moves (can edit in automate_sequences.py line 87)
- **Multiple takes**: Just re-run the category, no harm in recording twice
- **Focus**: Make sure no notifications pop up during recording

## Complete Workflow Example

```bash
# 1. Setup
cd disp
mkdir -p recordings figures

# 2. Launch screen recorder (SimpleScreenRecorder)
simplescreenrecorder &

# 3. Run automation
./AUTOMATE.sh demo_friendly

# 4. For each sequence:
#    - Start recording in SimpleScreenRecorder
#    - Press ENTER in terminal
#    - Watch it execute
#    - Stop recording, save to recordings/<name>.mp4
#    - Press ENTER for next

# 5. Convert all to GIFs
nix develop --command bash -c '
  for mp4 in recordings/*.mp4; do
    name=$(basename "$mp4" .mp4)
    ./scripts/video_to_gif.sh "$mp4" "figures/sequence_$name.gif" 640 20
  done
'

# 6. Done! Check figures/
ls -lh figures/sequence_*.gif
```

## Estimated Time

- Setup: 2 minutes
- Recording 4 sequences (demo_friendly): 5-10 minutes
- Converting to GIFs: 2 minutes
- **Total: ~15 minutes**

Much faster than manual execution, perfectly consistent!
