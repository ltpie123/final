# Quick Recording Guide

## Install pyautogui (one-time)

```bash
pip install --user pyautogui python3-xlib
```

## Test keyboard automation (verify it works)

```bash
cd disp
python3 test_keyboard.py
```

Watch the Hyperspeedcube window - does it respond to keyboard input?

## Run automated recording

```bash
cd disp
python3 automate_recording.py
```

This will:
1. Launch Hyperspeedcube
2. Record all 3 priority sequences
3. Save videos to `recordings/`

## If automation doesn't work

Fall back to manual method:
1. Launch Hyperspeedcube manually
2. Start screen recorder (SimpleScreenRecorder or `ffmpeg -f x11grab...`)
3. Type moves manually: FR Enter, UF Enter, etc.
4. Stop recording
5. Convert to GIF

## Convert videos to GIFs

```bash
cd disp
./scripts/video_to_gif.sh recordings/FR_single.mp4 figures/sequence_FR_single.gif 640 20
./scripts/video_to_gif.sh recordings/FO_FO.mp4 figures/sequence_FO_FO.gif 640 20
./scripts/video_to_gif.sh recordings/FR_FR.mp4 figures/sequence_FR_FR.gif 640 20
```

## Check results

```bash
ls -lh figures/sequence_*.gif
```

Goal: Each GIF should be < 5MB and show the cube animating through the sequence.
