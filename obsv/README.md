# obsv - Analysis & Observation

Statistical analysis and data observation module for the 4D hypercube trajectory exploration.

## Purpose

- **Data Storage**: All experimental results from `ctrl/` are stored in `obsv/logs/`
- **Analysis Tools**: Python scripts for statistical analysis and visualization
- **Environment**: Python virtual environment managed by `uv`

## Structure

```
obsv/
├── logs/              # All JSON results and logs from ctrl experiments (gitignored)
├── analyze.py         # Statistical analysis of trajectory data
├── generate_report.sh # Generate markdown summary reports
├── pyproject.toml     # Python dependencies
└── main.py            # Main entry point (if needed)
```

## Usage

### Running Analysis

```bash
# From project root
python3 obsv/analyze.py

# Or use uv
cd obsv
uv run analyze.py
```

### Generating Reports

```bash
cd obsv
bash generate_report.sh
```

## Data Flow

1. `ctrl/` scripts run experiments → generate JSON/logs → output to `obsv/logs/`
2. `obsv/` scripts read from `obsv/logs/` → analyze → produce reports

## Python Environment

This module uses `uv` for Python package management. The virtual environment and dependencies are managed automatically.