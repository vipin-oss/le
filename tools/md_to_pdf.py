#!/usr/bin/env python3
"""md_to_pdf.py — render the PAPER_PROJECT manuscript (Markdown) to a journal-style PDF.

Why this exists: the sandbox has no LaTeX, pandoc, LibreOffice or any HTML-to-PDF engine
(checked 2026-10-01). The manuscript therefore cannot be typeset the usual way. This script
builds a faithful single-column preprint PDF directly from `manuscript_IJHMT.md` using
reportlab, with

  * DejaVu Serif (regular/bold/italic/bold-italic) so Greek letters, unicode super- and
    subscripts, x, ~=, -, degree signs etc. render correctly;
  * display equations rendered by matplotlib's mathtext (the manuscript has three of them,
    numbered (1)-(3)) and embedded as images;
  * the eight figures of 11_Figures/ embedded with their captions;
  * markdown tables rendered as ruled journal tables with wrapped cells;
  * LaTeX-style `_{...}` / `^{...}` groups converted to real sub/superscripts.

It changes no content: the PDF is generated from the same .md that also produces the .docx.

Usage:
    python3 tools/md_to_pdf.py [-i manuscript_IJHMT.md] [-o manuscript_IJHMT.pdf]
"""
import argparse
import os
import re
import sys
import tempfile
import unicodedata

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, Image as RLImage, KeepTogether,
                                PageBreak, PageTemplate, Paragraph, Spacer, Table, TableStyle)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MANUSCRIPT_DIR = os.path.join(ROOT, 'PAPER_PROJECT', '13_Manuscript')
DEFAULT_IN = os.path.join(MANUSCRIPT_DIR, 'manuscript_IJHMT.md')
DEFAULT_OUT = os.path.join(MANUSCRIPT_DIR, 'manuscript_IJHMT.pdf')

FONT_DIR = os.path.join(os.path.dirname(matplotlib.__file__), 'mpl-data', 'fonts', 'ttf')
FONTS = {
    'DJV':       'DejaVuSerif.ttf',
    'DJV-B':     'DejaVuSerif-Bold.ttf',
    'DJV-I':     'DejaVuSerif-Italic.ttf',
    'DJV-BI':    'DejaVuSerif-BoldItalic.ttf',
    'DJVS':      'DejaVuSans.ttf',
    'DJVS-B':    'DejaVuSans-Bold.ttf',
    'STIX':      'STIXGeneral.ttf',      # only for the few glyphs DejaVu Serif lacks (e.g. ≲)
}
RUNNING_TITLE = 'Cavity thermoelasticity in monoclinic beta-Ga2O3 — verified continuum study'


def register_fonts():
    for name, fname in FONTS.items():
        pdfmetrics.registerFont(TTFont(name, os.path.join(FONT_DIR, fname)))
    pdfmetrics.registerFontFamily('DJV', normal='DJV', bold='DJV-B',
                                  italic='DJV-I', boldItalic='DJV-BI')


# ----------------------------------------------------------------------------- text conversion
def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


# Characters DejaVu Serif does not carry -> drawn with STIX General (serif math font).
FALLBACK_CHARS = '≲≳⪅⪆⩽⩾'

# Combining marks that reportlab cannot position (it has no mark-to-base positioning).
# They are drawn as explicit composite glyphs instead (see composite_glyph()).
COMBINING = '̄̂̇̃̆'
DIAC_SPACING = {'̄': '¯',      # macron
                '̂': 'ˆ',      # circumflex
                '̇': '˙',      # dot above
                '̃': '˜',      # tilde
                '̆': '˘'}      # breve


_GLYPH_CACHE = {}
_GLYPH_PX = 320               # rasterisation size of composite glyphs (px per em)


def composite_glyph(base, diac, style, size, tmpdir):
    """Return (path, width_pt, height_pt, baseline_from_bottom_pt) for `base`+`diac`.

    reportlab lays text out glyph by glyph and gives combining marks their own advance,
    so 'κ' + U+0304 would come out as 'κ' followed by a floating dash.  We therefore
    rasterise the composite with PIL (base glyph + spacing diacritic centred above it)
    and inline it as an image aligned on the text baseline.
    """
    from PIL import Image, ImageDraw, ImageFont
    key = (base, diac, style, round(size, 2))
    if key in _GLYPH_CACHE:
        return _GLYPH_CACHE[key]
    spacing = DIAC_SPACING.get(diac)
    fontfile = FONTS[style]
    font = ImageFont.truetype(os.path.join(FONT_DIR, fontfile), _GLYPH_PX)
    asc, desc = font.getmetrics()

    def ink(ch):
        """ink bbox (x0, y0, x1, y1) of ch, y measured downward from the baseline."""
        m = font.getmask(ch, mode='L')
        w, h = m.size
        bbox = m.getbbox()
        if bbox is None:                       # blank glyph
            return (0.0, 0.0, 0.0, 0.0)
        x0, y0, x1, y1 = bbox
        # the mask origin sits at the 'la' anchor, i.e. ascender top == y = 0 in mask space
        return (x0, y0 - asc, x1, y1 - asc)

    bx0, by0, bx1, by1 = ink(base)
    dx0, dy0, dx1, dy1 = ink(spacing)
    pad = int(0.35 * _GLYPH_PX)
    gap = 0.055 * _GLYPH_PX                       # clearance between base ink and diacritic
    # want: diacritic ink bottom (= -dy1 after shift) == (-by0) + gap  above the baseline
    shift = (by0 - gap) - dy1                     # positive = move down, in mask-space px
    W = pad * 2 + int(max(bx1, dx1 - dx0 + bx0) + 4)
    H = pad * 2 + int(asc + desc + gap + (dy1 - dy0) + 8)
    img = Image.new('L', (W, H), 0)
    drw = ImageDraw.Draw(img)
    base_anchor = (pad, pad + asc)
    drw.text(base_anchor, base, font=font, fill=255, anchor='ls')
    x = pad + (bx0 + bx1) / 2 - (dx0 + dx1) / 2
    drw.text((x, base_anchor[1] + shift), spacing, font=font, fill=255, anchor='ls')
    bbox = img.getbbox()
    img = img.crop(bbox)
    out = os.path.join(tmpdir, 'glyph_%s_%s.png' % (
        unicodedata.name(base, 'u%04x' % ord(base)).replace(' ', '')[:16],
        abs(hash(key))))
    img.point(lambda v: 255 - v).convert('RGB').save(out)   # black ink on white
    k = size / _GLYPH_PX
    res = (out, (bbox[2] - bbox[0]) * k, (bbox[3] - bbox[1]) * k,
           (bbox[3] - (pad + asc)) * k)
    _GLYPH_CACHE[key] = res
    return res


_B, _BC, _I, _IC = '\x02', '\x03', '\x04', '\x05'


def to_markup(s, size=9.5, style='DJV', tmpdir=None):
    """Markdown-ish inline text -> reportlab mini-HTML.

    Walks the string keeping track of bold/italic state so that composite glyphs
    (base letter + combining mark) can be inlined with the right font variant.
    """
    s = esc(s)
    s = re.sub(r'\*\*(.+?)\*\*', _B + r'\1' + _BC, s, flags=re.S)
    s = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', _I + r'\1' + _IC, s, flags=re.S)
    # LaTeX-style groups -> real sub/superscripts (one nesting level)
    for _ in range(2):
        s = re.sub(r'_\{([^{}]{1,24})\}', r'<sub>\1</sub>', s)
        s = re.sub(r'\^\{([^{}]{1,24})\}', r'<super>\1</super>', s)
    # bare one/two-character sub- and superscripts (N_r, gamma_B, t_w, t_th, R^2 ...).
    # The trailing guard keeps real identifiers (MASTER_PROMPT, EVIDENCE_UNAVAILABLE,
    # CODE_FREEZE_v2_gate.json) untouched.
    G = 'A-Za-z0-9\\u0370-\\u03ff\\u0391-\\u03c9\\u2207'
    s = re.sub(r'([%s])_([%s])(?![A-Za-z0-9])' % (G, G), r'\1<sub>\2</sub>', s)
    s = re.sub(r'([%s])_([a-z]{2})(?![A-Za-z0-9])' % G, r'\1<sub>\2</sub>', s)
    s = re.sub(r'([%s])\^([%s])(?![A-Za-z0-9])' % (G, G), r'\1<super>\2</super>', s)

    out = []
    bold = ital = False
    i, n = 0, len(s)

    def variant():
        return style + ('-BI' if bold and ital else '-B' if bold else
                        '-I' if ital else '')

    while i < n:
        ch = s[i]
        if ch == _B:
            bold = True
            out.append('<b>')
        elif ch == _BC:
            bold = False
            out.append('</b>')
        elif ch == _I:
            ital = True
            out.append('<i>')
        elif ch == _IC:
            ital = False
            out.append('</i>')
        elif i + 1 < n and s[i + 1] in COMBINING and tmpdir is not None:
            path, w, h, bl = composite_glyph(ch, s[i + 1], variant(), size, tmpdir)
            out.append('<img src="%s" width="%.2f" height="%.2f" valign="%.2f"/>'
                       % (path, w, h, -bl))
            i += 1
        elif ch in FALLBACK_CHARS:
            out.append('<font face="STIX">%s</font>' % ch)
        else:
            out.append(ch)
        i += 1
    if bold:
        out.append('</b>')
    if ital:
        out.append('</i>')
    return ''.join(out)


# ----------------------------------------------------------------------------- equations
def render_equation(latex, outpath, fontsize=11.5, dpi=260):
    """Render a display equation with matplotlib mathtext; return (path, w_px, h_px)."""
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.patch.set_alpha(0.0)
    fig.text(0, 0, f'${latex}$', fontsize=fontsize)
    fig.savefig(outpath, dpi=dpi, transparent=True, bbox_inches='tight', pad_inches=0.03)
    plt.close(fig)
    with Image.open(outpath) as im:
        return outpath, im.size[0], im.size[1]


# ----------------------------------------------------------------------------- styles
def make_styles():
    S = {}
    S['title'] = ParagraphStyle('title', fontName='DJV-B', fontSize=14.5, leading=18,
                                alignment=TA_CENTER, spaceAfter=8, textColor=colors.black)
    S['author'] = ParagraphStyle('author', fontName='DJV-I', fontSize=9.5, leading=13,
                                 alignment=TA_CENTER, spaceAfter=4)
    S['h1'] = ParagraphStyle('h1', fontName='DJV-B', fontSize=11.5, leading=14,
                             spaceBefore=13, spaceAfter=5)
    S['h2'] = ParagraphStyle('h2', fontName='DJV-B', fontSize=10, leading=13,
                             spaceBefore=9, spaceAfter=4)
    S['body'] = ParagraphStyle('body', fontName='DJV', fontSize=9.5, leading=13.2,
                               alignment=TA_JUSTIFY, spaceAfter=5)
    S['caption'] = ParagraphStyle('caption', fontName='DJV', fontSize=8.5, leading=11,
                                  alignment=TA_JUSTIFY, spaceBefore=4, spaceAfter=10)
    S['bullet'] = ParagraphStyle('bullet', parent=S['body'], leftIndent=13, bulletIndent=3,
                                 spaceAfter=3, bulletFontName='DJV', bulletFontSize=8)
    S['ref'] = ParagraphStyle('ref', fontName='DJV', fontSize=8.6, leading=11.4,
                              leftIndent=14, firstLineIndent=-14, spaceAfter=2.5,
                              alignment=TA_JUSTIFY)
    S['cell'] = ParagraphStyle('cell', fontName='DJV', fontSize=8.0, leading=10.2)
    S['cellh'] = ParagraphStyle('cellh', fontName='DJV-B', fontSize=8.0, leading=10.2)
    S['eqnum'] = ParagraphStyle('eqnum', fontName='DJV', fontSize=9.5, leading=13)
    return S


# ----------------------------------------------------------------------------- document build
def build(md_path, pdf_path, tmpdir):
    register_fonts()
    S = make_styles()
    text = open(md_path, encoding='utf-8').read()
    lines = text.split('\n')

    content_w = 17.0 * cm
    story = []

    def mk(txt, st):
        """inline markup for style `st` (used with the right point size everywhere)"""
        # keep 'Fig. 3', 'Table 4', 'Section 2' from being split across lines
        txt = re.sub(r'\b(Fig|Figs|Table|Section|Eq|Ref)(\.?)\s+(?=\d)',
                     lambda m: m.group(1) + m.group(2) + '\u00a0', txt)
        return to_markup(txt, size=st.fontSize, tmpdir=tmpdir)

    def col_widths(rows, ncol, size):
        """Minimum width per column = widest unbreakable word (measured with the real
        font) + padding; the remaining slack is shared out like the character shares."""
        mins, lens = [], [1.0] * ncol
        for j in range(ncol):
            m = 1.0
            for r in rows:
                if j >= len(r):
                    continue
                txt = re.sub(r'[_^]\{[^{}]*\}', lambda mo: mo.group(0)[2:-1],
                             r[j].replace('*', '').strip())
                lens[j] = max(lens[j], len(r[j].strip()))
                for w in txt.split():
                    m = max(m, pdfmetrics.stringWidth(w, 'DJV', size))
            mins.append(m + 9)                      # cell padding
        if sum(mins) > content_w:
            return None, mins, lens
        slack = content_w - sum(mins)
        tot = float(sum(lens))
        return [mins[j] + slack * lens[j] / tot for j in range(ncol)], mins, lens

    def flush_table(rows):
        if not rows:
            return
        ncol = max(len(r) for r in rows)
        # shrink the cell font (in steps) until every column can hold its longest word
        for size in (8.0, 7.4, 6.8, 6.2, 5.6):
            widths, mins, lens = col_widths(rows, ncol, size)
            if widths is not None:
                break
        if widths is None:                            # give up: use the minimum widths
            size, widths = 5.6, mins
        cs = ParagraphStyle('cell%d' % id(rows), parent=S['cell'], fontSize=size,
                            leading=size * 1.28)
        ch = ParagraphStyle('cellh%d' % id(rows), parent=S['cellh'], fontSize=size,
                            leading=size * 1.28)
        header = [Paragraph(mk(c.strip(), ch), ch) for c in rows[0]]
        body = [[Paragraph(mk(c.strip(), cs), cs) for c in r] for r in rows[1:]]
        data = [header] + body
        t = Table(data, colWidths=widths, repeatRows=1, hAlign='CENTER')
        t.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LINEABOVE', (0, 0), (-1, 0), 0.9, colors.black),
            ('LINEBELOW', (0, 0), (-1, 0), 0.5, colors.black),
            ('LINEBELOW', (0, -1), (-1, -1), 0.9, colors.black),
            ('TOPPADDING', (0, 0), (-1, -1), 3),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ('LEFTPADDING', (0, 0), (-1, -1), 4),
            ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ]))
        story.append(t)
        story.append(Spacer(1, 3))

    table_rows = []
    pending_figure = []          # a figure waits for its caption so they stay together
    first_section = True

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            if table_rows:
                flush_table(table_rows)
                table_rows = []
            continue

        # ---- tables -------------------------------------------------------
        if line.lstrip().startswith('|'):
            cells = [c for c in line.strip().strip('|').split('|')]
            if all(re.fullmatch(r':?-{2,}:?', c.strip()) for c in cells if c.strip()):
                continue                      # separator row
            table_rows.append(cells)
            continue
        if table_rows:
            flush_table(table_rows)
            table_rows = []

        # ---- figures ------------------------------------------------------
        m = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', line.strip())
        if m:
            rel = m.group(2)
            img_path = os.path.normpath(os.path.join(MANUSCRIPT_DIR, rel))
            if not os.path.exists(img_path):
                story.append(Paragraph(f'[missing figure: {rel}]', S['caption']))
                continue
            with Image.open(img_path) as im:
                iw, ih = im.size
            scale = min(content_w / iw, 10.5 * cm / ih)
            pending_figure.append(Spacer(1, 4))
            pending_figure.append(RLImage(img_path, width=iw * scale, height=ih * scale,
                                          hAlign='CENTER'))
            continue

        # ---- display equations --------------------------------------------
        if line.strip().startswith('$$'):
            latex = line.replace('$$', '').strip().replace('\\\\', '\\')
            num = ''
            mnum = re.search(r'\\qquad\s*\((\d+)\)\s*$', latex)
            if mnum:
                num = mnum.group(1)
                latex = re.sub(r'\\qquad\s*\(\d+\)\s*$', '', latex).strip()
            eq_png = os.path.join(tmpdir, f'eq_{len(story)}.png')
            _, wpx, hpx = render_equation(latex, eq_png)
            # leave 1.6 cm on the right for the equation number
            max_w = max(content_w - 1.6 * cm, 0.35 * content_w)
            scale = min(max_w / wpx, 3.2 * cm / hpx)
            w, h = wpx * scale, hpx * scale
            numcol = content_w - w
            img = RLImage(eq_png, width=w, height=h)
            row = Table([[img, Paragraph(f'({num})', S['eqnum'])]],
                        colWidths=[w, numcol], hAlign='CENTER')
            row.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                     ('LEFTPADDING', (0, 0), (-1, -1), 0),
                                     ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                                     ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
            story.append(Spacer(1, 3))
            story.append(KeepTogether([row]))
            story.append(Spacer(1, 5))
            continue

        # ---- headings ------------------------------------------------------
        if line.startswith('### '):
            story.append(Paragraph(mk(line[4:].strip(), S['h2']), S['h2']))
            continue
        if line.startswith('## '):
            head = line[3:].strip()
            if not first_section:
                story.append(Spacer(1, 2))
            first_section = False
            story.append(Paragraph(mk(head, S['h1']), S['h1']))
            continue
        if line.startswith('# '):
            story.append(Paragraph(mk(line[2:].strip(), S['title']), S['title']))
            continue

        # ---- bullets -------------------------------------------------------
        if line.startswith('- '):
            story.append(Paragraph(mk(line[2:].strip(), S['bullet']), S['bullet'],
                                   bulletText='•'))
            continue

        body = line.strip()

        # ---- authors placeholder -------------------------------------------
        if body.startswith('*[Authors'):
            story.append(Paragraph(mk(body, S['author']), S['author']))
            continue

        # ---- references -----------------------------------------------------
        if re.match(r'^\[\d+\]', body):
            story.append(Paragraph(mk(body, S['ref']), S['ref']))
            continue

        # ---- captions --------------------------------------------------------
        if re.match(r'\*\*(Fig|Table)\.?\s*\d', body):
            cap = Paragraph(mk(body, S['caption']), S['caption'])
            if pending_figure:                       # figure + caption on one page
                story.append(KeepTogether(pending_figure + [cap]))
                pending_figure = []
            else:
                story.append(cap)
            continue

        story.append(Paragraph(mk(body, S['body']), S['body']))

    if table_rows:
        flush_table(table_rows)
    story.extend(pending_figure)

    # ---------------------------------------------------------------- document
    doc = BaseDocTemplate(pdf_path, pagesize=A4,
                          leftMargin=2.0 * cm, rightMargin=2.0 * cm,
                          topMargin=2.1 * cm, bottomMargin=1.9 * cm,
                          title='Orientation-dependent wall stress around circular and '
                                'elliptical cavities in monoclinic beta-Ga2O3',
                          author='PAPER_PROJECT (authors to be completed)',
                          subject='Verified continuum study — manuscript draft')
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='body')

    def decorate(canv, docu):
        canv.saveState()
        if canv.getPageNumber() > 1:          # no running title on the title page
            canv.setFont('DJV-I', 7.6)
            canv.setFillColor(colors.HexColor('#555555'))
            canv.drawString(doc.leftMargin, A4[1] - 1.45 * cm, RUNNING_TITLE)
            canv.setStrokeColor(colors.HexColor('#999999'))
            canv.setLineWidth(0.4)
            canv.line(doc.leftMargin, A4[1] - 1.62 * cm, A4[0] - doc.rightMargin,
                      A4[1] - 1.62 * cm)
        canv.setFont('DJV', 8.6)
        canv.setFillColor(colors.black)
        canv.drawRightString(A4[0] - doc.rightMargin, 1.25 * cm, str(canv.getPageNumber()))
        canv.restoreState()

    doc.addPageTemplates([PageTemplate(id='main', frames=[frame], onPage=decorate)])
    doc.build(story)
    return pdf_path


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('-i', '--input', default=DEFAULT_IN)
    ap.add_argument('-o', '--output', default=DEFAULT_OUT)
    args = ap.parse_args()
    with tempfile.TemporaryDirectory() as tmp:
        out = build(args.input, args.output, tmp)
    print('wrote', out, os.path.getsize(out), 'bytes')


if __name__ == '__main__':
    sys.exit(main())
