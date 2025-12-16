#!/bin/bash
# Systematic exploration of move sequences

echo "=== Testing 3-move sequences ==="
cargo run --release -- --puzzle ft_hypercube:3 --moves FR,UF,OR --max-iterations 50000 --output results_3mov_FRUFOR.json &
cargo run --release -- --puzzle ft_hypercube:3 --moves FR,OR,UF --max-iterations 50000 --output results_3mov_FRORUF.json &
cargo run --release -- --puzzle ft_hypercube:3 --moves UF,FR,OR --max-iterations 50000 --output results_3mov_UFFRОР.json &

echo "=== Testing repeated moves ==="
cargo run --release -- --puzzle ft_hypercube:3 --moves FR,FR,UF --max-iterations 50000 --output results_3mov_FFRUF.json &
cargo run --release -- --puzzle ft_hypercube:3 --moves FR,UF,UF --max-iterations 50000 --output results_3mov_FRUFF.json &

echo "=== Testing 4-move sequences ==="
cargo run --release -- --puzzle ft_hypercube:3 --moves FR,UF,OR,RO --max-iterations 50000 --output results_4mov_FRUFORRO.json &

wait
echo "All explorations complete!"
