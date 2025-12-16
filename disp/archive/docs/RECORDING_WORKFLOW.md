# Quick Recording Workflow

## Step 1: Launch Hyperspeedcube (in Terminal 1)

```bash
cd disp
./launch_hyperspeedcube.sh
```

This will:
- Load Nix environment with X11 libraries
- Launch Hyperspeedcube GUI
- Window should appear on your screen

**Wait for the GUI to fully load** (may have startup dialogs/welcome screen)

## Step 2: Set Up Puzzle in Hyperspeedcube

In the GUI:
1. Dismiss any startup/welcome dialogs
2. Load 3^4 puzzle if not default (File > Open Puzzle > 3^4)
3. Press **Ctrl+R** to reset to solved state
4. **Settings > Animation > Speed: 0.25x** (important - slow enough to see)
5. **Settings > Stickers > High Contrast** (optional, looks better)
6. Rotate view to show 4D structure clearly

## Step 3: Record a Sequence (in Terminal 2)

Open a **new terminal** and run:

```bash
cd disp
./record_sequence.sh SEQUENCE_NAME DURATION
```

**Examples:**

```bash
# FR single move (baseline) - 10 seconds
./record_sequence.sh FR_single 10

# FO→FO (most chaotic) - 12 seconds  
./record_sequence.sh FO_FO 12

# FR→FR (self-composition) - 12 seconds
./record_sequence.sh FR_FR 12
```

**What happens:**
1. 3-second countdown
2. Recording starts
3. You type moves in Hyperspeedcube (Terminal 1 window)
4. Recording stops after duration
5. Video saved to `recordings/`

## Step 4: Perform Moves in Hyperspeedcube

When you see "🔴 RECORDING NOW":

**For FR single:**
- Type: `FR` (Enter)
- Wait ~2 seconds (for animation at 0.25x)
- Type: `FR` (Enter)
- Wait ~2 seconds
- Repeat 2-3 more times

**For FO→FO:**
- Type: `FO` (Enter), `FO` (Enter)
- Wait ~2 seconds
- Type: `FO` (Enter), `FO` (Enter)
- Repeat 2-3 more times

**For FR→FR:**
- Type: `FR` (Enter), `FR` (Enter)
- Wait ~2 seconds
- Type: `FR` (Enter), `FR` (Enter)
- Repeat 2-3 more times

## Step 5: Convert to GIF

After recording:

```bash
# In Terminal 2 (or new terminal 3)
cd disp
./scripts/video_to_gif.sh recordings/FR_single.mp4 figures/sequence_FR_single.gif

# Check size
ls -lh figures/sequence_FR_single.gif
```

## Step 6: Repeat for Other Sequences

**TIER 1 Priority (3 sequences):**
1. ✅ FR_single → `sequence_FR_single.gif`
2. ⬜ FO_FO → `sequence_FO_FO.gif`
3. ⬜ FR_FR → `sequence_FR_FR.gif`

**TIER 2 (if time permits):**
4. ⬜ RO_RO → `sequence_RO_RO.gif`
5. ⬜ FR_UF → `sequence_FR_UF.gif` (warning: 10,080 period, just show a few moves)

## Troubleshooting

**"Hyperspeedcube window doesn't appear"**
- Check if process is running: `ps aux | grep hyperspeedcube`
- Try running without Nix: `cd ../hyper/Hyperspeedcube && ./target/release/hyperspeedcube`
- Check DISPLAY: `echo $DISPLAY` (should show :0 or similar)

**"Recording captures wrong window"**
- Make Hyperspeedcube window active/visible
- Script auto-detects window, but may need to be in focus

**"Moves go too fast"**
- Reduce animation speed further: Settings > Animation > 0.1x
- Increase recording duration: `./record_sequence.sh NAME 20`

**"GIF too large"**
- Reduce size: `./scripts/video_to_gif.sh input.mp4 output.gif 320 10`

## Quick Reference

**Terminal 1:** Hyperspeedcube GUI
```bash
cd disp
./launch_hyperspeedcube.sh
```

**Terminal 2:** Recording
```bash
cd disp
./record_sequence.sh SEQUENCE_NAME DURATION
```

**Terminal 2/3:** Conversion
```bash
cd disp
./scripts/video_to_gif.sh recordings/FILE.mp4 figures/sequence_NAME.gif
```

---

**Total time for 3 sequences:** ~30 minutes (10 min each including setup/conversion)
