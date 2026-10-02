import re
from collections import Counter

base = '/home/user/FEM3/'
for name in ('BFS_FEM3_main_AUDITED_FINAL.tex', 'main.tex'):
    s = open(base + name, encoding='utf-8', errors='replace').read()
    body = re.sub(r'^%.*$', '', s, flags=re.M)
    body = body[body.find('\\begin{document}'):]
    txt = re.sub(r'\\(begin|end)\{[a-zA-Z\*]+\}', ' ', body)
    txt = re.sub(r'\\[a-zA-Z]+', ' ', txt)
    words = len(txt.split())
    print('=' * 70)
    print('%s' % name)
    print('  bytes            : %d' % len(s))
    print('  words (rough)    : %d   -> ~%d pages at ~600 w/p with 8 figs' % (words, words / 600))
    print('  \\section        : %d' % len(re.findall(r'\\section\{', body)))
    print('  \\subsection     : %d' % len(re.findall(r'\\subsection\{', body)))
    print('  \\subsubsection  : %d' % len(re.findall(r'\\subsubsection\{', body)))
    print('  \\paragraph      : %d' % len(re.findall(r'\\paragraph\{', body)))
    print('  equation envs   : %d' % len(re.findall(r'\\begin\{(equation|align|gather|multline|eqnarray)\*?\}', body)))
    print('  figure envs     : %d' % len(re.findall(r'\\begin\{figure\*?\}', body)))
    print('  table envs      : %d' % len(re.findall(r'\\begin\{table\*?\}', body)))
    print('  \\cite commands  : %d (unique keys %d)' %
          (len(re.findall(r'\\cite[a-z]*?\{', body)),
           len({k for c in re.findall(r'\\cite[a-z]*?\{([^}]*)\}', body) for k in c.split(',')})))
    print('  \\input/\\include: %s' % re.findall(r'\\(?:input|include)\{([^}]*)\}', s)[:6])
    print('  --- sections:')
    for m in re.finditer(r'\\(section|subsection|subsubsection)\{([^}]*)\}', body):
        if m.group(1) == 'section':
            print('    ' + m.group(2)[:88])
        else:
            print('      %s %s' % ('  -' if m.group(1) == 'subsection' else '    +', m.group(2)[:80]))

for bib in ('BFS_FEM3_references_AUDITED_FINAL.bib', 'references_paper.bib', 'references.bib'):
    s = open(base + bib, encoding='utf-8', errors='replace').read()
    kinds = Counter(re.findall(r'@(\w+)\{', s))
    print('=' * 70)
    print('%s : %d entries %s' % (bib, sum(kinds.values()), dict(kinds)))

# the giant calculation file
s = open(base + 'BFS_FEM3_calculation_AUDITED_FINAL.tex', encoding='utf-8', errors='replace').read()
body = re.sub(r'^%.*$', '', s, flags=re.M)
print('=' * 70)
print('CALCULATION file: %d bytes' % len(s))
print('  \\section        : %d' % len(re.findall(r'\\section\{', body)))
print('  \\subsection     : %d' % len(re.findall(r'\\subsection\{', body)))
print('  \\subsubsection  : %d' % len(re.findall(r'\\subsubsection\{', body)))
print('  equation envs   : %d' % len(re.findall(r'\\begin\{(equation|align|gather|multline|eqnarray)\*?\}', body)))
print('  words (rough)   : %d' % len(re.sub(r'\\[a-zA-Z]+', ' ', body).split()))
print('  --- first 40 headings:')
for m in list(re.finditer(r'\\(section|subsection|subsubsection)\{([^}]*)\}', body))[:40]:
    print('    %-14s %s' % (m.group(1), m.group(2)[:80]))
