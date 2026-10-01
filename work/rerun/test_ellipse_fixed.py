import sys, os, json, time
os.environ['OPENBLAS_NUM_THREADS']='1'
sys.path.insert(0,'/home/user/work/rerun/proj'); sys.path.insert(0,'/home/user/work/rerun/proj/src')
import numpy as np
import run_production as rp
from cg_model import Cij_GPa, GPa, alpha_crys
orig = rp.rotate_Q_beta
def fixed(Q, beta, phi):
    Qr, br = orig(Q, beta, phi)
    c, s = np.cos(phi), np.sin(phi)
    br = br.copy(); br[1] += 4*s*c*Cij_GPa['C25']*GPa*alpha_crys[1]
    return Qr, br
rp.rotate_Q_beta = fixed
out='/home/user/work/rerun/out_ell'; os.makedirs(out,exist_ok=True); rp.DATA=out
stored=lambda tag: json.load(open(f'/home/user/work/rerun/proj/data/PROD/{tag}.json'))['sig_max']
rows=[]
for phi in range(0,180,15):
    q=rp.run_config(f'fixed_chi2_phi{phi:03d}','FOURIER',0.0,2.0,phi,rp.A0)
    rows.append((phi, abs(stored(f'A_chi2_phi{phi:03d}')), abs(q['sig_max'])))
print("\nphi | ellipse stored (Pa/K) | ellipse FIXED (Pa/K) | rel diff")
for phi,s,f in rows: print(f"{phi:3d} | {s:.1f} | {f:.1f} | {(f-s)/s:+.3e}")
S=np.array([r[1] for r in rows]); F=np.array([r[2] for r in rows])
amp=lambda x:(x.max()-x.min())/x.mean()
print("amplitude stored: %.4f   FIXED: %.4f" % (amp(S),amp(F)))
print("range stored: %.4f - %.4f MPa/K ; FIXED: %.4f - %.4f MPa/K" % (S.min()/1e6,S.max()/1e6,F.min()/1e6,F.max()/1e6))
json.dump(dict(rows=rows),open('/home/user/work/rerun/ellipse_fixed_summary.json','w'))
