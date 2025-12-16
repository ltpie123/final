#!/bin/bash
# Test 5-move sequences attempting to beat current record (41,496)

cd "$(dirname "$0")/.."
mkdir -p logs

echo "=== Testing 5-Move Sequences ==="
echo "Current record: 41,496 (FR,UF,OR,RO)"
echo "Goal: Find period > 41,496"
echo ""

# Strategy: Maximize distinct planes and dimensional coverage
sequences=(
    "FR,UF,OR,RO,UO"  # Add 5th plane to winner
    "FR,UF,UR,FO,LU"  # All different axes
    "FR,UO,RL,UF,OR"  # Mix 3D/4D heavily
    "UF,OR,FR,UO,RL"  # Variation
    "FR,UF,OR,UO,RL"  # Different ordering
    "FR,UO,UF,OR,RO"  # Another ordering
)

completed=0
total=${#sequences[@]}

for seq in "${sequences[@]}"; do
    completed=$((completed + 1))
    seq_name=$(echo "$seq" | tr ',' '_')

    echo "[$completed/$total] Testing: $seq"

    cargo run --release -- \
        --puzzle ft_hypercube:3 \
        --moves "$seq" \
        --max-iterations 100000 \
        --output "logs/results_5mov_${seq_name}.json" \
        > "logs/5mov_${seq_name}.log" 2>&1 &

    # Limit parallel jobs
    if [ $(jobs -r | wc -l) -ge 4 ]; then
        wait -n
    fi
done

wait

echo ""
echo "=== Results ==="
for seq in "${sequences[@]}"; do
    seq_name=$(echo "$seq" | tr ',' '_')
    file="logs/results_5mov_${seq_name}.json"

    if [ -f "$file" ]; then
        period=$(python3 -c "import json; print(json.load(open('$file')).get('period', 'N/A'))" 2>/dev/null)
        states=$(python3 -c "import json; print(json.load(open('$file')).get('unique_states_visited', 'N/A'))" 2>/dev/null)
        echo "$seq: period=$period, states=$states"
    fi
done

echo ""
echo "Check logs/5mov_*.log for detailed output"
