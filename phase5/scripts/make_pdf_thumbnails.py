#!/usr/bin/env python3
"""Render a PDF into paginated, approximately 100-dpi contact sheets.
Requires PyMuPDF and Pillow; never substitutes for full-resolution proofing."""
from pathlib import Path
import argparse
import math
import pymupdf
from PIL import Image, ImageDraw, ImageFont

parser = argparse.ArgumentParser()
parser.add_argument("pdf", type=Path)
parser.add_argument("outdir", type=Path)
parser.add_argument("--per-sheet", type=int, default=40)
parser.add_argument("--cols", type=int, default=5)
parser.add_argument("--dpi", type=int, default=100)
args = parser.parse_args()
if args.per_sheet < 1 or args.cols < 1 or args.dpi < 1:
    parser.error("--per-sheet, --cols, and --dpi must be positive")

doc = pymupdf.open(args.pdf)
args.outdir.mkdir(parents=True, exist_ok=True)
# A US-letter page at the selected DPI fills one tile without downsampling.
cell_w = round(612 * args.dpi / 72)
cell_h = round(792 * args.dpi / 72)
label_h = max(28, round(args.dpi * 0.30))
for start in range(0, len(doc), args.per_sheet):
    stop = min(start + args.per_sheet, len(doc))
    n = stop - start
    nrows = math.ceil(n / args.cols)
    sheet = Image.new("RGB", (args.cols * cell_w, nrows * (cell_h + label_h)), "white")
    draw = ImageDraw.Draw(sheet)
    for idx in range(start, stop):
        page = doc[idx]
        scale = args.dpi / 72
        pix = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), alpha=False)
        image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        image.thumbnail((cell_w - 8, cell_h - 8), Image.Resampling.LANCZOS)
        local = idx - start
        tile_x = (local % args.cols) * cell_w
        tile_y = (local // args.cols) * (cell_h + label_h)
        x = tile_x + (cell_w - image.width) // 2
        y = tile_y + (cell_h - image.height) // 2
        sheet.paste(image, (x, y))
        label = f"Page {idx + 1:03d} | {len(page.get_text().strip())} chars"
        draw.text((tile_x + 8, tile_y + cell_h + 3), label, fill="black")
    name = f"pages-{start + 1:03d}-{stop:03d}.png"
    sheet.save(args.outdir / name, optimize=True)
    print(args.outdir / name)
print(f"pages={len(doc)}; dpi={args.dpi}; pages/sheet<={args.per_sheet}; contact sheets={math.ceil(len(doc) / args.per_sheet)}")
