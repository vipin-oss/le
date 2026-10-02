#!/usr/bin/env python3
"""build_references_3.py — expand the verified reference list from 23 to 54 entries.

Source: CROSSREF_VERIFICATION_3_2026-10-02.json, whose records were read out of the
Crossref REST API (api.crossref.org/works, rows=1, field-select) on 2026-10-02.  Nothing
is invented here: every author, title, journal, volume, issue, page and DOI below is the
value Crossref returned for the query recorded with each record.  Records that Crossref
could not confirm (Lekhnitskii 1963, Savin 1961, Roache 1998, Celik et al. 2008,
Nowacki 1986) were dropped rather than back-filled; see the "_rejected" list in that file.

Usage:
    python3 build_references_3.py            # appends refs 24..54 to REFERENCES_VERIFIED.json
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'CROSSREF_VERIFICATION_3_2026-10-02.json')
REF = os.path.join(HERE, 'REFERENCES_VERIFIED.json')
LEVEL = 'METADATA VERIFIED (Crossref 2026-10-02)'

# Order = order of first citation in the expanded manuscript (Section 2 onward).
ORDER = [
    'greenlindsay1972', 'greennaghdi1993', 'hetnarski1993', 'ignaczak2010', 'straughan2011',
    'hetnarski2019', 'eslami2013', 'chandra1986', 'josephpreziosi1989', 'kaminski1990',
    'roychoudhuri2007', 'chen2001', 'majumdar1993', 'tzou2014',
    'prevost1983', 'narayanan1982', 'davies1979', 'weeks1966', 'talbot1979', 'abate2006',
    'dehoog1982',
    'ting1996', 'hwu2010', 'stroh1958', 'chen2008', 'fahmy2018',
    'pearton2018', 'galazka2022',
    'richardson1927', 'oberkampf2010', 'pelletier2000',
]

# Crossref stores some names in a form that would read badly if initialised literally.
FAMILY_OVERRIDE = {'Choudhuri': ('Roy Choudhuri', 'S. K.')}


def initials(given):
    """'Joseph' -> 'J.', 'F. R.' -> 'F.R.', 'Lewis Fry' -> 'L.F.'"""
    toks = [t for t in re.split(r'\s+', (given or '').strip()) if t]
    out = []
    for t in toks:
        if re.fullmatch(r'(?:[A-Z]\.)+', t):
            out.append(t)
        elif t.endswith('.'):
            out.append(t)
        elif t:
            out.append(t[0].upper() + '.')
    return ''.join(out)


def author_string(authors):
    names = []
    for fam, giv in authors:
        if fam in FAMILY_OVERRIDE:
            fam, giv = FAMILY_OVERRIDE[fam]
        ini = initials(giv)
        item = f'{fam}, {ini}'.strip().rstrip(',')
        if item not in names:
            names.append(item)
    if len(names) > 6:
        names = names[:6] + ['et al.']
    return ', '.join(names)


def clean(t):
    t = re.sub(r'<[^>]+>', '', t or '')
    t = re.sub(r'\s+', ' ', t).strip()
    t = re.sub(r'Ga\s*2\s*O\s*3', 'Ga2O3', t)
    for a, b in (('β −', 'β-'), ('β−', 'β-'), ('β ‐', 'β-'), ('β‐', 'β-'), ('β -', 'β-')):
        t = t.replace(a, b)
    return t


def format_ref(k, m):
    head = f'{author_string(m["authors"])} {clean(m["title"])}.'
    doi = f'https://doi.org/{m["doi"]}'
    if m['type'] in ('book', 'monograph', 'edited-book'):
        pub = clean(m['publisher'])
        if m.get('container'):
            pub = f'{pub}, {clean(m["container"])}'
        return f'{head} {pub} ({m["year"]}). {doi}'
    if m['type'] == 'book-chapter':
        return f'{head} In {clean(m["container"])}, {m["pages"]} ({m["year"]}). {doi}'
    loc = m.get('volume', '')
    if m.get('issue'):
        loc += f'({m["issue"]})'
    return f'{head} {clean(m["container"])}, {loc}, {m["pages"]} ({m["year"]}). {doi}'


def main():
    j = json.load(open(SRC, encoding='utf-8'))
    refs = json.load(open(REF, encoding='utf-8'))
    have = {r['key'] for r in refs}
    n = max(r['n'] for r in refs)
    added = []
    for k in ORDER:
        if k in have:
            raise SystemExit(f'key {k} already present in REFERENCES_VERIFIED.json')
        m = j[k]
        n += 1
        refs.append(dict(n=n, key=k, text=format_ref(k, m), doi=m['doi'], level=LEVEL))
        added.append((n, k, format_ref(k, m)))
    json.dump(refs, open(REF, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(f'REFERENCES_VERIFIED.json now holds {len(refs)} entries')
    for n, k, t in added:
        print(f'  [{n:2d}] {k}: {t}')


if __name__ == '__main__':
    main()
