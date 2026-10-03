#!/usr/bin/env python3
"""md_to_tex.py — turn the manuscript markdown into a journal-quality elsarticle source.

Why: the project maintains the manuscript as `manuscript_IJHMT.md` (the source of the .docx and
of the PDF).  This converter regenerates the LaTeX submission source from that same file, so the
two cannot drift apart.  It is deliberately conservative:

  * no content is added — text, numbers, tables and figure calls come from the .md;
  * unicode (Greek, sub/superscripts, x, ~=, combining accents, -) is converted to portable
    LaTeX so that the file compiles with pdflatex;
  * display equations become numbered `equation` environments (the hard-coded `\\qquad (n)` of
    the markdown is dropped; LaTeX numbers them) and text references become \\eqref / \\ref;
  * citations `[1,2]` become \\cite{key} using the keys of the verified reference list;
  * tables become booktabs/tabularx tables, figures become figure environments that keep the
    numbering of the manuscript.

Two conventions keep the conversion sane:
  * PROT ('\\x01') delimits regions that are already finished; text-mode work never touches them;
  * an odd-indexed part of a PROT split is complete math, dollars included.

Usage:
    python3 tools/md_to_tex.py [-i .../manuscript_IJHMT.md] [-o .../FINAL_REVISED_MANUSCRIPT.tex]
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MS = os.path.join(ROOT, 'PAPER_PROJECT', '13_Manuscript')
DEFAULT_IN = os.path.join(MS, 'manuscript_IJHMT.md')
DEFAULT_OUT = os.path.join(MS, 'FINAL_REVISED_MANUSCRIPT.tex')
REFS = os.path.join(ROOT, 'PAPER_PROJECT', '01_Literature', 'REFERENCES_VERIFIED.json')
_ORDERED = os.path.join(ROOT, 'PAPER_PROJECT', '13_Manuscript', 'REFERENCES_ORDERED.json')
if os.path.exists(_ORDERED):      # the manuscript prints its list in order of first citation; the .tex
    REFS = _ORDERED               # \cite mapping must use the same numbering or the two disagree


# ------------------------------------------------------------------ unicode -> LaTeX tables
GREEK = {
    'α': '\\alpha', 'β': '\\beta', 'γ': '\\gamma', 'δ': '\\delta', 'ε': '\\varepsilon',
    'ϵ': '\\epsilon', 'ζ': '\\zeta', 'η': '\\eta', 'θ': '\\theta', 'ϑ': '\\vartheta',
    'ι': '\\iota', 'κ': '\\kappa', 'λ': '\\lambda', 'μ': '\\mu', 'µ': '\\mu', 'ν': '\\nu',
    'ξ': '\\xi', 'π': '\\pi', 'ρ': '\\rho', 'σ': '\\sigma', 'ς': '\\varsigma', 'τ': '\\tau',
    'υ': '\\upsilon', 'φ': '\\varphi', 'ϕ': '\\phi', 'χ': '\\chi', 'ψ': '\\psi', 'ω': '\\omega',
    'Γ': '\\Gamma', 'Δ': '\\Delta', 'Θ': '\\Theta', 'Λ': '\\Lambda', 'Ξ': '\\Xi', 'Π': '\\Pi',
    'Σ': '\\Sigma', 'Υ': '\\Upsilon', 'Φ': '\\Phi', 'Ψ': '\\Psi', 'Ω': '\\Omega',
}
SUP = {'⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5',
       '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', '⁺': '+', '⁻': '-', 'ⁿ': 'n', 'ᵀ': 'T'}
SUB = {'₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4', '₅': '5',
       '₆': '6', '₇': '7', '₈': '8', '₉': '9'}
SYM = {                                     # math symbols: wrapped in $ in text mode
    '×': '\\times', '−': '-', '≈': '\\approx', '≲': '\\lesssim', '≤': '\\leq', '≥': '\\geq',
    '→': '\\to', '·': '\\cdot', '√': '\\sqrt', '°': '^{\\circ}', '½': '\\frac{1}{2}',
    '∞': '\\infty', '±': '\\pm', '≠': '\\neq', '∂': '\\partial', '∇': '\\nabla',
    '∫': '\\int', '∑': '\\sum', '∏': '\\prod', '∈': '\\in', '⊗': '\\otimes',
    '…': '\\ldots', '\u2032': "'", '\u2016': '\\Vert',
    '⟨': '\\langle', '⟩': '\\rangle', '∝': '\\propto', '≪': '\\ll', '≫': '\\gg',
}
TEXT_SYM = {                                # text-mode constructs: never wrapped in $
    '–': '--', '—': '---', '“': '``', '”': "''", '‘': '`', '’': "'",
    'é': "\\'e", 'è': "\\`e", 'ê': "\\^e", 'ë': '\\"e', 'ö': '\\"o', 'ü': '\\"u',
    'ä': '\\"a', 'ç': '\\c{c}', 'ñ': '\\~n', 'å': '\\aa',
}
COMB = {'̄': 'bar', '̂': 'hat', '̃': 'tilde',
        '́': 'acute', '̀': 'grave', '̇': 'dot'}
SUPRUN, SUBRUN = ''.join(SUP), ''.join(SUB)
BASE = '0-9A-Za-z)\u2032' + ''.join(GREEK)
BODY = r'(?:(?:[^{}]|\{[^{}]*\}){1,40})'          # one nesting level inside a group
PROT = '\x01'                                     # protects finished math from further work


def _math(s):
    """convert a fragment that already sits inside math mode (no $ inserted)"""
    if not s:
        return s
    s = s.replace('\u2032', '^{\\prime}')
    s = s.replace('\u2016', '\\Vert')
    s = re.sub(r'(.)([' + ''.join(COMB) + r'])',
               lambda m: '\\' + COMB[m.group(2)] + '{' + _math(m.group(1)) + '}', s)
    for _ in range(3):
        s = re.sub(r'([' + BASE + r']*)([_^])\{(' + BODY + r')\}',
                   lambda m: m.group(1) + m.group(2) + '{' + _math(m.group(3)) + '}', s)
    s = re.sub(r'([' + BASE + r'])([' + SUPRUN + r']+)',
               lambda m: m.group(1) + '^{' + ''.join(SUP[c] for c in m.group(2)) + '}', s)
    s = re.sub(r'([' + BASE + r'])([' + SUBRUN + r']+)',
               lambda m: m.group(1) + '_{' + ''.join(SUB[c] for c in m.group(2)) + '}', s)
    # a command name ends at the first non-letter, so \rho followed by 'c' needs a space
    for tbl in (GREEK, SYM):
        for ch, cmd in tbl.items():
            if ch in s:
                s = re.sub(re.escape(ch) + r'(?=[A-Za-z])', lambda m, c=cmd: c + ' ', s)
                s = s.replace(ch, cmd)
    s = s.replace('–', '--').replace('—', '\\text{---}')
    return s


def _plain(s):
    """escape and convert a text-mode fragment (math symbols get their own $...$)"""
    if not s:
        return s
    for ch, cmd in TEXT_SYM.items():
        s = s.replace(ch, cmd)
    s = re.sub(r'(?<!\\)([&%#])', r'\\\1', s)
    s = s.replace('~', '\\textasciitilde{}')
    for ch, cmd in GREEK.items():
        s = s.replace(ch, '$' + cmd + '$')
    for ch, cmd in SYM.items():
        s = s.replace(ch, '$' + cmd + '$')
    s = re.sub(r'([' + SUPRUN + r']+)',
               lambda m: '$^{' + ''.join(SUP[c] for c in m.group(1)) + '}$', s)
    s = re.sub(r'([' + SUBRUN + r']+)',
               lambda m: '$_{' + ''.join(SUB[c] for c in m.group(1)) + '}$', s)
    s = re.sub(r'(?<!\\)_', r'\\_', s)
    return s


def _apply(t, fn):
    """apply fn to the text-mode (unprotected) parts of t only"""
    parts = t.split(PROT)
    for k in range(0, len(parts), 2):
        parts[k] = fn(parts[k])
    return PROT.join(parts)


def _text(t):
    """text mode: discover the math, protect it, escape the rest"""
    t = t.replace('Ga₂O₃', PROT + 'Ga$_2$O$_3$' + PROT)

    # file paths and identifiers such as PAPER_PROJECT/06_Source_Code/src or ANALYSIS_V2.json
    # must stay literal: without this the bare-subscript rule below turns 09_Raw into 09_{Raw}.
    def path(m):
        return PROT + _plain(m.group(0)) + PROT
    t = _apply(t, lambda x: re.sub(r'[A-Z0-9]{2,}_[A-Za-z0-9_./]*', path, x))

    def grp(m):
        return (PROT + '$' + _math(m.group(1)) + m.group(2)
                + '{' + _math(m.group(3)) + '}$' + PROT)

    def sup(m):
        return PROT + '$' + _math(m.group(1)) + '^{' \
            + ''.join(SUP[c] for c in m.group(2)) + '}$' + PROT

    def sub(m):
        return PROT + '$' + _math(m.group(1)) + '_{' \
            + ''.join(SUB[c] for c in m.group(2)) + '}$' + PROT

    def bare(m):
        return PROT + '$' + _math(m.group(1)) + '_{' + _math(m.group(2)) + '}$' + PROT

    for _ in range(4):                       # nested groups, innermost first
        t = _apply(t, lambda x: re.sub(r'([' + BASE + r']+)([_^])\{(' + BODY + r')\}', grp, x))
    t = _apply(t, lambda x: re.sub(r'([' + BASE + r'])([' + SUPRUN + r']+)', sup, x))
    t = _apply(t, lambda x: re.sub(r'([' + BASE + r'])([' + SUBRUN + r']+)', sub, x))
    t = _apply(t, lambda x: re.sub(
        r'(?<![A-Za-z0-9_])([A-Za-z0-9]{1,2})_([A-Za-z0-9]{1,4})(?![A-Za-z0-9])', bare, x))
    return _apply(t, _plain)


MATHY = re.compile(r'^\$([A-Za-z]\w{0,15}|\\[A-Za-z]+(?:\{[^{}]*\})?)\$$')


def _adopt(s):
    """let a single-symbol math group adopt a subscript that the markdown left outside it:

    ``$\\gamma$_B`` -> ``$\\gamma_B$``  and  ``N_$\\theta$`` -> ``$N_\\theta$``.
    Works on the PROT-split parts, so protected groups (chemical formulae) are untouched.
    """
    parts = s.split(PROT)
    for k in range(1, len(parts), 2):
        m = MATHY.match(parts[k])
        if not m:
            continue
        sym = m.group(1)
        if k + 1 < len(parts):                       # trailing subscript:  $sym$_B
            mm = re.match(r'\\?_([A-Za-z0-9]{1,6})(?![A-Za-z0-9])', parts[k + 1])
            if mm:
                parts[k] = '$%s_%s$' % (sym, mm.group(1))
                parts[k + 1] = parts[k + 1][mm.end():]
        m = MATHY.match(parts[k])
        if m and k - 1 >= 0:                         # leading identifier:  N_$sym$
            mm = re.search(r'(?<![A-Za-z0-9_])([A-Za-z0-9]{1,6})\\?_$', parts[k - 1])
            if mm:
                parts[k] = '$%s_%s$' % (mm.group(1), m.group(1))
                parts[k - 1] = parts[k - 1][:mm.start()]
    return PROT.join(parts)


def u2l(s):
    """unicode -> portable LaTeX, keeping text mode and math mode separate"""
    if not s:
        return s
    # (0) combining accents:  kappa-macron, sigma-hat, s-bar  ->  \bar{\kappa} etc.
    s = re.sub(r'(.)([' + ''.join(COMB) + r'])',
               lambda m: PROT + '$'
               + _math('\\' + COMB[m.group(2)] + '{' + m.group(1) + '}') + '$' + PROT, s)
    # (1) math already delimited in the markdown is converted and protected as a whole
    parts = s.split('$')
    for k in range(1, len(parts), 2):
        parts[k] = '$' + _math(parts[k]) + '$'
    s = PROT.join(parts)
    # (2) the unprotected remainder is text
    s = _apply(s, _text)
    # (3) adopt stray subscripts, (4) drop the protection markers
    for _ in range(3):
        s = _adopt(s)
    s = s.replace(PROT, '')
    # (5) tidy adjacent math groups:  $a$$b$  ->  $ab$  (with a space after a command name)
    def merge(m):
        a, b = m.group(1), m.group(2)
        return '$%s%s%s$' % (a, ' ' if re.search(r'\\[A-Za-z]+$', a) else '', b)

    for _ in range(4):
        s = re.sub(r'\$([^$]{1,60})\$\$([^$]{1,60})\$', merge, s)
    return s


def inline(s, refmap, secmap):
    """markdown inline markup -> LaTeX, with cross-references and citations"""
    s = u2l(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', s, flags=re.S)
    s = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'\\emph{\1}', s, flags=re.S)
    s = s.replace('`', '')
    s = re.sub(r'Eq\.\s*\((\d+)\)', lambda m: '\\eqref{eq:%s}' % m.group(1), s)
    s = re.sub(r'Figs?\.\s*(\d+)([a-z]?)',
               lambda m: '\\figurename~\\ref{fig:%s}%s' % (m.group(1), m.group(2)), s)
    s = re.sub(r'Tables?\s*(\d+)', lambda m: 'Table~\\ref{tab:%s}' % m.group(1), s)
    s = re.sub(r'Sections?\s*(\d+(?:\.\d+)?)',
               lambda m: 'Section~\\ref{%s}'
               % secmap.get(m.group(1), 'sec:%s' % m.group(1)), s)

    def cit(m):
        keys = [refmap.get(k) for k in re.findall(r'\d+', m.group(1))]
        keys = [k for k in keys if k]
        return '\\cite{%s}' % ','.join(keys) if keys else m.group(0)
    s = re.sub(r'\[([0-9,\s]+)\]', cit, s)
    return s


def colspec(rows, ncol):
    lens = [max([len(r[j]) for r in rows if j < len(r)] or [0]) for j in range(ncol)]
    spec = ''.join('X' if L > 26 else ('l' if L > 6 else 'c') for L in lens)
    return spec, ('X' in spec)


# ----------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('-i', '--input', default=DEFAULT_IN)
    ap.add_argument('-o', '--output', default=DEFAULT_OUT)
    ap.add_argument('-c', '--companion', action='store_true',
                    help='slim preamble for a companion document (no abstract/highlights)')
    a = ap.parse_args()

    refs = json.load(open(REFS, encoding='utf-8'))
    refmap = {str(r['n']): r['key'] for r in refs}
    md = open(a.input, encoding='utf-8').read()
    lines = md.split('\n')

    out = []
    secmap, eq, fig, tab = {}, 0, 0, 0
    tbl = []
    pending_caption = None          # (kind, number, text) waiting for its float
    pending_fig = None              # figure block waiting for its caption
    in_refs = False

    def flush_table():
        nonlocal tab, tbl, pending_caption
        if not tbl:
            return
        ncol = max(len(r) for r in tbl)
        spec, wide = colspec(tbl, ncol)
        env = 'tabularx' if wide else 'tabular'
        kind, num, cap = pending_caption or ('Table', '?', '')
        tab = num
        pending_caption = None
        out.append('\\begin{table}[htbp]')
        out.append('\\centering')
        out.append('\\caption{%s}' % inline(cap, refmap, secmap))
        out.append('\\label{tab:%s}' % num)
        out.append('\\begin{%s}%s{%s}' % (env, '{\\textwidth}' if wide else '', spec))
        out.append('\\toprule')
        out.append(' & '.join(inline(c, refmap, secmap) for c in tbl[0]) + ' \\\\')
        out.append('\\midrule')
        for r in tbl[1:]:
            cells = [inline(c, refmap, secmap) for c in r] + [''] * (ncol - len(r))
            out.append(' & '.join(cells) + ' \\\\')
        out.append('\\bottomrule')
        out.append('\\end{%s}' % env)
        out.append('\\end{table}')
        out.append('')
        tbl = []

    i = 0
    while i < len(lines):
        line = lines[i]
        st = line.strip()

        if st.startswith('## References'):
            in_refs = True
            i += 1
            continue
        if in_refs:
            if st.startswith('#'):
                in_refs = False
            else:
                i += 1
                continue
        if not st:
            flush_table()
            i += 1
            continue

        # ---- tables
        if st.startswith('|'):
            cells = st.strip('|').split('|')
            if all(re.fullmatch(r':?-{2,}:?', c.strip()) for c in cells if c.strip()):
                i += 1
                continue
            tbl.append([c.strip() for c in cells])
            i += 1
            continue

        # ---- display equations
        if st.startswith('$$'):
            flush_table()
            eq += 1
            tex = _math(re.sub(r'\\qquad\s*\(\d+\)\s*$', '', st.replace('$$', '').strip()))
            out.append('\\begin{equation}')
            out.append(tex)
            out.append('\\label{eq:%d}' % eq)
            out.append('\\end{equation}')
            out.append('')
            i += 1
            continue

        # ---- figure call (its caption follows in the markdown)
        m = re.match(r'!\[[^\]]*\]\(([^)]+)\)', st)
        if m:
            flush_table()
            fig += 1
            path = m.group(1)
            frac = 0.85
            try:
                from PIL import Image
                with Image.open(os.path.normpath(os.path.join(MS, path))) as im:
                    w, h = im.size
                frac = 0.95 if w / h > 2.2 else (0.80 if w / h > 1.3 else 0.62)
            except Exception:
                pass
            pending_fig = ['\\begin{figure}[htbp]',
                           '\\centering',
                           '\\includegraphics[width=%.2f\\textwidth]{%s}' % (frac, path)]
            i += 1
            continue

        # ---- headings
        if st.startswith('### '):
            flush_table()
            head = st[4:].strip()
            key = head.split(' ')[0].rstrip('.')
            secmap[key] = 'sec:%s' % key
            out.append('\\subsection{%s}'
                       % inline(re.sub(r'^\d+(?:\.\d+)*\.?\s*', '', head), refmap, secmap))
            out.append('\\label{%s}' % secmap[key])
            out.append('')
            i += 1
            continue
        if st.startswith('## '):
            flush_table()
            head = st[3:].strip()
            i += 1
            if head == 'Abstract':
                while i < len(lines) and not lines[i].startswith('#'):
                    i += 1
                continue                                    # emitted in the front matter
            if head == 'Highlights':
                out.append('\\begin{highlights}')
                while i < len(lines) and not lines[i].strip().startswith('- '):
                    if lines[i].startswith('#'):
                        break
                    i += 1
                while i < len(lines) and lines[i].strip().startswith('- '):
                    out.append('\\item %s' % inline(lines[i].strip()[2:], refmap, secmap))
                    i += 1
                out.append('\\end{highlights}')
                out.append('')
                continue
            if head == 'References':
                continue
            if head in ('Declarations', 'Acknowledgements'):   # Elsevier: unnumbered
                out.append('\\section*{%s}' % head)
                out.append('')
                continue
            if head.startswith('Appendix'):
                out.append('\\appendix')
                out.append('\\section{%s}'
                           % inline(head.split('.', 1)[-1].strip(), refmap, secmap))
                out.append('\\label{sec:appendix}')
                out.append('')
                continue
            key = head.split(' ')[0].rstrip('.')
            secmap[key] = 'sec:%s' % key
            out.append('\\section{%s}'
                       % inline(re.sub(r'^\d+(?:\.\d+)*\.?\s*', '', head), refmap, secmap))
            out.append('\\label{%s}' % secmap[key])
            out.append('')
            continue
        if st.startswith('# '):
            i += 1
            continue

        # ---- front-matter lines that must not be repeated in the body
        if st.startswith('*[Authors') or st.startswith('**Keywords'):
            i += 1
            continue

        # ---- bullets
        if st.startswith('- '):
            flush_table()
            out.append('\\begin{itemize}')
            while i < len(lines) and lines[i].strip().startswith('- '):
                out.append('\\item %s' % inline(lines[i].strip()[2:], refmap, secmap))
                i += 1
            out.append('\\end{itemize}')
            out.append('')
            continue

        # ---- captions
        m = re.match(r'\*\*Fig\.\s*(\d+)\.\*\*\s*(.*)$', st) or \
            re.match(r'\*\*Table\s*(\d+)\.\*\*\s*(.*)$', st)
        if m:
            pending_caption = ('Fig' if 'Fig' in st[:8] else 'Table', m.group(1),
                               m.group(2).strip())
            if pending_fig is not None:
                pending_fig.append('\\caption{%s}'
                                   % inline(m.group(2).strip(), refmap, secmap))
                pending_fig.append('\\label{fig:%s}' % m.group(1))
                pending_fig += ['\\end{figure}', '']
                out.extend(pending_fig)
                pending_fig = None
                pending_caption = None
            i += 1
            continue

        # ---- ordinary paragraph
        flush_table()
        out.append(inline(st, refmap, secmap))
        out.append('')
        i += 1

    flush_table()
    if pending_fig is not None:                     # figure without a caption: keep it anyway
        out.extend(pending_fig + ['\\end{figure}', ''])

    # ------------------------------------------------------------------ front matter
    mt = re.search(r'^# (.+)$', md, flags=re.M)
    title = u2l(mt.group(1)) if mt else '[TITLE]'
    mabs = re.search(r'## Abstract\n+(.+?)\n\n', md, flags=re.S)
    abstract = inline(mabs.group(1).strip(), refmap, secmap) if mabs else ''
    mkw = re.search(r'\*\*Keywords:\*\*\s*(.+)', md)
    keywords = ' \\sep '.join(inline(k.strip(), refmap, secmap)
                              for k in mkw.group(1).split(';')) if mkw else ''
    if '\\begin{highlights}' in out:
        k = out.index('\\begin{highlights}')
        j = out.index('\\end{highlights}')
        highlights = '\n'.join(out[k + 1:j]) + '\n'
        del out[k:j + 1]
    else:
        highlights = ''

    if a.companion:                                  # companion / calculation document
        preamble = r"""%s.tex
%% Generated by tools/md_to_tex.py --companion from %s -- regenerate rather than hand-edit.
%% Companion to FINAL_REVISED_MANUSCRIPT.tex; shares the bibliography with it.
\documentclass[preprint,12pt]{elsarticle}
\usepackage{amsmath,amssymb}
\usepackage{bm}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{graphicx}
\usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue]{hyperref}
\bibliographystyle{elsarticle-num}

\begin{document}
\begin{frontmatter}
\title{%s}
%% [AUTHOR INPUT REQUIRED] names, affiliations, ORCID and corresponding author, e.g.
%% \author{Firstname Lastname\corref{cor1}}
%% \ead{author@institution}
%% \affiliation{organization={...},addressline={...},city={...},country={...}}
%% \cortext[cor1]{Corresponding author.}
\author{[AUTHOR INPUT REQUIRED --- names, affiliations and corresponding author]}
\end{frontmatter}
""" % (os.path.splitext(os.path.basename(a.output))[0],
       os.path.basename(a.input), title)
    else:
        preamble = r"""%% FINAL_REVISED_MANUSCRIPT.tex
%% Generated by tools/md_to_tex.py from manuscript_IJHMT.md -- regenerate rather than hand-edit,
%% so that the .tex, the .md, the .docx and the PDF cannot drift apart.
%% Target: International Journal of Heat and Mass Transfer (Elsevier, elsarticle).
\documentclass[preprint,12pt]{elsarticle}
\usepackage{amsmath,amssymb}
\usepackage{bm}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{graphicx}
\usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue]{hyperref}
\bibliographystyle{elsarticle-num}

\begin{document}
\begin{frontmatter}
\title{%s}
%%%% [AUTHOR INPUT REQUIRED] names, affiliations, ORCID and corresponding author, e.g.
%% \author{Firstname Lastname\corref{cor1}}
%% \ead{author@institution}
%% \affiliation{organization={...},addressline={...},city={...},country={...}}
%% \cortext[cor1]{Corresponding author.}
\author{[AUTHOR INPUT REQUIRED --- names, affiliations and corresponding author]}
\begin{abstract}
%s
\end{abstract}
\begin{highlights}
%s\end{highlights}
\begin{keyword}
%s
\end{keyword}
\end{frontmatter}
    """ % (title, abstract, highlights, keywords)

    tail = r"""
%% ------------------------------------------------------------------ bibliography
%% The reference list comes from FINAL_REVISED_REFERENCES.bib (54 Crossref-verified entries);
%% numbering follows the order of first citation (elsarticle-num).
\bibliography{FINAL_REVISED_REFERENCES}

\end{document}
"""
    open(a.output, 'w', encoding='utf-8').write(preamble + '\n'.join(out) + tail)
    print('wrote', a.output, os.path.getsize(a.output), 'bytes')
    print('  equations %d, figures %d, tables %s' % (eq, fig, tab))


if __name__ == '__main__':
    sys.exit(main())
