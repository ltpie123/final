#!/bin/bash
# Test commutators [A,B] = A,B,A',B' - Phase 3 of systematic exploration

cd "$(dirname "$0")/.."
mkdir -p ../obsv/logs

echo "=== Commutator Analysis ==="
echo "Testing if key move pairs commute"
echo "Format: [A,B] = A,B,A',B'"
echo ""

# Key pairs to test
pairs=(
    "OF,OU"
    "FR,UF"
    "OR,OU"
    "FR,OR"
    "UF,OU"
    "FR,UO"
    "UF,OR"
)

for pair in "${pairs[@]}"; do
    m1=$(echo $pair | cut -d, -f1)
    m2=$(echo $pair | cut -d, -f2)

    echo "Testing commutator [$m1,$m2]"
    cargo run --release -- \
        --puzzle ft_hypercube:3 \
        --moves "$m1,$m2,${m1}',${m2}'" \
        --max-iterations 10000 \
        --output "../obsv/logs/results_comm_${m1}_${m2}.json" \
        > "../obsv/logs/comm_${m1}_${m2}.log" 2>&1

    # Extract summary from log
    grep -A 8 "Dynamical Systems Summary" "../obsv/logs/comm_${m1}_${m2}.log"
    echo "---"
done

echo ""
echo "=== Interpretation ==="
echo "Period 1: Moves commute perfectly"
echo "Period <10: Moves nearly commute"
echo "Period >100: Moves don't commute (high complexity expected)"