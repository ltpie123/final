#!/bin/bash
# Analyze all JSON results and create summary

cd "$(dirname "$0")/.."

echo "=== Analysis of All Results ==="
echo ""

# Check if jq is available
if ! command -v jq &> /dev/null; then
    echo "jq not found. Showing simple summary instead."
    echo ""
    echo "Single Move Orders:"
    for f in results_order_*.json; do
        [ -f "$f" ] || continue
        period=$(grep -o '"period":[0-9]*' "$f" | cut -d: -f2)
        moves=$(grep -o '"move_sequence":\[[^]]*\]' "$f" | sed 's/.*\[\(.*\)\].*/\1/' | tr -d '"')
        echo "  $moves: period $period"
    done

    echo ""
    echo "Top 10 Longest Periods (2-move):"
    for f in results_2mov_*.json; do
        [ -f "$f" ] || continue
        period=$(grep -o '"period":[0-9]*' "$f" | cut -d: -f2)
        moves=$(grep -o '"move_sequence":\[[^]]*\]' "$f" | sed 's/.*\[\(.*\)\].*/\1/' | tr -d '"' | sed 's/,/ → /g')
        [ -n "$period" ] && echo "$period|$moves"
    done | sort -rn | head -10 | awk -F'|' '{printf "  %6d: %s\n", $1, $2}'

    exit 0
fi

echo "Single Move Orders:"
echo "==================="
for f in results_order_*.json; do
    [ -f "$f" ] || continue
    jq -r '"\(.move_sequence | join(",")): period \(.period // "N/A")"' "$f" | sed 's/^/  /'
done | sort

echo ""
echo "2-Move Sequences (sorted by period):"
echo "====================================="
for f in results_2mov_*.json; do
    [ -f "$f" ] || continue
    jq -r '"\(.period // 999999)|\(.move_sequence | join(" → "))"' "$f"
done | sort -rn | head -20 | awk -F'|' '{printf "%6s | %s\n", $1, $2}' | sed 's/^/  /'

echo ""
echo "3-Move Sequences (sorted by period):"
echo "====================================="
for f in results_3mov_*.json; do
    [ -f "$f" ] || continue
    jq -r '"\(.period // 999999)|\(.move_sequence | join(" → "))"' "$f"
done | sort -rn | head -10 | awk -F'|' '{printf "%6s | %s\n", $1, $2}' | sed 's/^/  /'

echo ""
echo "4-Move Sequences (sorted by period):"
echo "====================================="
for f in results_4mov_*.json; do
    [ -f "$f" ] || continue
    jq -r '"\(.period // 999999)|\(.move_sequence | join(" → "))"' "$f"
done | sort -rn | head -10 | awk -F'|' '{printf "%6s | %s\n", $1, $2}' | sed 's/^/  /'

echo ""
echo "Commutator Results:"
echo "==================="
for f in results_comm_*.json; do
    [ -f "$f" ] || continue
    jq -r '"\(.move_sequence | join(",")): period \(.period // "N/A")"' "$f" | sed 's/^/  /'
done | sort