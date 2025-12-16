# Recording Plan

## Sequences Organized by Category

### Basic Rotations (3 sequences)
Single moves, period 8, trivial dynamics:
- **FR_single**: FR × 2 cycles
- **UF_single**: UF × 2 cycles  
- **OR_single**: OR × 2 cycles

### Self-Compositions (2 sequences)
Extremely chaotic, period 4:
- **FR_FR**: FR → FR × 2 cycles (λ=5.94)
- **FO_FO**: FO → FO × 2 cycles (λ=6.09) ⭐ Most chaotic!

### Short Orbits (2 sequences)
Complex patterns, short periods:
- **OF_OU_OB_OD**: OF → OU → OB → OD × 2 cycles (λ=5.64, period 6)
- **FR_OR_FL_OL**: FR → OR → FL → OL × 2 cycles (λ=4.65, period 12)

### Interesting Pairs (2 sequences)
Long periods, high chaos:
- **FR_UF_short**: FR → UF × 1 cycle (period 10,080, λ=3.95)
- **FR_UO**: FR → UO × 1 cycle (period 840, λ=2.81)

## Recording Commands

**Record everything:**
```bash
./RECORD.sh all
```

**Record by category:**
```bash
./RECORD.sh basic
./RECORD.sh self_comp
./RECORD.sh short_orbits
./RECORD.sh interesting_pairs
```

**With custom delay:**
```bash
nix develop --command uv run python3 record_sequences.py --category all --delay 2.0
```

## Expected Output

9 sequences total:
- ~34 total moves recorded
- Estimated time: 2-3 minutes
- Output: `recordings/*.mp4`

## Convert to GIFs

```bash
cd disp
nix develop --command bash -c '
  for mp4 in recordings/*.mp4; do
    name=$(basename "$mp4" .mp4)
    ./scripts/video_to_gif.sh "$mp4" "figures/sequence_$name.gif" 640 20
  done
'
```

## Priority for Presentation

1. **FO_FO** - Most chaotic self-composition
2. **FR_single** - Baseline single rotation
3. **OF_OU_OB_OD** - Complex 4-move pattern
4. **FR_UF_short** - Sample of huge period sequence

These 4 show: baseline → self-composition → complex orbit → long period
