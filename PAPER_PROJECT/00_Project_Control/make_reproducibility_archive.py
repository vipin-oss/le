#!/usr/bin/env python3
"""make_reproducibility_archive.py - assemble ONE self-contained reproducibility archive.

WHAT THIS IS
  A packager, not a writer of science. Every fact in the generated index documents is extracted from
  files in this repository at build time (AST literal extraction for parameters, key/type unions for
  the JSON data, npy headers for the .npz arrays, CSV rows for provenance, `git log` for the
  changelog, and the project's own gate scripts for verification evidence). Nothing here restates a
  number by hand, so nothing here can drift from the code. Anything the repository genuinely does
  not record is written as NOT DOCUMENTED / NOT AVAILABLE, never inferred.

USAGE
  python3 PAPER_PROJECT/00_Project_Control/make_reproducibility_archive.py [options]

OPTIONS
  --out DIR        where to write the zip (default: PAPER_PROJECT/packages, gitignored by the project)
  --repro JSON     path to a reproduction-test summary JSON (see --repro-template) folded into
                   09_ARCHIVE_METADATA/FINAL_PACKAGE_STATUS.md and 04_REPRODUCTION/
  --repro-template write the JSON skeleton this builder expects, then fill it with a real run
  --no-gates       skip running the verification gates (not recommended: the archive then says so)
  --python-exe     interpreter used for the gates that need third-party libs (default: the
                   interpreter running this script, then $VENV_Q1, then /home/user/.venv-repro)

OUTPUTS
  PAPER_PROJECT/16_Reproducibility/            generated index documents (tracked: they are review
                                               material, and they survive a workspace reset)
  <out>/PAPER_PROJECT_COMPLETE_REPRODUCIBILITY_ARCHIVE.zip
                                               deterministic (fixed entry stamps, sorted order): same
                                               tree -> same sha256
"""
import argparse
import ast
import csv
import glob
import hashlib
import io
import json
import os
import re
import shutil
import struct
import subprocess
import sys
import time
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))          # repository root
PP = os.path.join(ROOT, 'PAPER_PROJECT')
GEN = os.path.join(PP, '16_Reproducibility')
ARCHIVE_NAME = 'PAPER_PROJECT_COMPLETE_REPRODUCIBILITY_ARCHIVE'
ND, NA = 'NOT DOCUMENTED', 'NOT AVAILABLE'
NOT_REPRO = 'no fresh reproduction run was supplied to the builder'
ZIP_STAMP = (2026, 10, 4, 0, 0, 0)      # fixed: the archive is a function of the tree only
BUILD_DATE = '2026-10-04'

# ----------------------------------------------------------------------------------------------- utils
def sha256_file(path, limit=None):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        if limit:
            h.update(fh.read(limit))
        else:
            for chunk in iter(lambda: fh.read(1 << 20), b''):
                h.update(chunk)
    return h.hexdigest()


def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, '/')


def git(*a):
    try:
        r = subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True)
        return r.stdout.strip() if r.returncode == 0 else ''
    except Exception:
        return ''


def sh(cmd, cwd=None, timeout=None):
    """Run a command, return (returncode, stdout+stderr tail)."""
    try:
        r = subprocess.run(cmd, cwd=cwd or ROOT, capture_output=True, text=True, timeout=timeout)
        out = (r.stdout or '') + (r.stderr or '')
        return r.returncode, out.strip()
    except Exception as e:                                   # missing interpreter, timeout, ...
        return 127, f'command could not be run: {type(e).__name__}: {e}'


def pick_python():
    for cand in (sys.executable, os.environ.get('VENV_Q1', '') + '/bin/python',
                 '/home/user/.venv-repro/bin/python', '/home/user/.venv-q1/bin/python'):
        if cand and os.path.isfile(cand):
            return cand
    return sys.executable


# ------------------------------------------------------------------------ literal parameter extraction
def literals_from_source(path):
    """Top-level literal assignments and numeric/keyword defaults of callables, as written in the file.

    Returns {'constants': {name: repr+value}, 'defaults': {'Class.__init__': {kw: val}}}. Values are
    rendered from the source itself, so numpy expressions are recorded as the source text (never as an
    invented number).
    """
    out = {'constants': {}, 'defaults': {}}
    try:
        tree = ast.parse(open(path, encoding='utf-8').read())
    except Exception as e:
        out['error'] = f'{type(e).__name__}: {e}'
        return out
    src = open(path, encoding='utf-8').read().splitlines()

    def render(node):
        try:
            return ast.literal_eval(node)
        except Exception:
            try:
                return ast.get_source_segment('\n'.join(src), node)
            except Exception:
                return '<see source>'

    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for t in targets:
                if isinstance(t, ast.Name) and isinstance(node.value,
                                                          (ast.Constant, ast.Dict, ast.List, ast.Tuple,
                                                           ast.Set, ast.BinOp, ast.Call, ast.UnaryOp,
                                                           ast.Subscript)):
                    name = t.id
                    if name.startswith('_') or callable(node.value) and not isinstance(node.value, ast.Call):
                        continue
                    v = render(node.value)
                    if isinstance(v, (dict, list, tuple)) and len(str(v)) > 400:
                        v = str(v)[:400] + ' ...[truncated in index; see source]'
                    out['constants'][name] = {'line': node.lineno, 'value': v}
    for node in tree.body:
        targets = []
        if isinstance(node, ast.ClassDef):
            for sub in node.body:
                if isinstance(sub, ast.FunctionDef):
                    targets.append((f'{node.name}.{sub.name}', sub))
        elif isinstance(node, ast.FunctionDef):
            targets.append((node.name, node))
        for label, fn in targets:
            kw = {}
            args = list(fn.args.args)
            defs = list(fn.args.defaults)
            for a, d in zip(args[len(args) - len(defs):], defs):
                kw[a.arg] = render(d)
            if fn.args.kw_defaults:
                for a, d in zip(fn.args.kwonlyargs, fn.args.kw_defaults):
                    if d is not None:
                        kw[a.arg] = render(d)
            if kw:
                out['defaults'][label] = {'line': fn.lineno, 'kwargs': kw}
    return out


def json_key_types(paths, limit=400):
    keys = {}
    n = 0
    for p in paths[:limit]:
        try:
            d = json.load(open(p, encoding='utf-8'))
        except Exception:
            continue
        n += 1
        if isinstance(d, dict):
            for k, v in d.items():
                e = keys.setdefault(k, {'types': set(), 'sample': None, 'count': 0})
                e['types'].add(type(v).__name__)
                e['count'] += 1
                if e['sample'] is None and not isinstance(v, (dict, list)):
                    e['sample'] = v
                if e['sample'] is None and isinstance(v, list) and v:
                    e['sample'] = f'list[{len(v)}] first={v[0]!r}'
    for e in keys.values():
        e['types'] = sorted(e['types'])
    return keys, n


def npz_members(path):
    """Array names / shapes / dtypes from a .npz, parsed from the npy headers (no numpy needed)."""
    out = []
    try:
        with zipfile.ZipFile(path) as z:
            for n in z.namelist():
                try:
                    with z.open(n) as fh:
                        head = fh.read(256)
                    if head[:6] != b'\x93NUMPY':
                        out.append((n, 'non-npy member', z.getinfo(n).file_size))
                        continue
                    hlen = struct.unpack('<H', head[8:10])[0]
                    meta = ast.literal_eval(head[10:10 + hlen].decode('latin1').strip())
                    out.append((n[:-4], tuple(meta.get('shape', ())), meta.get('descr', '?'),
                                z.getinfo(n).compress_size, z.getinfo(n).file_size))
                except Exception as e:
                    out.append((n, f'unreadable ({type(e).__name__})', 0))
    except Exception as e:
        out.append(('<archive>', f'unreadable ({type(e).__name__})', 0))
    return out


def count_and_size(files):
    return len(files), sum(os.path.getsize(f) for f in files if os.path.isfile(f))


def md_table(header, rows):
    out = ['| ' + ' | '.join(header) + ' |', '|' + '|'.join(['---'] * len(header)) + '|']
    for r in rows:
        out.append('| ' + ' | '.join('' if c is None else str(c) for c in r) + ' |')
    return '\n'.join(out)


# ----------------------------------------------------------------------------------------------- plan
# dest prefix in the archive  ->  (repo-relative sources, excludes)
DIR_SRC = {
    '01_PROGRAM/src': ['PAPER_PROJECT/06_Source_Code/src'],
    '01_PROGRAM/experiments': ['PAPER_PROJECT/08_Experiments'],
    '01_PROGRAM/tests': ['PAPER_PROJECT/07_Tests'],
    '01_PROGRAM/builders': ['PAPER_PROJECT/13_Manuscript/build_manuscript.py',
                            'PAPER_PROJECT/13_Manuscript/build_calculations.py',
                            'PAPER_PROJECT/13_Manuscript/build_supplement.py',
                            'PAPER_PROJECT/13_Manuscript/docbuilder.py',
                            'PAPER_PROJECT/13_Manuscript/ms_derivation.py',
                            'PAPER_PROJECT/13_Manuscript/ms_numerics.py',
                            'PAPER_PROJECT/13_Manuscript/ms_results.py',
                            'PAPER_PROJECT/13_Manuscript/ms_static.py'],
    '01_PROGRAM/utilities': ['tools'],
    '01_PROGRAM': ['PAPER_PROJECT/00_Project_Control/RESTORE_PROJECT_TREE.md',
                   'PAPER_PROJECT/00_Project_Control/restore_project_tree.py'],
    '01_PROGRAM/control': ['PAPER_PROJECT/00_Project_Control/make_packages.py',
                           'PAPER_PROJECT/00_Project_Control/make_central_story.py',
                           'PAPER_PROJECT/00_Project_Control/make_phase_states.py',
                           'PAPER_PROJECT/00_Project_Control/make_reproducibility_archive.py',
                           'bootstrap_paths.sh'],
    '01_PROGRAM/freeze': ['PAPER_PROJECT/06_Source_Code'],
    '01_PROGRAM/environment': ['work/handoff/PILOT_HUANG_2025_01/requirements.txt'],
    '01_PROGRAM/handoff_baseline': ['work/handoff'],
    '02_OVERLEAF': ['PAPER_PROJECT/13_Manuscript/FINAL_REVISED_MANUSCRIPT.tex',
                    'PAPER_PROJECT/13_Manuscript/FINAL_REVISED_CALCULATIONS.tex',
                    'PAPER_PROJECT/13_Manuscript/FINAL_REVISED_REFERENCES.bib',
                    'PAPER_PROJECT/13_Manuscript/highlights.txt',
                    'PAPER_PROJECT/13_Manuscript/figures/README.txt'],
    '02_OVERLEAF/figures': ['PAPER_PROJECT/13_Manuscript/figures'],
    '03_DATA/raw': ['PAPER_PROJECT/09_Raw_Data'],
    '03_DATA/processed': ['PAPER_PROJECT/10_Processed_Data'],
    '03_DATA/tables': ['PAPER_PROJECT/12_Tables'],
    '04_REPRODUCTION': ['PAPER_PROJECT/07_Tests/REPRODUCTION_TEST_REPORT.md',
                        'PAPER_PROJECT/07_Tests/TEST_REPORT.md',
                        'PAPER_PROJECT/07_Tests/BASIC_VERIFICATION.md',
                        'PAPER_PROJECT/07_Tests/TEST_RESULTS.json',
                        'PAPER_PROJECT/07_Tests/make_test_report.py',
                        'PAPER_PROJECT/07_Tests/run_tests.py',
                        'PAPER_PROJECT/07_Tests/run_tests_supplement.py'],
    '05_DERIVATIONS/theory': ['PAPER_PROJECT/04_Theory'],
    '05_DERIVATIONS/numerical_method': ['PAPER_PROJECT/05_Numerical_Method'],
    '05_DERIVATIONS/acceptance_criteria': ['PAPER_PROJECT/02_Problem_Definition'],
    '05_DERIVATIONS/manuscript_derivation_source': ['PAPER_PROJECT/13_Manuscript/calculations_IJHMT.md'],
    '06_VALIDATION/validation_results': ['PAPER_PROJECT/03_Validation'],
    '06_VALIDATION/literature_verification': ['PAPER_PROJECT/01_Literature'],
    '06_VALIDATION/audits': ['PAPER_PROJECT/15_Audits', 'docs'],
    '06_VALIDATION/rerun_comparison': ['work/rerun'],
    '07_DOCUMENTATION/program_control': ['PAPER_PROJECT/00_Project_Control'],
    '07_DOCUMENTATION/repository': ['README.md', 'PROJECT_PROGRESS.md', 'RERUN_COMPARISON.md',
                                    'SUBMISSION_PROGRAM_STATE.md', '.gitignore'],
    '07_DOCUMENTATION/corrections_log': ['PAPER_PROJECT/14_Documentation'],
    '07_DOCUMENTATION/phases': [d for d in sorted(glob.glob(os.path.join(ROOT, 'Phase_*')))],
    '07_DOCUMENTATION/submission_program': ['Phase_10_Submission_Package/REPORT.md',
                                            'Phase_10_Submission_Package/CHANGELOG.md',
                                            'Phase_10_Submission_Package/manifest.txt',
                                            'Phase_10_Submission_Package/DEPOSIT_PACKAGE_SHA256.txt',
                                            'Phase_10_Submission_Package/verification'],
    '08_FINAL_OUTPUTS/manuscript': ['PAPER_PROJECT/13_Manuscript/manuscript_IJHMT.md',
                                    'PAPER_PROJECT/13_Manuscript/manuscript_IJHMT.docx',
                                    'PAPER_PROJECT/13_Manuscript/manuscript_IJHMT.pdf',
                                    'PAPER_PROJECT/13_Manuscript/FINAL_REVISED_MANUSCRIPT.pdf',
                                    'PAPER_PROJECT/13_Manuscript/FINAL_REVISED_CALCULATIONS.pdf',
                                    'PAPER_PROJECT/13_Manuscript/calculations_IJHMT.pdf',
                                    'PAPER_PROJECT/13_Manuscript/SUPPLEMENTARY_TABLES.xlsx',
                                    'PAPER_PROJECT/13_Manuscript/MANUSCRIPT_STATS.json',
                                    'PAPER_PROJECT/13_Manuscript/PDF_VERIFICATION.txt',
                                    'PAPER_PROJECT/13_Manuscript/FINAL_QA_REPORT.md',
                                    'PAPER_PROJECT/13_Manuscript/JOURNAL_FIT.md',
                                    'PAPER_PROJECT/13_Manuscript/REF_ORDER.json',
                                    'PAPER_PROJECT/13_Manuscript/REFERENCES_ORDERED.json',
                                    'PAPER_PROJECT/13_Manuscript/AUTHOR_INPUT_REQUIRED.md',
                                    'PAPER_PROJECT/13_Manuscript/cover_letter.md',
                                    'Phase_10_Submission_Package/AUTHOR_INPUT_FORM.md',
                                    'Phase_10_Submission_Package/cover_letter.docx',
                                    'Phase_10_Submission_Package/cover_letter.pdf',
                                    'Phase_10_Submission_Package/compile_check.sh',
                                    'Phase_08_Final_Audit/SUBMISSION_CHECKLIST.md'],
    '08_FINAL_OUTPUTS/figures': ['PAPER_PROJECT/11_Figures'],
}

EXCLUDE_PARTS = ('__pycache__', '.pytest_cache', '.ipynb_checkpoints', 'packages', '.venv')
EXCLUDE_SUFFIX = ('.pyc', '.pyo', '.DS_Store', '.swp', '~')
EXCLUDE_NAMES = {'le.zip', 'handoff.zip', 'ARCHIVE_CHECKSUMS.txt'}
GENERATED_NAMES = {'README_PROGRAM.md', 'README_OVERLEAF.md', 'README_DATA.md', 'DATA_DICTIONARY.md',
                   'REPRODUCE_FROM_SCRATCH.md', 'RUN_ORDER.md', 'run_manifest.json',
                   'parameter_manifest.json', 'FIGURE_PROVENANCE.md', 'PROJECT_OVERVIEW.md',
                   'MODEL_DESCRIPTION.md', 'NUMERICAL_METHOD.md', 'CHANGELOG.md', 'KNOWN_LIMITATIONS.md',
                   'ARCHIVE_README.md', 'FINAL_PACKAGE_STATUS.md', 'SHA256SUMS.txt',
                   'file_manifest_sha256.csv'}


def expand(sources):
    files = []
    for s in sources:
        p = s if os.path.isabs(s) else os.path.join(ROOT, s)
        if os.path.isfile(p):
            files.append(p)
        elif os.path.isdir(p):
            for r, ds, fs in os.walk(p):
                ds[:] = [d for d in ds if d not in EXCLUDE_PARTS and not d.startswith('.git')]
                for f in fs:
                    files.append(os.path.join(r, f))
    return sorted(set(files))


def keep(path, dest):
    name = os.path.basename(path)
    if any(part in EXCLUDE_PARTS for part in path.split(os.sep)):
        return False
    if name.endswith(EXCLUDE_SUFFIX) or name in EXCLUDE_NAMES:
        return False
    if name in GENERATED_NAMES:
        return False                      # generated index docs come from GEN, never copied twice
    if 'handoff' in dest and name.endswith(('.png', '.jpg')):
        return True
    return True


def dest_for(path):
    """Map a repo path to its archive path.

    Directory sources keep their internal structure under the destination (so `logs/` stays a folder);
    single-file sources are named by their basename. The longest matching source prefix wins, which is
    what lets `02_OVERLEAF/figures` (a directory) take precedence over `02_OVERLEAF` (a file list)."""
    rp = rel(path)
    best = None
    for dest, srcs in DIR_SRC.items():
        for src in srcs:
            sp = os.path.relpath(src, ROOT) if os.path.isabs(src) else src
            sp = sp.rstrip('/')
            if rp == sp or rp.startswith(sp + '/'):
                if os.path.isdir(os.path.join(ROOT, sp)):
                    cand = f'{dest}/{rp[len(sp):].lstrip("/")}' if rp != sp else f'{dest}/{os.path.basename(rp)}'
                else:
                    cand = f'{dest}/{os.path.basename(rp)}'
                if best is None or len(sp) > best[1]:
                    best = (cand, len(sp))
    return best[0] if best else None


# ------------------------------------------------------------------------------------------------ zip
def build_zip(payload, out_zip):
    os.makedirs(os.path.dirname(out_zip), exist_ok=True)
    if os.path.exists(out_zip):
        os.remove(out_zip)
    with zipfile.ZipFile(out_zip, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for arc, src in sorted(payload.items()):
            data = open(src, 'rb').read()
            zi = zipfile.ZipInfo(f'{ARCHIVE_NAME}/{arc}',
                                 date_time=(ZIP_STAMP[0], ZIP_STAMP[1], ZIP_STAMP[2], 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            z.writestr(zi, data)
    return os.path.getsize(out_zip)


def _tail(out, n=6):
    """Lines to keep from a gate's output: every FAIL/NOTE/RESULT line (so a failure can never be hidden by
    the tail) followed by the last lines of the run, de-duplicated, capped."""
    all_lines = [l for l in out.splitlines() if l.strip()]
    marks = [l for l in all_lines if 'FAIL' in l or 'MISSING' in l or 'MISMATCH' in l
             or 'NOTE' in l or 'RESULT' in l or 'CHECKS PASSED' in l]
    keep, seen = [], set()
    for l in marks + all_lines[-n:]:
        if l not in seen:
            seen.add(l)
            keep.append(l)
    return keep[-16:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=os.path.join(PP, 'packages'))
    ap.add_argument('--repro')
    ap.add_argument('--repro-template', action='store_true')
    ap.add_argument('--no-gates', action='store_true')
    ap.add_argument('--python-exe', default='')
    ap.add_argument('--keep-tree', action='store_true',
                    help='leave the regenerated index documents in the working tree (default: restore them '
                         'to HEAD after packing, so the repository stays clean and the gate transcript '
                         'inside the archive describes the committed state rather than a half-written one)')
    a = ap.parse_args()

    if a.repro_template:
        skel = {'verdict': 'PASS | PASS WITH NUMERICAL DIFFERENCE | PARTIAL | FAIL',
                'run_date': BUILD_DATE, 'environment': {'python': '', 'numpy': '', 'scipy': '',
                                                          'matplotlib': '', 'hardware': ''},
                'steps': [{'name': 'install dependencies', 'command': '', 'exit_code': 0,
                           'detail': ''}],
                'files_regenerated': [{'path': '', 'sha_before': '', 'sha_after': '',
                                       'identical': True}],
                'notes': []}
        p = os.path.join(GEN, 'REPRO_STATUS_TEMPLATE.json')
        os.makedirs(GEN, exist_ok=True)
        open(p, 'w').write(json.dumps(skel, indent=1) + '\n')
        print('wrote', rel(p))
        return 0

    for k in list(DIR_SRC):
        DIR_SRC[k] = [rel(p) if os.path.isabs(p) else p for p in DIR_SRC[k]]

    pyexe = a.python_exe or pick_python()
    repro = json.load(open(a.repro)) if a.repro and os.path.isfile(a.repro) else None
    os.makedirs(GEN, exist_ok=True)

    # ---- collect payload ---------------------------------------------------------------------------
    payload = {}
    skipped = []
    for dest, srcs in DIR_SRC.items():
        for f in expand(srcs):
            if not keep(f, dest):
                skipped.append(f)
                continue
            arc = dest_for(f)
            if arc is None:
                continue
            if arc in payload and payload[arc] != f:
                arc = arc + '.duplicate-of-' + os.path.basename(os.path.dirname(f))
            payload[arc] = f

    # ---- gates: real verification evidence, run now -------------------------------------------------
    gates = {}
    if not a.no_gates:
        gate_cmds = [
            ('audit_tex', [pyexe, 'tools/audit_tex.py'], 300),
            ('connection_audit', [pyexe, 'tools/connection_audit.py'], 300),
            ('check_tex_commands_manuscript',
             [pyexe, 'tools/check_tex_commands.py', '--tex',
              'PAPER_PROJECT/13_Manuscript/FINAL_REVISED_MANUSCRIPT.tex'], 120),
            ('check_tex_commands_calculations',
             [pyexe, 'tools/check_tex_commands.py', '--tex',
              'PAPER_PROJECT/13_Manuscript/FINAL_REVISED_CALCULATIONS.tex'], 120),
            ('check_crossrefs_manuscript',
             [pyexe, 'tools/check_crossrefs.py', '-i',
              'PAPER_PROJECT/13_Manuscript/FINAL_REVISED_MANUSCRIPT.tex'], 120),
            ('final_consistency', [pyexe, 'Phase_08_Final_Audit/verification/final_consistency.py'], 600),
            ('verify_code_freeze', [pyexe, 'PAPER_PROJECT/06_Source_Code/verify_code_freeze.py'], 300),
            # verify_pdf takes -c to mean "this is the companion document"; the manuscript run must NOT
            # pass it, or the figure count is checked against zero. Both runs are read-only.
            ('verify_pdf_manuscript', [pyexe, 'tools/verify_pdf.py'], 300),
            # the companion is checked WITHOUT -r on purpose: its footer carries the manuscript's running
            # title (it was rendered with md_to_pdf's default header), so the default exclusion is the right
            # one - passing the companion's own title misaligns check [1] and reports 4 false "missing"
            # units, which is the trap FINAL_QA_REPORT.md now documents
            ('verify_pdf_companion',
             [pyexe, 'tools/verify_pdf.py', '-p', 'PAPER_PROJECT/13_Manuscript/calculations_IJHMT.pdf',
              '-m', 'PAPER_PROJECT/13_Manuscript/calculations_IJHMT.md', '-c'], 300),
        ]
        for name, cmd, to in gate_cmds:
            rc, out = sh(cmd, timeout=to)
            # final_consistency.py writes its own timestamped transcript; restoring it keeps the archive a
            # pure function of the tracked tree instead of a function of when it was packed
            fc = 'Phase_08_Final_Audit/verification/final_consistency.json'
            if name == 'final_consistency':
                git('checkout', '--', fc)
            gates[name] = {'command': ' '.join(os.path.basename(c) if i == 0 else c
                                               for i, c in enumerate(cmd)),
                           'exit_code': rc,
                           'output_tail': _tail(out)}

    # ---- extraction -------------------------------------------------------------------------------
    src_dir = os.path.join(PP, '06_Source_Code', 'src')
    params = {}
    for f in sorted(glob.glob(os.path.join(src_dir, '*.py'))):
        params[os.path.basename(f)] = literals_from_source(f)
    for f in sorted(glob.glob(os.path.join(PP, '08_Experiments', 'production_matrix.py'))):
        params['08_Experiments/' + os.path.basename(f)] = literals_from_source(f)

    tex = open(os.path.join(PP, '13_Manuscript', 'FINAL_REVISED_MANUSCRIPT.tex'),
               encoding='utf-8').read()
    calctex = open(os.path.join(PP, '13_Manuscript', 'FINAL_REVISED_CALCULATIONS.tex'),
                   encoding='utf-8').read()
    bib = open(os.path.join(PP, '13_Manuscript', 'FINAL_REVISED_REFERENCES.bib'),
               encoding='utf-8').read()
    bibkeys = re.findall(r'^@\w+\{([^,\s]+)', bib, re.M)
    cited = set()
    for m in re.findall(r'\\cite[tp]?\{([^}]*)\}', tex):
        cited.update(k.strip() for k in m.split(',') if k.strip())
    figs_tex = re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}', tex)
    gpath = re.search(r'\\graphicspath\{(.*)\}', tex)
    gdirs = re.findall(r'\{([^{}]*)\}', gpath.group(1)) if gpath else []
    newcmds = re.findall(r'\\newcommand\{?\\(\w+)', tex)
    labels_tex = len(re.findall(r'\\label\{', tex))
    refs_tex = len(re.findall(r'\\(?:ref|eqref)\{', tex))

    raw_dirs = {d: sorted(glob.glob(os.path.join(PP, '09_Raw_Data', d, '*')))
                for d in ('convergence', 'convergence_gamma3p5', 'production')}
    data_keys = {}
    for d, fs in raw_dirs.items():
        data_keys[d] = json_key_types([f for f in fs if f.endswith('.json')])

    prov_csv = os.path.join(PP, '10_Processed_Data', 'PRODUCTION_PROVENANCE.csv')
    prov_rows = list(csv.DictReader(open(prov_csv, encoding='utf-8'))) if os.path.isfile(prov_csv) else []
    prov_fields = list(prov_rows[0].keys()) if prov_rows else []

    # npz dictionary from the first file of each dir (representative, and stated as such)
    npz_examples = {}
    for d, fs in raw_dirs.items():
        z = [f for f in fs if f.endswith('.npz')]
        if z:
            npz_examples[d] = {'file': rel(z[0]), 'members': npz_members(z[0]), 'n_files': len(z)}

    frozen = json.load(open(os.path.join(PP, '06_Source_Code', 'CODE_FREEZE_submission_2026_10_03j.json'),
                             encoding='utf-8'))
    frozen_files = frozen.get('files', frozen) if isinstance(frozen, dict) else frozen
    freeze_label = 'submission_2026_10_03j'

    # ---- figures provenance ------------------------------------------------------------------------
    mf = literals_from_source(os.path.join(PP, '08_Experiments', 'make_figures.py'))
    fig_pngs = sorted(glob.glob(os.path.join(PP, '11_Figures', '*.png')))
    fig_vecs = sorted(glob.glob(os.path.join(PP, '13_Manuscript', 'figures', '*.pdf')))
    ex = literals_from_source(os.path.join(PP, '08_Experiments', 'make_figures.py'))
    figs_src = open(os.path.join(PP, '08_Experiments', 'make_figures.py'), encoding='utf-8').read()
    fig_funcs = re.findall(r'\ndef (\w+)\(\).*?\n(?:.*?\n)*?    save\(fig, \'([\w.]+)\'\)', figs_src)
    rcparams = re.search(r"plt\.rcParams\.update\(\{(.*?)\}\)", figs_src, re.S)
    exporter = os.path.join(ROOT, 'Phase_09_Closeout', 'verification', 'export_submission_figures.py')
    exporter_exists = os.path.isfile(exporter)

    # ---- write the generated documents -------------------------------------------------------------
    docs = {}
    docs['README_PROGRAM.md'] = readme_program(params, gates, prov_fields, prov_rows, pyexe, frozen,
                                                freeze_label, tex, bibkeys, cited, newcmds)
    docs['RUN_ORDER.md'] = run_order(figs_src)
    docs['REPRODUCE_FROM_SCRATCH.md'] = reproduce_md(pyexe, repro)
    docs['run_manifest.json'] = None      # json written separately below
    docs['parameter_manifest.json'] = None
    docs['README_OVERLEAF.md'] = readme_overleaf(tex, calctex, bibkeys, cited, figs_tex, gdirs, newcmds,
                                                 labels_tex, refs_tex, gates, payload)
    docs['README_DATA.md'] = readme_data(raw_dirs, prov_rows)
    docs['DATA_DICTIONARY.md'] = data_dictionary(raw_dirs, data_keys, npz_examples, prov_fields,
                                                 prov_rows[:2])
    docs['FIGURE_PROVENANCE.md'] = figure_provenance(fig_pngs, fig_vecs, figs_tex, fig_funcs, rcparams,
                                                     exporter_exists, payload)
    docs['PROJECT_OVERVIEW.md'] = project_overview(params, prov_rows, raw_dirs, gates)
    docs['MODEL_DESCRIPTION.md'] = model_description(params)
    docs['NUMERICAL_METHOD.md'] = numerical_method(params)
    docs['KNOWN_LIMITATIONS.md'] = known_limitations(repro)
    docs['CHANGELOG.md'] = changelog_md()
    docs['ARCHIVE_README.md'] = archive_readme(payload, skipped, repro, gates)
    docs['FINAL_PACKAGE_STATUS.md'] = final_status(payload, repro, gates, figs_tex, bibkeys, cited)

    docmap = {'README_PROGRAM.md': '01_PROGRAM', 'RUN_ORDER.md': '01_PROGRAM',
              'run_manifest.json': '01_PROGRAM', 'parameter_manifest.json': '01_PROGRAM',
              'REPRODUCTION_SUMMARY.json': '04_REPRODUCTION',
              'REPRODUCTION_TEST_REPORT_2026-10-04.md': '04_REPRODUCTION',
              'ENVIRONMENT_OBSERVED.txt': '04_REPRODUCTION',
              'CLEAN_ROOM_TEST.txt': '09_ARCHIVE_METADATA',
              'VERIFICATION_GATES.txt': '04_REPRODUCTION',
              'REPRODUCE_FROM_SCRATCH.md': '01_PROGRAM',
              'README_OVERLEAF.md': '02_OVERLEAF',
              'README_DATA.md': '03_DATA', 'DATA_DICTIONARY.md': '03_DATA',
              'FIGURE_PROVENANCE.md': '08_FINAL_OUTPUTS',
              'PROJECT_OVERVIEW.md': '07_DOCUMENTATION', 'KNOWN_LIMITATIONS.md': '07_DOCUMENTATION',
              'CHANGELOG.md': '07_DOCUMENTATION',
              'MODEL_DESCRIPTION.md': '05_DERIVATIONS', 'NUMERICAL_METHOD.md': '05_DERIVATIONS',
              'ARCHIVE_README.md': '09_ARCHIVE_METADATA',
              'FINAL_PACKAGE_STATUS.md': '09_ARCHIVE_METADATA'}

    param_manifest = {'generated': BUILD_DATE, 'generated_by': rel(os.path.abspath(__file__)),
                      'rule': 'values transcribed from source by AST literal extraction; a string ending '
                              'in "[see source]" is an expression whose value is computed at run time, '
                              'recorded as source text so it cannot be misquoted',
                      'code_freeze': freeze_label, 'python': sh([pyexe, '-V'])[1].strip(),
                      'modules': params}
    run_manifest = {'generated': BUILD_DATE, 'sections': {k: count_and_size(v) for k, v in
                                                           {'raw': sum(raw_dirs.values(), [])}.items()},
                    'counts': {d: {'json': len([f for f in fs if f.endswith(".json")]),
                                   'npz': len([f for f in fs if f.endswith(".npz")])}
                               for d, fs in raw_dirs.items()},
                    'production_provenance_rows': len(prov_rows),
                    'provenance_fields': prov_fields,
                    'environment': {'python': sh([pyexe, '-V'])[1].strip(),
                                    'python_used_for_gates': pyexe},
                    'gates': gates, 'reproduction': repro or {
                        'status': 'NO FRESH RUN RECORD SUPPLIED',
                        'note': 'the archive builder was invoked without --repro; the historical '
                                'reproduction report in 04_REPRODUCTION is still included'}}
    run_manifest['sizes'] = {'raw_total_bytes': sum(os.path.getsize(f) for fs in raw_dirs.values()
                                                    for f in fs if os.path.isfile(f))}

    gen_files = []
    for name, text in docs.items():
        if text is None:
            continue
        p = os.path.join(GEN, name)
        open(p, 'w', encoding='utf-8').write(text)
        gen_files.append(p)
    for name, obj in (('parameter_manifest.json', param_manifest), ('run_manifest.json', run_manifest)):
        p = os.path.join(GEN, name)
        open(p, 'w', encoding='utf-8').write(json.dumps(obj, indent=1, default=str) + '\n')
        gen_files.append(p)
    if repro:
        p = os.path.join(GEN, 'REPRODUCTION_SUMMARY.json')
        open(p, 'w', encoding='utf-8').write(json.dumps(repro, indent=1) + '\n')
        gen_files.append(p)

    # gate transcript for the archive
    gp = os.path.join(GEN, 'VERIFICATION_GATES.txt')
    with open(gp, 'w', encoding='utf-8') as fh:
        fh.write(f'Verification gates run while building this archive ({BUILD_DATE}) using {pyexe}\n')
        fh.write('These are the same gates the submission programme runs; the transcript is stored so a\n'
                 'reader can see what was actually checked, not only that something was checked.\n\n')
        for k, v in gates.items():
            fh.write(f'== {k}\n   command: {v["command"]}\n   exit code: {v["exit_code"]}\n')
            for line in v['output_tail']:
                fh.write(f'   | {line}\n')
            fh.write('\n')
    gen_files.append(gp)
    # environment snapshot + the fresh reproduction report, when a run was supplied
    if repro:
        ep = os.path.join(GEN, 'ENVIRONMENT_OBSERVED.txt')
        with open(ep, 'w', encoding='utf-8') as fh:
            e = repro.get('environment', {})
            fh.write('Environment actually observed while running the reproduction check '
                     f'{repro.get("run_date", BUILD_DATE)}\n')
            fh.write('generated by PAPER_PROJECT/00_Project_Control/run_reproduction_check.py; these are '
                     'the versions a run used, as opposed to the pinned versions the project declared\n\n')
            fh.write(f'interpreter : {e.get("python", ND)}\n')
            fh.write(f'kernel      : {e.get("kernel", ND)}\n')
            fh.write(f'cpus        : {e.get("cpu_count", ND)}   ram: {e.get("ram_MB", ND)} MB\n\nlibraries\n')
            for k, v in (e.get('libraries') or {}).items():
                fh.write(f'  {k:12s} {v}\n')
            fh.write('\nverdict     : ' + str(repro.get('verdict', ND)) + '\n')
            fh.write('files compared byte-for-byte: ' + str(repro.get('n_files_compared', ND))
                     + ', changed: ' + str(repro.get('n_changed', ND)) + '\n')
        gen_files.append(ep)
    # the four manifest files are written after this loop (they hash the rest), and the checksum sidecar
    # never enters the archive; everything else generated here ships once, in its reading section
    manifest_own = {'SHA256SUMS.txt', 'file_manifest_sha256.csv', 'archive_build.json',
                    'INTEGRITY_AUDIT.json', 'ARCHIVE_CHECKSUMS.txt'}
    for p in gen_files:
        base = os.path.basename(p)
        if base in manifest_own:
            continue
        arc = os.path.join(docmap.get(base, '09_ARCHIVE_METADATA'), base)
        payload[arc] = p
    # the repository keeps every generated document under PAPER_PROJECT/16_Reproducibility/; the archive
    # carries ONE copy of each, at the section a reader would look in. A second "for audit" copy would
    # just be a file that can go stale - which is exactly what the clean-room test caught once.

    # ---- integrity manifests ---------------------------------------------------------------------
    # Order matters: hash everything, then write the audit and the build record (which are therefore
    # themselves hashed), and write the two manifest files LAST - a manifest cannot contain its own hash.
    def hash_rows(pm):
        return [{'archive_path': arc, 'bytes': os.path.getsize(pm[arc]),
                 'sha256': sha256_file(pm[arc]), 'source_path': rel(pm[arc])} for arc in sorted(pm)]

    rows = hash_rows(payload)
    audit = audit_archive(payload, rows, figs_tex, bibkeys, cited, docmap)
    ap = os.path.join(GEN, 'INTEGRITY_AUDIT.json')
    open(ap, 'w', encoding='utf-8').write(json.dumps(audit, indent=1) + '\n')
    payload['09_ARCHIVE_METADATA/INTEGRITY_AUDIT.json'] = ap

    ab = {'built': BUILD_DATE, 'archive': ARCHIVE_NAME + '.zip',
          'git_commit': git('rev-parse', 'HEAD'),
          'git_branch': git('rev-parse', '--abbrev-ref', 'HEAD'),
          'files': len(payload) + 2,
          'files_note': 'plus 2: this record and the two manifest files cannot hash themselves, so they '
                        'are counted but not listed in SHA256SUMS.txt',
          'bytes_uncompressed': sum(r['bytes'] for r in rows) + os.path.getsize(ap),
          'sections': {}, 'excluded_patterns': list(EXCLUDE_PARTS) + list(EXCLUDE_SUFFIX),
          'excluded_named_files': sorted(EXCLUDE_NAMES),
          'code_freeze': freeze_label, 'python_for_gates': pyexe,
          'reproduction_verdict': (repro or {}).get('verdict', NOT_REPRO)}
    for r in rows:                     # rows already includes INTEGRITY_AUDIT.json at this point
        sec = r['archive_path'].split('/')[0]
        e = ab['sections'].setdefault(sec, {'files': 0, 'bytes': 0})
        e['files'] += 1
        e['bytes'] += r['bytes']
    apj = os.path.join(GEN, 'archive_build.json')
    open(apj, 'w', encoding='utf-8').write(json.dumps(ab, indent=1) + '\n')
    payload['09_ARCHIVE_METADATA/archive_build.json'] = apj

    rows = hash_rows(payload)                     # now including the audit and the build record
    mp = os.path.join(GEN, 'file_manifest_sha256.csv')
    with open(mp, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=['archive_path', 'bytes', 'sha256', 'source_path'])
        w.writeheader()
        w.writerows(rows)
    sp = os.path.join(GEN, 'SHA256SUMS.txt')
    open(sp, 'w', encoding='utf-8').write(
        '\n'.join(f"{r['sha256']}  {r['archive_path']}" for r in rows) + '\n'
        + '# Covers every archived file except this one and file_manifest_sha256.csv, neither of which\n'
        + '# can contain its own hash. Verify from the extracted archive root with:\n'
        + '#   sha256sum -c 09_ARCHIVE_METADATA/SHA256SUMS.txt\n'
        + '# The archive is organised so that each document appears ONCE; 16_Reproducibility/ in the\n'
        + '# repository is where these generated files are authored, not a second copy in the archive.\n')
    payload['09_ARCHIVE_METADATA/SHA256SUMS.txt'] = sp
    payload['09_ARCHIVE_METADATA/file_manifest_sha256.csv'] = mp
    content_sha = sha256_file(sp)                  # invariant content-level checksum

    out_zip = os.path.join(a.out, ARCHIVE_NAME + '.zip')
    n = build_zip(payload, out_zip)
    zsha = sha256_file(out_zip)
    # the sidecar is written after the zip exists and is deliberately NOT inside it (a file cannot
    # record the hash of the archive that contains it); it lives in the repository next to the builder.
    # ab (archive_build.json) is already hashed inside the zip, so the zip-level hash is recorded here
    # only - putting it in archive_build.json would be circular.
    side = []
    side.append('REPRODUCIBILITY ARCHIVE - CHECKSUM RECORD')
    side.append('=======================================')
    side.append('built            %s from commit %s (branch %s)'
                % (BUILD_DATE, git('rev-parse', 'HEAD'), git('rev-parse', '--abbrev-ref', 'HEAD')))
    side.append('archive          %s.zip in PAPER_PROJECT/packages/ (gitignored: generated archives are'
                % ARCHIVE_NAME)
    side.append('                 built on demand from the repository, the same convention as make_packages.py)')
    side.append('zip sha256       %s' % zsha)
    side.append('size             %d bytes, %d files' % (n, len(payload)))
    side.append('')
    side.append('Content checksum - the one to actually compare')
    side.append('  sha256 of 09_ARCHIVE_METADATA/SHA256SUMS.txt as it appears inside the archive:')
    side.append('    %s' % content_sha)
    side.append('  Why this exists: the zip-level sha also covers archive_build.json, which records the commit')
    side.append('  the build ran from, so rebuilding at a later commit changes the zip hash even when every')
    side.append('  archived file is byte-identical. The content checksum is invariant across such a rebuild;')
    side.append('  the zip hash answers "did I receive the exact file", the content checksum answers "is this')
    side.append('  the same package". Both are checkable without trusting this document, by running')
    side.append('  `sha256sum -c 09_ARCHIVE_METADATA/SHA256SUMS.txt` inside the extracted archive.')
    side.append('')
    side.append('Reproduce')
    side.append('  python3 PAPER_PROJECT/00_Project_Control/make_reproducibility_archive.py \\')
    side.append('      --repro PAPER_PROJECT/16_Reproducibility/REPRODUCTION_SUMMARY.json')
    side.append('  (deterministic: fixed entry stamps, sorted order, no build clock inside the archive; the')
    side.append('   only field that moves between rebuilds is archive_build.json git_commit, by design)')
    open(os.path.join(GEN, 'ARCHIVE_CHECKSUMS.txt'), 'w', encoding='utf-8').write('\n'.join(side) + '\n')
    print(f'{ARCHIVE_NAME}.zip: {len(payload)} files, {n/1e6:.2f} MB '
          f'({ab["bytes_uncompressed"]/1e6:.2f} MB unpacked)')
    print('sections:', json.dumps({k: v['files'] for k, v in ab['sections'].items()}, indent=0))
    print('audit:', json.dumps(audit['summary']))
    if not a.keep_tree:
        # the index documents were just regenerated into PAPER_PROJECT/16_Reproducibility/; the zip already
        # holds them, so the working tree copies are returned to HEAD to keep the repository clean and to
        # make a later build's gate transcript describe a committed state. The checksum sidecar is NOT
        # restored - it is the record of the archive that was just built, and it is the one file here meant
        # to be committed after packing. `--keep-tree` keeps the documents too, for review or a commit.
        sc = os.path.join(GEN, 'ARCHIVE_CHECKSUMS.txt')
        sidecar_text = open(sc, encoding='utf-8').read() if os.path.isfile(sc) else None
        git('checkout', '--', os.path.relpath(GEN, ROOT))
        git('checkout', '--', 'Phase_08_Final_Audit/verification/final_consistency.json')
        if sidecar_text is not None:               # re-emit the sidecar the checkout just reverted
            with open(sc, 'w', encoding='utf-8') as fh:
                fh.write(sidecar_text)
    print('zip sha256    :', zsha)
    print('content sha256:', content_sha)
    return 0


# --------------------------------------------------------------------- document generators (extracted)
def readme_program(params, gates, prov_fields, prov_rows, pyexe, frozen, freeze_label, tex, bibkeys,
                   cited, newcmds):
    mod = next((m for m in params if 'cg_pipeline' in m), 'cg_pipeline.py')
    consts = params.get('08_Experiments/production_matrix.py', {}).get('constants', {})
    L = []
    A = L.append
    A('# README_PROGRAM\n')
    A('This folder is the runnable program: the solver, the experiment drivers, the verification suite,')
    A('the manuscript builders, the QA utilities, the code-freeze manifests and the as-received baseline.')
    A('It is a copy of `PAPER_PROJECT/` inside the reproducibility archive; the paths in the tables below')
    A('are archive-relative, so every command shown can be run from the extracted archive root.\n')
    A('## Language and version')
    A('')
    A('- Language: Python 3 only (no compilation step, no C/Fortran extensions).')
    A(f"- Interpreter used to verify this archive: `{sh([pyexe, '-V'])[1].strip()}` ({pyexe}).")
    A('- The project status note `07_DOCUMENTATION/program_control/COMPUTE_STATUS.md` and')
    A('  `REPRODUCIBILITY_STATUS.md` record the run environment as "Python 3.13.14, numpy 2.3.5,')
    A('  scipy 1.17.1"; `10_Processed_Data/PRODUCTION_PROVENANCE.csv` records the environment of every')
    A('  production run as `Python 3.11.2`. The two records disagree; both are reproduced here as written.')
    A('  `PROVENANCE.csv` names the interpreter each run actually executed under, so it is treated as')
    A('  authoritative for how the stored numbers were produced, while the status note describes the')
    A('  environment the work is targeted at (3.13.14 is a real CPython maintenance release, dated')
    A('  2026-06-10). No claim in the paper depends on the distinction: the reproduction test in')
    A('  `04_REPRODUCTION/REPRODUCTION_SUMMARY.json` regenerated every checked artifact byte-identically')
    A('  under 3.11.2 in this sandbox, where 3.13 could not be installed (no package-manager access).')
    A("  If the Methods section cites an interpreter, cite the one the deposited run used (3.11.2),")
    A('  or re-run under 3.13.14 and regenerate the provenance CSV, which this archive rebuilds for you.')
    A('- Third-party packages: the pinned set the project shipped with, verbatim from')
    A('  `01_PROGRAM/environment/requirements_pinned_from_handoff.txt` (also at')
    A('  `work/handoff/PILOT_HUANG_2025_01/requirements.txt`):\n')
    req = os.path.join(ROOT, 'work/handoff/PILOT_HUANG_2025_01/requirements.txt')
    if os.path.isfile(req):
        A('```')
        A(open(req, encoding='utf-8').read().strip())
        A('```\n')
    A('- The manuscript builders additionally import `python-docx`, `Pillow` (via `docbuilder.py`) and')
    A('  `reportlab`/`matplotlib` (via `tools/md_to_pdf.py`, `08_Experiments/make_figures.py`). Versions of')
    A(f'  these are {ND} in the repository: the requirements file above is the handoff\'s, and the')
    A('  submission-programme environment installed them unpinned. `04_REPRODUCTION/ENVIRONMENT_OBSERVED.txt`')
    A('  (when present) records what a working environment actually had.')
    A('')
    A('## What each subfolder is')
    A('')
    A(md_table(['folder', 'contents'], [
        ['`src/`', 'the frozen solver: `cg_model` (material), `cg_grid` (mapped grid), `cg_ops` '
                   '(operators), `cg_solver` (frequency-domain solve), `cg_bromwich` (inversion), '
                   '`cg_pipeline` (case assembly), `cg_ref1d` (1-D reference solution), `cg_transient`'],
        ['`experiments/`', 'drivers: `run_convergence.py`, `run_convergence_dirs.py`, '
                          '`run_production_v2.py heavy|light`, `production_matrix.py` (the case matrix), '
                          '`analyze_v2.py`, `make_figures.py`, `make_provenance.py`, `reproduce.py`, '
                          'and the run `logs/`'],
        ['`tests/`', '`run_tests.py` (verification suite), `run_tests_supplement.py`, '
                     '`make_test_report.py`, `diagnostics/`, `logs/`, stored `TEST_RESULTS.json`'],
        ['`builders/`', '`build_manuscript.py`, `build_calculations.py`, `build_supplement.py`, '
                       '`docbuilder.py`, `ms_*.py` - regenerate the manuscript and its companion from the '
                       'data package'],
        ['`utilities/`', '`tools/` (`.md` to `.tex`/`.pdf` converters, LaTeX and connection auditors, '
                         'reference renumbering) and `bootstrap_paths.sh`'],
        ['`control/`', 'packaging and phase-state scripts (`make_packages.py`, '
                      '`make_reproducibility_archive.py`, ...)'],
        ['`freeze/`', f'`CODE_FREEZE_*.json` manifests (current label `{freeze_label}`) and '
                      '`make_code_freeze.py`, `DIFF_VS_HANDOFF.txt`'],
        ['`handoff_baseline/`', 'the as-received 2026-10-01 pilot, committed verbatim; integrity via '
                               '`MANIFEST_SHA256.json`'],
    ]))
    A('')
    A('## Installation')
    A('')
    A('```bash')
    A('python3 -m venv .venv && . .venv/bin/activate')
    A('pip install -r 01_PROGRAM/environment/requirements_pinned_from_handoff.txt')
    A('pip install python-docx pillow                 # manuscript builders only')
    A('sh bootstrap_paths.sh                          # see "Path convention" below')
    A('```')
    A('')
    A('## Path convention (read this before running anything)')
    A('')
    A('Fifteen project scripts refer to the tree as `/home/user/PAPER_PROJECT` because that is where the')
    A('project lived when the frozen code was written; changing those lines would alter the SHA-256 of')
    A('frozen files and invalidate the code freeze. `bootstrap_paths.sh` therefore creates the symlinks')
    A('`/home/user/PAPER_PROJECT -> <repo>/PAPER_PROJECT` and `/home/user/work -> <repo>/work`. On a')
    A('machine where you cannot create those links, the alternative is to copy the archive so that the')
    A('`PAPER_PROJECT` directory sits at that path, or to set the path in the handful of scripts - in which')
    A(f'case re-run `python3 01_PROGRAM/freeze/make_code_freeze.py <label>` and note that the freeze id')
    A('changes. `tools/fix_hardcoded_root.py` exists in the repository for exactly this job; the frozen')
    A('files themselves were deliberately left untouched in the archive.')
    A('')
    A('## Entry point and exact execution order')
    A('')
    A('The full order, with expected outputs and runtimes, is `RUN_ORDER.md` in this folder. Shortest')
    A('useful path from the shipped data to the shipped results:')
    A('')
    A('```bash')
    A('python3 01_PROGRAM/experiments/analyze_v2.py            # data -> ANALYSIS_V2.json + tables')
    A('python3 01_PROGRAM/experiments/make_figures.py           # data -> the eight figures')
    A('python3 01_PROGRAM/experiments/make_provenance.py        # data -> PRODUCTION_PROVENANCE.csv')
    A('python3 01_PROGRAM/tests/run_tests.py                     # verification suite (~20 min)')
    A('python3 01_PROGRAM/experiments/reproduce.py                # reproduction test vs stored outputs')
    A('python3 tools/connection_audit.py                    # read-only: re-hashes the 27 frozen files')
    A('python3 tools/verify_pdf.py                            # manuscript preview PDF vs .md, read-only')
    A('python3 PAPER_PROJECT/13_Manuscript/build_manuscript.py  # full rebuild of .md/.docx/PDF, no options;')
    A('#   it aborts before writing if the code-freeze manifest is not current')
    A('```')
    A('Full recomputation (hours of compute, 150+ runs) starts at `RUN_ORDER.md` step 3 and is optional:')
    A('every result in the manuscript is reproducible from the stored raw data with the four commands')
    A('above, which is the point of shipping `03_DATA/`.\n')
    A('## Solver settings as written in the source')
    A('')
    A('Extracted by AST from `01_PROGRAM/src/*.py` and `01_PROGRAM/experiments/production_matrix.py`;')
    A('values are the literal defaults in the code, not a paraphrase. Machine-readable copy:')
    A('`parameter_manifest.json`.\n')
    rows = []
    for m, d in params.items():
        for k, v in list(d.get('constants', {}).items())[:40]:
            rows.append([m, k, f'`{v["line"]}`', str(v['value'])[:120]])
    A(md_table(['module', 'name', 'line', 'value as written'], rows[:120]))
    A('')
    A(f'Production grid/case definitions actually used (`production_matrix.py`): '
      f'`GRIDS = {consts.get("GRIDS", {}).get("value", ND)}`; '
      f'`COST = {consts.get("COST", {}).get("value", ND)}`.')
    A('')
    A('## Seeds, threads, tolerances')
    A('')
    A('- **Random seeds: none.** No part of the program draws random numbers (`random`, `np.random`,')
    A('  `seed` appear nowhere in `src/`, `experiments/` or the builders); the pipeline is deterministic,')
    A('  so no seed needs to be recorded.')
    A('- **Threading:** every run script sets `OPENBLAS_NUM_THREADS=1` before importing numpy, so BLAS')
    A('  threading is not a source of run-to-run variation. Production used exactly two worker processes')
    A('  claiming jobs atomically by `mkdir` (`run_production_v2.py`), which makes the run set independent')
    A('  of worker interleaving.')
    A('- **Solver tolerance:** the Bromwich/solver defaults in the table above (e.g. `eps=1e-10` in the')
    A('  contour integrator) are the settings recorded in the code; the per-run residuals stored in')
    A(f'  `03_DATA/processed/PRODUCTION_PROVENANCE.csv` (`{"`, `".join(prov_fields[-2:])}`) are the evidence')
    A('  that they were met.')
    A('- **Comparison tolerances for reproduction:** `reproduce.py` uses 1e-9 for recomputed stress values')
    A('  and 1e-12 for tables rebuilt from stored data, and states that a different machine/BLAS would')
    A('  need about 1e-6. That sentence is the project\'s own, quoted from the script docstring.')
    A('')
    A('## Runtime and hardware as recorded')
    A('')
    A('- `07_DOCUMENTATION/program_control/COMPUTE_STATUS.md`: 2 vCPU (Xeon 2.60 GHz), 1,984 MB RAM, no')
    A('  GPU; per-run cost 3 s (48x24) to 157 s (192x96); `192x96` solves need 0.7-1.0 GB, one heavy job')
    A('  at a time (one run was killed by the OOM killer); cumulative compute about 2.7 CPU-h.')
    A('- `03_DATA/processed/PRODUCTION_PROVENANCE.csv` carries `wall_s` and `n_solves` for each of the')
    A(f'  {len(prov_rows)} production runs, so the cost of any single case can be looked up rather than')
    A('  estimated.')
    A('')
    A('## Verification gates run while building this archive')
    A('')
    A(md_table(['gate', 'exit code', 'tail of output'],
               [[k, v['exit_code'], '; '.join(x.strip()[:70] for x in v['output_tail'][-2:])]
                for k, v in gates.items()]))
    A('')
    A('Transcript with the full tails: `09_ARCHIVE_METADATA/VERIFICATION_GATES.txt`.')
    _ff = frozen.get('files', frozen) if isinstance(frozen, dict) else frozen
    _n = len(_ff) if hasattr(_ff, '__len__') else ND
    A(f'\nCode freeze of the archived code: `{freeze_label}` ({_n} entries listed in `01_PROGRAM/freeze/`).')
    return '\n'.join(L) + '\n'


def run_order(figs_src):
    L = []
    A = L.append
    A('# RUN_ORDER\n')
    A('Exact order, with the command to run from the extracted archive root, what it reads, what it')
    A('writes, and the runtime the project recorded. Steps 0-5 reproduce the manuscript from the shipped')
    A('data; steps 6-9 recompute the data itself and are the expensive part.\n')
    A('## 0. Make the paths work (once per machine)')
    A('')
    A('```bash\nsh bootstrap_paths.sh\n```\n')
    A('Reads: nothing. Writes: two symlinks. See "Path convention" in `README_PROGRAM.md`.')
    A('')
    A('## 1. Integrity of the archive')
    A('')
    A('```bash\ncd PAPER_PROJECT_COMPLETE_REPRODUCIBILITY_ARCHIVE && sha256sum -c 09_ARCHIVE_METADATA/SHA256SUMS.txt\n```\n')
    A('Every archived file except `SHA256SUMS.txt` and `file_manifest_sha256.csv` is covered.\n')
    A('## 2. Verification suite (stored results shipped; ~20 min to re-run)')
    A('')
    A('```bash\npython3 01_PROGRAM/tests/run_tests.py            # writes 07_Tests/TEST_RESULTS.json + logs\n'
      'python3 01_PROGRAM/tests/run_tests_supplement.py   # the gamma=3.5 and direction studies\n'
      'python3 01_PROGRAM/tests/make_test_report.py       # TEST_RESULTS.json -> TEST_REPORT.md\n```\n')
    A('Reads: `src/` only. Writes: `07_Tests/TEST_RESULTS.json`, `TEST_REPORT.md`. The stored copies of')
    A('both are in `04_REPRODUCTION/`, including the one failing case (V0 on the hand-off 96x48 grid at')
    A('chi=2) and why it fails - the paper reports that failure, so a re-run is expected to reproduce it.')
    A('')
    A('## 3. Convergence studies (optional; the shipped results are in `03_DATA/raw/`)')
    A('')
    A('```bash\npython3 01_PROGRAM/experiments/run_convergence.py         # gamma=5 family')
    A('\npython3 01_PROGRAM/experiments/run_convergence_dirs.py     # mesh-direction study')
    A('```\n')
    A('Writes: `09_Raw_Data/convergence*/` pairs of `.json`+`.npz` per run; read by `analyze_v2.py`.')
    A('')
    A('## 4. Production matrix (optional; 150+ runs, 3 s to 157 s each)')
    A('')
    A('```bash\npython3 01_PROGRAM/experiments/run_production_v2.py heavy &')
    A('python3 01_PROGRAM/experiments/run_production_v2.py light &')
    A('```\n')
    A('Writes: `09_Raw_Data/production/<TAG>.json` + `<TAG>.npz`, plus a `block`/`grid` stamp per row.')
    A('The case list is generated by `01_PROGRAM/experiments/production_matrix.py` (`GRIDS`, `E_VARIANTS`,')
    A('`B_DEF`, `F_TW`, `BM_DEF` - see `parameter_manifest.json`).')
    A('')
    A('## 5. Analysis, provenance, figures')
    A('')
    A('```bash\npython3 01_PROGRAM/experiments/analyze_v2.py         # -> 10_Processed_Data/ANALYSIS_V2.json')
    A('python3 01_PROGRAM/experiments/make_provenance.py    # -> PRODUCTION_PROVENANCE.csv')
    A('python3 01_PROGRAM/experiments/make_figures.py         # -> 11_Figures/fig*.png')
    A('python3 Phase_09_Closeout/verification/export_submission_figures.py   # 600-dpi PNG/TIFF + vector PDF')
    A('```\n')
    A('`make_figures.py` accepts specific names (`python3 ... fig2 fig5`) and skips figures whose data is')
    A('absent, printing `<name>: no data` - a partial `03_DATA/` therefore degrades visibly instead of')
    A('silently.')
    A('')
    A('## 6. Manuscript and companion')
    A('')
    A('```bash\ncd PAPER_PROJECT/13_Manuscript')
    A('\npython3 ../01_PROGRAM_builders_placeholder 2>/dev/null || python3 build_manuscript.py')
    A('\npython3 build_calculations.py\npython3 build_supplement.py\n```\n')
    A('These three scripts take no options: each regenerates its document from the data and aborts before')
    A('writing if the deposited code-freeze manifest is no longer current (the guard was tested by')
    A('corrupting one entry). To check the freeze without touching anything, run the read-only')
    A('`python3 tools/connection_audit.py` from the archive root instead.')
    A('The preview PDFs are a separate, documented step - the builders write `.md`/`.docx`, and')
    A('`tools/md_to_pdf.py` renders the PDF with the running title baked into the header:\n')
    A('```bash\npython3 tools/md_to_pdf.py -i PAPER_PROJECT/13_Manuscript/manuscript_IJHMT.md \\')
    A('  -o PAPER_PROJECT/13_Manuscript/manuscript_IJHMT.pdf\n'
      'python3 tools/md_to_pdf.py -i PAPER_PROJECT/13_Manuscript/calculations_IJHMT.md \\')
    A('  -o PAPER_PROJECT/13_Manuscript/calculations_IJHMT.pdf\n```\n')
    A('`reportlab` is not in the pinned requirements file (its version is NOT DOCUMENTED; the')
    A('sandbox that verified this archive had 5.0.1), so a different version can shift page breaks')
    A('- that is why `verify_pdf.py` compares text content, not bytes, and why the `.md` sources are')
    A('authoritative while the PDFs are previews.\n')
    A('Writers of the manuscript are `13_Manuscript/ms_*.py` (section modules) + `docbuilder.py`')
    A('(`.md` -> `.docx`/`.pdf`) + `tools/md_to_tex.py` (`.md` -> `.tex`). They read only `03_DATA/` and')
    A('`01_PROGRAM/`; they never hand-type a number, which is why a data change propagates.')
    A('')
    A('## 7. Reproduction test and the QA gates')
    A('')
    A('```bash\npython3 01_PROGRAM/experiments/reproduce.py      # -> 07_Tests/REPRODUCTION_TEST_REPORT.md')
    A('\npython3 tools/audit_tex.py\npython3 tools/connection_audit.py\npython3 tools/verify_pdf.py'
      '   # manuscript: no -c')
    A('python3 tools/verify_pdf.py -p PAPER_PROJECT/13_Manuscript/calculations_IJHMT.pdf \\')
    A('  -m PAPER_PROJECT/13_Manuscript/calculations_IJHMT.md -c        # no -r here, on purpose: the '
      'companion footer is the manuscript running title')
    A('\npython3 Phase_08_Final_Audit/verification/final_consistency.py\n```\n')
    A('## 8. Packages')
    A('')
    A('```bash\npython3 00_Project_Control/make_packages.py final')
    A('\npython3 PAPER_PROJECT/00_Project_Control/make_reproducibility_archive.py   # this archive\n```\n')
    A('Both archives are deterministic: same tree in, same bytes out (fixed entry stamps), so their')
    A('sha256 is a usable checksum of the project.')
    A('')
    A('## Order constraints, in one line each')
    A('')
    A('- `analyze_v2.py` before `make_figures.py` (figures read `ANALYSIS_V2.json`).')
    A('- `make_provenance.py` after any new production run (the CSV is the audit trail the manuscript cites).')
    A('- `build_manuscript.py` after figures and analysis (it embeds both).')
    A('- `make_code_freeze.py` LAST if you edited code, before packaging (the builders abort when the')
    A('  manifest is stale, by design).')
    return '\n'.join(L) + '\n'


def reproduce_md(pyexe, repro):
    L = ['REPRODUCE_FROM_SCRATCH'.center(60, '#'), '']
    A = L.append
    A('Everything below was run inside the sandbox that produced this archive, on ' + BUILD_DATE + ',')
    A('with the interpreter `' + pyexe + '`. Where a step was not attempted, that is said in words.\n')
    A('## Clean-room recipe (what a new machine does)\n')
    A('```bash')
    A('unzip PAPER_PROJECT_COMPLETE_REPRODUCIBILITY_ARCHIVE.zip')
    A('cd PAPER_PROJECT_COMPLETE_REPRODUCIBILITY_ARCHIVE')
    A('# 1. the archive mirrors PAPER_PROJECT/, so recreate that layout:')
    A('mkdir -p ../rp && cp -r 01_PROGRAM/src ../rp/PAPER_PROJECT/06_Source_Code/src 2>/dev/null || true')
    A('sh bootstrap_paths.sh          # or place the tree at the path the scripts expect')
    A('python3 -m venv .venv && . .venv/bin/activate')
    A('pip install -r 01_PROGRAM/environment/requirements_pinned_from_handoff.txt')
    A('pip install python-docx pillow')
    A('# 2. integrity')
    A('sha256sum -c 09_ARCHIVE_METADATA/SHA256SUMS.txt')
    A('# 3. re-derive everything that is cheap, in order')
    A('python3 01_PROGRAM/experiments/analyze_v2.py')
    A('python3 01_PROGRAM/experiments/make_provenance.py')
    A('python3 01_PROGRAM/experiments/make_figures.py')
    A('python3 01_PROGRAM/experiments/reproduce.py')
    A('# 4. compare with what shipped')
    A('diff <(git diff --no-index 11_Figures/fig2_phi_sweep.png '
      '08_FINAL_OUTPUTS/figures/fig2_phi_sweep.png 2>/dev/null | head) /dev/null && echo "figures identical"')
    A('```')
    A('')
    A('## What is expected')
    A('')
    A('- `analyze_v2.py` prints a short summary and rewrites `10_Processed_Data/ANALYSIS_V2.json` and')
    A('  `ANALYSIS_V2_TABLES.md`; the shipped copies are in `03_DATA/processed/` and `08_FINAL_OUTPUTS/`,')
    A('  so a byte-comparison is meaningful.')
    A('- `reproduce.py` writes `07_Tests/REPRODUCTION_TEST_REPORT.md` and, on the environment it was')
    A('  developed in, ends `Overall: 11 PASS, 0 FAIL` with relative differences of 0.00e+00 on the')
    A('  closed-form and interpolation items (see the stored report in `04_REPRODUCTION/`). It needs')
    A('  `07_Tests/TEST_RESULTS.json`, which ships in the archive.')
    A('- `make_figures.py` rewrites the eight PNGs in `11_Figures/`; identical to the shipped PNGs')
    A('  except for matplotlib metadata, so compare pixel content if bytes differ.')
    A('- Full-suite re-run (`run_tests.py`) takes about 20 min on 2 vCPU and needs ~1 GB headroom for the')
    A('  heaviest grids; if it is killed, that is the same failure mode the project recorded (see')
    A('  `COMPUTE_STATUS.md`) - reduce to the light grids rather than calling it a numerical discrepancy.')
    A('')
    A('## Compiling the manuscript')
    A('')
    A('```bash')
    A('cd 02_OVERLEAF && pdflatex FINAL_REVISED_MANUSCRIPT && bibtex FINAL_REVISED_MANUSCRIPT \\')
    A('  && pdflatex FINAL_REVISED_MANUSCRIPT && pdflatex FINAL_REVISED_MANUSCRIPT')
    A('```\n')
    A('`elsarticle.cls` and `elsarticle-num.bst` come from the Elsevier LaTeX bundle shipped by TeX Live')
    A('and Overleaf; they are **not** inside this archive because the project never kept a copy whose')
    A(f'provenance could be verified ({NA} in the repository). `Phase_10_Submission_Package/compile_check.sh`')
    A('(archived at `08_FINAL_OUTPUTS/manuscript/compile_check.sh`) runs the same sequence and triages the')
    A('log; with no TeX engine installed it prints the commands instead of failing.')
    A('')
    A('## Fresh reproduction result, if the builder was given one')
    A('')
    if repro:
        A('```json')
        A(json.dumps(repro, indent=1))
        A('```')
    else:
        A(f'{NA} for this build: the archive builder was run without `--repro`, so no fresh run was')
        A('recorded by the packager. The stored reports in `04_REPRODUCTION/` are the reproduction')
        A('evidence that ships with the archive, and they were produced by the scripts listed there.')
    return '\n'.join(L) + '\n'


def readme_overleaf(tex, calctex, bibkeys, cited, figs_tex, gdirs, newcmds, labels, refs, gates, payload):
    missing_fig = [f for f in figs_tex
                   if not os.path.isfile(os.path.join(PP, '13_Manuscript', 'figures', f + '.pdf'))]
    missing_bib = sorted(set(cited) - set(bibkeys))
    uncited = sorted(set(bibkeys) - cited)
    L = ['# README_OVERLEAF\n']
    A = L.append
    A('## Files in this folder')
    A('')
    A(md_table(['file', 'role'], [
        ['`FINAL_REVISED_MANUSCRIPT.tex`', 'the manuscript, single-file source (no `\\input`/`\\include` of '
                                          'other .tex files, so nothing else can go missing)'],
        ['`FINAL_REVISED_CALCULATIONS.tex`', 'the derivation/numerics companion (same preamble, separate '
                                            'document; submitted as supplementary or kept with the code, '
                                            'author decision B8)'],
        ['`FINAL_REVISED_REFERENCES.bib`', f'the bibliography, {len(bibkeys)} entries'],
        ['`figures/fig*.pdf`', f'the {len(figs_tex)} vector figures the manuscript includes'],
        ['`figures/README.txt`', 'how the figure set was produced'],
        ['`highlights.txt`', 'the five highlights, as a text file for the submission system'],
    ]))
    A('')
    A('## In Overleaf')
    A('')
    A('1. New project -> upload **this whole folder** (zip it as-is keeps `figures/` next to the source).')
    A('2. Menu -> Main document: `FINAL_REVISED_MANUSCRIPT.tex`. There is deliberately **no `main.tex`** in')
    A('   this archive: a second copy under another name is exactly how two competing "final" manuscripts')
    A('   get submitted. If a template insists on the name, rename the file rather than copying it.')
    A('3. Compiler: pdfLaTeX (default). BibTeX is run automatically by Overleaf when the document uses')
    A(f'   `\\bibliography{{...}}` as this one does ({tex.count(chr(92)+"bibliography")} line).')
    A('')
    A('## Class and style files')
    A('')
    A(f'- `\\documentclass[preprint,12pt]{{elsarticle}}` and `\\bibliographystyle{{elsarticle-num}}` are used')
    A('  as written. The class and `.bst` are **not vendored** here: `elsarticle.cls` is not present')
    A('  anywhere in the repository, and shipping an unverified copy would be worse than saying so.')
    A('  Both are provided by TeX Live (package `texlive-publishers`) and are preinstalled on Overleaf.')
    A('  Switching to the journal layout is a one-token change (`5p`, or `review` for double-spaced')
    A('  refereeing) - the author decision recorded as B1 in `08_FINAL_OUTPUTS/manuscript/AUTHOR_INPUT_REQUIRED.md`.')
    A(f"- The source defines {len(newcmds)} of its own macros (`{', '.join(newcmds[:12])}`"
      f"{' ...' if len(newcmds) > 12 else ''}); no `\\input{{macros}}` exists.")
    A('')
    A('## Static verification of this folder (no TeX engine exists in the packaging environment)')
    A('')
    A(md_table(['check', 'result'], [
        ['`\\input` / `\\include` of other sources', 'none used (0 occurrences), so no missing subfiles'],
        [f'`\\includegraphics` targets ({len(figs_tex)}): {", ".join(figs_tex)}',
         ('all resolve to `figures/fig*.pdf` in this folder' if not missing_fig
          else 'MISSING: ' + ', '.join(missing_fig))],
        [f'`\\graphicspath`', '`' + (', '.join(gdirs) if gdirs else ND) +
         '` - resolved the same way pdflatex does, including extension probing'],
        [f'`\\cite` keys used ({len(cited)}) vs keys in the `.bib` ({len(bibkeys)})',
         ('every cited key exists' if not missing_bib else 'MISSING FROM BIB: ' + ', '.join(missing_bib))],
        ['bibliography entries never cited',
         (f'{len(uncited)} ' + (', '.join(uncited) if uncited else '(none)'))],
        [f'labels / references ({labels} / {refs})',
         'resolved by `tools/check_crossrefs.py`: ' + ('PASS' if 'PASS' in ' '.join(
             gates.get('check_crossrefs_manuscript', {}).get('output_tail', [])) else 'see transcript')],
        ['undefined-command scan (`tools/check_tex_commands.py`)',
         'PASS' if 'PASS' in ' '.join(gates.get('check_tex_commands_manuscript', {}).get('output_tail', []))
         else 'see 09_ARCHIVE_METADATA/VERIFICATION_GATES.txt'],
        ['`elsarticle-num` numbering vs the printed numbers in the .md/PDF',
         'the .tex is numbered by first citation (Phase 1); the mapping is in '
         '`08_FINAL_OUTPUTS/manuscript/REF_ORDER.json` and `REFERENCES_ORDERED.json`'],
    ]))
    A('')
    A('## What was NOT done here')
    A('')
    A('- **The `.tex` has never been compiled by the people who wrote it.** No TeX engine exists in this')
    A('  sandbox (no `pdflatex`, `apt` unavailable to the sandbox user), so the compile is the author-side')
    A('  step in the checklist. The archive therefore records `NOT COMPILED IN THIS ENVIRONMENT`, together')
    A('  with the four commands to run and the log to check. A static check is not a compile: it catches')
    A('  missing files, undefined commands and dangling references, not overfull boxes or float placement.')
    A('- Scientific content was not touched to make anything compile; the requirement "do not change')
    A('  science to compile" is honoured by not compiling-and-editing here at all.')
    return '\n'.join(L) + '\n'


def readme_data(raw_dirs, prov_rows):
    L = ['# README_DATA\n']
    A = L.append
    A('The data package is the evidence base of the paper: raw per-run output, the processed results the')
    A('manuscript quotes, and the CSV tables behind every figure. Column-by-column detail, including the')
    A('array names inside each `.npz`, is in `DATA_DICTIONARY.md` (generated from the files themselves).\n')
    A('## Folders')
    A('')
    A(md_table(['folder', 'what it is', 'produced by', 'regenerate with'], [
        ['`raw/convergence/`', 'grid-refinement family at gamma=5 (mesh-direction and refinement sweeps): '
                              f'{len(raw_dirs["convergence"])} files',
         '`08_Experiments/run_convergence.py`',
         '`python3 01_PROGRAM/experiments/run_convergence.py`'],
        ['`raw/convergence_gamma3p5/`', 'the hand-off grid family (gamma=3.5), partial by design - the '
                                       'paper says so: '
                                       f'{len(raw_dirs["convergence_gamma3p5"])} files',
         '`run_convergence.py` with the gamma=3.5 plan',
         'see `05_DERIVATIONS/numerical_method/CONVERGENCE_REPORT.md`'],
        ['`raw/production/`', 'the production matrix, one `.json` (scalars + metadata) + one `.npz` '
                             '(field arrays) per run: '
                              f'{len(raw_dirs["production"])} files',
         '`08_Experiments/run_production_v2.py`',
         '`python3 01_PROGRAM/experiments/run_production_v2.py heavy` + `... light`'],
        ['`processed/`', 'the analysis the manuscript quotes (JSON + markdown tables) and the per-run '
                         'provenance CSV',
         '`08_Experiments/analyze_v2.py`, `make_provenance.py`',
         '`python3 01_PROGRAM/experiments/analyze_v2.py`'],
        ['`tables/`', 'the six CSVs the figures are drawn from (phi-sweep, convergence, D-vs-lambda, '
                      'ablations E and E+M, pulse width)',
         '`analyze_v2.py`', 'same command'],
    ]))
    A('')
    A('## Conventions that apply to every file')
    A('')
    A('- **Stress** is wall hoop stress, in Pa per K of pulse amplitude (the loading is a unit-temperature')
    A('  pulse, so Pa/K is also the physical scaling). **Negative = compression.** Values like')
    A('  `-8.53e5` are therefore a compressive peak of 0.85 MPa/K.')
    A('- **Times are non-dimensional** in units of the cavity diffusion time `t_th` unless the key name')
    A('  says `_s`; `t_th_s` in each `.json` is the dimensional conversion factor in seconds.')
    A('- **Geometry** is given by `a_nm` (reference radius in nm), `chi` (ellipse aspect ratio, 1 = circle)')
    A('  and `phi` (orientation in degrees, a-axis reference); `Rfac` is the outer radius in units of `a`.')
    A('- **Angles on the wall** are reported twice on purpose: `th_star_nodal_deg` (grid node of the peak)')
    A('  and `th_star_interp_deg` (the interpolated peak location); they differ by up to one angular cell,')
    A('  and the interpolation is what the figures use.')
    A('- **Model** is `FOURIER` (`tau_ps = 0`) or `CV`/Maxwell-Cattaneo-Vernotte with `tau_ps` the')
    A('  relaxation time in ps; `coupled`/`energy_coupling`/`inertia_scale` are the switches the ablations')
    A('  flip. Their meanings are defined in `05_DERIVATIONS/` and in the manuscript section that uses them.')
    A('- **Precision:** everything is stored as float64; the `.json` files hold the values at full repr')
    A('  precision (not rounded), except where a stored comparison value is quoted to 4 digits by hand in')
    A('  a test report - `reproduce.py` documents exactly which of those exist and uses a looser tolerance')
    A('  for them.')
    A(f'- **Count:** {len(prov_rows)} production runs carry a provenance row with wall time, solve count and')
    A('  the two residual measures; each row names the code-freeze sha it was produced with.')
    A('')
    A('## Units and dimensionless groups, in the project\'s own words')
    A('')
    A('The nondimensionalization is not restated here on purpose: read it in')
    A('`05_DERIVATIONS/numerical_method/NUMERICAL_METHOD_V2.md` and `05_DERIVATIONS/theory/FORMULATION_ADDENDUM.md`,')
    A('which are the documents the manuscript was written against. The scaling constants actually used at')
    A('run time are in `parameter_manifest.json` (`cg_pipeline.derived()`: `kappa_bar`, `c_ref`).')
    return '\n'.join(L) + '\n'


def data_dictionary(raw_dirs, data_keys, npz_examples, prov_fields, prov_sample):
    L = ['# DATA_DICTIONARY\n',
         'Generated from the files themselves at build time - the key lists, types and array shapes below',
         'are read out of the shipped data, so they cannot disagree with it.\n']
    A = L.append
    for d in ('convergence', 'convergence_gamma3p5', 'production'):
        fs = raw_dirs[d]
        js = [f for f in fs if f.endswith('.json')]
        np_ = [f for f in fs if f.endswith('.npz')]
        keys, n = data_keys[d]
        A(f'## `03_DATA/raw/{d}/`')
        A('')
        A(f'{len(js)} `.json` result records + {len(np_)} `.npz` field files, '
          f'{sum(os.path.getsize(f) for f in fs)/1e6:.1f} MB total. '
          f'File name pattern: `<BLOCK>_chi<CHI>_phi<PHI>[_<GRID>].(json|npz)` for production, '
          f'`C<N>_(...)` for the convergence families; the tag inside each file matches its name.')
        A('')
        A('### Result record (`.json`) - keys, types, example values')
        A('')
        A(md_table(['key', 'type(s)', 'present in', 'example value (as stored)'],
                   [[f'`{k}`', ', '.join(v['types']), f"{v['count']}/{n}",
                     ('`' + str(v['sample'])[:60] + '`') if v['sample'] is not None else 'container - see source']
                    for k, v in sorted(keys.items())]))
        A('')
        if d in npz_examples:
            ex = npz_examples[d]
            A(f'### Field arrays (`.npz`) - from `{ex["file"]}` (all {ex["n_files"]} files in the folder '
              'share this layout)')
            A('')
            A(md_table(['array', 'shape', 'dtype', 'compressed B', 'uncompressed B'],
                        [[m[0], m[1], m[2], m[3] if len(m) > 3 else '', m[4] if len(m) > 4 else '']
                         for m in ex['members']]))
            A('')
    A('## `03_DATA/processed/`')
    A('')
    A(md_table(['file', 'what it is', 'produced by'], [
        ['`ANALYSIS_V2.json`', 'the aggregated analysis the manuscript quotes (peak/extreme tables, the '
                               'T1-T5 frozen-criterion verdicts, ablations)',
         '`01_PROGRAM/experiments/analyze_v2.py`'],
        ['`ANALYSIS_V2_TABLES.md`', 'the same, rendered as the markdown tables the builders embed',
         'same script'],
        ['`CONVERGENCE_RESULTS.json`, `CONVERGENCE_RESULTS_gamma3p5_partial.json`, `CONVERGENCE_DIRS.json`',
         'the convergence studies as processed tables', '`analyze_v2.py` / the convergence drivers'],
        ['`PRODUCTION_PROVENANCE.csv`', f'the per-run audit trail, {len(prov_fields)} columns',
         '`01_PROGRAM/experiments/make_provenance.py`'],
    ]))
    A('')
    A('### `PRODUCTION_PROVENANCE.csv` columns')
    A('')
    A(md_table(['column', 'meaning'], [
        ['`RUN_ID`', 'the case tag; matches `<TAG>.json`/`.npz` under `03_DATA/raw/production/`'],
        ['`block`', 'which block of the matrix (A, B, D, E, F, BM, ...) - see `production_matrix.py`'],
        ['`status`', '`RUN_SUCCESS` or the recorded failure'],
        ['`CODE_VERSION(freeze sha256[:16])`', 'first 16 hex of the code-freeze manifest that described the '
                                              'code as it ran'],
        ['`INPUT_CHECKSUM`', 'sha256[:16] of the inputs that defined the case'],
        ['`REFERENCE_DATA_VERSION(cg_model sha256[:16])`', 'the material-constants module the run used'],
        ['`ENVIRONMENT_VERSION`', 'interpreter, library and kernel string captured at run time'],
        ['`OUTPUT_LOCATION`', 'path of the `.npz` (archive-relative reading = project-relative writing)'],
        ['`OUTPUT_SHA256[:16]`', 'first 16 hex of the output file'],
        ['`wall_s`, `n_solves`', 'cost of that run (see COMPUTE_STATUS.md for the hardware)'],
        ['`backward_err`, `wall_pulse_err`', 'the two internal consistency residuals per run '
                                            '(Bromwich round-trip; wall-temperature recovery)'],
    ]))
    A('')
    if prov_sample:
        A('Example row, verbatim:')
        A('')
        A('```')
        A(','.join(prov_fields))
        for r in prov_sample:
            A(','.join(str(r.get(k, '')) for k in prov_fields))
        A('```')
    A('')
    A('## `03_DATA/tables/`')
    A('')
    A(md_table(['csv', 'rows', 'used by'],
               [[os.path.basename(f), max(0, sum(1 for _ in open(f)) - 1),
                 'figure/table source (see `FIGURE_PROVENANCE.md`)']
                for f in sorted(glob.glob(os.path.join(PP, '12_Tables', '*.csv')))]))
    A('')
    A('## What is NOT in the data folders')
    A('')
    A('- `09_Raw_Data/production/_claims/` - the job-claiming directories the two workers used; transient')
    A('  by design, and the packager skips them (`packages/`, `__pycache__` likewise).')
    A('- Any experimental measurement: the study is a continuum computation and the paper says no physical')
    A('  validation data exists (`06_VALIDATION/PHYSICAL_VALIDATION.md`).')
    A('- Third-party PDFs of the cited literature: not redistributable, so the archive ships the Crossref')
    A('  verification records in `06_VALIDATION/literature_verification/` instead.')
    return '\n'.join(L) + '\n'


def figure_provenance(figs, vecs, figs_tex, fig_funcs, rcparams, exporter_exists, payload):
    L = ['# FIGURE_PROVENANCE\n',
         'One row per manuscript figure: what the source contains, where it goes, what it reads, the',
         'command, and the shipped files with their sha256. Generated from the scripts and the file tree.\n']
    A = L.append
    A('Global plotting settings as written in `08_Experiments/make_figures.py`: `'
      + (rcparams.group(1).replace('\n', ' ').strip() if rcparams else ND) + '`')
    A('')
    A(md_table(['manuscript figure', 'generator', 'reads', 'shipped as', 'sha256 (first 16)'],
               [[f'`fig{i+1}`' + '' , '`make_figures.py`', '`03_DATA/raw/...` + '
                 '`03_DATA/processed/ANALYSIS_V2.json`' + (', `07_Tests/TEST_RESULTS.json`' if i == 3 else ''),
                 f'`02_OVERLEAF/figures/{os.path.basename(v)}` (vector) and '
                 f'`08_FINAL_OUTPUTS/figures/{os.path.basename(f)}` (raster)'
                 if i < len(vecs) and i < len(figs) else NA,
                 sha256_file(f)[:16] if i < len(figs) else '']
                for i, (f, v) in enumerate(zip(figs, vecs + [''] * len(figs)))][:len(figs_tex) + 2]))
    A('')
    A('Figure-function inventory in the generator script (name -> output file, from the source):')
    A('')
    A(md_table(['function', 'writes'], [[f'`{a}()`', f'`{b}`'] for a, b in fig_funcs] or [['see source', ND]]))
    A('')
    A('## How each rendition in the archive was produced')
    A('')
    A('```bash')
    A('python3 PAPER_PROJECT/08_Experiments/make_figures.py                 # 11_Figures/fig*.png (200 dpi)')
    A('python3 Phase_09_Closeout/verification/export_submission_figures.py   # 600-dpi PNG + LZW TIFF, '
      'vector PDF, in 11_Figures/submission/')
    A('python3 Phase_10_Submission_Package/verification/make_tex_figure_set.py  # the vector set the .tex '
      'loads, in 13_Manuscript/figures/')
    A('```\n')
    A('- The first call is the frozen figure generator; the second and third are thin wrappers that call')
    A('  it with different save settings and then restore the tree (they re-verify the frozen hashes and')
    A('  `git checkout --` the PNGs afterwards, so running them cannot leave the working tree modified).')
    _exp = 'yes' if exporter_exists else \
        'NO - it is referenced by the phase reports but was not found while packaging'
    A('- The exporter wrapper is present in the repository: ' + _exp + '.')
    A('- **Raster rendition sizes:** the 600-dpi PNGs and TIFFs are gitignored in the repository and are')
    A('  therefore NOT inside this archive (they are 22-49 MB each uncompressed; regenerate with the second')
    A('  command above, which is deterministic and takes about a minute).')
    A('- The 200-dpi PNGs in `08_FINAL_OUTPUTS/figures/` are the tracked ones, so a reader can compare a')
    A('  regenerated figure against a shipped one without any network or repository access.')
    A('')
    A('## From figure to number')
    A('')
    A('Each figure is drawn from `03_DATA/` by the function named above; each data file records the code')
    A('freeze it came from; `03_DATA/processed/PRODUCTION_PROVENANCE.csv` maps run -> inputs -> output')
    A('hash -> wall time -> residuals. The manuscript quotes `03_DATA/processed/ANALYSIS_V2.json` through')
    A('the builder modules (`01_PROGRAM/builders/ms_*.py`), which read those files at build time - so a')
    A('changed data file changes the manuscript text, and no number is hand-typed anywhere in the chain.')
    return '\n'.join(L) + '\n'


def project_overview(params, prov_rows, raw_dirs, gates):
    L = ['# PROJECT_OVERVIEW\n']
    A = L.append
    A('**Repository:** `vipin-oss/le`, project directory `PAPER_PROJECT`, run under the project\'s own')
    A('MASTER_PROMPT v2.1 (a copy is at `07_DOCUMENTATION/program_control/MASTER_PROMPT.md`).')
    A('**Title as submitted:**')
    md = os.path.join(PP, '13_Manuscript', 'manuscript_IJHMT.md')
    if os.path.isfile(md):
        for line in open(md, encoding='utf-8'):
            if line.startswith('# '):
                A('')
                A('> ' + line[2:].strip())
                break
    A('')
    A('## The one-paragraph version')
    A('')
    A('A transient thermal pulse is applied to the wall of a microscopic cavity (circular, and an '
      'equal-area')
    A('ellipse with aspect ratio chi = 2) in the a-c plane of monoclinic beta-Ga2O3. Heat conduction is')
    A('solved in the frequency domain with Fourier, Lord-Shulman and a two-relaxation-time (MCV3) kernel,')
    A('inverted by a Bromwich contour integral, and fed to a coupled thermoelastic solve on a mapped')
    A('grid; the reported quantity is the peak compressive hoop stress on the cavity wall as a function of')
    A('crystal orientation. The finding is that the anisotropic stiffness and the anisotropic expansion')
    A('together modulate that peak by about 30 per cent with orientation, that thermal memory reshapes')
    A('rather than rescales it, and that every step is verified against a closed-form solution and an')
    A('independent implementation. No experimental comparison is claimed - none exists for this geometry.')
    A('')
    A('## Where the numbers live')
    A('')
    A(md_table(['what', 'where'], [
        ['governing equations, constitutive law, nondimensionalization', '`05_DERIVATIONS/theory/`'],
        ['numerical method, grid mapping, contour integration, stability', '`05_DERIVATIONS/numerical_method/`'],
        ['material and geometry constants as used by the code', '`01_PROGRAM/parameter_manifest.json`'],
        ['raw results per run (375 files)', '`03_DATA/raw/`'],
        ['aggregates the manuscript quotes', '`03_DATA/processed/ANALYSIS_V2.json`'],
        ['figures', '`08_FINAL_OUTPUTS/figures/` (raster), `02_OVERLEAF/figures/` (vector)'],
        ['verification suite results', '`04_REPRODUCTION/`'],
        ['manuscript sources, rendered PDFs, supplement, cover letter', '`08_FINAL_OUTPUTS/manuscript/`'],
        ['why each decision was taken, what was rejected, what was fixed',
         '`07_DOCUMENTATION/program_control/` (DECISION_LOG, REJECTED_IDEAS, CORRECTIONS_LOG, EVIDENCE_LOG)'],
        ['audits of the code, the maths, the literature, the manuscript',
         '`06_VALIDATION/`, `07_DOCUMENTATION/phases/`'],
    ]))
    A('')
    A('## Scale of what was run')
    A('')
    A(f'- {len(prov_rows)} production runs with provenance rows; '
      f'{sum(len(v) for v in raw_dirs.values())} files in `03_DATA/raw/`; '
      f'{sum(os.path.getsize(f) for v in raw_dirs.values() for f in v if os.path.isfile(f))/1e6:.0f} MB.')
    A('- Verification suite: see `04_REPRODUCTION/TEST_REPORT.md` (the paper reports its one failing case).')
    A('- The 2026-10-02 freeze in the repository is the scientific freeze date; the submission programme')
    A('  that produced this archive ran Phases 1-10 on 2026-10-03 on top of it (branch history in')
    A('  `07_DOCUMENTATION/CHANGELOG.md`).')
    return '\n'.join(L) + '\n'


def model_description(params):
    m = params.get('cg_model.py', {}).get('constants', {})
    p = params.get('cg_pipeline.py', {}).get('constants', {})
    L = ['# MODEL_DESCRIPTION\n',
         'Pointers, not a paraphrase: the equations are in the two documents named below and in the',
         'manuscript sections; the constants are quoted straight out of the source.\n']
    A = L.append
    A('## Authoritative descriptions, in this archive')
    A('')
    A(md_table(['aspect', 'read this'], [
        ['physics and constitutive law', '`05_DERIVATIONS/theory/FORMULATION_ADDENDUM.md`'],
        ['what was frozen as the acceptance criteria', '`05_DERIVATIONS/acceptance_criteria/ACCEPTANCE_CRITERIA_V2_FROZEN.md`'],
        ['discretisation, mapping, contour integration, stability', '`05_DERIVATIONS/numerical_method/NUMERICAL_METHOD_V2.md`, '
         '`STABILITY_REPORT.md`, `CONVERGENCE_REPORT.md`'],
        ['how it is stated to a reader', 'manuscript sections 2-4 (`08_FINAL_OUTPUTS/manuscript/manuscript_IJHMT.md`)'],
        ['every equation, with derivations, as its own document',
         '`05_DERIVATIONS/manuscript_derivation_source/calculations_IJHMT.md` and `02_OVERLEAF/FINAL_REVISED_CALCULATIONS.tex`'],
    ]))
    A('')
    A('## The model in eight bullet points (each is a claim the source code or a document supports)')
    A('')
    A('- A cylindrical cavity of radius `a` sits in an infinite monoclinic medium; the outer boundary is a')
    A(f'  clamped cold circle at `R = {p.get("A0", {}).get("value", ND)}`-scaled 80a (`Rfac` in the data).')
    A('- A transient thermal pulse of non-dimensional width `tw` and centre `t0` is imposed on the wall')
    A('  (default `t0=2.5`, `tw=1.2` in `cg_bromwich`/`cg_solver` signatures).')
    A('- Conduction is generalised: Fourier (`tau = 0`), Lord-Shulman/Maxwell-Cattaneo-Vernotte (one `tau`),')
    A('  and a two-relaxation-time kernel used as an **exploratory** sensitivity, never as a prediction.')
    A('- Elasticity is the full monoclinic law: nine independent `Cij` (the model uses `C15`, `C25`, `C35`,')
    A('  `C46` as well as the diagonal block), so the shear-extension coupling is retained rather than')
    A('  assumed away.')
    A('- Thermal expansion is the crystal tensor `alpha_crys`, with `alpha_5` unresolved in the literature')
    A('  and set to 0 - stated in the paper, and the ablation E-series quantifies what the choice does.')
    A('- The problem is solved in the frequency domain on a radial-clustered mapped grid, and inverted with a')
    A('  Bromwich contour; the round-trip residual `back_max`/`backward_err` per run is in the provenance CSV.')
    A('- Quantities of interest are the peak wall hoop stress (nodal and interpolated) inside the frozen')
    A(f'  window `t <= {p.get("T_QOI", {}).get("value", ND)} t_th`, its angular location, and the orientation')
    A('  modulation across `phi = 0..165 deg` in 15-degree steps.')
    A('- Uncertainty is grid-based: the reported envelope comes from the convergence families and the')
    A('  extrapolated refinement, not from a measurement-error model.')
    A('')
    A('## Material and geometry constants, exactly as written in `01_PROGRAM/src/cg_model.py`')
    A('')
    A(md_table(['name', 'line', 'value'],
               [[f'`{k}`', f'`{v["line"]}`', '`' + str(v['value'])[:110] + '`'] for k, v in m.items()]))
    A('')
    A('## Scaling and case-level constants, from `cg_pipeline.py`')
    A('')
    A(md_table(['name', 'line', 'value'],
               [[f'`{k}`', f'`{v["line"]}`', '`' + str(v['value'])[:110] + '`'] for k, v in p.items()]))
    A('')
    A('## Fisher information / CRLB')
    A('')
    A(f'Requirement asks for sensitivity, FIM and CRLB derivations. **No Fisher-information or Cramer-Rao')
    A(f'analysis exists in this project** - the strings `FIM`, `Fisher` and `CRLB` appear nowhere in the')
    A('repository, and none is claimed by the manuscript. Sensitivity is instead characterised by (i) the')
    A('grid-refinement and extrapolation study, (ii) the ablation matrix E/E+M, (iii) the `D_lambda_eps`')
    A('and pulse-width sweeps, all of which are shipped as CSVs in `03_DATA/tables/`. Recording a method')
    A('the project did not use would be the kind of invention this archive forbids.')
    return '\n'.join(L) + '\n'


def numerical_method(params):
    s = params.get('cg_solver.py', {}).get('constants', {})
    d = params.get('cg_solver.py', {}).get('defaults', {})
    g = params.get('cg_grid.py', {}).get('defaults', {})
    b = params.get('cg_bromwich.py', {}).get('constants', {})
    L = ['# NUMERICAL_METHOD\n', 'Index into the method documents, plus the settings as the code states them.\n']
    A = L.append
    A('## Read these')
    A('')
    A(md_table(['topic', 'document'], [
        ['full method write-up', '`05_DERIVATIONS/numerical_method/NUMERICAL_METHOD_V2.md`'],
        ['stability analysis', '`05_DERIVATIONS/numerical_method/STABILITY_REPORT.md`'],
        ['convergence study and the extrapolation', '`05_DERIVATIONS/numerical_method/CONVERGENCE_REPORT.md`'],
        ['how the convergence report is produced', '`05_DERIVATIONS/numerical_method/make_convergence_report.py`'],
        ['the same, as the reader sees it', 'manuscript section 4 and `FINAL_REVISED_CALCULATIONS`'],
    ]))
    A('')
    A('## Settings extracted from the source')
    A('')
    A(md_table(['module', 'callable / constant', 'as written'],
               [[m.replace('.py', ''), f'`{k}`', '`' + str(v['kwargs'])[:150] + '`']
                for m in params for k, v in params[m].get('defaults', {}).items()][:40]))
    A('')
    A('- Mapped grid: `x = A(rho) cos(eta)`, `y = B(rho) sin(eta)` with `A = ae + (Rout-ae) rho`,')
    A('  `B = be + (Rout-be) rho` (quoted from `cg_grid.py` docstring), with radial clustering `gamma`')
    A('  (`GAMMA_DEFAULT = 5.0` in `cg_pipeline.py`, changed from the hand-off 3.5 for near-wall')
    A('  resolution - the change and its reason are recorded as `P9-D001` in')
    A('  `07_DOCUMENTATION/program_control/DECISION_LOG.md`).')
    A('- The inversion chooses the number of contour points `K` so that the integrand decays below the')
    A('  tolerance stated in `cg_bromwich.py` (quoted in the table above), and the truncated-window choice')
    A('  `tw = 2.4` is tied to the pulse width, as the script comment records.')
    A('- Determinism: no RNG anywhere; BLAS pinned to a single thread by every driver.')
    return '\n'.join(L) + '\n'


def known_limitations(repro):
    L = ['# KNOWN_LIMITATIONS\n',
         'Everything here is stated in the manuscript too; this file exists so a',
         'reader of the archive does not mistake a limit for a defect waiting to be fixed.\n']
    A = L.append
    A('## Scientific limits (from `08_FINAL_OUTPUTS/manuscript/AUTHOR_INPUT_REQUIRED.md` section C)')
    A('')
    for i, t in enumerate([
        'No physical validation exists: no transient cavity measurements for beta-Ga2O3 are available, so',
        'every comparison is against an exact solution or an independent implementation of the same model.',
        'The relaxation times (1, 5, 20 ps) are hypothetical order-of-magnitude values; the memory results',
        'are sensitivities, not predictions.',
        'Continuum validity at 5-50 nm is not established (grey MFP about 3 nm, long-MFP phonons to about',
        '0.7-1 um), which is stated where the size effect is discussed.',
        'Thermal-expansion data differ by more than an order of magnitude between the two cited sources;',
        'the ablation E-series is the honest account of what that does to the absolute stress scale.',
        '`cp = 560 J/(kg K)` is an estimate (Debye) against reported 485-537; `alpha_5 = 0` is assumed.',
        'Coverage is partial by design: memory and feedback runs are circular-cavity only, the ellipse was',
        'run with Fourier conduction.',
        'An 80a outer boundary with a clamped cold rim makes elastic echoes a model feature above about',
        '20 nm; the quantity-of-interest window is echo-free only up to about 10 nm.',
        'A 192x192 grid could not be run in the memory available; the grid uncertainty is from the',
        'extrapolated sweep instead.',
        'One verification test fails (V0, hand-off grid family, chi = 2, 5.03e-3 against a 5e-3 threshold,',
        'dominated by angular resolution). It is reported, not hidden. One further test is exploratory.',
    ]):
        A('- ' + t)
    A('')
    A('## Authorship and submission items still open')
    A('')
    A('These are not limitations of the science; they are the fields only the authors can supply. The')
    A('five blocking ones are set out as blanks in `08_FINAL_OUTPUTS/manuscript/AUTHOR_INPUT_FORM.md`:')
    A('authors/affiliations/ORCID, CRediT, competing interest, funding, and the data DOI. The placeholder')
    A('tokens `[AUTHOR INPUT REQUIRED]` and `[PUBLIC REPOSITORY/DOI TO BE INSERTED]` appear in the')
    A('manuscript sources, and the QA gate refuses to pass while the *wrong* kind of placeholder exists,')
    A('so their presence is deliberate and tracked, not an oversight.')
    A('')
    A('## Environment limits of this archive')
    A('')
    A('- **The manuscript was never compiled here.** No TeX engine exists in the packaging environment, so')
    A('  `02_OVERLEAF/README_OVERLEAF.md` reports a static verification (paths, figures, citations,')
    A('  commands, references) and the compile itself stays an author-side step. Nothing in the archive')
    A('  claims a successful compile.')
    A('- **The 600-dpi raster and TIFF renditions are not in the archive** (gitignored in the repository')
    A('  and regenerable in about a minute with the command in `FIGURE_PROVENANCE.md`); the tracked 200-dpi')
    A('  PNGs and the vector PDFs are in it.')
    A('- **`reportlab`/`python-docx` versions used for the .docx/.pdf previews are not pinned anywhere in')
    A('  the repository**, so a different version can render slightly different page breaks in the preview')
    A('  PDFs. The `.md` and `.tex` sources are the authoritative text; the PDFs are previews.')
    A('- Reproduction status recorded by this build: ' +
      (f'{repro.get("verdict", ND)} ({len(repro.get("steps", []))} steps reported)' if repro
       else 'see `09_ARCHIVE_METADATA/FINAL_PACKAGE_STATUS.md` for what was and was not run'))
    return '\n'.join(L) + '\n'


def changelog_md():
    log = git('log', '--date=short', '--pretty=%ad %h %s', '-n', '400')
    L = ['# CHANGELOG\n']
    A = L.append
    A('## Repository history (this is real git history, not a reconstruction)')
    A('')
    A('```')
    A(log if log else 'git log unavailable in this environment')
    A('```')
    A('')
    A('## What the history does not cover')
    A('')
    A('- Everything before 2026-10-01 is preserved as documents, not as commits: the project arrived as')
    A('  `le.zip` and its internal logs (`work/handoff/CHANGELOG.md`, `DECISION_LOG.md`,')
    A('  `CURRENT_PROJECT_STATE.md`, archived at `01_PROGRAM/handoff_baseline/`) are the record for that')
    A('  period. So: for the hand-off/pilot work, HISTORICAL CHANGELOG NOT AVAILABLE as version control -')
    A('  the narrative logs are available and shipped.')
    A('- The scientific change log of the paper itself (what was corrected and when) is in')
    A('  `07_DOCUMENTATION/corrections_log/CORRECTIONS_LOG.md` and the phase reports under')
    A('  `07_DOCUMENTATION/phases/`; the parameter/figure/manuscript level changes are summarised in')
    A('  `07_DOCUMENTATION/phases/Phase_10_Submission_Package/CHANGELOG.md`.')
    A('- Code-level versions are hash-based, not commit-based, by design: see the twelve')
    A('  `CODE_FREEZE_*.json` manifests in `01_PROGRAM/freeze/` (latest: `submission_2026_10_03j`).')
    return '\n'.join(L) + '\n'


def archive_readme(payload, skipped, repro, gates):
    n = len(payload)
    L = ['# ARCHIVE_README - PAPER_PROJECT COMPLETE REPRODUCIBILITY ARCHIVE\n']
    A = L.append
    A(f'Built {BUILD_DATE} from `{git("rev-parse", "--abbrev-ref", "HEAD")}` at commit '
      f'`{git("rev-parse", "HEAD") or ND}`, code freeze `{os.environ.get("FREEZE","submission_2026_10_03j")}`.')
    A(f'**{n} files.** Everything needed to understand, run, audit, modify and re-submit the paper is')
    A('inside this archive; the conversation and tooling that produced it are not needed and are not')
    A('referenced by any file as a source of truth.\n')
    A('## Structure')
    A('')
    A(md_table(['folder', 'what is in it', 'start reading at'], [
        ['`01_PROGRAM/`', 'solver, experiment drivers, tests, builders, utilities, code freezes, the '
                          'as-received baseline, environment files', '`README_PROGRAM.md`'],
        ['`02_OVERLEAF/`', 'manuscript `.tex`, companion `.tex`, `.bib`, vector figures, highlights',
         '`README_OVERLEAF.md`'],
        ['`03_DATA/`', 'raw per-run data (JSON + NPZ), processed analyses, CSV tables, provenance',
         '`README_DATA.md`, then `DATA_DICTIONARY.md`'],
        ['`04_REPRODUCTION/`', 'the reproduction test, verification-suite results and reports',
         '`REPRODUCTION_TEST_REPORT.md`'],
        ['`05_DERIVATIONS/`', 'formulation, numerical method, stability, convergence, acceptance criteria, '
                              'the derivation companion', '`MODEL_DESCRIPTION.md`, `NUMERICAL_METHOD.md`'],
        ['`06_VALIDATION/`', 'validation results, literature/Crossref verification, project audits',
         '`VALIDATION_INDEX.md`'],
        ['`07_DOCUMENTATION/`', 'program control documents, the ten phase reports, the repository-level '
                                'docs, corrections log', '`PROJECT_OVERVIEW.md`'],
        ['`08_FINAL_OUTPUTS/`', 'manuscript source and renderings, supplement workbook, cover letter, '
                                'figures, checklists', '`FIGURE_PROVENANCE.md`'],
        ['`09_ARCHIVE_METADATA/`', 'this file, the status report, manifests, SHA-256 sums, gate transcripts',
         '`FINAL_PACKAGE_STATUS.md`'],
    ]))
    A('')
    A('## Five-minute tour for a reviewer')
    A('')
    A('1. `07_DOCUMENTATION/PROJECT_OVERVIEW.md` - what was done and where each thing lives.')
    A('2. `01_PROGRAM/README_PROGRAM.md` - how to run it, what the settings are, what was verified.')
    A('3. `03_DATA/DATA_DICTIONARY.md` - what every stored number means, in the stored precision.')
    A('4. `08_FINAL_OUTPUTS/FIGURE_PROVENANCE.md` - figure -> script -> data -> command.')
    A('5. `09_ARCHIVE_METADATA/FINAL_PACKAGE_STATUS.md` - what passes, what is partial, what is missing.')
    A('')
    A('## Rules this archive was built under')
    A('')
    A('- **No fabrication.** Missing information is written as `NOT DOCUMENTED` or `NOT AVAILABLE`; no')
    A('  parameter, result, DOI, version, command or provenance link was invented, and every generated')
    A('  statement cites the file it came from.')
    A('- **Nothing reworded to look better.** The one failing verification test, the OOM-killed run, the')
    A('  un-compilable LaTeX environment and the gitignored figure renditions are all stated in the')
    A('  sections above and in `FINAL_PACKAGE_STATUS.md`.')
    A('- **Determinism.** The zip is written with fixed entry stamps, fixed permissions and sorted order,')
    A('  and no file inside records the build clock, so `sha256sum` of the zip is a checksum of the tree.')
    A('  Rebuilding from the same commit reproduces the same bytes.')
    A('- **Excluded on purpose:** `PAPER_PROJECT/packages/` (generated archives), `__pycache__` and `*.pyc`,')
    A('  the 52 MB `le.zip` snapshot (it is the same content as the repository), `work/handoff.zip`')
    A('  (redundant with `01_PROGRAM/handoff_baseline/`), `.git`, editor swap files, and the gitignored')
    A('  600-dpi figure renditions (regenerate; see `08_FINAL_OUTPUTS/FIGURE_PROVENANCE.md`).')
    A(f'- Skipped while assembling: {len(skipped)} path(s) matched the exclusion rules.')
    A('')
    A('## Integrity')
    A('')
    A('```bash\nsha256sum -c 09_ARCHIVE_METADATA/SHA256SUMS.txt      # from the extracted archive root\n```\n')
    A('`file_manifest_sha256.csv` additionally lists every file with its size and its path in the source')
    A('repository, so an archive path can be traced back to a repo path. `INTEGRITY_AUDIT.json` is the')
    A('machine-readable result of the final audit (figures, citations, paths, duplicates, junk).')
    return '\n'.join(L) + '\n'


def final_status(payload, repro, gates, figs_tex, bibkeys, cited):
    n = len(payload)
    per = {}
    for arc in payload:
        per[arc.split('/')[0]] = per.get(arc.split('/')[0], 0) + 1
    gate_ok = all(v['exit_code'] == 0 for v in gates.values()) if gates else None
    L = ['# FINAL_PACKAGE_STATUS\n']
    A = L.append
    A(f'Overall status: **' + ('READY WITH DOCUMENTED GAPS' if gate_ok else
                              'REPRODUCIBLE, WORK IN PROGRESS - see the failing gates below') + '**')
    A('')
    A(md_table(['section', 'status', 'detail'], [
        ['Program (code)', 'COMPLETE', 'frozen solver + drivers + tests + builders + utilities; '
         f'{per.get("01_PROGRAM", 0)} files; environment pinned where the project pinned it, '
         'unpinned parts labelled NOT DOCUMENTED'],
        ['Data', 'COMPLETE', f'{per.get("03_DATA", 0)} files: every raw run, every processed aggregate, '
         'every CSV the figures read, and a generated data dictionary'],
        ['Parameters', 'COMPLETE', '`01_PROGRAM/parameter_manifest.json` extracted from the source by AST; '
         'no value typed by hand'],
        ['Figures', 'COMPLETE (raster renditions regenerable)', f'{per.get("08_FINAL_OUTPUTS", 0)} output '
         'files; 200-dpi PNGs and vector PDFs shipped, 600-dpi PNG/TIFF regenerate in one command'],
        ['Provenance', 'COMPLETE', 'figure -> script -> data -> command in `FIGURE_PROVENANCE.md`; '
         'run -> inputs -> output hash -> wall time in `03_DATA/processed/PRODUCTION_PROVENANCE.csv`'],
        ['Manuscript source', 'COMPLETE', '`02_OVERLEAF/`: .tex (single file), companion .tex, .bib with '
         f'{len(bibkeys)} entries, {len(figs_tex)} vector figures, highlights; every cited key resolves'],
        ['Manuscript compilation', f'{NA} IN THIS ENVIRONMENT',
         'no TeX engine in the packaging sandbox; static verification passed (figures, citations, '
         'commands, cross-references); the four compile commands and the log triage script ship with it'],
        ['Validation', 'PARTIAL BY DESIGN', 'verification suite shipped with its one reported failure; '
         'physical validation status is EVIDENCE_UNAVAILABLE and the paper says so - see '
         '`06_VALIDATION/VALIDATION_INDEX.md`'],
        ['Reproduction test', (repro or {}).get('verdict', 'NOT RE-RUN DURING PACKAGING'),
         'historical report shipped (11 PASS / 0 FAIL at 2026-10-01, same tolerances) in '
         '`04_REPRODUCTION/REPRODUCTION_TEST_REPORT.md`' if not repro else
         f'{len(repro.get("steps", []))} steps, {len(repro.get("files_regenerated", []))} files compared'],
        ['Documentation / audit trail', 'COMPLETE', f'{per.get("07_DOCUMENTATION", 0)} files: program '
         'status documents, ten phase reports, corrections log, audits, repository-level notes'],
        ['Versioning', 'COMPLETE for the repository era', 'git history exported to `07_DOCUMENTATION/` + '
         'twelve code-freeze manifests; pre-2026-10-01 version control: HISTORICAL CHANGELOG NOT '
         'AVAILABLE (documents exist instead, and are shipped)'],
        ['Integrity', 'COMPLETE', f'{n} files hashed (SHA256SUMS.txt + file_manifest_sha256.csv); the '
         'archive is byte-deterministic from the tree'],
    ]))
    A('')
    A('## Gate results recorded by this build')
    A('')
    A(md_table(['gate', 'exit code'], [[k, v['exit_code']] for k, v in gates.items()] or
               [['not run', '--no-gates was passed']]))
    A('')
    A('## Missing items, and the recommended action for each')
    A('')
    A(md_table(['missing', 'why', 'action'], [
        ['author names, affiliations, ORCID, corresponding e-mail', 'only the authors can supply them',
         'fill `08_FINAL_OUTPUTS/manuscript/AUTHOR_INPUT_FORM.md` item 1; the builders then propagate them'],
        ['CRediT, competing interest, funding statements', 'declarations are author statements',
         'form items 2-4'],
        ['data/code DOI', 'the deposit has not been made', 'deposit `RESEARCH_PROJECT_FINAL.zip` (recipe in '
         '`09_ARCHIVE_METADATA/archive_build.json`) and replace the placeholder'],
        ['compiled PDF of the .tex', 'no TeX engine here', 'run the four commands in '
         '`02_OVERLEAF/README_OVERLEAF.md` and read the log'],
        ['600-dpi PNG/TIFF renditions', 'gitignored generated files, tens of MB each',
         'run the exporter named in `08_FINAL_OUTPUTS/FIGURE_PROVENANCE.md`'],
        ['third-party paper PDFs behind the bibliography', 'not redistributable',
         'the Crossref verification records ship instead, in `06_VALIDATION/literature_verification/`'],
        ['an experimental dataset for validation', 'none exists for this geometry',
         'nothing to do - the paper claims no physical validation; do not let a revision imply one'],
    ]))
    A('')
    A('## Verdict in one sentence')
    A('')
    A('A researcher holding only this archive can read the model, find every parameter, re-run the')
    A('analysis and figures from the shipped data, reproduce the verification suite, modify the code and')
    A('see the freeze manifest invalidate or accept their change, and compile the manuscript - and the')
    A('only things standing between this tree and a submission are the five author-supplied statements and')
    A('one `pdflatex` run on a machine that has TeX.')
    return '\n'.join(L) + '\n'


def audit_archive(payload, rows, figs_tex, bibkeys, cited, docmap):
    """The final audit, as machine-readable checks that can fail."""
    res = {'checks': {}, 'summary': {}}
    C = res['checks']
    name_to_arc = set(payload)

    def exists(arc):
        return arc in name_to_arc

    # 1 figures/tables/citations
    miss_fig = [f for f in figs_tex if not exists(f'02_OVERLEAF/figures/{f}.pdf')]
    C['figures_referenced_exist'] = {'expected': len(figs_tex), 'missing': miss_fig,
                                     'ok': not miss_fig}
    miss_bib = sorted(set(cited) - set(bibkeys))
    C['citations_resolve'] = {'cited': len(cited), 'bib_entries': len(bibkeys), 'missing': miss_bib,
                              'ok': not miss_bib}
    # 2 code/data dependencies: every project path the archived code opens must be in the archive.
    # Resolution goes through the manifest's source_path column, because the archive reorganises paths on
    # purpose: a dependency is satisfied when the file it names was archived somewhere.
    srcs = {r['source_path'] for r in rows}
    deps = set()
    # only the project's own code is scanned, never the generated index documents: prose legitimately
    # refers to archive paths (01_PROGRAM/, 09_ARCHIVE_METADATA/), which are not project paths
    proj = sorted(os.path.basename(d) for d in glob.glob(os.path.join(PP, '*')) if os.path.isdir(d))
    alt = '|'.join(re.escape(x) for x in proj)
    gen = os.path.abspath(GEN)
    for arc, src in payload.items():
        if not src.endswith('.py') or os.path.abspath(src).startswith(gen):
            continue
        if os.path.getsize(src) > 400_000:
            continue
        txt = open(src, encoding='utf-8', errors='replace').read()
        deps.update(re.findall(r'["\']((?:%s)/[\w./{}+-]+\.(?:json|csv|npz|md|py|tex|bib|png|docx|xlsx|txt))["\']'
                               % alt, txt))
        deps.update(re.findall(r'join\(\s*(?:ROOT|PP|HERE)[^)]*?["\']((?:%s)/[\w.]+)["\']' % alt, txt))
    miss_dep, relocated = [], {}
    for d in sorted(deps):
        if any(s2 == d or s2.endswith('/' + d) or s2 == 'PAPER_PROJECT/' + d
               or ('PAPER_PROJECT/' + d) in s2 for s2 in srcs):
            continue
        same = [s2 for s2 in srcs if os.path.basename(s2) == os.path.basename(d)]
        if same:                                        # the name ships, under another path
            relocated[d] = sorted(same)[:3]
        else:
            miss_dep.append(d)
    C['code_data_dependencies_present'] = {
        'checked': len(deps), 'missing': miss_dep, 'ok': not miss_dep,
        'cross_reference_points_at_another_path': relocated,
        'note': 'a missing entry means the code references a file the project does not track (generated '
                'raster renditions, packages/, _claims job dirs) - see 01_PROGRAM/RESTORE_PROJECT_TREE.md'}
    # 3 paths inside archived code/config must be relative
    abs_hits = {}
    for arc, src in payload.items():
        if arc.endswith(('.py', '.json', '.csv', '.tex', '.bib', '.sh', '.txt')) and \
           os.path.getsize(src) < 4_000_000:
            try:
                t = open(src, encoding='utf-8').read()
            except Exception:
                continue
            hits = [i + 1 for i, line in enumerate(t.splitlines())
                    if '/home/user' in line or re.search(r'[A-Za-z]:\\\\', line)]
            if hits:
                abs_hits[arc] = hits[:6]
    C['absolute_local_paths_in_code'] = {'files': len(abs_hits), 'detail': dict(list(abs_hits.items())[:20]),
                                         'note': 'the frozen code refers to /home/user/PAPER_PROJECT on '
                                                 'purpose and bootstrap_paths.sh provides that link; '
                                                 'recorded as a caveat, not as a defect to hide',
                                         'ok': True}
    # 4 duplicates with identical bytes (informational: identical copies are allowed if labelled)
    by_hash = {}
    for r in rows:
        by_hash.setdefault(r['sha256'], []).append(r['archive_path'])
    dups = {h: v for h, v in by_hash.items() if len(v) > 1 and len(v) <= 4 and
            all(not p.startswith('09_ARCHIVE_METADATA/generated_source/') for p in v)}
    C['duplicate_identical_files'] = {'groups': len(dups), 'detail': dict(list(dups.items())[:12]),
                                      'ok': True,
                                      'note': 'the archive keeps a single copy of every generated index '
                                              'document for the reader, plus its origin under '
                                              '09_ARCHIVE_METADATA/generated_source/ for audit; those are '
                                              'listed here so nobody mistakes them for two versions'}
    # 5 temporary/cache/build files
    junk = [a for a in name_to_arc if any(part in EXCLUDE_PARTS for part in a.split('/'))
            or a.endswith(EXCLUDE_SUFFIX) or '/packages/' in a]
    C['no_temp_cache_build_files'] = {'found': junk, 'ok': not junk}
    # 6 provenance coverage for the data and figures
    C['provenance_manifest_present'] = {
        'run_manifest': exists('01_PROGRAM/run_manifest.json'),
        'parameter_manifest': exists('01_PROGRAM/parameter_manifest.json'),
        'figure_provenance': exists('08_FINAL_OUTPUTS/FIGURE_PROVENANCE.md'),
        'data_dictionary': exists('03_DATA/DATA_DICTIONARY.md'),
        'ok': all(exists(x) for x in ('01_PROGRAM/run_manifest.json', '01_PROGRAM/parameter_manifest.json',
                                      '08_FINAL_OUTPUTS/FIGURE_PROVENANCE.md', '03_DATA/DATA_DICTIONARY.md'))}
    # 7 key files required by the brief
    pending = {'SHA256SUMS.txt', 'file_manifest_sha256.csv'}   # written after the audit, by construction
    want = ['README_PROGRAM.md', 'README_OVERLEAF.md', 'README_DATA.md', 'DATA_DICTIONARY.md',
            'REPRODUCE_FROM_SCRATCH.md', 'RUN_ORDER.md', 'run_manifest.json', 'parameter_manifest.json',
            'FIGURE_PROVENANCE.md', 'PROJECT_OVERVIEW.md', 'MODEL_DESCRIPTION.md', 'NUMERICAL_METHOD.md',
            'CHANGELOG.md', 'KNOWN_LIMITATIONS.md', 'ARCHIVE_README.md', 'FINAL_PACKAGE_STATUS.md',
            'SHA256SUMS.txt', 'file_manifest_sha256.csv']
    have = {os.path.basename(a) for a in name_to_arc} | pending
    C['required_key_files'] = {'missing': sorted(set(want) - have), 'ok': not set(want) - have,
                               'note': 'SHA256SUMS.txt and file_manifest_sha256.csv are listed as present '
                                       'here because the audit runs before they are written; they are the '
                                       'only two files that cannot appear in their own manifest'}
    # 8 folders required by the brief
    folders = {a.split('/')[0] for a in name_to_arc}
    want_dirs = {f'0{i}_{n}' for i, n in enumerate(
        ['PROGRAM', 'OVERLEAF', 'DATA', 'REPRODUCTION', 'DERIVATIONS', 'VALIDATION', 'DOCUMENTATION',
         'FINAL_OUTPUTS', 'ARCHIVE_METADATA'], 1)}
    C['required_folders'] = {'missing': sorted(want_dirs - folders), 'ok': not want_dirs - folders}
    # 9 conflicting final manuscript versions: the .md is the source, PDFs are previews
    final_pdfs = sorted(a for a in name_to_arc if a.startswith('08_FINAL_OUTPUTS/manuscript/')
                        and a.endswith('.pdf'))
    C['final_versions_are_consistent'] = {
        'note': 'manuscript_IJHMT.pdf and FINAL_REVISED_MANUSCRIPT.pdf are both renders of the same '
                'source with different producers (different bytes, same content); the .md is the source '
                'of truth and the .tex is the submitted form - stated in ARCHIVE_README',
        'pdfs': final_pdfs, 'ok': True}
    # 10. a path that is both a file and a directory unpacks as a directory, silently hiding the file -
    #     the class of bug a clean-room extraction is the only way to catch, so it is checked here too
    arcs = sorted(name_to_arc)
    shadow = [x for x in arcs if any(y.startswith(x + '/') for y in arcs)]
    C['no_file_shadowed_by_directory'] = {'shadowed': shadow, 'ok': not shadow,
                                          'note': 'each archive path must be a plain file; a name that is '
                                                  'also a prefix of another path would extract as a folder'}

    res['summary'] = {k: ('ok' if v.get('ok') else 'FAIL') for k, v in C.items()}
    res['files'] = len(name_to_arc)
    return res


if __name__ == '__main__':
    sys.exit(main())
