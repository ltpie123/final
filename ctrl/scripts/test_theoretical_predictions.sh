#!/bin/bash
# Test theoretical predictions about move periods

cd "$(dirname "$0")/.."
mkdir -p logs

echo "=== Testing Theoretical Predictions ==="
echo ""

echo "Prediction 1: Period(A,B) = Period(B,A)?"
echo "Testing commutivity of period calculation..."
echo ""

# Test pairs in both orders
test_pairs=(
    "FR,UF:UF,FR"
    "OR,UF:UF,OR"
    "FR,OR:OR,FR"
)

for pair_combo in "${test_pairs[@]}"; do
    pair1=$(echo $pair_combo | cut -d: -f1)
    pair2=$(echo $pair_combo | cut -d: -f2)

    echo "Testing: $pair1 vs $pair2"

    # Test first order
    cargo run --release -- \
        --puzzle ft_hypercube:3 \
        --moves "$pair1" \
        --max-iterations 20000 \
        --output "logs/results_order_test_$(echo $pair1 | tr ',' '_').json" \
        > "logs/order_test_$(echo $pair1 | tr ',' '_').log" 2>&1

    # Test second order
    cargo run --release -- \
        --puzzle ft_hypercube:3 \
        --moves "$pair2" \
        --max-iterations 20000 \
        --output "logs/results_order_test_$(echo $pair2 | tr ',' '_').json" \
        > "logs/order_test_$(echo $pair2 | tr ',' '_').log" 2>&1

    # Compare
    p1=$(python3 -c "import json; print(json.load(open('logs/results_order_test_$(echo $pair1 | tr ',' '_').json')).get('period', '?'))")
    p2=$(python3 -c "import json; print(json.load(open('logs/results_order_test_$(echo $pair2 | tr ',' '_').json')).get('period', '?'))")

    if [ "$p1" = "$p2" ]; then
        echo "  ✓ Period($pair1) = Period($pair2) = $p1"
    else
        echo "  ✗ Period($pair1) = $p1, Period($pair2) = $p2"
    fi
    echo ""
done

echo ""
echo "Prediction 2: Period(A,B) = Period(A',B)? (Inverse moves)"
echo "Testing if using inverse affects period..."
echo ""

# Test with inverses
echo "Testing FR,UF vs FR',UF"
cargo run --release -- \
    --puzzle ft_hypercube:3 \
    --moves "FR',UF" \
    --max-iterations 20000 \
    --output "logs/results_inverse_test_FRp_UF.json" \
    > "logs/inverse_test_FRp_UF.log" 2>&1

p_normal=$(python3 -c "import json; print(json.load(open('results_2mov_FR_UF.json')).get('period', '?'))" 2>/dev/null || echo "?")
p_inverse=$(python3 -c "import json; print(json.load(open('logs/results_inverse_test_FRp_UF.json')).get('period', '?'))")

echo "  Period(FR,UF) = $p_normal"
echo "  Period(FR',UF) = $p_inverse"

if [ "$p_normal" = "$p_inverse" ]; then
    echo "  ✓ Inverse doesn't change period"
else
    echo "  ✗ Inverse DOES change period"
fi

echo ""
echo "Prediction 3: Period((A,B)^n) relationships"
echo "Testing repeated sequences..."
echo ""

# Test (FR,UF)^2
echo "Testing FR,UF,FR,UF (square of FR,UF)"
cargo run --release -- \
    --puzzle ft_hypercube:3 \
    --moves "FR,UF,FR,UF" \
    --max-iterations 20000 \
    --output "logs/results_square_FRUF.json" \
    > "logs/square_FRUF.log" 2>&1

p_base=$(python3 -c "import json; print(json.load(open('results_2mov_FR_UF.json')).get('period', '?'))" 2>/dev/null || echo "?")
p_square=$(python3 -c "import json; print(json.load(open('logs/results_square_FRUF.json')).get('period', '?'))")

echo "  Period(FR,UF) = $p_base"
echo "  Period((FR,UF)^2) = $p_square"
echo "  Ratio: $(python3 -c "print($p_base/$p_square if $p_square != 0 else '?')" 2>/dev/null || echo '?')"

echo ""
echo "=== Predictions Summary ==="
echo "Results logged to results_*_test_*.json"