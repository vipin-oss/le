"""run_convergence_dirs.py — Phase 9 C4: which mesh direction controls the ellipse-tip stress? (2026-10-01)
Ellipse phi=30 deg (Fourier, a=10 nm): radial refinement, angular refinement and radial clustering varied separately."""
import sys, os, json, time
sys.dont_write_bytecode = True
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, '06_Source_Code', 'src'))
import numpy as np
import cg_pipeline as cp
RAW = os.path.join(ROOT, '09_Raw_Data', 'convergence'); os.makedirs(RAW, exist_ok=True)
OUT = os.path.join(ROOT, '10_Processed_Data', 'CONVERGENCE_DIRS.json')
cases = [(96, 48, 3.5), (192, 48, 3.5), (96, 96, 3.5), (96, 144, 3.5), (96, 48, 5.0), (96, 48, 6.5), (96, 96, 5.0), (144, 72, 5.0), (192, 96, 3.5)]
phi = float(sys.argv[1]) if len(sys.argv) > 1 else 30.0
res = {}
for Nr, Nt, gam in cases:
    tag = f'C4_ell_phi{int(phi):03d}_Nr{Nr}_Nt{Nt}_gam{gam:g}'
    src = {(96, 48, 3.5): f'C1_ell_phi{int(phi):03d}_F_g96', (192, 96, 3.5): f'C1_ell_phi{int(phi):03d}_F_g192'}.get((Nr, Nt, gam))
    if src and os.path.exists(os.path.join(RAW, src + '.json')):
        q = json.load(open(os.path.join(RAW, src + '.json')))
    elif os.path.exists(os.path.join(RAW, tag + '.json')):
        q = json.load(open(os.path.join(RAW, tag + '.json')))
    else:
        q = cp.run_config(tag, 'FOURIER', 0.0, 2.0, phi, cp.A0, outdir=RAW, Nr=Nr, Nt=Nt, gamma_grid=gam, quiet=True)
    res[f'{Nr}x{Nt}_gam{gam:g}'] = dict(sig_interp=q['sig_interp'], sig_nodal=q['sig_nodal'], th=q['th_star_interp_deg'], t_star=q['t_star'], wall_s=q.get('wall_s'))
    print(f'Nr={Nr:3d} Nt={Nt:3d} gamma={gam:.1f}: sig_interp={q["sig_interp"]:.1f}  nodal={q["sig_nodal"]:.1f}  th*={q["th_star_interp_deg"]:.1f}  ({q.get("wall_s", 0):.0f}s)', flush=True)
    json.dump(res, open(OUT, 'w'), indent=1)
