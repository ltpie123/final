# SIMPLE RECORDING WORKFLOW
# Using Hyperspeedcube's Built-in Macros

## Created Macro Files

✅ `macros/FR_single.hscm` - FR move repeated 4 times
✅ `macros/FO_FO.hscm` - FO→FO repeated 4 times  
✅ `macros/FR_FR.hscm` - FR→FR repeated 4 times

## Recording Steps (For Each Sequence)

### 1. Load Macro in Hyperspeedcube

In Hyperspeedcube GUI:
- Click **Macros** menu (or press M key if that's the hotkey)
- Click **Load Macro** or **Open**
- Navigate to: `/home/hi/School/math538/final/disp/macros/`
- Select the macro file (e.g., `FR_single.hscm`)

### 2. Prepare for Recording

- Press **Ctrl+R** to reset puzzle to solved state
- Make sure animation speed is **0.25x** (Settings > Animation > Speed)
- Position window so it's fully visible

### 3. Start Recording

In a terminal:
```bash
cd /home/hi/School/math538/final/disp
./manual_record.sh FR_single 15
```

Wait for countdown (5 seconds)...

### 4. Play Macro When Recording Starts

When you see "🔴 RECORDING NOW":
- In Hyperspeedcube: Click **Play** button on the macro panel
- Or press the macro play hotkey (check Hyperspeedcube UI)
- Let it run through all moves
- Recording auto-stops after 15 seconds

### 5. Convert to GIF

```bash
nix develop --command ./scripts/video_to_gif.sh recordings/FR_single.mp4 figures/sequence_FR_single.gif
```

### 6. View Result

```bash
xdg-open figures/sequence_FR_single.gif
```

## All 3 Sequences

**Sequence 1: FR_single**
```bash
./manual_record.sh FR_single 15
# Load macros/FR_single.hscm, play macro
```

**Sequence 2: FO_FO**
```bash
./manual_record.sh FO_FO 20
# Load macros/FO_FO.hscm, play macro
```

**Sequence 3: FR_FR**
```bash
./manual_record.sh FR_FR 20
# Load macros/FR_FR.hscm, play macro
```

## Converting All at Once

After recording all 3:
```bash
cd /home/hi/School/math538/final/disp
nix develop --command bash -c '
for video in recordings/FR_single.mp4 recordings/FO_FO.mp4 recordings/FR_FR.mp4; do
    name=$(basename "$video" .mp4)
    ./scripts/video_to_gif.sh "$video" "figures/sequence_${name}.gif"
done
'
```

## Troubleshooting

**Can't find Macros menu?**
- Look for M hotkey in keybindings (Settings > Keybindings)
- Or right-click in UI to find macro options

**Macro doesn't load?**
- Check file format (plain text, one move per line)
- Verify move notation matches what Hyperspeedcube expects

**Moves too fast/slow?**
- Adjust animation speed in Settings > Animation > Speed
- Or adjust twist_duration in config file

---

**Total time: ~15 minutes for all 3 sequences**
