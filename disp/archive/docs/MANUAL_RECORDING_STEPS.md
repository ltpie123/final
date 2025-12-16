# Manual Recording - Simple Steps

## Prerequisites
- Hyperspeedcube must be in **RTK keybind mode**
- Window should be visible and sized reasonably (not too small)

## Recording Process

### 1. Start Hyperspeedcube
```bash
cd disp
nix develop
hyperspeedcube &
```

### 2. Configure Keybinds
In Hyperspeedcube menu:
- Go to Settings → Keybinds
- Switch to **RTK mode** if not already

### 3. Record Each Sequence

Run this for each sequence:

```bash
# FR_single (8 repetitions, ~24 seconds)
./scripts/record_manual_simple.sh FR_single "F R" 8 24

# FO_FO (4 cycles, ~20 seconds) 
./scripts/record_manual_simple.sh FO_FO "F O" 4 20

# FR_FR (4 cycles, ~20 seconds)
./scripts/record_manual_simple.sh FR_FR "F R" 4 20
```

**What to do when script runs:**
1. Script will focus the Hyperspeedcube window
2. You'll see countdown: "Recording in 3...2...1..."
3. **Immediately start typing the moves** (just the letters, no Enter)
4. Type steadily, pausing ~2 seconds between each move
5. Repeat for the specified number of cycles
6. Recording stops automatically after the duration

### 4. Verify Recording
After each recording:
```bash
ls -lh recordings/SEQUENCE_NAME.mp4
# Should be >10KB, not tiny

# Play it to verify:
ffplay recordings/SEQUENCE_NAME.mp4
```

### 5. Convert to GIF
```bash
./scripts/video_to_gif.sh recordings/SEQUENCE_NAME.mp4 figures/sequence_SEQUENCE_NAME.gif
```

## Troubleshooting

**Recording is blank/black:**
- Hyperspeedcube window wasn't focused
- Window was minimized or hidden
- Re-run script, make sure window is visible

**Recording too short/too long:**
- Adjust the duration parameter (last number in command)
- Add 2-3 seconds buffer to be safe

**Moves not showing:**
- Make sure you're typing in the Hyperspeedcube window
- Verify RTK mode is active
- Type slowly and deliberately
