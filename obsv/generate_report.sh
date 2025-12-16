#!/bin/bash
# Generate a comprehensive summary report

cd "$(dirname "$0")"

OUTPUT="ANALYSIS_REPORT.md"

cat > "$OUTPUT" << 'HEADER'
# Trajectory Analysis Report - 4D Hypercube

**Generated**: $(date)
**Puzzle**: 3×3×3×3 Hypercube (ft_hypercube:3)
**Tool**: CTRL v0.1.0

---

HEADER

echo "## Quick Statistics" >> "$OUTPUT"
echo "" >> "$OUTPUT"
python3 analyze.py >> "$OUTPUT"

echo "" >> "$OUTPUT"
echo "---" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "## All Results (sorted by period)" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "| Period | Length | Move Sequence | States | Time (s) |" >> "$OUTPUT"
echo "|--------|--------|---------------|--------|----------|" >> "$OUTPUT"

# Sort all results by period
for file in logs/results_*.json; do
    [ -f "$file" ] || continue
    python3 -c "
import json, sys
with open('$file') as f:
    d = json.load(f)
    moves = ' → '.join(d.get('move_sequence', []))
    period = d.get('period', 999999)
    length = len(d.get('move_sequence', []))
    states = d.get('unique_states_visited', 0)
    time = d.get('exploration_time_ms', 0) / 1000
    print(f'{period}|{length}|{moves}|{states}|{time:.2f}')
"
done | sort -rn | awk -F'|' '{
    printf "| %s | %s | %s | %s | %s |\n", $1, $2, $3, $4, $5
}' >> "$OUTPUT"

echo "" >> "$OUTPUT"
echo "---" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "Report saved to: $OUTPUT"
cat "$OUTPUT"