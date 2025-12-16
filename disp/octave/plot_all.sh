#!/usr/bin/env bash
# Master script - generates all statistical plots

cd "$(dirname "$0")"

DATA_FILE="../obsv/logs/lyapunov_data.csv"

if [ ! -f "$DATA_FILE" ]; then
    echo "Error: Data file not found: $DATA_FILE"
    echo "Run obsv analysis first: cd ../obsv && uv run python scripts/run_lyapunov.py"
    exit 1
fi

mkdir -p figures

echo "Generating all plots from $DATA_FILE..."

octave --eval "
    plot_lyapunov_vs_length('$DATA_FILE', 'figures/lyapunov_vs_length.png');
    plot_period_vs_lambda('$DATA_FILE', 'figures/period_vs_lambda.png');
    plot_classification_pie('$DATA_FILE', 'figures/classification_pie.png');
    plot_top_sequences('$DATA_FILE', 'figures/top_chaotic_sequences.png', 10);
    plot_perturbation_histogram('$DATA_FILE', 'figures/perturbation_histogram.png');
    plot_divergence_correlation('$DATA_FILE', 'figures/divergence_correlation.png');
"

echo ""
echo "Done! Figures saved to figures/"
ls -lh figures/*.png
