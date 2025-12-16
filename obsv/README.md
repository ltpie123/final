# obsv - Analysis & Observation

Statistical analysis and data observation module for the 4D hypercube trajectory exploration.

## Purpose

- **Data Storage**: All experimental results from `ctrl/` are stored in `obsv/logs/`
- **Statistical Analysis**: Comprehensive period analysis, prime factorization, performance metrics
- **Lyapunov Analysis**: Discrete Lyapunov exponents for chaos detection
- **Random Testing**: Chaos detection and strategy validation via random sequence testing
- **Environment**: Python virtual environment managed by `uv`

## Structure

```
obsv/
├── obsv/                   # Python package
│   ├── __init__.py        # Package exports
│   ├── ctrl_runner.py     # Interface to CTRL Rust program
│   ├── analyze.py         # Statistical analysis of trajectory data
│   ├── lyapunov.py        # Lyapunov exponent computation
│   └── random_test.py     # Random sequence testing suite
├── scripts/               # Executable scripts
│   ├── run_analysis.py    # Run statistical analysis
│   ├── run_lyapunov.py    # Run Lyapunov analysis
│   └── run_random_test.py # Run random testing suite
├── logs/                  # All JSON results and logs (gitignored)
├── generate_report.sh     # Generate markdown summary reports
├── pyproject.toml         # Python dependencies (managed by uv)
└── README.md              # This file
```

## Installation

```bash
cd obsv
uv sync  # Install dependencies
```

## Usage

### Statistical Analysis

Analyze all sequences in `logs/`:

```bash
uv run python scripts/run_analysis.py
```

Or use the package directly:

```bash
uv run python -m obsv.analyze
```

### Lyapunov Exponent Analysis

**What it does**: Computes discrete Lyapunov exponents to measure sensitivity to perturbations. High λ values indicate chaotic-like behavior (sequences where small changes cause large differences in period).

**Analyze existing sequences from logs**:

```bash
# Analyze first 5 sequences with 10 perturbations each
uv run python scripts/run_lyapunov.py --from-logs --max-sequences 5 --n-perturbations 10
```

**Analyze specific sequences**:

```bash
# Test the high-period FR,UF sequence
uv run python scripts/run_lyapunov.py --sequences FR,UF --n-perturbations 15
```

**Default demo** (analyzes 4 interesting sequences):

```bash
uv run python scripts/run_lyapunov.py
```

**Perturbation types**:
- `substitute`: Replace one move with a different move (default)
- `swap`: Swap two adjacent moves
- `insert`: Insert a random move
- `delete`: Delete a move

Example with different perturbation:

```bash
uv run python scripts/run_lyapunov.py --sequences FR,UF,OR --perturbation-type swap
```

**Output**:
- Individual results: `logs/lyapunov_*.json`
- Summary statistics: `logs/lyapunov_summary.json`
- CSV for Octave: `logs/lyapunov_data.csv`

### Random Sequence Testing

Test 100 random sequences and compare with strategic ones:

```bash
uv run python scripts/run_random_test.py --count 100 --compare
```

With chaos detection:

```bash
uv run python scripts/run_random_test.py --count 50 --compare --chaos
```

Options:
- `--count N`: Number of random sequences to test (default: 100)
- `--min-length N`: Minimum sequence length (default: 2)
- `--max-length N`: Maximum sequence length (default: 6)
- `--compare`: Compare random vs strategic sequences
- `--chaos`: Run chaos sensitivity analysis
- `--max-iterations N`: Max iterations per sequence (default: 50000)

### Generating Reports

```bash
bash generate_report.sh
```

Outputs: `ANALYSIS_REPORT.md`

## Data Flow

1. **ctrl/** scripts run experiments → generate JSON/logs → output to **obsv/logs/**
2. **obsv/** Python tools read from **obsv/logs/** → analyze → produce reports
3. **disp/** Octave scripts read CSV exports → create publication-quality visualizations

## Analysis Features

### Statistical Analysis (`analyze.py`)
- Overall statistics (min/max/mean/median periods)
- Grouping by sequence length with top 5 for each
- Period distribution histogram
- Most common periods (e.g., the "840 phenomenon")
- Prime factorization analysis
- Performance metrics (time per iteration)

### Lyapunov Analysis (`lyapunov.py`)
- **Discrete Lyapunov Exponent**: λ = (1/n) Σ log|Period(S_perturbed) / Period(S)|
- **Classification**: Sequences categorized as "chaotic" (λ > ln(2)), "sensitive" (λ > 0.1), or "regular"
- **Perturbation Strategies**: Multiple methods to test sensitivity
- **Batch Processing**: Analyze all sequences from logs
- **CSV Export**: Data ready for Octave visualization in `disp/`

**Interpretation**:
- λ > 0.69 (ln 2): Chaotic-like, high sensitivity to perturbations
- λ ≈ 0.1-0.69: Sensitive, moderate changes from perturbations
- λ < 0.1: Regular, stable behavior under perturbations

### Random Testing (`random_test.py`)
- **Period Distribution**: Statistical baseline from random sequences
- **Strategy Validation**: Compare strategic vs random selection (t-test)
- **Chaos Detection**: Sensitivity analysis via perturbation
- **Percentile Ranking**: Where does our record of 41,496 fall?

## Dependencies

- **numpy**: Numerical computations
- **scipy**: Statistical tests (t-test)

Managed by `uv` - no manual version pinning required.

## Mathematical Background

See `docs/mathematical_framework.md` Section 10.1 for the theoretical foundation of the discrete Lyapunov exponent.

The discrete Lyapunov exponent measures the average exponential divergence rate under perturbations, analogous to the continuous Lyapunov exponent in classical chaos theory.