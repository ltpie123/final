# How to Add Recording Keybinds

## Manual Method (Easiest - 2 minutes)

1. Open: `~/.config/hyperspeedcube/hyperspeedcube.yaml`

2. Find the line `Rubiks4D:` (around line 492)

3. Find the `active: Default` line

4. Add these keybinds to the Default preset's `keybinds:` list:

```yaml
  - sc: KeyF
    command:
      twist:
        axis: F
        direction: x
        layers: "1"
  
  - sc: KeyO
    command:
      twist:
        axis: F
        direction: w
        layers: "1"
```

5. Save the file

6. Test in Hyperspeedcube:
   - Press F key → should execute FR move
   - Press O key → should execute FO move

7. If it works, run: `./record_with_nix.sh`

## Quick Test

```bash
# After adding keybinds, test them:
cd disp
uv run python3 test_correct_keys.py
```

If F and O keys execute the moves correctly, automation will work!

## Alternative: Use Existing Keys

Check which keys in the current Default keybinds perform FR and FO moves, then update our automation script to use those keys instead.

From the config file, look at the Rubiks4D → Default keybinds and tell me which keys correspond to:
- FR (Front cell, rotate toward Right)
- FO (Front cell, rotate toward Outside)
