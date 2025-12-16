#!/bin/bash
# Test individual move orders - Phase 1 & 2 of systematic exploration

cd "$(dirname "$0")/.."
mkdir -p logs

echo "=== Testing Individual Move Orders ==="
echo "Finding the period of each basic move applied repeatedly"
echo ""

moves="OF OU OR OL FR UF UR FU RF RO UO FO"

for move in $moves; do
    echo "Testing move: $move"
    cargo run --release -- \
        --puzzle ft_hypercube:3 \
        --moves "$move" \
        --max-iterations 20 \
        --output "results_order_${move}.json" \
        > "logs/order_${move}.log" 2>&1

    # Extract summary from log
    grep -A 12 "Dynamical Systems Summary" "logs/order_${move}.log"
    echo "---"
done

echo ""
echo "=== Summary ==="
echo "Results saved to results_order_*.json"
echo "Logs saved to logs/order_*.log"