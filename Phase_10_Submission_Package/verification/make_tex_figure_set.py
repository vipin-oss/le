#!/usr/bin/env python3
"""Phase 10 - materialise the figure set the LaTeX source actually needs.

`tools/md_to_tex.py` used to write `\\includegraphics{../11_Figures/figN.png}`: a path that
climbs out of the manuscript folder. It works only when the whole repository layout travels
with the .tex file, which is exactly what a submission upload does not do, and it points at
the 200-dpi PNGs while Phase 9 produced 600-dpi and vector renditions.

This script gives the LaTeX source a self-contained figure folder:

    PAPER_PROJECT/13_Manuscript/figures/figN.pdf     (vector renditions from Phase 9)

If the Phase 9 renditions are not on disk (they are regenerable and the raster ones are
gitignored), it runs the exporter first. Nothing under 08_Experiments or 06_Source_Code is
touched, so the code freeze stays valid; the Markdown and the locally generated PDF keep
embedding the frozen 200-dpi PNGs, and only the .tex switches to the vector set. The script
prints the sha256 of every file it places so the folder can be compared with the deposit
manifest.
"""
import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUB = ROOT / 'PAPER_PROJECT' / '11_Figures' / 'submission'
FIGDIR = ROOT / 'PAPER_PROJECT' / '13_Manuscript' / 'figures'
EXPORTER = ROOT / 'Phase_09_Closeout' / 'verification' / 'export_submission_figures.py'
FROZEN_FIGS = ROOT / 'PAPER_PROJECT' / '11_Figures'


def ensure_renditions():
    have = sorted(SUB.glob('fig*.pdf'))
    if len(have) >= 8:
        return have
    print('vector renditions incomplete (%d) - running the Phase 9 exporter' % len(have))
    if not EXPORTER.exists():
        raise SystemExit('exporter missing: %s' % EXPORTER)
    r = subprocess.run([sys.executable, str(EXPORTER)], cwd=str(ROOT))
    if r.returncode:
        raise SystemExit('exporter failed (%d)' % r.returncode)
    return sorted(SUB.glob('fig*.pdf'))


def main():
    pdfs = ensure_renditions()
    FIGDIR.mkdir(exist_ok=True)
    placed = []
    for src in pdfs:
        dst = FIGDIR / src.name
        same = dst.exists() and hashlib.sha256(dst.read_bytes()).hexdigest() == \
            hashlib.sha256(src.read_bytes()).hexdigest()
        if not same:
            shutil.copyfile(src, dst)
            placed.append(dst)
        else:
            placed.append(dst)
    (FIGDIR / 'README.txt').write_text(
        'Figure set for the LaTeX source (FINAL_REVISED_MANUSCRIPT.tex).\n'
        'Vector renditions of the eight manuscript figures, exported by\n'
        'Phase_09_Closeout/verification/export_submission_figures.py from the frozen\n'
        '08_Experiments/make_figures.py, and copied here by\n'
        'Phase_10_Submission_Package/verification/make_tex_figure_set.py.\n\n'
        'tools/md_to_tex.py points \\graphicspath at this folder and includes the figures by\n'
        'name only, so the .tex file plus this folder compile on their own. The Markdown and\n'
        'the locally rendered preview PDF still use the frozen 200-dpi PNGs in 11_Figures/, so\n'
        'the provenance of the figures the reported numbers were read from is unchanged.\n'
        'If this folder is absent, md_to_tex.py falls back to the PNG paths automatically.\n')
    print('placed %d file(s) in PAPER_PROJECT/13_Manuscript/figures/:' % len(placed))
    for dst in sorted(FIGDIR.glob('fig*.pdf')):
        print('   %-24s %8d B  sha256 %s' % (dst.name, dst.stat().st_size,
                                             hashlib.sha256(dst.read_bytes()).hexdigest()[:16]))
    stems = sorted(p.stem for p in FIGDIR.glob('fig*.pdf'))
    need = sorted(p.stem for p in FROZEN_FIGS.glob('fig*.png'))
    if stems != need:
        print('PROBLEM: figure set %s does not match the manuscript figures %s' % (stems, need))
        return 1
    print('RESULT: OK - %d figures, names match the manuscript exactly' % len(stems))
    return 0


if __name__ == '__main__':
    sys.exit(main())
