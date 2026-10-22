#!/usr/bin/env python3
"""Render a PDF into paginated thumbnail contact sheets for visual review.
Requires PyMuPDF and Pillow; never substitutes for full-resolution proofing."""
from pathlib import Path
import argparse
import math
import pymupdf
from PIL import Image, ImageDraw, ImageFont

parser=argparse.ArgumentParser()
parser.add_argument('pdf', type=Path)
parser.add_argument('outdir', type=Path)
parser.add_argument('--per-sheet', type=int, default=24)
parser.add_argument('--cols', type=int, default=6)
args=parser.parse_args()
doc=pymupdf.open(args.pdf)
args.outdir.mkdir(parents=True, exist_ok=True)
cell_w, cell_h, label_h = 250, 315, 28
rows=math.ceil(args.per_sheet/args.cols)
for start in range(0,len(doc),args.per_sheet):
    stop=min(start+args.per_sheet,len(doc))
    n=stop-start; nrows=math.ceil(n/args.cols)
    sheet=Image.new('RGB',(args.cols*cell_w,nrows*(cell_h+label_h)),'white')
    draw=ImageDraw.Draw(sheet)
    for idx in range(start,stop):
        page=doc[idx]
        pix=page.get_pixmap(matrix=pymupdf.Matrix(.38,.38),alpha=False)
        image=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
        image.thumbnail((cell_w-12,cell_h-12))
        local=idx-start; x=(local%args.cols)*cell_w+(cell_w-image.width)//2
        y=(local//args.cols)*(cell_h+label_h)+(cell_h-image.height)//2
        sheet.paste(image,(x,y))
        label=f'p.{idx+1:03d} | {len(page.get_text().strip())} chars'
        draw.text(((local%args.cols)*cell_w+8,(local//args.cols)*(cell_h+label_h)+cell_h+4),label,fill='black')
    name=f'pages-{start+1:03d}-{stop:03d}.png'
    sheet.save(args.outdir/name)
    print(args.outdir/name)
print(f'pages={len(doc)}; contact sheets={math.ceil(len(doc)/args.per_sheet)}')
