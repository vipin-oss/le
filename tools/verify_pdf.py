#!/usr/bin/env python3
"""verify_pdf.py — check that the generated manuscript PDF contains the whole .md source.

The PDF is produced by `tools/md_to_pdf.py` from `manuscript_IJHMT.md`.  This script is the
independent check that nothing was dropped or reordered on the way:

  1. every text unit of the markdown (paragraph, heading, caption, table row, reference)
     must appear in the PDF text, in the same order;
  2. no text may spill outside the text block (2 cm margins);
  3. the eight figures must sit on the same page as their caption, and the three display
     equations must be present as images.

Tolerated differences, by design:
  * a unit that is present in the PDF but out of the strict reading order (a paragraph that
    straddles a page break) is counted as 'out-of-order', not as missing — only text that is
    nowhere in the PDF is a failure, and a MISSING report now says after how many characters
    the PDF stops agreeing with the markdown, which is what makes such a line debuggable;
  * display equations are images (their LaTeX is not PDF text);
  * κ̄, σ̂, C̄, s̄ are drawn as composite glyph images, so the base letter is not text;
  * bullets are drawn as '•', table rules are drawn as lines;
  * the page number printed by the footer can be extracted in the middle of a run.

Needs: PyMuPDF (`pip3 install --break-system-packages pymupdf`).

Usage:
    python3 tools/verify_pdf.py [-p PAPER_PROJECT/13_Manuscript/manuscript_IJHMT.pdf]
                                [-m PAPER_PROJECT/13_Manuscript/manuscript_IJHMT.md]
"""
import argparse
import os
import re
import sys

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DEFAULT_PDF = os.path.join(ROOT, 'PAPER_PROJECT', '13_Manuscript', 'manuscript_IJHMT.pdf')
DEFAULT_MD = os.path.join(ROOT, 'PAPER_PROJECT', '13_Manuscript', 'manuscript_IJHMT.md')
RUNNING_TITLE = 'Cavity thermoelasticity in monoclinic beta-Ga2O3 — verified continuum study'
COMBINING_RE = re.compile('.[\u0302\u0303\u0304\u0306\u0307]')   # base + combining mark:
#   md_to_pdf draws these as one raster glyph, so neither base nor mark is PDF text


def norm(t):
    """markdown -> comparable character stream (markup removed)."""
    t = re.sub(r'!\[[^\]]*\]\([^)]*\)', ' ', t)          # figure links
    for _ in range(4):
        t = re.sub(r'[_^]\{([^{}]*)\}', r'\1', t)        # _{...} / ^{...} groups
    t = t.replace('**', '').replace('*', '')
    t = re.sub(r'\|[\s:|-]+\|', '', t)                   # table separator rows
    t = t.replace('{', '').replace('}', '').replace('^', '').replace('_', '')
    t = re.sub(r'^\s*#+\s*', '', t, flags=re.M)
    t = re.sub(r'(?m)^\s*-\s+', '', t)                   # bullet markers
    t = t.replace('|', ' ').replace('\\', '')
    t = COMBINING_RE.sub('', t)
    return re.sub(r'\s+', '', t)


def fuzzy_find(needle, hay, start):
    """locate `needle` from `start`, tolerating digit runs (footer page numbers) in `hay`."""
    head = needle[:20]
    s = hay.find(head, start)
    while s >= 0:
        i, j, ok = 0, s, True
        while i < len(needle):
            if j < len(hay) and hay[j] == needle[i]:
                i += 1
                j += 1
                continue
            if j < len(hay) and hay[j].isdigit():
                j += 1
                continue
            ok = False
            break
        if ok:
            return s, j
        s = hay.find(head, s + 1)
    return -1, -1


def split_units(md):
    """markdown -> [(kind, text)] keeping table rows separate (they can straddle pages)."""
    units, cur, mode = [], [], None
    for line in md.split('\n'):
        st = line.strip()
        is_tab = st.startswith('|')
        if not st or st.startswith('$$'):
            if cur:
                units.append((mode, '\n'.join(cur)))
                cur = []
            mode = None
            continue
        if is_tab:
            if mode != 'tab' and cur:
                units.append((mode, '\n'.join(cur)))
                cur = []
            if re.fullmatch(r'\|[\s:|-]+\|', st):
                continue
            units.append(('tab', line))
            mode = 'tab'
            continue
        if mode == 'tab':
            units.append((mode, '\n'.join(cur)))
            cur = []
            mode = None
        cur.append(line)
        mode = 'txt'
    if cur:
        units.append((mode, '\n'.join(cur)))
    return units


def prefix_match(needle, hay):
    """length of the longest prefix of `needle` that occurs anywhere in `hay` (diagnosis of a
    MISSING unit: monotone in the prefix length, so a binary search is enough)."""
    lo, hi = 0, len(needle)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if needle[:mid] in hay:
            lo = mid
        else:
            hi = mid - 1
    return lo


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('-p', '--pdf', default=DEFAULT_PDF)
    ap.add_argument('-m', '--md', default=DEFAULT_MD)
    ap.add_argument('-r', '--running-title', default=RUNNING_TITLE)
    ap.add_argument('-c', '--companion', action='store_true',
                    help='verify a companion document: no figures, fewer equations')
    a = ap.parse_args()

    doc = pymupdf.open(a.pdf)
    md = open(a.md, encoding='utf-8').read()
    print('pdf : %s  (%d pages, %d bytes)' % (a.pdf, doc.page_count, os.path.getsize(a.pdf)))
    print('md  : %s' % a.md)

    # ---------------------------------------------------------------- 1. text fidelity
    pdf_text = '\n'.join(p.get_text() for p in doc).replace(a.running_title, ' ')
    # braces: the PDF keeps them when they are not part of a _{...} group, and norm() drops
    # them on the markdown side, so drop them here too
    hay = (re.sub(r'\s+', '', pdf_text).replace('\u2022', '').replace('|', '').replace('_', '').replace('{', '').replace('}', ''))
    pos, bad, order, n_unit, n_rows = 0, 0, 0, 0, 0
    for kind, txt in split_units(md):
        n = norm(txt)
        if len(n) < 3:
            continue
        n_unit += 1
        n_rows += (kind == 'tab')
        s, e = fuzzy_find(n, hay, pos)
        if s < 0:
            # A unit that is simply out of order (a paragraph that straddles a page break, where
            # the footer line number is tolerated but the block order on the page is not always the
            # reading order) is not a dropped paragraph: look for it from the start of the stream.
            s2, e2 = fuzzy_find(n, hay, 0)
            if s2 >= 0:
                order += 1
                pos = max(pos, e2)
                continue
            k = prefix_match(n, hay)
            i = hay.find(n[:k]) if k else -1
            bad += 1
            print('   MISSING (%s): %s' % (kind, n[:90]))
            print('             PDF agrees on the first %d of %d chars, then:' % (k, len(n)))
            print('             md  after : ...%s' % n[k:k + 64])
            if i >= 0:
                print('             pdf after : ...%s' % hay[i + k:i + k + 64])
        else:
            pos = e
    print('\n[1] text fidelity : %s — %d units (%d table rows), %d missing, %d out-of-order'
          % ('PASS' if bad == 0 else 'FAIL', n_unit, n_rows, bad, order))

    # ---------------------------------------------------------------- 2. margins
    lm = 2.0 / 2.54 * 72
    over = []
    for i, p in enumerate(doc):
        rm = p.rect.width - lm
        for b in p.get_text('blocks'):
            if b[4] and a.running_title in b[4] and b[1] < 1.9 / 2.54 * 72:
                continue                                    # running title (the one actually passed in)
            if b[0] < lm - 1.5 or b[2] > rm + 1.5:
                over.append((i + 1, [round(v, 1) for v in b[:4]]))
    print('[2] margins       : %s — %d block(s) outside the 2 cm text column'
          % ('PASS' if not over else 'FAIL', len(over)))
    for o in over[:5]:
        print('      page %d bbox %s' % o)

    # ---------------------------------------------------------------- 3. figures & equations
    figs, eqs, orphan = [], [], []
    for i, p in enumerate(doc):
        t = p.get_text()
        caps = re.findall(r'Fig\.\s*\d+\.', t)
        for im in p.get_image_info():
            w = im['bbox'][2] - im['bbox'][0]
            h = im['bbox'][3] - im['bbox'][1]
            if w > 150 and h > 100:
                figs.append(i + 1)
            elif w > 300 and h <= 100:
                eqs.append(i + 1)
        for im in p.get_image_info():
            w = im['bbox'][2] - im['bbox'][0]
            h = im['bbox'][3] - im['bbox'][1]
            if w > 150 and h > 100 and not caps:
                orphan.append(i + 1)
    print('[3] figures       : %d on pages %s (expected %d)'
          % (len(figs), figs, 0 if a.companion else 8))
    print('[4] equations     : %d on pages %s' % (len(eqs), eqs))
    print('[5] figure/caption: %s — %d figure(s) without a caption on the same page'
          % ('PASS' if not orphan else 'FAIL', len(orphan)))

    if a.companion:
        ok = (bad == 0) and not over and len(figs) == 0 and len(eqs) >= 20 and not orphan
    else:
        ok = (bad == 0) and not over and len(figs) == 8 and len(eqs) >= 75 and not orphan
    print('\nRESULT: %s' % ('ALL CHECKS PASSED' if ok else 'PROBLEMS FOUND (see above)'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
