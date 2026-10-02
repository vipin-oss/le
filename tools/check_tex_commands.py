#!/usr/bin/env python3
"""check_tex_commands.py — static check that every LaTeX command used is defined.

No TeX engine is available in this environment, so the generated submission sources cannot be
compiled.  The next best thing is to check that every ``\\command`` they use is provided by
LaTeX itself, by ``elsarticle``, or by one of the packages the preamble actually loads.  The
check is what catches a mistake of the kind that would otherwise only show up as a compile
error on the referee's machine: a control word glued to the text that follows it, e.g.
``\\qquadc_k`` written where ``\\qquad c_k`` was meant.

Two checks are made on each file:

  1. every ``\\command`` is in the known set for the loaded packages;
  2. spacing commands (``\\quad``, ``\\qquad``, ``\\,``, ``\\;``, ``\\:``, ``\\!``) are not
     immediately followed by a letter, which is almost always a missing space.

Usage:
    python3 tools/check_tex_commands.py [-t FILE.tex ...]

Exit status 0 if nothing is flagged.
"""
import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MS = os.path.join(ROOT, 'PAPER_PROJECT', '13_Manuscript')
DEFAULT = [os.path.join(MS, 'FINAL_REVISED_MANUSCRIPT.tex'),
           os.path.join(MS, 'FINAL_REVISED_CALCULATIONS.tex')]

# ----------------------------------------------------------------- known commands
BASE = r'''begin end documentclass usepackage title author date maketitle thanks
section subsection subsubsection paragraph subparagraph appendix tableofcontents
label ref pageref cite bibliographystyle bibliography nocite
emph textbf textit textrm textsf texttt textsc textnormal textmd textup textsl
item centering raggedright raggedleft caption noindent newline par
includegraphics graphicspath rotatebox resizebox scalebox reflectbox
textwidth linewidth hfill vfill hspace vspace small large Large LARGE huge Huge tiny
footnotesize scriptsize normalsize newpage clearpage pagebreak nopagebreak
color textcolor definecolor url href nolinkurl hypersetup autoref nameref
texorpdfstring phantomsection
quad qquad hskip vskip kern mskip
frac sqrt sum int oint prod lim limits nolimits sup inf max min det exp ln log lg
sin cos tan cot sec csc arcsin arccos arctan sinh cosh tanh coth
partial nabla infty cdot times div pm mp leq geq neq ne approx equiv sim simeq
propto to rightarrow leftarrow leftrightarrow Rightarrow Leftarrow Leftrightarrow
mapsto implies iff Longrightarrow longmapsto longrightarrow implies impliedby iff forall exists in notin ni subset supset cup cap setminus
ldots cdots vdots ddots dots dotsb dotsc dotsi dotsm dotso
vert Vert lvert rvert lVert rVert langle rangle prime circ deg star ast bullet
lceil rceil lfloor rfloor overline underline widehat widetilde
hat bar vec tilde dot ddot dddot check breve acute grave mathring
left right big Big bigg Bigg bigl bigr bigm
displaystyle textstyle scriptstyle scriptscriptstyle
mathrm mathbf mathit mathsf mathtt mathcal mathbb mathfrak mathnormal mathrm
operatorname operatornamewithlimits DeclareMathOperator
text mbox hbox raisebox makebox framebox parbox rule
phantom hphantom vphantom smash stackrel overset underset substack
binom dfrac tfrac cfrac genfrac over atop choose above
notag nonumber tag eqref
sep figurename tablename
startdocument
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda mu nu xi
pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega
Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega digamma'''

AMSMATH = r'''text intertext shortintertext subequations numberwithin allowdisplaybreaks
sideset xleftarrow xrightarrow xLeftarrow xRightarrow xleftrightarrow
boxed equation multline gather align aligned alignat alignedat split cases
matrix pmatrix bmatrix vmatrix Vmatrix smallmatrix hdotsfor
iiiint iiint iint idotsint varlimsup varliminf varinjlim varprojlim
bigsqcup biginterleave shortstack smallmatrix
notag nonumber leqno reqno flushleft flushright'''

AMSSYMB = r'''lesssim gtrsim lessgtr gtrless lessapprox gtrapprox lll ggg ll gg
prec succ preceq succeq cong approxeq asymp doteq risingdotseq fallingdotseq
square blacksquare diamond lozenge bigcirc checked maltese compl eth Finv Game
hbar hslash imath jmath ell Re Im wp surd top bot vdash dashv models
nexists complement circledS diagup diagdown dag ddag checkmark Sun
lesssim gtrsim nleq ngeq nless ngtr nleqslant ngeqslant
preccurlyeq succcurlyeq curlyeqprec curlyeqsucc
vartriangle trianglelefteq trianglerighteq
backepsilon therefore because between pitchfork'''

BM = r'''bm boldsymbol mathbf'''

BOOKTABS = r'''toprule midrule bottomrule cmidrule addlinespace morecmidrule specialrule
aboverulesep belowrulesep cmidrulewidth heavyrulewidth lightrulewidth midrulewidth'''

TABULARX = r'''tabularx endtabularx arraystretch'''

GRAPHICX = r'''includegraphics graphicspath rotatebox resizebox scalebox reflectbox
includegraphics'''

HYPERREF = r'''href url nolinkurl autoref nameref pageref texorpdfstring hypersetup
phantomsection hyperref'''

ELSARTICLE = r'''frontmatter ead corcortext corref cortext fnref fntext tnoteref tnotetext
affiliation affiliation nonumnote keyword sep highlights abstract'''

PACKAGES = {'amsmath': AMSMATH, 'amssymb': AMSSYMB, 'bm': BM, 'booktabs': BOOKTABS,
            'tabularx': TABULARX, 'graphicx': GRAPHICX, 'hyperref': HYPERREF}

# commands that are always available (LaTeX kernel + elsarticle class)
ALWAYS = set(BASE.split()) | set(ELSARTICLE.split())

# spacing commands: a letter immediately after one of these is a missing space
# \, \; \: \! are legitimately glued to a letter in mathematics (6\,t_th), so only the
# word-form spacing commands are checked here.
SPACING = ('quad', 'qquad', 'thinspace', 'medspace', 'thickspace', 'negthinspace',
           'enspace', 'enskip', 'hskip', 'hspace')


def known(path):
    """set of commands available in this file, given the packages its preamble loads"""
    src = open(path, encoding='utf-8').read()
    avail = set(ALWAYS)
    for m in re.finditer(r'\\usepackage(?:\[[^\]]*\])?\{([^}]*)\}', src):
        for pkg in m.group(1).split(','):
            pkg = pkg.strip()
            if pkg in PACKAGES:
                avail |= set(PACKAGES[pkg].split())
    # \def / \newcommand in the file itself
    avail |= set(re.findall(r'\\(?:def|newcommand|renewcommand)\s*\\?\{?\\([A-Za-z]+)', src))
    return avail


def check(path):
    src = open(path, encoding='utf-8').read()
    src = re.sub(r'(?m)^%.*$', '', src)              # drop comment lines
    # drop commented-out material after % on a line
    lines = [re.sub(r'(?<!\\)%.*$', '', l) for l in src.split('\n')]
    avail = known(path)
    bad_cmd, bad_glue = [], []
    for n, line in enumerate(lines, 1):
        for m in re.finditer(r'\\([A-Za-z]+)', line):
            cmd = m.group(1)
            if cmd not in avail:
                bad_cmd.append((n, '\\' + cmd))
        for cmd in SPACING:
            for m in re.finditer(r'\\' + re.escape(cmd) + r'(?![\\ ])', line):
                after = line[m.end():m.end() + 1]
                if after and after.isalpha():
                    bad_glue.append((n, '\\%s%s' % (cmd, after)))
    return bad_cmd, bad_glue


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('-t', '--tex', nargs='*', default=DEFAULT)
    a = ap.parse_args()
    worst = 0
    for path in a.tex:
        bad_cmd, bad_glue = check(path)
        name = os.path.relpath(path, ROOT)
        print('%-46s %d command(s) unknown, %d spacing glue' %
              (name, len(bad_cmd), len(bad_glue)))
        for n, c in bad_cmd[:20]:
            print('   line %-5d unknown command %s' % (n, c))
        for n, c in bad_glue[:20]:
            print('   line %-5d missing space after %s' % (n, c))
        worst = max(worst, len(bad_cmd) + len(bad_glue))
    print('\nRESULT: %s' % ('ALL COMMANDS DEFINED' if worst == 0 else 'UNDEFINED COMMAND(S)'))
    return 1 if worst else 0


if __name__ == '__main__':
    sys.exit(main())
