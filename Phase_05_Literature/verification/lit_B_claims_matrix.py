#!/usr/bin/env python3
"""lit_B_claims_matrix.py — Phase 5 (finding B21): the claim <-> citation matrix for the load-bearing citations.

For every sentence in the manuscript that carries a citation, this records the sentence, the reference(s) it
cites, and the *level of verification the project actually has* for that reference (from
01_Literature/REFERENCES_VERIFIED.json: metadata verified via Crossref, or abstract/full text inspected).

That distinction matters: a metadata-verified record shows that a paper with that title, in that journal, in that
year, exists and says what its title says. It does not show that the paper establishes the claim the sentence
attaches to it. Where the sentence uses a strong verb ("shows", "establishes", "proves", "demonstrates") over a
metadata-only citation, the claim must either be softened or the source read. This script counts and lists those
cases; it changes nothing.

Writes verification/claims_matrix.json.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJ = HERE.parents[1] / 'PAPER_PROJECT'
MS = PROJ / '13_Manuscript'

refs = json.loads((PROJ / '01_Literature' / 'REFERENCES_VERIFIED.json').read_text())
by_n = {r['n']: r for r in refs}
md = (MS / 'manuscript_IJHMT.md').read_text()

CITE = re.compile(r'\[(\d+(?:\s*[,;-]\s*\d+)*)\]')
STRONG = re.compile(r'\b(shows?\|establishes?\|proves?\|demonstrates?\|confirms?\|proved\|shown\|established'
                    r'\|derived\b|exact\b|guarantees?\|valid for\b)\b', re.I)

# section boundaries, to identify load-bearing placement (framing, model, analytical claims)
sec = None
rows = []
for line in md.split('\n'):
    m = re.match(r'^##\s+(\d+)\.\s+(.*)$', line)
    if m:
        sec = (m.group(1), m.group(2).strip())
    if not line.strip() or line.startswith('#') or line.startswith('|') or line.startswith('!['):
        continue
    for c in CITE.findall(line) or []:
        nums = []
        for part in re.split(r'[,;]', c):
            part = part.strip()
            if '-' in part:
                lo, hi = part.split('-')
                nums.extend(range(int(lo), int(hi) + 1))
            elif part.isdigit():
                nums.append(int(part))
        for n in nums:
            if n not in by_n:      # bracketed years and table notes are not citations
                continue
            r = by_n[n]
            lvl = str(r.get('level', ''))
            full = ('FULL' in lvl.upper()) or ('ABSTRACT INSPECTED' in lvl.upper()) or ('READ' in lvl.upper())
            rows.append({'section': (sec[0] + '. ' + sec[1]) if sec else '', 'ref': n,
                         'key': r.get('key', ''), 'strong_verb': bool(STRONG.search(line)),
                         'metadata_only': not full,
                         'level': lvl, 'sentence': line.strip()[:240]})

flagged = [r for r in rows if r['strong_verb'] and r['metadata_only'] and r['section'].split('.')[0] in ('1', '2', '3')]
OUT = {
    'citations_found': len(rows),
    'distinct_references_cited': len({r['ref'] for r in rows}),
    'references_total_in_list': len(refs),
    'uncited_entries': sorted({int(r['n']) for r in refs} - {r['ref'] for r in rows}),
    'sentences_with_strong_verbs_over_metadata_only_citation_in_framing_or_theory_sections': len(flagged),
    'verification_levels': {lvl: sum(1 for r in refs if str(r.get('level', '')).strip() == lvl)
                            for lvl in sorted({str(r.get('level', '')).strip() for r in refs})},
    'flagged': flagged[:24],
    'note': ('"metadata_only" means the project record for that entry is Crossref metadata; the full text was not '
             'read here (only Klimm 2023 open access and Adachi 2018 values were checked against full/open text). '
             'A flag is a prompt to soften the wording or to read the source - not an assertion that the citation '
             'is wrong.'),
}
(HERE / 'claims_matrix.json').write_text(json.dumps(OUT, indent=2))
for k in ('citations_found', 'distinct_references_cited', 'references_total_in_list', 'uncited_entries',
          'sentences_with_strong_verbs_over_metadata_only_citation_in_framing_or_theory_sections'):
    print('%s: %s' % (k, OUT[k]))
print('verification levels:', json.dumps(OUT['verification_levels'])[:400])
for f in OUT['flagged'][:6]:
    print('  flagged [%d] %s | %s' % (f['ref'], f['section'][:24], f['sentence'][:130]))
