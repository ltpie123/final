# Manual Recording Guide for Hypercube Sequences

## Setup
1. Launch Hyperspeedcube: `hyperspeedcube &`
2. Press F4 to load 3×3×3×3 puzzle
3. Start your screen recorder (SimpleScreenRecorder, OBS, etc.)
4. Focus the Hyperspeedcube window

## Key Bindings (Default Rubiks4D)
- **Grip keys** (hold): s=Front, e=Up, v=Outside, f=Right
- **Twist keys** (tap while holding grip): i=x, j=y, k=x', l=y', o=z, u=z'
- **Reset**: Ctrl+R
- **Load puzzle**: F4 (3×3×3×3)

## Move Execution
**Example: FR (Front→Right)**
1. Hold 's' (Front grip)
2. While holding, tap 'i' (x direction)
3. Release 's'
4. Wait 1-2 seconds for animation

**Example: UO (Up→Outside)**
1. Hold 'e' (Up grip)
2. While holding, tap 'o' (z direction)
3. Release 'e'

## Recommended Sequences for Presentation (demo_friendly)

### 1. FR_orbit_demo (Baseline)
- **Sequence**: FR × 16 times
- **Total moves**: 16
- **Why**: Shows 2 complete orbits (period 8), baseline regular behavior
- **How**:
  ```
  Hold 's', tap 'i', release
  (repeat 16 times)
  ```

### 2. FO_FO_demo (MOST CHAOTIC)
- **Sequence**: (FO, FO) × 8 iterations = 16 moves
- **Total moves**: 16
- **Why**: λ=6.09, highest chaos, 2 complete orbits
- **How**:
  ```
  Repeat 8 times:
    1. Hold 's', tap 'o', release  (FO)
    2. Hold 's', tap 'o', release  (FO)
  ```

### 3. OF_OU_OB_OD_demo (Complex Orbit)
- **Sequence**: (OF, OU, OB, OD) × 12 iterations = 48 moves
- **Total moves**: 48
- **Why**: 4-move pattern, λ=5.64, shows complex dynamics
- **How**:
  ```
  Repeat 12 times:
    1. Hold 'v', tap 'j', release  (OF)
    2. Hold 'v', tap 'o', release  (OU)
    3. Hold 'v', tap 'l', release  (OB)
    4. Hold 'v', tap 'u', release  (OD)
  ```

### 4. FR_UF_demo (Long Period Sample)
- **Sequence**: (FR, UF) × 15 iterations = 30 moves
- **Total moves**: 30
- **Why**: Period 10,080, λ=3.95, shows never repeating in short time
- **How**:
  ```
  Repeat 15 times:
    1. Hold 's', tap 'i', release  (FR)
    2. Hold 'e', tap 'j', release  (UF)
  ```

## Recording Checklist
- [ ] Reset puzzle (Ctrl+R) before each recording
- [ ] Start recording
- [ ] Execute sequence (use checklist/counter)
- [ ] Stop recording
- [ ] Save as: `sequence_NAME.mp4`
- [ ] Verify video shows cube movement (not black!)

## Complete Move Reference
| Move | Grip | Twist | Description |
|------|------|-------|-------------|
| FR   | s    | i     | Front → Right |
| FO   | s    | o     | Front → Outside |
| OF   | v    | j     | Outside → Front |
| OU   | v    | o     | Outside → Up |
| OB   | v    | l     | Outside → Back |
| OD   | v    | u     | Outside → Down |
| UF   | e    | j     | Up → Front |
| OR   | v    | i     | Outside → Right |
| FL   | s    | k     | Front → Left |
| OL   | v    | k     | Outside → Left |
| UO   | e    | o     | Up → Outside |

## Tips
- **Timing**: Wait for animation to complete (~1.5s per move)
- **Accuracy**: Use a physical counter or checklist
- **Quality**: Record at 1920×1080 if possible, 30fps minimum
- **Length**: 
  - FR_orbit: ~24 seconds
  - FO_FO: ~24 seconds  
  - OF_OU_OB_OD: ~72 seconds
  - FR_UF: ~45 seconds

## Converting to GIF
After recording:
```bash
cd disp
nix develop --command ./scripts/video_to_gif.sh \
  recordings/sequence_NAME.mp4 \
  figures/sequence_NAME.gif \
  640 \
  20
```

## Verification
Check that your GIF:
- Shows cube rotating
- Completes at least 1 full orbit (returns to solved state) for short sequences
- Is under 5MB file size
- Loops smoothly

## Quick Reference Card (Print This)
```
═══════════════════════════════════════════════════════
  HYPERCUBE RECORDING QUICK REFERENCE
═══════════════════════════════════════════════════════

SETUP: F4 (load puzzle), Ctrl+R (reset)

FR  = Hold 's', tap 'i'    |    OF  = Hold 'v', tap 'j'
FO  = Hold 's', tap 'o'    |    OU  = Hold 'v', tap 'o'
UF  = Hold 'e', tap 'j'    |    OB  = Hold 'v', tap 'l'
UO  = Hold 'e', tap 'o'    |    OD  = Hold 'v', tap 'u'

SEQUENCES:
  1. FR × 16                (baseline)
  2. (FO FO) × 8            (MOST CHAOTIC)
  3. (OF OU OB OD) × 12     (complex)
  4. (FR UF) × 15           (huge period)

Wait 1.5s between moves!
═══════════════════════════════════════════════════════
```
