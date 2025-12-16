#!/usr/bin/env bash
cd "$(dirname "$0")"
echo "🎬 Starting automated recording with default keybinds..."
nix develop --command bash -c "uv run python3 final_record.py"
