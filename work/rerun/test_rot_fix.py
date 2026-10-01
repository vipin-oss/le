import sys, os, json, time
os.environ['OPENBLAS_NUM_THREADS']='1'
sys.path.insert(0,'/home/user/work/rerun/proj'); sys.path.insert(0,'/home/user/work/rerun/proj/src')
import numpy as np
import run_production as rp
import cg_model
from cg_model import Cij_GPa, GPa, alpha_crys

orig = rp.rotate_Q_beta
def fixed(Q, beta, phi):
    Qr, br = orig(Q, beta, phi)
    c, s = np.cos(phi), np.sin(phi)
    br = br.copy()
    br[1] += 4*s*c*Cij_GPa['C25']*GPa*alpha_crys[1]      # correct sign of the 2*s*c*C25 cross-term in C23'
    return Qr, br

out = '/home/user/work/rerun/out'; os.makedirs(out, exist_ok=True)
rp.DATA = out
stored = lambda tag: json.load(open(f'/home/user/work/rerun/proj/data/PROD/{tag}.json'))['sig_max']
res = {}
for mode in ('orig','fixed'):
    rp.rotate_Q_beta = orig if mode=='orig' else fixed
    for phi in (15, 45, 105, 135):
        tag = f'{mode}_chi1_phi{phi:03d}'
        q = rp.run_config(tag, 'FOURIER', 0.0, 1.0, phi, rp.A0)
        res[(mode,phi)] = q['sig_max']
print()
print("phi | stored(handoff)   | rerun-orig        | rerun-FIXED       | orig vs stored")
for phi in (15,45,105,135):
    s = stored(f'A_chi1_phi{phi:03d}')
    print(f"{phi:3d} | {s:.6f} | {res[('orig',phi)]:.6f} | {res[('fixed',phi)]:.6f} | {abs(res[('orig',phi)]-s)/abs(s):.2e}")
print()
for a,b in ((15,105),(45,135)):
    s0 = stored('A_chi1_phi000')
    print(f"90-deg pair ({a},{b}):  ORIGINAL rel diff = {abs(res[('orig',a)]-res[('orig',b)])/abs(res[('orig',a)]):.3e}   |   FIXED rel diff = {abs(res[('fixed',a)]-res[('fixed',b)])/abs(res[('fixed',a)]):.3e}")
vals_fixed = [abs(res[('fixed',p)]) for p in (15,45,105,135)] + [abs(stored('A_chi1_phi000'))]
print("FIXED circle scatter over {0,15,45,105,135}: %.3e" % ((max(vals_fixed)-min(vals_fixed))/np.mean(vals_fixed)))
print("FIXED sig values:", [f"{v:.4f}" for v in vals_fixed])
