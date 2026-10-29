#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ ! -d "$ROOT/tools/node_modules" ]]; then
  echo "Install pinned renderer dependencies with: npm ci --prefix '$ROOT/tools'" >&2
  exit 2
fi
node "$ROOT/tools/render_svg_pdf.js" "$ROOT/figures/source" "$ROOT/master/figures/source"
# Keep the phase-level asset inventory mirrored for static checks and archives.
cp "$ROOT"/master/figures/source/*.pdf "$ROOT/figures/source/"
# The master folder is self-contained; keep its source SVG mirrors in sync too.
cp "$ROOT"/figures/source/*.svg "$ROOT/master/figures/source/"
