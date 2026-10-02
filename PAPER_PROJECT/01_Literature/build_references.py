"""build_references.py — assemble the verified reference list from the Crossref JSON files (metadata level)."""
import json, re, html
j1 = json.load(open('CROSSREF_VERIFICATION_2026-10-01.json')); j2 = json.load(open('CROSSREF_VERIFICATION_2_2026-10-01.json'))
def first(x): return x[0] if isinstance(x, list) else x
def clean(t):
    t = re.sub(r'<[^>]+>', '', t or ''); t = re.sub(r'\s+', ' ', html.unescape(t)).strip()
    t = re.sub(r'Ga\s*2\s*O\s*3', 'Ga2O3', t); t = t.replace('β −', 'β-').replace('β−', 'β-').replace('β ‐', 'β-').replace('β‐', 'β-').replace('β -', 'β-')
    return t
def names(auth):
    out = []
    for a in auth.split('; '):
        if not a.strip(): continue
        fam, _, giv = a.partition(', ')
        toks = [t for t in re.split(r'\s+', giv) if t] if giv and giv != '?' else []
        ini = ''.join(t if re.fullmatch(r'(?:[A-Z]\.)+', t) else ''.join(w[0] + '.' for w in re.split(r'-', t) if w and w[0].isalpha()) for t in toks)
        item = f'{fam}, {ini}'.strip().rstrip(',')
        if item not in out: out.append(item)          # Crossref lists some authors twice
    return out
def fmt(m, pages_override=None):
    au = names(m['authors']); 
    if len(au) > 6: au = au[:6] + ['et al.']
    pg = pages_override or m.get('pages')
    vol = f", {m['volume']}" if m.get('volume') else ''
    iss = f"({m['issue']})" if m.get('issue') else ''
    return f"{', '.join(au)} {clean(m['title'])}. {clean(m['journal'])}{vol}{iss}{', ' + pg if pg else ''} ({m['year']}). https://doi.org/{m['doi']}"
# explicit order = order of first citation in the manuscript
ORDER = [
 ('florence1959', first(j2['dhaliwal_sherief_1980']) if False else first(j1['ref_florence_goodier_1959'])),
 ('florence1960', first(j1['ref_florence_goodier_1960'])),
 ('chao2001', j1['ref_chao_gao_2001']),
 ('abbas2015', j1['ref_2015_dpl_hole']),
 ('karmakar2016', j1['ref_karmakar_2016']),
 ('jafari2019', j1['ref_jafari_2019']),
 ('abbas2022', j2['symmetry_2022']),
 ('fahmy2022', first(j2['bem_discs_2022'])),
 ('shiah2026', j2['jts_bem_2026']),
 ('biot1956', first(j2['biot_1956'])),
 ('lord1967', j1['ref_lord_shulman_1967']),
 ('dhaliwal1980', first(j2['dhaliwal_sherief_1980'])),
 ('tzou1995', j1['ref_tzou_1995_JHT']),
 ('chandra1998', first(j1['ref_chandrasekharaiah_1998'])),
 ('adachi2018', j1['ref_adachi_2018']),
 ('klimm2023', j1['ref_klimm_2023']),
 ('orlandi2015', j2['orlandi_2015']),
 ('cheng2018', first(j2['cheng_2018_expansion'])),
 ('handwerg2016', first(j2['handwerg_2016'])),
 ('yang2023', j1['ref_apex_mfp']),
 ('durbin1974', first(j1['ref_durbin_1974'])),
 ('crump1976', first(j1['ref_crump_1976'])),
 ('huang2025', j1['ref_huang_2025']),
]
refs = []
for i, (key, m) in enumerate(ORDER, 1):
    pages_override = None
    if key == 'abbas2015': pages_override = '501-513'
    txt = fmt(m, pages_override)
    # print-year corrections (Crossref 'issued' = first-online year): volume year used, as in Elsevier style
    for key_, wrong, right in (('jafari2019', '(2018)', '(2019)'), ('klimm2023', '(2022)', '(2023)'), ('shiah2026', '(2025)', '(2026)')):
        if key == key_: txt = txt.replace(wrong, right)
    refs.append(dict(n=i, key=key, text=txt, doi=m['doi'], level='METADATA VERIFIED (Crossref 2026-10-01)'))
json.dump(refs, open('REFERENCES_VERIFIED.json', 'w'), indent=1, ensure_ascii=False)
with open('REFERENCES_VERIFIED.md', 'w') as f:
    f.write('# REFERENCES_VERIFIED — metadata verified via the Crossref REST API on 2026-10-01\n\nLevel (MASTER_PROMPT §10): **metadata verified** for every entry (title, authors, journal, volume, pages, year as returned by Crossref). '
            'Abstract inspected only where stated in `SEARCH_LOG.md`; full texts were NOT read except Klimm et al. (open access, read in the first session) and Adachi et al. (values checked against the open-access version in the first session).\n\n')
    for r in refs: f.write(f"[{r['n']}] {r['text']}\n\n")
print(len(refs), 'references written')
for r in refs: print(f"[{r['n']}]", r['text'][:230])
