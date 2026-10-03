#!/usr/bin/env python3
"""Phase 9 - submission-grade figure renditions, without touching the frozen code.

`08_Experiments/make_figures.py` (a frozen file: it is one of the 27 entries of the code
freeze, and it produced the figures that the paper's numbers were read from) saves at
`savefig.dpi = 200`. Elsevier asks for half-tone artwork at 300 dpi or better, so the
submission set needs a higher-resolution rendition of the same eight figures.

Rather than edit the frozen script - which would silently change the provenance of the
figures the manuscript quotes - this wrapper *runs* the frozen script with two things
patched in memory:

  * the savefig dpi and the output directory, so every figure is additionally written to
    `PAPER_PROJECT/11_Figures/submission/` at 600 dpi PNG and 600 dpi TIFF;
  * a second savefig call per figure that writes a vector PDF rendition into the same
    folder.

No file under 08_Experiments or 11_Figures/fig*.png is modified, and the code freeze stays
valid (the script is unmodified; the new files are derived artifacts).

Prints a table of what was produced, with the dpi actually recorded in each file, so the
claim is checkable rather than asserted.
"""
import hashlib
import os
import re
import struct
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIG = ROOT / 'PAPER_PROJECT' / '11_Figures'
OUT = FIG / 'submission'
SRC_SCRIPT = ROOT / 'PAPER_PROJECT' / '08_Experiments' / 'make_figures.py'
DPI = 600


def png_dpi(path):
    """pHYs chunk -> effective dpi (unit 1 == metre)."""
    with open(path, 'rb') as fh:
        data = fh.read(4096)
    i = data.find(b'pHYs')
    if i < 0:
        return None
    w, h, unit = struct.unpack('>IIB', data[i + 4:i + 13])
    if unit != 1:
        return None
    return round(w * 0.0254), round(h * 0.0254)


def tiff_dpi(path):
    """minimal TIFF IFD scan for tag 282/283 (X/Y resolution, RATIONAL)."""
    with open(path, 'rb') as fh:
        b = fh.read(4_000_000)
    if b[:2] == b'II':
        end = '<'
    elif b[:2] == b'MM':
        end = '>'
    else:
        return None
    off = struct.unpack(end + 'I', b[4:8])[0]
    n = struct.unpack(end + 'H', b[off:off + 2])[0]
    out = {}
    for k in range(n):
        e = off + 2 + k * 12
        tag, typ, cnt = struct.unpack(end + 'HHI', b[e:e + 8])
        if tag in (282, 283) and typ == 5:
            voff = struct.unpack(end + 'I', b[e + 8:e + 12])[0]
            num, den = struct.unpack(end + 'II', b[voff:voff + 8])
            out[tag] = round(num / den) if den else None
    return out.get(282), out.get(283)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    src_hash = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in FIG.glob('fig*.png')}
    before = sorted(src_hash)
    if not before:
        print('no source figures found under %s' % FIG)
        return 1

    # Run the frozen generator with the patched savefig behaviour.
    drv = "\n".join([
        "import matplotlib",
        "matplotlib.use('Agg')",
        "import matplotlib.pyplot as plt",
        "from matplotlib.figure import Figure",
        "import os, sys",
        "OUT = %r" % str(OUT),
        "os.makedirs(OUT, exist_ok=True)",
        "_orig = Figure.savefig",
        "def _save(self, fname, *a, **kw):",
        "    p = _orig(self, fname, *a, **kw)",
        "    try:",
        "        base = os.path.splitext(os.path.basename(str(fname)))[0]",
        "        if base.startswith('fig'):",
        "            for ext in ('png', 'tiff', 'pdf'):",
        "                k2 = dict(kw); k2.pop('dpi', None)",
        "                if ext == 'tiff':",
        "                    k2['pil_kwargs'] = {'compression': 'tiff_lzw'}",
        "                _orig(self, os.path.join(OUT, base + '.' + ext), dpi=%d, **k2)" % DPI,
        "    except Exception as e:",
        "        sys.stderr.write('export note: %s\\n' % e)",
        "    return p",
        "Figure.savefig = _save",
        "src = %r" % str(SRC_SCRIPT),
        "g = {'__name__': '__main__', '__file__': src}",
        "exec(compile(open(src).read(), src, 'exec'), g)",
        "print('generator finished')",
    ])
    with tempfile.NamedTemporaryFile('w', suffix='.py', delete=False) as fh:
        fh.write(drv)
        driver = fh.name
    r = subprocess.run([sys.executable, driver], cwd=str(ROOT), capture_output=True, text=True)
    print(r.stdout.strip()[-400:])
    if r.returncode:
        print('generator failed:\n' + r.stderr[-1500:])
        return 1
    if 'export note' in r.stderr:
        print(r.stderr.strip()[-500:])

    # The generator writes its 200-dpi PNGs into 11_Figures/ as it always does, so those
    # tracked files are restored from git afterwards and the byte-identity of the frozen
    # figures is re-verified. The submission renditions live in 11_Figures/submission/,
    # which is untracked and therefore unaffected by the restore.
    subprocess.run(['git', 'checkout', '--', str(FIG.relative_to(ROOT))], cwd=str(ROOT),
                   capture_output=True, text=True)
    after = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in FIG.glob('fig*.png')}
    changed = [n for n in before if src_hash[n] != after.get(n)]
    if changed:
        print('!! the frozen figure PNGs are still modified after restore (%s)' % changed)
        return 2
    print('\nsource figures restored and byte-identical to the frozen 200-dpi PNGs: %d' % len(before))
    for n in before:
        p = FIG / n
        print('   %-22s %8d B  sha256 %s' % (n, p.stat().st_size,
                                             hashlib.sha256(p.read_bytes()).hexdigest()[:12]))
    print('\nsubmission renditions in 11_Figures/submission/:')
    rows, missing = [], []
    for base in [os.path.splitext(n)[0] for n in before]:
        for ext in ('png', 'tiff', 'pdf'):
            p = OUT / (base + '.' + ext)
            if not p.exists():
                missing.append(base + '.' + ext)
                continue
            dpi = None
            if ext == 'png':
                dpi = png_dpi(p)
                dpi = dpi[0] if dpi else None
            elif ext == 'tiff':
                dpi = tiff_dpi(p)
                dpi = dpi[0] if dpi and isinstance(dpi, tuple) else None
            rows.append((p.name, p.stat().st_size, dpi))
    for name, size, dpi in rows:
        print('   %-26s %9d B  dpi=%s' % (name, size, dpi if dpi else 'vector/n/a'))
    if missing:
        print('   MISSING: %s' % missing[:8])
    bad = [r for r in rows if r[0].endswith('.png') and (r[2] or 0) < 300]
    bad += [r for r in rows if r[0].endswith('.tiff') and (r[2] or 0) < 300]
    print('\nRESULT: %s' % ('OK - every raster rendition is >= 300 dpi and all three formats '
                           'exist for every figure' if not bad and not missing else
                           'PROBLEM: missing=%s low-dpi=%s' % (missing[:4], [b[0] for b in bad][:4])))
    (OUT / 'README.txt').write_text(
        'Submission renditions of the eight manuscript figures.\n'
        'Generated by Phase_09_Closeout/verification/export_submission_figures.py, which runs the\n'
        'frozen 08_Experiments/make_figures.py unchanged and re-saves each figure at %d dpi in PNG\n'
        'and TIFF plus a vector PDF. The 200-dpi PNGs in 11_Figures/ are the files the manuscript\n'
        'and its PDF preview embed; they are untouched, and the code freeze still describes them.\n'
        'Upload either the TIFF/PNG set (%d dpi) or the vector PDFs; do not mix formats between\n'
        'figures.\n' % (DPI, DPI))
    return 0


if __name__ == '__main__':
    sys.exit(main())
