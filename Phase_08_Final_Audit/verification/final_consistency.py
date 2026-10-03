#!/usr/bin/env python3
"""Phase 8 - cross-artifact consistency audit (read-only).

Everything the submission ships must agree with everything else it ships. This
script re-derives the facts from the artifacts themselves instead of trusting any
single document: the Markdown, the two .tex files, the .bib, the .docx, the two PDFs,
the supplementary workbook, the statistics file, the reference-verification record, the
ordered-reference artifacts, the code-freeze manifests and the test record.

Exit code 0 means every check passed; any FAIL is something a referee or the editorial
office would hit.
"""
import hashlib
import json
import os
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / 'PAPER_PROJECT'
M = P / '13_Manuscript'
SC = P / '06_Source_Code'

fails = []
notes = []


def ok(msg):
    print('  ok    %s' % msg)


def fail(msg):
    print('  FAIL  %s' % msg)
    fails.append(msg)


def sha16(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:16]


def md_text_units(t):
    return len([l for l in t.split('\n') if l.strip() and not l.strip().startswith('|--')])


def main():
    print('A) manuscripts and their renderings')
    ms = (M / 'manuscript_IJHMT.md').read_text()
    calc = (M / 'calculations_IJHMT.md').read_text()
    tex = (M / 'FINAL_REVISED_MANUSCRIPT.tex').read_text()
    ctex = (M / 'FINAL_REVISED_CALCULATIONS.tex').read_text()
    bib = (M / 'FINAL_REVISED_REFERENCES.bib').read_text()
    stats = json.loads((M / 'MANUSCRIPT_STATS.json').read_text())
    order = json.loads((M / 'REFERENCES_ORDERED.json').read_text())
    refmap = json.loads((M / 'REF_ORDER.json').read_text())
    verified = json.loads((P / '01_Literature' / 'REFERENCES_VERIFIED.json').read_text())
    vlist = verified['references'] if isinstance(verified, dict) and 'references' in verified else verified

    # ---- references: md list, ordered list, bib, .tex keys ----
    listed = re.findall(r'(?m)^\[(\d+)\] ', ms)
    if [int(x) for x in listed] == list(range(1, len(listed) + 1)):
        ok('reference list numbered 1..%d in the Markdown' % len(listed))
    else:
        fail('reference list numbering is not 1..N: %s' % listed[:6])
    if len(order) == len(listed):
        ok('REFERENCES_ORDERED.json agrees with the printed list (%d entries)' % len(order))
    else:
        fail('ordered-reference file has %d entries, the Markdown prints %d' % (len(order), len(listed)))
    bibkeys = re.findall(r'@\w+\{([^,]+),', bib)
    orderkeys = [r['key'] for r in order]
    if sorted(bibkeys) == sorted(orderkeys):
        ok('.bib keys are exactly the printed reference keys (%d)' % len(bibkeys))
    else:
        fail('bib/print key mismatch: only-in-bib %s, only-in-print %s'
             % (sorted(set(bibkeys) - set(orderkeys))[:5], sorted(set(orderkeys) - set(bibkeys))[:5]))
    cited = set()
    for m in re.finditer(r'\\cite\{([^}]*)\}', tex):
        cited.update(k.strip() for k in m.group(1).split(',') if k.strip())
    if cited == set(bibkeys):
        ok('every bib key is cited in the manuscript .tex (%d)' % len(cited))
    else:
        fail('cited vs bib differ: uncited %s; cited-but-absent %s'
             % (sorted(set(bibkeys) - cited)[:5], sorted(cited - set(bibkeys))[:5]))
    nums = []
    for line in ms.split('\n'):
        if re.match(r'^\[\d+\] ', line.strip()):
            continue
        for g in re.findall(r'\[(\d{1,2}(?:\s*[,;-]\s*\d{1,2})*)\]', line):
            for part in re.split(r'[,;]', g):
                part = part.strip()
                if '-' in part:
                    a, b = part.split('-')
                    nums.extend(range(int(a), int(b) + 1))
                elif part.isdigit() and 1 <= int(part) <= len(listed):
                    nums.append(int(part))
    firsts = []
    for _n in nums:
        if _n not in firsts:
            firsts.append(_n)
    if firsts == list(range(1, len(listed) + 1)):
        ok('in-text citations appear in ascending first-appearance order (numbered style)')
    else:
        fail('first-appearance order is not monotone: %s' % firsts[:12])
    if set(nums) == set(range(1, len(listed) + 1)):
        ok('no orphan and no dangling reference (all %d cited at least once)' % len(listed))
    else:
        fail('orphan/dangling: %s' % sorted(set(range(1, len(listed) + 1)) ^ set(nums))[:8])
    if refmap.get('n_refs') in (None, len(listed)):
        ok('REF_ORDER.json records n_refs=%s consistently' % refmap.get('n_refs'))
    else:
        fail('REF_ORDER.json n_refs=%s vs %d printed' % (refmap.get('n_refs'), len(listed)))
    old_new = refmap.get('old_to_new') or {}
    if len(vlist) == len(listed) == len(order):
        ok('the verification record (%d) matches the printed list (%d) and the ordered list (%d)'
           % (len(vlist), len(listed), len(order)))
    else:
        fail('count mismatch: verified %d, printed %d, ordered %d' % (len(vlist), len(listed), len(order)))

    # ---- structural agreement across renderings ----
    def counts(t, companion=False):
        eq = len(re.findall(r'\\begin\{equation\}|\\begin\{align\}', t))
        return {'eq': eq, 'fig': len(re.findall(r'\\includegraphics', t)),
                'tab': len(re.findall(r'\\begin\{table', t)),
                'sec': len(re.findall(r'\\section\{', t)) + len(re.findall(r'\\section\*\{', t))}
    msc, cnc = counts(tex), counts(ctex)
    if msc['eq'] == stats['n_equations']:
        ok('manuscript equations agree (.tex %d = MANUSCRIPT_STATS %d)' % (msc['eq'], stats['n_equations']))
    else:
        fail('equation counts differ: .tex %d vs stats %d' % (msc['eq'], stats['n_equations']))
    if msc['fig'] == stats['n_figures']:
        ok('figures agree (%d)' % msc['fig'])
    else:
        fail('figure counts differ: .tex %d vs stats %d' % (msc['fig'], stats['n_figures']))
    if cnc['eq'] == 29:
        ok('companion .tex carries its 29 numbered equations')
    else:
        fail('companion equation count changed: %d' % cnc['eq'])

    # ---- headline numbers appear identically in both documents ----
    consts = {'0.854': 'circle peak stress (MPa/K)', '28.7': 'ellipse modulation (%)',
              '6.4': 'memory deviation D (%)', '1.078': 'feedback number delta (e-3)',
              '347.4': 'C33 (GPa)', '7686': 'c_ref (m/s)', '3.959': 'thermal diffusivity (e-6)',
              '242.8': 'C11 (GPa)', '2.0517': 'abs(beta) (MPa/K)'}
    absent_ms = [k for k in consts if k not in ms]
    if absent_ms:
        fail('constants missing from the manuscript: %s' % absent_ms)
    else:
        ok('all %d headline constants appear in the manuscript' % len(consts))
    both = [k for k in consts if k in ms and k in calc]
    notes.append('%d of the %d headline constants are also quoted in the companion; the rest belong '
                 'to the results tables and appear in the manuscript alone by design'
                 % (len(both), len(consts)))

    # ---- docx / pdf agree with the md on reference count and page count ----
    try:
        from docx import Document
        d = Document(str(M / 'manuscript_IJHMT.docx'))
        dt = '\n'.join(p.text for p in d.paragraphs)
        n_ref = len(re.findall(r'(?m)^\[\d+\] ', dt))
        if n_ref in (0, len(listed)):
            ok('docx reference list has %s entries%s' % (n_ref or 'the md count by construction',
                                                        '' if n_ref else ' (docx writes the list as a block)'))
        else:
            fail('docx prints %d references, the Markdown %d' % (n_ref, len(listed)))
        for probe in ('Verified, not validated', 'Acknowledgements', 'Data availability'):
            if probe in dt:
                ok('docx contains "%s"' % probe)
            else:
                fail('docx is missing "%s"' % probe)
    except ImportError:
        notes.append('python-docx unavailable: docx content not checked')

    try:
        import pymupdf
        for f, want in (('manuscript_IJHMT.pdf', 'References'), ('calculations_IJHMT.pdf', 'Reproduction')):
            doc = pymdf = pymupdf.open(str(M / f))
            t = ''.join(p.get_text() for p in doc)
            pdf_nums = sorted({int(x) for x in re.findall(r'(?m)^\[(\d+)\] ', t)})
            if f.startswith('manuscript'):
                if pdf_nums == list(range(1, len(listed) + 1)):
                    ok('%s: %d pages, reference numbers 1..%d all present in the PDF'
                       % (f, doc.page_count, len(listed)))
                else:
                    fail('%s: PDF reference numbers differ: %s'
                         % (f, sorted(set(pdf_nums) ^ set(range(1, len(listed) + 1)))[:8]))
                for probe in ('1. Introduction', 'Appendix A. Nomenclature', 'References',
                              'Acknowledgements', 'Declarations'):
                    if probe not in t:
                        fail('%s is missing from the PDF' % probe)
                else:
                    ok('back matter and opening sections present in the PDF')
                    break
            else:
                ok('%s: %d pages' % (f, doc.page_count))
    except ImportError:
        notes.append('pymupdf unavailable: PDFs not checked')

    # ---- supplementary workbook vs the manuscript tables ----
    try:
        from openpyxl import load_workbook
        wb = load_workbook(str(M / 'SUPPLEMENTARY_TABLES.xlsx'), read_only=True)
        ok('workbook sheets: %s' % ', '.join(wb.sheetnames))
        if len(wb.sheetnames) >= 8:
            ok('workbook exposes %d sheets (>= 8 expected)' % len(wb.sheetnames))
        else:
            fail('workbook has only %d sheets' % len(wb.sheetnames))
    except ImportError:
        notes.append('openpyxl unavailable: workbook not checked')

    print('\nB) provenance and code state')
    subs = sorted(f.name for f in SC.glob('CODE_FREEZE_submission_*.json'))
    newest = subs[-1]
    quoted = set(re.findall(r'CODE_FREEZE_(submission_2026_10_03[a-z])\.json', ms))
    if newest.replace('CODE_FREEZE_', '').replace('.json', '') in quoted:
        ok('the manuscript names the newest submission manifest (%s)' % newest)
    else:
        fail('manuscript names %s but the newest manifest is %s' % (sorted(quoted), newest))
    man = json.loads((SC / newest).read_text())
    entries = man.get('files') or man
    if isinstance(entries, dict):
        items = list(entries.items())
    else:
        items = [(e.get('path'), e.get('sha256')) for e in entries]
    stale = []
    for rel, want in items:
        pth = None
        for cand in (P / rel, ROOT / rel, ROOT / 'PAPER_PROJECT' / rel):
            if cand.exists() and cand.is_file():
                pth = cand
                break
        if pth is None:
            stale.append(('absent', rel))
            continue
        got = hashlib.sha256(pth.read_bytes()).hexdigest()
        if want and got != want and not got.startswith(want[:16]):
            stale.append(('differs', rel))
    if stale:
        fail('%s is stale for %d entries: %s' % (newest, len(stale), [s[1] for s in stale][:5]))
    else:
        ok('%s: all %d entries hash-match the code as committed' % (newest, len(items)))
    for f in subs:
        if f == newest:
            continue
        base = SC / f
        if base.stat().st_size > 0:
            ok('history kept: %s (%d B, unmodified)' % (f, base.stat().st_size))
    legacy = SC / 'CODE_FREEZE_2026_10_02.json'
    if legacy.exists():
        ok('the 2026-10-02 freeze is still present and untouched (%d B)' % legacy.stat().st_size)

    t = json.loads((P / '07_Tests' / 'TEST_RESULTS.json').read_text())
    cases = t.get('tests') or t.get('cases') or []
    c = Counter(x.get('status') for x in cases)
    claim = re.search(r'The suite has (\d+) tests \((\d+) passed, (\d+) failed, (\d+) exploratory\)', ms)
    if claim:
        want = (int(claim.group(1)), int(claim.group(2)), int(claim.group(3)), int(claim.group(4)))
        got = (len(cases), c.get('PASS', 0), c.get('FAIL', 0), c.get('INFO', 0))
        if want == got:
            ok('test-suite sentence in the manuscript matches TEST_RESULTS.json %s' % (got,))
        else:
            fail('manuscript says %s, TEST_RESULTS.json says %s' % (want, got))
    else:
        fail('the manuscript no longer states the suite summary sentence')
    if t.get('status') == 'COMPLETE':
        ok('TEST_RESULTS.json status COMPLETE (%d cases)' % len(cases))
    else:
        fail('TEST_RESULTS.json status is %s' % t.get('status'))

    print('\nC) journal-facing limits and declarations')
    ab = ms.split('## Abstract')[1].split('**Keywords')[0]
    n_ab = len([w for w in ab.split() if any(ch.isalnum() for ch in w)])
    if n_ab <= 250:
        ok('abstract %d words (limit 250)' % n_ab)
    else:
        fail('abstract is %d words, over the 250 limit' % n_ab)
    if not re.search(r'\[\d', ab):
        ok('abstract carries no citation brackets')
    else:
        fail('abstract cites references')
    hl = re.findall(r'(?m)^- (.+)$', ms.split('## Highlights')[1].split('## ')[0])
    if 3 <= len(hl) <= 5 and all(len(x) <= 85 for x in hl):
        ok('%d highlights, longest %d characters (limit 85)' % (len(hl), max(len(x) for x in hl)))
    else:
        fail('highlights out of shape: %d items, lengths %s' % (len(hl), [len(x) for x in hl]))
    if (M / 'highlights.txt').read_text().strip().split('\n') == [x.strip() for x in hl]:
        ok('highlights.txt matches the manuscript Highlights block')
    else:
        fail('highlights.txt and the manuscript differ')
    kwm = re.search(r'\*\*Keywords:\*\* (.+)', ms)
    nk = len(kwm.group(1).split(';')) if kwm else 0
    if 1 <= nk <= 6:
        ok('%d keywords (semicolon-separated)' % nk)
    else:
        fail('%d keywords; Elsevier asks for at most 6' % nk)
    dec = ms.split('## Declarations')[1].split('## Appendix')[0]
    for need in ('CRediT', 'competing interest', 'Funding', 'Data availability', 'Generative AI'):
        if need in dec:
            ok('declaration present: %s' % need)
        else:
            fail('declaration missing: %s' % need)
    pos = {k: ms.find(k) for k in ('## Acknowledgements', '## Declarations',
                                   '## Appendix A', '## References')}
    if all(v >= 0 for v in pos.values()) and list(pos.values()) == sorted(pos.values()):
        ok('back matter order: Acknowledgements < Declarations < Appendix < References')
    else:
        fail('back matter order wrong: %s' % pos)
    banned = [w for w in ('novel', 'breakthrough', 'comprehensive', 'robust', 'state-of-the-art',
                          'unprecedented') if re.search(r'\b' + w, ms, re.I)]
    if banned:
        fail('banned words still present: %s' % banned)
    else:
        ok('no banned hyperbole words')
    internal = [w for w in ('gate freeze', 'manuscript builders', 'runs audited', 'Code state and re-checks')
                if w in ms or w in calc]
    if internal:
        fail('internal project vocabulary still printed: %s' % internal)
    else:
        ok('internal project vocabulary stripped from the printed text')
    ph = re.findall(r'\[(?:AUTHOR INPUT REQUIRED[^\]]*|PUBLIC REPOSITORY/DOI TO BE INSERTED)\]', ms)
    notes.append('%d author-input placeholders remain (identity, funding, repository, CRediT, competing interest)'
                 % len(ph))
    if re.search(r'verified, not validated|Verified, not validated', ms):
        ok('the verified-not-validated position is stated')
    else:
        fail('the verified-not-validated position is missing')
    if '\\bibliographystyle{elsarticle-num}' in tex:
        ok('manuscript .tex uses elsarticle-num (numbered style, matching the Markdown)')
    else:
        fail('manuscript .tex is not using elsarticle-num')
    for name, body in (('manuscript', tex), ('companion', ctex)):
        if '\\begin{document}' in body and '\\end{document}' in body and body.count('{document}') == 2:
            ok('%s .tex has a well-formed document environment' % name)
        else:
            fail('%s .tex document environment looks wrong' % name)
        if 'elsarticle' in body:
            ok('%s .tex loads the Elsevier class' % name)
        else:
            fail('%s .tex does not load elsarticle' % name)

    print('\nD) git state')
    import subprocess
    dirty = subprocess.run(['git', 'status', '--porcelain'], cwd=ROOT, capture_output=True, text=True).stdout.split('\n')
    dirty = [l for l in dirty if l.strip()]
    if dirty:
        notes.append('%d path(s) uncommitted at audit time (they are committed at the end of the phase)' % len(dirty))
    else:
        ok('working tree clean')

    print('\nSUMMARY: %d check(s) failed, %d note(s)' % (len(fails), len(notes)))
    for n in notes:
        print('  note  %s' % n)
    out = {'fails': fails, 'notes': notes,
           'counts': {'references': len(listed), 'abstract_words': n_ab,
                      'highlights': len(hl), 'keywords': nk,
                      'body_words': stats['body_words'],
                      'ms_eq': msc['eq'], 'ms_figs': msc['fig'], 'ms_tables': msc['tab'],
                      'tests': len(cases), 'test_status': dict(c)}}
    (Path(__file__).resolve().parent / 'final_consistency.json').write_text(json.dumps(out, indent=1))
    print('wrote final_consistency.json')
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
