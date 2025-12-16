# Hyperspeedcube Recording Quick Start

## Step 1: Launch Hyperspeedcube

```bash
cd /home/hi/School/math538/final/hyper/Hyperspeedcube
./target/release/hyperspeedcube
```

## Step 2: Set Up the Puzzle

1. The 3×3×3×3 puzzle should load by default
2. Press **Ctrl+R** to reset to solved state
3. Adjust view:
   - Mouse drag: Rotate view
   - Mouse wheel: Zoom in/out
   - Get a good angle showing the 4D structure

## Step 3: Configure for Recording

### Recommended Settings:
- **View → Projection**: Schlegel or Stereographic (better 4D visualization)
- **View → Stickers → High Contrast**: ON (better visibility in video)
- **Settings → Animation Speed**: 0.25× (slow enough to see what's happening)

### Background:
- Choose solid color (Settings → Appearance → Background)
- Black or white works best

## Step 4: Record Your First Sequence (FO→FO)

### Option A: Using Screen Recorder (Recommended)

1. **Start your screen recorder** (OBS, SimpleScreenRecorder, or built-in):
   - Frame the Hyperspeedcube window
   - 30 fps, 1920×1080 or 1280×720

2. **Perform the moves**:
   - Type: `FO` (Front-Out move)
   - Wait for animation to complete
   - Type: `FO` again
   - Let it complete
   - Record 2-3 more full cycles (period is 4, so watch it return)

3. **Stop recording**

4. **Save video** as `recordings/FO_FO.mp4`

### Option B: Hyperspeedcube Macro (Advanced)

If you want automated recording:

1. Create `macros/FO_FO.hscm`:
   ```
   FO
   FO
   ```

2. `Macros → Load Macro → FO_FO.hscm`

3. Start screen recording

4. `Macros → Run` (or hotkey)

5. Stop recording when complete

## Step 5: Convert to GIF

```bash
cd /home/hi/School/math538/final/disp
./scripts/video_to_gif.sh recordings/FO_FO.mp4 figures/sequence_FO_FO.gif 480 15
```

## Priority Recording Order

### MUST RECORD (for presentation):
1. **FR** (single move) - trivial baseline
2. **FO→FO** - highest chaos (λ=6.093)
3. **FR→FR** - compare single vs composition

### Nice to have:
4. RO→RO
5. FR→UF (huge period)
6. FR→OR→UF

## Keyboard Shortcuts in Hyperspeedcube

- **Ctrl+R**: Reset puzzle to solved
- **Ctrl+Z**: Undo last move
- **Ctrl+Shift+Z**: Redo
- **Space**: Pause/resume animation
- **ESC**: Cancel current move

## Move Notation Reference

Type these moves directly in Hyperspeedcube:

```
FR = Front face, Right direction
FL = Front face, Left direction
FU = Front face, Up direction
FO = Front face, Out direction (4th dimension!)

RO = Right face, Out direction
OR = Out face, Right direction

(etc.)
```

## Troubleshooting

### Hyperspeedcube won't launch:
```bash
# Check if binary exists
ls -la target/release/hyperspeedcube

# If missing, rebuild:
cargo build --release
```

### Moves not working:
- Make sure puzzle window has focus
- Wait for current animation to finish
- Check caps lock is OFF

### Recording laggy:
- Reduce animation speed to 0.25×
- Record at lower resolution (720p)
- Close other applications

## File Organization

```
disp/
├── recordings/          # Raw MP4 videos go here
│   ├── FO_FO.mp4
│   ├── FR_single.mp4
│   └── FR_FR.mp4
├── figures/            # Converted GIFs go here
│   ├── sequence_FO_FO.gif
│   ├── sequence_FR_single.gif
│   └── sequence_FR_FR.gif
└── scripts/
    └── video_to_gif.sh # Conversion script
```

## Tips for Good Recordings

1. **Start from solved**: Always Ctrl+R before recording
2. **Record extras**: Better to have too much footage than too little
3. **Full cycles**: For chaotic sequences, show at least 2-3 full periods
4. **Steady cam**: Don't rotate the view during recording (do it before)
5. **Test first**: Do a test run without recording to verify the moves

## What Makes a Good Demo?

The goal is to SHOW the audience the difference between:
- **Trivial** (FR): Returns quickly, predictable
- **Chaotic** (FO→FO): Also returns (period 4) but the *trajectory* is wild

The GIF should make it OBVIOUS that something different is happening, even though both sequences are periodic!

## Ready?

Once Hyperspeedcube finishes building, you're ready to go!

Check build status:
```bash
ls -la ../hyper/Hyperspeedcube/target/release/hyperspeedcube
```

When it exists, launch and start recording!