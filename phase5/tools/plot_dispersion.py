#!/usr/bin/env python3
"""Generate a script-generated dispersion-relation figure (PDF + SVG) using only
the Python standard library (no matplotlib). Draws phase speed c/c0 versus
wave number k for three 1-D models treated in Section 7:

  classical  : c/c0 = 1                              (flat, Eq. 7.4 with xi = 0)
  non-local  : c/c0 = 1 / sqrt(1 + (xi k)^2)         (decreases to 0, Eq. 7.4)
  gradient   : c/c0 = sqrt(1 + (ell k)^2)            (increases, Eq. 7.3)

All curves are computed from the stated relations; none are hand-drawn.

Usage: python3 phase5/tools/plot_dispersion.py
Writes: phase5/master/figures/source/fig_dispersion.pdf
        phase5/master/figures/source/fig_dispersion.svg
"""
import math
import os

OUT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "master", "figures", "source", "fig_dispersion.pdf",
)

W, H = 612.0, 432.0
M_L, M_R, M_T, M_B = 72.0, 72.0, 54.0, 72.0
X0, Y0 = M_L, M_B
X1, Y1 = W - M_R, H - M_T
XMAX = 4.0
# Max gradient value at x=4: sqrt(1+(0.45*4)^2) = sqrt(4.24) ≈ 2.06.
# YMAX >= 1.05 * max to keep all curves inside the frame.
YMAX = 2.2

def px(x): return X0 + (x / XMAX) * (X1 - X0)
def py(y): return Y0 + (y / YMAX) * (Y1 - Y0)
def esc(s):
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")

ops = []
def wl(n):   ops.append(f"{n:.2f} w")
def rg(r,g,b): ops.append(f"{r:.3f} {g:.3f} {b:.3f} RG")
def m(x,y):  ops.append(f"{x:.2f} {y:.2f} m")
def l(x,y):  ops.append(f"{x:.2f} {y:.2f} l")
def s():     ops.append("S")
def fnt(size): ops.append(f"/F1 {size} Tf")
def td(x,y): ops.append(f"{x:.2f} {y:.2f} Td")
def tj(s):   ops.append(f"({esc(s)}) Tj")

# axes
wl(1.0); rg(0,0,0)
m(X0, Y0); l(X1, Y0); s()
m(X0, Y0); l(X0, Y1); s()
# x ticks and labels
for i in range(1, 5):
    x = px(i)
    m(x, Y0-5); l(x, Y0+5); s()
    td(x-7, Y0-19); fnt(8); tj(str(i)); fnt(10)
# y ticks and labels: positions and labels computed from the SAME values
# so tick spacing in coordinates matches tick spacing in values.
for i in range(0, 12):
    yval = YMAX * i / 11.0   # 0.0, 0.2, ..., 2.2  (12 ticks)
    m(X0-5, py(yval)); l(X0+5, py(yval)); s()
    td(X0-30, py(yval)-4); fnt(8); tj(f"{yval:.1f}"); fnt(10)

# x axis label
td(X0 + (X1-X0)/2 - 40, Y0-32); fnt(10); tj("wave number  k  (1/ell)"); fnt(10)
# y axis quantity label (horizontal, top-left inside plot)
td(X0+8, Y1-22); fnt(9); tj("phase speed  c / c0  (arrow up)"); fnt(10)

# curves
def curve(fn, color, width):
    rg(*color); wl(width)
    first = True
    for j in range(201):
        x = XMAX * j / 200.0
        y = fn(x)
        if first:
            m(px(x), py(y)); first = False
        else:
            l(px(x), py(y))
    s()

curve(lambda x: 1.0, (0,0,0), 1.2)
curve(lambda x: 1.0/math.sqrt(1.0+(1.0*x)**2), (0.6,0,0), 1.2)
curve(lambda x: math.sqrt(1.0+(0.45*x)**2), (0,0,0.6), 1.2)

# legend: top-left inside plot area, below the title, away from all curves.
# Classical curve is flat at c/c0=1 (mid-height). Non-local decreases toward
# bottom-right. Gradient increases toward top-right. Top-left corner is clear
# of all three curves at every x.
lx, ly = X0 + 10, Y1 - 62
rg(0,0,0); wl(1.0); m(lx+8, ly+7); l(lx+26, ly+7); s()
rg(0.6,0,0); m(lx+8, ly+1); l(lx+26, ly+1); s()
rg(0,0,0.6); m(lx+8, ly-5); l(lx+26, ly-5); s()
rg(0,0,0); fnt(9)
td(lx+32, ly+3); tj("classical  c/c0 = 1"); fnt(10)
td(lx+32, ly-3); tj("non-local  decreases to 0"); fnt(10)
td(lx+32, ly-9); tj("gradient   grows with k"); fnt(10)

# title
td(W/2-86, H-30); fnt(11); tj("Dispersion: phase speed vs wave number"); fnt(10)

content = "BT\n" + "\n".join(ops) + "\nET\n"
stream = content.encode("latin-1", "replace")
obj5 = f"5 0 obj\n<< /Length {len(stream)} >>\nstream\n".encode("latin-1") + stream + b"\nendstream\nendobj\n"

objects = [
    (1, "<< /Type /Catalog /Pages 2 0 R >>"),
    (2, "<< /Type /Pages /Kids [3 0 R] /Count 1 /MediaBox [0 0 612 432] >>"),
    (3, "<< /Type /Page /Parent 2 0 R /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>"),
    (4, "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"),
]
parts = [b"%PDF-1.4\n"]
offsets = {}
pos = len(parts[0])
for num, txt in objects:
    offsets[num] = pos
    parts.append((str(num)+" 0 obj\n"+txt+"\nendobj\n").encode("latin-1"))
    pos += len(parts[-1])
offsets[5] = pos
parts.append(obj5)
pos += len(obj5)
xref_pos = pos
parts.append(f"xref\n0 {len(objects)+1}\n".encode("latin-1"))
parts.append(b"0000000000 65535 f \n")
for num in [1,2,3,4,5]:
    parts.append(f"{offsets[num]:010d} 00000 n \n".encode("latin-1"))
parts.append(f"trailer\n<< /Size {len(objects)+1} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n".encode("latin-1"))

pdf = b"".join(parts)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "wb") as f:
    f.write(pdf)
print("wrote", OUT, len(pdf), "bytes")

# --- SVG twin (editable source) ---
svg_out = OUT.replace(".pdf", ".svg")
def esc_xml(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# SVG y-coordinate is inverted (y=0 at top). Invert PDF py() so that
# y=0 appears at the bottom and y=YMAX at the top, matching the PDF.
def spy(y): return H - py(y)

# Recompute curves for SVG
def c_classical(x): return 1.0
def c_nonlocal(x): return 1.0 / math.sqrt(1.0 + (1.0 * x) ** 2)
def c_gradient(x): return math.sqrt(1.0 + (0.45 * x) ** 2)

svg = []
svg.append('<?xml version="1.0" encoding="UTF-8"?>')
svg.append(f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">')
svg.append(f'<rect width="{W}" height="{H}" fill="white"/>')
# axes (SVG y inverted: bottom=H-Y0, top=H-Y1)
svg.append(f'<line x1="{X0}" y1="{H-Y0}" x2="{X1}" y2="{H-Y0}" stroke="black" stroke-width="1"/>')
svg.append(f'<line x1="{X0}" y1="{H-Y0}" x2="{X0}" y2="{H-Y1}" stroke="black" stroke-width="1"/>')
# ticks and labels x
for i in range(1, 5):
    x = px(i)
    svg.append(f'<line x1="{x}" y1="{H-Y0-5}" x2="{x}" y2="{H-Y0+5}" stroke="black" stroke-width="1"/>')
    svg.append(f'<text x="{x-6}" y="{H-Y0+22}" font-size="10" text-anchor="middle">{i}</text>')
# y ticks and labels: positions and labels from the SAME values
for i in range(0, 12):
    yval = YMAX * i / 11.0
    spy_y = spy(yval)
    svg.append(f'<line x1="{X0-5}" y1="{spy_y}" x2="{X0+5}" y2="{spy_y}" stroke="black" stroke-width="1"/>')
    svg.append(f'<text x="{X0-28}" y="{spy_y+3}" font-size="10" text-anchor="end">{yval:.1f}</text>')
# axis labels
svg.append(f'<text x="{X0+(X1-X0)/2}" y="{H-Y0+38}" font-size="11" text-anchor="middle">wave number  k  (1/ell)</text>')
svg.append(f'<text x="{X0+8}" y="{H-Y1-20}" font-size="10">phase speed  c / c0</text>')
# curves (polylines)
def points(fn):
    return " ".join(f"{px(XMAX*j/200.0):.2f},{spy(fn(XMAX*j/200.0)):.2f}" for j in range(201))
svg.append(f'<polyline points="{points(c_classical)}" fill="none" stroke="black" stroke-width="1.2"/>')
svg.append(f'<polyline points="{points(c_nonlocal)}" fill="none" stroke="rgb(153,0,0)" stroke-width="1.2"/>')
svg.append(f'<polyline points="{points(c_gradient)}" fill="none" stroke="rgb(0,0,153)" stroke-width="1.2"/>')
# legend: top-left inside plot area, matching PDF position
lx, ly = X0 + 10, Y1 - 62
svg.append(f'<line x1="{lx+8}" y1="{H-ly-7}" x2="{lx+26}" y2="{H-ly-7}" stroke="black" stroke-width="1"/>')
svg.append(f'<line x1="{lx+8}" y1="{H-ly-1}" x2="{lx+26}" y2="{H-ly-1}" stroke="rgb(153,0,0)" stroke-width="1"/>')
svg.append(f'<line x1="{lx+8}" y1="{H-ly+5}" x2="{lx+26}" y2="{H-ly+5}" stroke="rgb(0,0,153)" stroke-width="1"/>')
svg.append(f'<text x="{lx+32}" y="{H-ly-4}" font-size="10">classical  c/c0 = 1</text>')
svg.append(f'<text x="{lx+32}" y="{H-ly+4}" font-size="10">non-local  decreases to 0</text>')
svg.append(f'<text x="{lx+32}" y="{H-ly+12}" font-size="10">gradient   grows with k</text>')
# title
svg.append(f'<text x="{W/2}" y="{H-25}" font-size="12" text-anchor="middle">Dispersion: phase speed vs wave number</text>')
svg.append('</svg>')
with open(svg_out, "w") as f:
    f.write("\n".join(svg))
print("wrote", svg_out)

def obj(num, txt):
    return f"{num} 0 obj\n{txt}\nendobj\n"
