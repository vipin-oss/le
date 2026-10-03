#!/usr/bin/env python3
"""Phase 10 - cover letter in uploadable formats.

`PAPER_PROJECT/13_Manuscript/cover_letter.md` is the text of record (it is read there by the
authors and refreshed in Phase 8). This script renders that same text to .docx and .pdf so it
can be pasted into the submission system, without keeping a second copy of the prose that
could drift: it parses the Markdown at run time, so re-running after any edit to the .md
regenerates both files.

Formatting: `#` -> title style, `**bold**` runs inline, blank-line paragraphs, bullet lines
kept as bullets. Bracketed author-input fields are preserved verbatim and additionally
highlighted (bold) in the .docx so nothing is overlooked at submission time.
"""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MD = os.path.join(ROOT, 'PAPER_PROJECT', '13_Manuscript', 'cover_letter.md')
OUTDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def blocks(text):
    out = []
    for para in re.split(r'\n\s*\n', text.strip()):
        para = para.strip('\n')
        if not para.strip():
            continue
        if para.lstrip().startswith('#'):
            out.append(('h1', para.lstrip('#').strip()))
        elif all(l.lstrip().startswith(('- ', '* ')) for l in para.split('\n') if l.strip()):
            for l in para.split('\n'):
                if l.strip():
                    out.append(('li', l.strip()[2:].strip()))
        else:
            out.append(('p', ' '.join(l.strip() for l in para.split('\n'))))
    return out


def segments(s):
    """split into (text, bold) runs on **...** markers, flagging [bracketed] fields bold."""
    segs, i = [], 0
    for m in re.finditer(r'\*\*(.+?)\*\*', s, flags=re.S):
        if m.start() > i:
            segs.append((s[i:m.start()], False))
        segs.append((m.group(1), True))
        i = m.end()
    if i < len(s):
        segs.append((s[i:], False))
    out = []
    for txt, bold in segs:
        for part in re.split(r'(\[[^\]]{6,}\])', txt):
            if part:
                out.append((part, bold or part.startswith('[')))
    return out


def make_docx(bl, path):
    from docx import Document
    from docx.shared import Pt
    d = Document()
    st = d.styles['Normal']
    st.font.name = 'Times New Roman'
    st.font.size = Pt(11)
    for kind, text in bl:
        if kind == 'h1':
            p = d.add_paragraph()
            r = p.add_run(text)
            r.bold = True
            r.font.size = Pt(13)
            continue
        p = d.add_paragraph(style='List Bullet' if kind == 'li' else None)
        for txt, bold in segments(text):
            r = p.add_run(txt)
            r.bold = bool(bold)
    d.save(path)
    print('wrote %s (%d B)' % (os.path.relpath(path, ROOT), os.path.getsize(path)))


def make_pdf(bl, path):
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import cm
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
    from reportlab.lib.enums import TA_JUSTIFY
    ss = getSampleStyleSheet()
    body = ss['BodyText'].clone('cl_body')
    body.fontName = 'Times-Roman'
    body.fontSize = 10.5
    body.alignment = TA_JUSTIFY
    body.leading = 14
    title = body.clone('cl_title')
    title.fontSize = 13
    title.spaceAfter = 8
    flow = []
    for kind, text in bl:
        esc = (text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
        esc = re.sub(r'\[(?!\[)([^\]]{6,})\]', r'<b>[\1]</b>', esc)
        if kind == 'h1':
            flow.append(Paragraph(esc, title))
        elif kind == 'li':
            flow.append(Paragraph('\u2022 ' + esc, body))
        else:
            flow.append(Spacer(1, 5))
            flow.append(Paragraph(esc, body))
    SimpleDocTemplate(path, pagesize=A4, topMargin=2.2 * cm, bottomMargin=2.2 * cm,
                      leftMargin=2.4 * cm, rightMargin=2.4 * cm,
                      title='Cover letter', author='manuscript builders').build(flow)
    print('wrote %s (%d B)' % (os.path.relpath(path, ROOT), os.path.getsize(path)))


def main():
    if not os.path.isfile(MD):
        print('missing %s' % MD)
        return 1
    bl = blocks(open(MD, encoding='utf-8').read())
    print('%d blocks parsed from cover_letter.md' % len(bl))
    make_docx(bl, os.path.join(OUTDIR, 'cover_letter.docx'))
    make_pdf(bl, os.path.join(OUTDIR, 'cover_letter.pdf'))
    txt = ' '.join(t for _, t in bl)
    unresolved = re.findall(r'\[[^\]]{6,}\]', txt)
    print('%d bracketed author-input fields remain in the letter (expected: %s)'
          % (len(unresolved), ', '.join(sorted({u.split(':')[0] + '...' for u in unresolved}))[:150]))
    print('RESULT: OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())
