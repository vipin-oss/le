#!/usr/bin/env python3
"""P19 gates: patch-table schemas, status vocabulary, DOI allowlist, no first
person in paper-facing text, and the guarantee that no .tex or .bib file of the
manuscript was touched.

Run from this directory:  python3 check_p19.py
Every check prints PASS or FAIL and the script exits non-zero on any FAIL.
"""
import csv
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
fails = []


def gate(name, ok, detail=''):
    print(('PASS  ' if ok else 'FAIL  ') + name + (('  [' + detail + ']') if detail and not ok else ''))
    if not ok:
        fails.append(name)


def rows(fname):
    with open(os.path.join(HERE, fname), newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def head(fname):
    with open(os.path.join(HERE, fname), newline='', encoding='utf-8') as f:
        return next(csv.reader(f))


STATUSES = {'VERIFIED-EXTERNALLY', 'RECORDED', 'NOT-VERIFIED', 'SOURCE NOT AVAILABLE'}

ALLOWED_DOIS = {d.lower() for d in [
    # the seven re-queried references
    '10.1103/PhysRevB.74.014110', '10.1115/1.4037775', '10.1140/epjp/i2016-16372-3',
    '10.1007/s10999-026-09892-7', '10.1115/1.4047510', '10.1007/s00339-022-05322-5',
    '10.1007/s00033-023-01996-w',
    # the fifteen author-name keys
    '10.1007/BF00253946', '10.1007/978-1-4612-0555-5', '10.1007/b97697',
    '10.1016/0020-7225(92)90141-3', '10.1016/S0167-6636(02)00278-8',
    '10.1007/978-3-030-03137-4', '10.1007/s00419-023-02364-w', '10.1088/1402-4896/ad97eb',
    '10.1108/hff-10-2023-0615', '10.1080/15376494.2023.2211065', '10.1108/hff-07-2023-0380',
    '10.1080/15376494.2023.2217420', '10.1080/15376494.2023.2291804',
    '10.1108/hff-10-2024-0804', '10.1108/hff-04-2025-0254',
    # DOIs quoted as evidence in doi_less_refs.csv (reviews, reprints, other editions)
    '10.1063/1.3128926', '10.1115/1.3641699', '10.1063/1.3057466',
    '10.1007/978-3-642-11051-1_5', '10.1190/1.9781560801931.ch3m',
    '10.1016/C2013-0-03247-1', '10.1002/9781118818275',
]}

DOI_RE = re.compile(r'10\.\d{4,9}/[^\s,;"\'\]]+')

FIRST_PERSON = re.compile(r'\b(I|we|We|our|Our|us|my|My|me)\b')

# ---------------------------------------------------------------- G1 file set
FILES = ['bib_patch.csv', 'author_name_patch.csv', 'journal_patch.csv',
         'journal_uniform_names.csv', 'r12_abstract_vs_table4.csv',
         'r15_caption_refs.csv', 'doi_less_refs.csv', 'editor_paragraph.md',
         'gl_ordering.md', 'report.md']
missing = [f for f in FILES if not os.path.exists(os.path.join(HERE, f))]
gate('G01 all ten deliverables present', not missing, str(missing))

# ---------------------------------------------------------- G2 Task 1 schema
h = head('bib_patch.csv')
gate('G02 bib_patch.csv header',
     h == ['key', 'field', 'old_value', 'new_value', 'crossref_record', 'doi',
           'source_query', 'status', 'note'], str(h))
b = rows('bib_patch.csv')
SEVEN = ['Maranganti2006', 'Julius2017', 'Ezzat2016', 'Das2026', 'Singh2020d',
         'Tiwari2022', 'Singh2023']
gate('G03 bib_patch.csv: one row per pages_fix reference, seven rows',
     len(b) == 7 and sorted(r['key'] for r in b) == sorted(SEVEN),
     str([r['key'] for r in b]))
gate('G04 bib_patch.csv: every patch is an eid (article number), never a guessed page range',
     all(r['field'] == 'eid' and re.fullmatch(r'\d{2,6}', r['new_value']) for r in b))
gate('G05 bib_patch.csv: every row carries a Crossref query and the VERIFIED-EXTERNALLY label',
     all('crossref' in r['source_query'].lower() and r['status'] == 'VERIFIED-EXTERNALLY' for r in b))

# --------------------------------------------- G3 author-name patch (Task 2)
a = rows('author_name_patch.csv')
gate('G06 author_name_patch.csv: fifteen entries, three columns of substance',
     len(a) == 15 and head('author_name_patch.csv')[:5] ==
     ['key', 'bib_file', 'bib_line', 'current_author_field', 'proposed_author_field'])
bad = []
for r in a:
    if r['proposed_author_field'].startswith('NO PATCH'):
        continue
    for part in re.split(r'\s+and\s+', r['proposed_author_field']):
        if ',' not in part:
            bad.append((r['key'], part))
gate('G07 author_name_patch.csv: every proposed author is "Surname, Given"', not bad, str(bad))
gate('G08 author_name_patch.csv: the mononym case is flagged, not inverted',
     any(r['key'] == 'Seema2024' and r['status'] == 'NOT-VERIFIED'
         and r['proposed_author_field'].startswith('NO PATCH') for r in a))

# ---------------------------------------------------- G4 journals (Task 3)
j = rows('journal_patch.csv')
gate('G09 journal_patch.csv: at least twelve rows and an ISSN or an explicit NOT ESTABLISHED',
     len(j) >= 12 and all(('NOT ESTABLISHED' in r['issn']) or re.fullmatch(r'[\dXx-]{9}',
                                                                           r['issn'].split(';')[0].strip())
                          for r in j))
gate('G10 journal_patch.csv: verified rows carry an ISSN, unverified rows do not',
     all((r['status'] == 'VERIFIED-EXTERNALLY') == ('NOT ESTABLISHED' not in r['issn']) for r in j))
u = rows('journal_uniform_names.csv')
gate('G11 journal_uniform_names.csv: ASME titles recorded as an exemption with no entry changed',
     any('ASME' in r['journal'] and r['status'] == 'RECORDED' for r in u))
gate('G12 journal_uniform_names.csv: one uniform full name per inconsistent journal',
     len(u) >= 6 and all(r['uniform_name_proposed'].strip() for r in u))

# ------------------------------------------------- G5 R12 discrepancy table
r12 = rows('r12_abstract_vs_table4.csv')
gate('G13 r12_abstract_vs_table4.csv: discrepancy columns only, no fix column',
     'fix' not in ' '.join(head('r12_abstract_vs_table4.csv')).lower() and len(r12) >= 7)
gate('G14 r12: the Green--Lindsay row records the absent row in Table 4',
     any('Lindsay' in r['item'] and 'no row' in r['table4_side'] for r in r12))
gate('G15 r12: the 9-against-7 count is stated',
     any('9' in r['discrepancy'] and '7' in r['discrepancy'] for r in r12))
gate('G16 r12: every row carries a source line number (.tex or .md)',
     all(re.search(r'\.(tex|md)(:| lines )(\d)', r['table4_file_line']) for r in r12))

# --------------------------------------------- G6 R15 caption cross-references
r15 = rows('r15_caption_refs.csv')
gate('G17 r15_caption_refs.csv: 21 in-caption references plus the statement and scan rows',
     len(r15) == 23 and sum(1 for r in r15 if r['verdict'] == 'OK') == 21)
gate('G18 r15: verdict vocabulary',
     {r['verdict'] for r in r15} <= {'OK', 'STATEMENT NOTE', 'SCAN SUMMARY'})
gate('G19 r15: the decision-sequence caption now resolves to Figure 39',
     any(r['caption_label'] == 'fig:guide' and r['printed_number_in_pdf'] == 'Figure 39'
         for r in r15))
gate('G20 r15: the scan row reports zero hard-coded numbers in captions',
     any(r['verdict'] == 'SCAN SUMMARY' and 'none found' in ' '.join(r.values()) for r in r15))

# ---------------------------------------------------- G7 DOI-less refs (Task 6)
d = rows('doi_less_refs.csv')
THIRTEEN = {'Auld1973', 'Boley1960', 'BornKarman1912', 'Cattaneo1948', 'Chadwick1960',
            'Danilovskaya1950', 'Duhamel1837', 'Gulyaev1969', 'Kumar2017', 'Love1911',
            'Nowacki1975', 'Tzou1997', 'Vernotte1958'}
gate('G21 doi_less_refs.csv: the referee list of thirteen is present',
     THIRTEEN <= {r['key'] for r in d})
gate('G22 doi_less_refs.csv: the fourteenth entry is named as such',
     len(d) == 14 and any(r['key'] == 'Scruby1990' and 'fourteenth' in r['note'] for r in d))
CATS = {'PRE-DOI JOURNAL', 'MONOGRAPH NOT REGISTERED', 'BOOK CHAPTER WITHOUT DOI',
        'JOURNAL NOT A CROSSREF MEMBER', 'EDITION MISMATCH'}
gate('G23 doi_less_refs.csv: every row has an allowed reason category',
     {r['reason_category'] for r in d} <= CATS, str({r['reason_category'] for r in d}))
gate('G24 doi_less_refs.csv: no DOI is invented for a DOI-less reference',
     all(r['doi_status'].startswith('NO DOI EXISTS') for r in d))

# ------------------------------------------------------- G8 status vocabulary
vocab_bad = []
for f in ['bib_patch.csv', 'author_name_patch.csv', 'journal_patch.csv',
          'journal_uniform_names.csv', 'r12_abstract_vs_table4.csv',
          'r15_caption_refs.csv', 'doi_less_refs.csv']:
    for i, r in enumerate(rows(f), 2):
        if r['status'] not in STATUSES:
            vocab_bad.append((f, i, r['status']))
gate('G25 status vocabulary is exactly the four permitted labels', not vocab_bad, str(vocab_bad))

# ------------------------------------------------------- G9 DOI allowlist
seen = set()
for f in FILES:
    p = os.path.join(HERE, f)
    if not os.path.exists(p):
        continue
    txt = open(p, encoding='utf-8', errors='replace').read()
    for m in DOI_RE.finditer(txt):
        seen.add(m.group(0).rstrip(').,;').lower())
unexpected = sorted(d for d in seen if d not in ALLOWED_DOIS)
gate('G26 every DOI quoted anywhere is one Crossref returned in this thread',
     not unexpected, str(unexpected))

# ------------------------------------------------------ G10 no first person
fp_bad = []
for f in ['editor_paragraph.md', 'gl_ordering.md', 'report.md']:
    p = os.path.join(HERE, f)
    txt = open(p, encoding='utf-8', errors='replace').read()
    for m in FIRST_PERSON.finditer(txt):
        fp_bad.append((f, m.group(0)))
gate('G27 no first-person pronoun in the paper-facing text', not fp_bad, str(fp_bad))

# ------------------------------------------- G11 editor paragraph length
txt = open(os.path.join(HERE, 'editor_paragraph.md'), encoding='utf-8').read()
prose = txt.split('---')[0]
prose = re.sub(r'^#.*$', '', prose, flags=re.M)
sent = [s for s in re.split(r'(?<=[.?])\s+', prose.strip()) if len(s.split()) > 3]
gate('G28 editor paragraph is three or four sentences', 3 <= len(sent) <= 4, str(len(sent)))
gate('G29 editor paragraph states the count of fourteen', 'Fourteen' in prose)

# --------------------------------------------------- G12 GL ordering (Task 7)
gl = open(os.path.join(HERE, 'gl_ordering.md'), encoding='utf-8').read()
gate('G30 gl_ordering.md: SOURCE NOT AVAILABLE is stated first',
     'SOURCE NOT AVAILABLE' in gl.split('\n')[2] or 'SOURCE NOT AVAILABLE' in gl[:400])
gate('G31 gl_ordering.md: all three locations are named with this build\'s numbering',
     all(k in gl for k in ['Eq. (38)', 'Table 15', 'Table 22']))
gate('G32 gl_ordering.md: the mapping alpha<->tau1 and h/d<->tau0 is stated',
     'α' in gl and 'τ₁' in gl and 'τ₀' in gl and 'h/d' in gl)

# --------------------------------- G13 manuscript sources untouched
try:
    st = subprocess.run(['git', 'status', '--porcelain'], cwd=REPO,
                        capture_output=True, text=True, check=True).stdout
    gate('G33 git status readable', True)
except Exception as exc:                                    # pragma: no cover
    st = ''
    gate('G33 git status readable', False, repr(exc))
dirty = []
for line in st.splitlines():
    path = line[3:].strip().strip('"')
    if path.endswith('.tex') or path.endswith('.bib') or path.endswith('.bst'):
        dirty.append(path)
p19 = os.path.abspath(os.path.join(HERE, 'check_p19.py'))
extra_py = [line[3:].strip() for line in st.splitlines()
            if line[3:].strip().endswith('.py')
            and os.path.abspath(os.path.join(REPO, line[3:].strip())) != p19
            and 'arena_deliverables' not in line]
gate('G34 no .tex, .bib or .bst file of the manuscript is modified, added or deleted',
     not dirty, str(dirty))
gate('G35 no script outside paper_v2/arena_deliverables is touched', not extra_py, str(extra_py))

# ------------------------------------------ G14 README row and no binaries
readme = open(os.path.join(REPO, 'paper_v2', 'README.md'), encoding='utf-8').read()
gate('G36 README lists P19_patches/', 'P19_patches/' in readme)
binary = [f for f in os.listdir(HERE) if f.lower().endswith(('.pdf', '.png', '.jpg', '.zip'))]
gate('G37 no binary or PDF artefact in P19_patches', not binary, str(binary))
link = [f for f in os.listdir(HERE)
        if re.search(r'drive\.google|https?://(?!api\.crossref\.org)',
                     open(os.path.join(HERE, f), encoding='utf-8', errors='replace').read())]
gate('G38 no external link other than the Crossref API', not link, str(link))

print()
if fails:
    print('%d CHECK(S) FAILED: %s' % (len(fails), '; '.join(fails)))
    sys.exit(1)
print('ALL P19 CHECKS PASSED')
