#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ ! -d "$ROOT/tools/node_modules" ]]; then
  echo "Install pinned renderer dependencies with: npm ci --prefix '$ROOT/tools'" >&2
  exit 2
fi
# Render SVGs to PDFs from the tracked master source directory.
node "$ROOT/tools/render_svg_pdf.js" "$ROOT/master/figures/source" "$ROOT/master/figures/source"
# Mirror assets to the phase-level inventory for static checks and archives (best-effort).
mkdir -p "$ROOT/figures/source"
cp "$ROOT"/master/figures/source/*.pdf "$ROOT/figures/source/" 2>/dev/null || true
cp "$ROOT"/figures/source/*.svg "$ROOT/master/figures/source/" 2>/dev/null || true
