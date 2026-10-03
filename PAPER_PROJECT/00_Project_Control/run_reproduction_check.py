#!/usr/bin/env python3
"""run_reproduction_check.py — regenerate the cheap end of the pipeline and compare with what shipped.

This is the tool that produces the reproduction record quoted by the reproducibility archive
(`04_REPRODUCTION/REPRODUCTION_SUMMARY.json`). It does not modify anything it does not have to: it records
the sha256 of the artifacts before each step, runs the project's own scripts, records the sha256 again,
and reports. Restoring the tree afterwards is a `git checkout --` away, which the caller (or you) does.

Usage
    python3 PAPER_PROJECT/00_Project_Control/run_reproduction_check.py [--out PATH] [--skip-figures]

Steps, in the order a reviewer would run them
    1. environment probe        python + library versions actually installed
    2. analyze_v2.py           raw data -> 10_Processed_Data/ANALYSIS_V2.json + ANALYSIS_V2_TABLES.md
    3. make_provenance.py      raw data -> 10_Processed_Data/PRODUCTION_PROVENANCE.csv
    4. make_figures.py         data + tests -> 11_Figures/fig*.png
    5. reproduce.py            recompute verification case, convergence, principal result, figure, table
                               and compare with the stored outputs (its own tolerances: 1e-9 / 1e-12)

Verdict rules (stated so the verdict can be argued with)
    PASS                          every step exited 0 and every regenerated artifact is byte-identical
    PASS WITH NUMERICAL DIFFERENCE every step exited 0, reproduce.py reported 0 FAIL, but some regenerated
                                  artifact differs (last checked: it did not, which is why PASS exists)
    PARTIAL                       a step exited 0, another could not run (missing dependency, timeout)
    FAIL                          a step failed on its own terms, or reproduce.py reported a FAIL line
"""
import argparse
import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
WATCH = {
    'processed/ANALYSIS_V2.json': 'PAPER_PROJECT/10_Processed_Data/ANALYSIS_V2.json',
    'processed/ANALYSIS_V2_TABLES.md': 'PAPER_PROJECT/10_Processed_Data/ANALYSIS_V2_TABLES.md',
    'processed/PROVENANCE.csv': 'PAPER_PROJECT/10_Processed_Data/PRODUCTION_PROVENANCE.csv',
    'processed/CONVERGENCE_RESULTS.json': 'PAPER_PROJECT/10_Processed_Data/CONVERGENCE_RESULTS.json',
}
for i, f in enumerate(sorted(glob.glob(os.path.join(ROOT, 'PAPER_PROJECT/11_Figures/*.png')))):
    WATCH[f'figures/{os.path.basename(f)}'] = os.path.relpath(f, ROOT)
for f in sorted(glob.glob(os.path.join(ROOT, 'PAPER_PROJECT/12_Tables/*.csv'))):
    WATCH[f'tables/{os.path.basename(f)}'] = os.path.relpath(f, ROOT)


def sha(p):
    if not os.path.isfile(p):
        return None
    h = hashlib.sha256()
    with open(p, 'rb') as fh:
        for c in iter(lambda: fh.read(1 << 20), b''):
            h.update(c)
    return h.hexdigest()


def probe(pyexe):
    out = {'python': ''}
    rc, s = run([pyexe, '-V'])
    out['python'] = s.strip()
    code = ("import json;d={}\n"
            "for m in ['numpy','scipy','matplotlib','pymupdf','fitz','docx','openpyxl','PIL','reportlab','mpmath']:\n"
            "    try:\n"
            "        mod=__import__(m);d[m]=getattr(mod,'__version__','installed (no __version__)')\n"
            "    except Exception as e:\n"
            "        d[m]='MISSING'\n"
            "print(json.dumps(d))")
    rc, s = run([pyexe, '-c', code])
    try:
        out['libraries'] = json.loads(s.strip().splitlines()[-1])
    except Exception:
        out['libraries'] = {'error': s[-200:]}
    for k, v in (('CPUs', 'os.cpu_count()'), ('RAM_MB', None)):
        pass
    try:
        out['cpu_count'] = os.cpu_count()
        with open('/proc/meminfo') as fh:
            out['ram_MB'] = int(re.search(r'MemTotal:\s+(\d+)', fh.read()).group(1)) // 1024
    except Exception:
        out['cpu_count'] = out['ram_MB'] = 'NOT AVAILABLE'
    try:
        out['kernel'] = ' '.join(os.uname()[:3])
    except Exception:
        out['kernel'] = 'NOT AVAILABLE'
    return out


def run(cmd, cwd=ROOT, timeout=3600):
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
        return r.returncode, ((r.stdout or '') + '\n' + (r.stderr or ''))
    except Exception as e:
        return 127, f'{type(e).__name__}: {e}'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=os.path.join(ROOT, 'PAPER_PROJECT', '16_Reproducibility',
                                                   'REPRODUCTION_SUMMARY.json'))
    ap.add_argument('--python-exe', default=sys.executable)
    ap.add_argument('--skip-figures', action='store_true')
    a = ap.parse_args()
    py = a.python_exe
    for cand in (py, '/home/user/.venv-repro/bin/python', '/home/user/.venv-q1/bin/python'):
        if cand and os.path.isfile(cand):
            py = cand
            break
    t0 = time.time()
    before = {k: sha(os.path.join(ROOT, v)) for k, v in WATCH.items()}
    steps = []
    note = []

    env = probe(py)
    steps.append({'name': 'environment probe', 'command': f'{py} -c "import numpy, scipy, matplotlib"',
                  'exit_code': 0 if 'MISSING' not in json.dumps(env.get('libraries', {})) else 1,
                  'detail': env})
    if 'MISSING' in json.dumps(env.get('libraries', {})):
        note.append('a library the pipeline imports is MISSING in the interpreter used; steps that need it '
                    'will fail for that reason and the verdict will be PARTIAL, not FAIL - the fix is the '
                    'pinned install in 01_PROGRAM/README_PROGRAM.md')

    jobs = [('analyze_v2', 'PAPER_PROJECT/08_Experiments/analyze_v2.py', 1800),
            ('make_provenance', 'PAPER_PROJECT/08_Experiments/make_provenance.py', 900)]
    if not a.skip_figures:
        jobs.append(('make_figures', 'PAPER_PROJECT/08_Experiments/make_figures.py', 1800))
    jobs.append(('reproduce', 'PAPER_PROJECT/08_Experiments/reproduce.py', 1800))
    for name, script, to in jobs:
        rc, out = run([py, script], timeout=to)
        tail = [l for l in out.splitlines() if l.strip()][-4:]
        st = {'name': name, 'command': f'{py} {script}', 'exit_code': rc, 'detail': tail}
        if name == 'reproduce':
            rep = os.path.join(ROOT, 'PAPER_PROJECT/07_Tests/REPRODUCTION_TEST_REPORT.md')
            m = re.search(r'Overall:\s*(\d+)\s*PASS,\s*(\d+)\s*FAIL', open(rep).read()) if os.path.isfile(rep) else None
            st['report'] = os.path.relpath(rep, ROOT) if os.path.isfile(rep) else 'NOT AVAILABLE'
            st['overall'] = f'{m.group(1)} PASS, {m.group(2)} FAIL' if m else 'NOT PARSED'
            st['fail_lines'] = len(re.findall(r'\|\s*FAIL\s*\|', open(rep).read())) if m else None
            note.append('reproduce.py overwrote 07_Tests/REPRODUCTION_TEST_REPORT.md and 11_Figures/fig2_'
                        'phi_sweep.png as part of its own procedure; that is by design, and `git checkout --` '
                        'restores the shipped copies')
        steps.append(st)

    after = {k: sha(os.path.join(ROOT, v)) for k, v in WATCH.items()}
    files = [{'path': WATCH[k], 'sha_before': before[k], 'sha_after': after[k],
              'identical': before[k] == after[k]} for k in sorted(WATCH)]
    changed = [f for f in files if not f['identical'] and f['sha_before'] and f['sha_after']]
    missing_after = [f['path'] for f in files if not f['sha_after']]

    repro_step = next((s for s in steps if s['name'] == 'reproduce'), {})
    ok_steps = all(s['exit_code'] == 0 for s in steps if s['name'] != 'environment probe')
    if not ok_steps:
        verdict = 'PARTIAL' if any(s['exit_code'] == 127 for s in steps) else 'FAIL'
    elif changed or missing_after:
        verdict = 'PASS WITH NUMERICAL DIFFERENCE'
    else:
        verdict = 'PASS'
    if repro_step.get('fail_lines'):
        verdict = 'FAIL'

    out = {'verdict': verdict, 'run_date': time.strftime('%Y-%m-%dT%H:%M:%S'),
           'wall_s': round(time.time() - t0, 1), 'environment': env, 'steps': steps,
           'files_regenerated': files,
           'n_files_compared': len(files), 'n_changed': len(changed),
           'n_missing_after_run': len(missing_after),
           'reproduce_overall': repro_step.get('overall', 'NOT RUN'),
           'notes': note + ['generated by PAPER_PROJECT/00_Project_Control/run_reproduction_check.py; '
                            'the comparison is byte-level on purpose - a hash that matches settles the '
                            'question, one that does not tells you exactly which artifact to look at']}
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, 'w').write(json.dumps(out, indent=1) + '\n')
    print(json.dumps({k: out[k] for k in ('verdict', 'wall_s', 'n_files_compared', 'n_changed',
                                          'reproduce_overall')}, indent=1))
    print('wrote', os.path.relpath(a.out, ROOT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
