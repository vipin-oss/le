#!/usr/bin/env python3
"""Records Phase 3 in the programme state files and writes the phase manifest (file list + digests)."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

R = Path('/home/user/le')

# ---------------------------------------------------------------- manifest.txt
files = subprocess.run(['git', 'diff', '--name-only', 'ca05217', 'HEAD'], cwd=R, capture_output=True, text=True).stdout.split()
here = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=R, capture_output=True, text=True).stdout.strip()
lines = [
    'Phase 3 - mathematical audit: manifest of changed and added files',
    'branch arena/01a10176-le; baseline of the phase = ca05217 (Phase 2 tip); recorded at %s' % here,
    'digests are sha256 of the file as it stands in the working tree at the time the phase was closed;',
    'recompute with: sha256sum <path>.  Generated documents are listed with their builders, because a',
    'regeneration from the builders is what makes them reproducible.',
    '',
]
for f in sorted(set(files)):
    p = R / f
    if p.exists():
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        lines.append('%s  %s' % (h[:16], f))
    else:
        lines.append('%s  %s' % ('-' * 16, f + '  (listed by git but absent from the tree)'))
lines += ['', 'Phase deliverables:', '  Phase_03_Mathematical_Audit/REPORT.md',
          '  Phase_03_Mathematical_Audit/FINDINGS_LEDGER.json',
          '  Phase_03_Mathematical_Audit/CHANGELOG.md',
          '  Phase_03_Mathematical_Audit/verification/audit_phase3.py (25 checks, re-created after a sandbox reset)',
          '  Phase_03_Mathematical_Audit/verification/AUDIT_phase3.json',
          '  Phase_03_Mathematical_Audit/verification/audit_phase3.log',
          '  Phase_03_Mathematical_Audit/verification/patch_phase3_batch1.py, patch_phase3_batch2.py (idempotent replay)',
          '  Phase_03_Mathematical_Audit/verification/suite_rerun_20261003.log, suite_rerun_20261003b.log',
          '  PAPER_PROJECT/06_Source_Code/CODE_FREEZE_submission_2026_10_03c.json (27 files, all byte-identical)',
          '', '%d files listed.' % (len(set(files)))]
(R / 'Phase_03_Mathematical_Audit/manifest.txt').write_text('\n'.join(lines) + '\n')
print('manifest.txt: %d files' % len(set(files)))

# ---------------------------------------------------------------- STATE json
sp = R / 'SUBMISSION_PROGRAM_STATE.json'
J = json.loads(sp.read_text())
p3 = None
for ph in J['phases']:
    if str(ph.get('number', ph.get('n', ''))) == '3' or '3' == str(ph)[:1] and False:
        p3 = ph
if p3 is None and isinstance(J['phases'][2], dict):
    p3 = J['phases'][2]
print('phase 3 entry before:', json.dumps(p3)[:300] if p3 else J['phases'][2])
if isinstance(p3, dict):
    for k in list(p3):
        if 'status' in k.lower():
            p3[k] = 'complete (audit green: 22 PASS, 3 INFO, 0 FAIL; documents rebuilt and gated)'
        if 'artifacts' in k.lower() or k.lower() == 'output':
            p3[k] = 'Phase_03_Mathematical_Audit/ (REPORT.md, FINDINGS_LEDGER.json, CHANGELOG.md, manifest.txt, verification/)'
        if 'note' in k.lower():
            p3[k] = ('constitutive algebra and every printed identity re-derived from the shipped code; the validity '
                     'bound computed from the pulse width; internal designations removed with the facts kept; AI '
                     'disclosure split per journal policy; n/a build guard added; freeze submission_2026_10_03c')
J['updated'] = '2026-10-03'
J['findings_ledger'] = ('Phase_03_Mathematical_Audit/FINDINGS_LEDGER.json (16 items: 12 closed, 2 advanced, '
                        '2 open) supersedes the Phase 2 ledger as the current one; '
                        'Phase_02_Verification/FINDINGS_LEDGER.json remains the record of that phase '
                        '(43 findings: 6 closed, 1 unresolvable in this sandbox, 36 open as raised)')
J['environment_note'] = J['environment_note'].replace('pip install numpy scipy matplotlib python-docx openpyxl reportlab pymupdf',
                                                       'pip install numpy scipy matplotlib python-docx openpyxl reportlab pymupdf sympy')
sp.write_text(json.dumps(J, indent=2) + '\n')
print('STATE json updated')

# ---------------------------------------------------------------- STATE md
mp = R / 'SUBMISSION_PROGRAM_STATE.md'
t = mp.read_text()
row = [l for l in t.split('\n') if re.match(r'\|\s*3\s*\|', l)]
print('md phase-3 row before:', row[:1])
if row:
    old = row[0]
    cells = old.split('|')
    words = ('pending', 'in progress', 'next', 'not started', 'complete', 'done')
    hit = [i for i, c in enumerate(cells) if any(w in c.lower() for w in words)]
    if hit:
        cells[hit[0]] = ' complete (audit green: 22 PASS, 3 INFO, 0 FAIL; documents rebuilt and gated) |'
        t = t.replace(old, '|'.join(cells), 1)
        print('md phase-3 row status cell replaced')
    else:
        print('WARNING: no status cell recognised in the phase-3 row; row left as is')
t = t.replace('**Open findings ledger:** the current one is `Phase_02_Verification/FINDINGS_LEDGER.json` (43 findings: 6 closed, 1 recorded\nunresolvable in this sandbox, 36 open).',
              '**Open findings ledger:** the current one is `Phase_03_Mathematical_Audit/FINDINGS_LEDGER.json` (16 findings: 12 closed,\n2 advanced, 2 open - one of them the unresolved `alpha_5`, which only the authors can close). '
              '`Phase_02_Verification/FINDINGS_LEDGER.json` (43 findings) stays as that phase\'s record.')
t = t.replace('| 8 | Final audit, consistency, compile, submission checklist, cover letter | pending | `Phase_08_Final_Audit/` |',
              '| 8 | Final audit, consistency, compile, submission checklist, cover letter | pending - inherits: the suite re-run after\nthe Phase 3 code change, the CV/MCV3 order-of-agreement wording, and refreshing the historical counts in\n`13_Manuscript/CHANGELOG.md`, `FINAL_QA_REPORT.md`, `JOURNAL_FIT.md` | `Phase_08_Final_Audit/` |')
mp.write_text(t)
print('STATE md updated')
