# Final Recording Steps

## One-Time Setup

### 1. Set Keybinds to RKT
**This is critical!** Without RKT keybinds, typing move names won't work.

1. Launch Hyperspeedcube manually:
   ```bash
   hyperspeedcube
   ```

2. In the UI:
   - Click **"Settings"** tab (left sidebar)
   - Scroll to **"Puzzle"** section
   - Find **"Keybinds"** dropdown
   - Change from "Default" → **"RKT"**

3. Close Hyperspeedcube - settings are saved

**Why?** RKT keybinds map keyboard letters to move notation. Default keybinds don't support typing "FR", "UF", etc.

## Recording

Now that keybinds are set:

```bash
cd disp
./record_with_nix.sh
```

This will:
1. Launch Hyperspeedcube (with RKT keybinds from config)
2. Record FR_single sequence
3. Record FO_FO sequence  
4. Record FR_FR sequence
5. Save videos to `recordings/`

**During recording:**
- Keep Hyperspeedcube window visible
- Don't touch mouse/keyboard
- Takes ~2-3 minutes total

## Convert to GIFs

After recording completes:

```bash
cd disp
nix develop --command bash -c "
  ./scripts/video_to_gif.sh recordings/FR_single.mp4 figures/sequence_FR_single.gif 640 20
  ./scripts/video_to_gif.sh recordings/FO_FO.mp4 figures/sequence_FO_FO.gif 640 20
  ./scripts/video_to_gif.sh recordings/FR_FR.mp4 figures/sequence_FR_FR.gif 640 20
"
```

Or all at once:
```bash
cd disp
nix develop --command bash -c "
  for f in recordings/{FR_single,FO_FO,FR_FR}.mp4; do
    name=\$(basename \"\$f\" .mp4)
    ./scripts/video_to_gif.sh \"\$f\" \"figures/sequence_\$name.gif\" 640 20
  done
"
```

## Verify

```bash
ls -lh figures/sequence_*.gif
```

Each GIF should be < 5MB and show the cube animating.

## Troubleshooting

**"Moves not executing"**
→ Check keybinds are set to RKT (step 1)

**"ffmpeg not found"**
→ Use `./record_with_nix.sh` not direct python

**"Window not found"**
→ Increase sleep time in script (line 52: `time.sleep(4)` → `time.sleep(8)`)

**Black video**
→ Check Hyperspeedcube window was visible during recording
