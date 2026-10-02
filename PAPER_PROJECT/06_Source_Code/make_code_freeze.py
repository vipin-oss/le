"""make_code_freeze.py — record SHA-256 of code, scripts and environment (MASTER_PROMPT §45, §83). Run at the production gate."""
import hashlib, json, os, platform, sys, time
import numpy, scipy, matplotlib
def _pp_root(_start):
    """walk up from _start to the PAPER_PROJECT directory (path-independent replacement
    for the hard-coded '/home/user/PAPER_PROJECT' that used to be here)."""
    _p = os.path.abspath(_start)
    while True:
        if os.path.basename(_p) == 'PAPER_PROJECT':
            return _p
        _q = os.path.dirname(_p)
        if _q == _p:
            break
        _p = _q
    return os.environ.get('PAPER_PROJECT_ROOT', '/home/user/PAPER_PROJECT')
ROOT = _pp_root(os.path.dirname(os.path.abspath(__file__)))
files = sorted([os.path.join(ROOT, '06_Source_Code', 'src', f) for f in os.listdir(os.path.join(ROOT, '06_Source_Code', 'src')) if f.endswith('.py')] +
               [os.path.join(ROOT, '08_Experiments', f) for f in ('production_matrix.py', 'run_production_v2.py', 'run_convergence.py', 'run_convergence_dirs.py', 'analyze_v2.py', 'make_figures.py', 'reproduce.py', 'make_provenance.py')] +
               [os.path.join(ROOT, '07_Tests', f) for f in ('run_tests.py', 'run_tests_supplement.py', 'make_test_report.py')] +
               [os.path.join(ROOT, '13_Manuscript', f) for f in ('build_manuscript.py', 'ms_static.py', 'ms_results.py', 'docbuilder.py', 'build_supplement.py')])
out = dict(date=time.strftime('%Y-%m-%dT%H:%M:%S'), label=sys.argv[1] if len(sys.argv) > 1 else 'freeze',
           python=sys.version.split()[0], numpy=numpy.__version__, scipy=scipy.__version__, matplotlib=matplotlib.__version__,
           platform=platform.platform(), files={os.path.relpath(f, ROOT): hashlib.sha256(open(f, 'rb').read()).hexdigest() for f in files if os.path.exists(f)})
name = os.path.join(ROOT, '06_Source_Code', f"CODE_FREEZE_{out['label']}.json")
json.dump(out, open(name, 'w'), indent=1); print('wrote', name, len(out['files']), 'files')
