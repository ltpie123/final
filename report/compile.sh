#!/usr/bin/env bash
# Quick compile script using tectonic

cd "$(dirname "$0")"

echo "🔨 Compiling presentation with tectonic..."
tectonic presentation.tex

if [ -f presentation.pdf ]; then
    echo "✅ Success! presentation.pdf created ($(du -h presentation.pdf | cut -f1))"
    echo ""
    echo "View with: xdg-open presentation.pdf"
    echo "Or: evince presentation.pdf"
else
    echo "❌ Compilation failed!"
    echo "Run with: tectonic --keep-logs presentation.tex"
fi
