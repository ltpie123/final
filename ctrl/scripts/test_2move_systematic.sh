#!/bin/bash
# Systematic 2-move testing - Phase 4 of systematic exploration

cd "$(dirname "$0")/.."

echo "=== Systematic 2-Move Period Testing ==="
echo "Testing representative combinations to map the period landscape"
echo ""

# Representative move set (8 moves covering different dimensional subspaces)
moves=(FR UF OR UO RL FU OL UD)

mkdir -p ../obsv/logs

total_tests=$((${#moves[@]} * ${#moves[@]}))
completed=0

for m1 in "${moves[@]}"; do
    for m2 in "${moves[@]}"; do
        completed=$((completed + 1))
        echo "[$completed/$total_tests] Testing: $m1,$m2"

        cargo run --release -- \
            --puzzle ft_hypercube:3 \
            --moves "$m1,$m2" \
            --max-iterations 50000 \
            --output "results_2mov_${m1}_${m2}.json" \
            > "../obsv/logs/${m1}_${m2}.log" 2>&1 &

        # Limit to 4 parallel jobs to avoid overwhelming the system
        if [ $(jobs -r | wc -l) -ge 4 ]; then
            wait -n
        fi
    done
done

wait

echo ""
echo "=== All Tests Complete ==="
echo "Results saved to results_2mov_*.json"
echo "Logs saved to logs/*.log"
