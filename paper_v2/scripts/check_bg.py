"""Bleustein-Gulyaev SH surface wave on a piezoelectric half-space y>0 (6mm, SH, polarisation along z).
u=A exp(-a y), phi=(e/eps)u + B exp(-k y); vacuum y<0: phi=C exp(k y).  Compare numeric secular determinant with closed forms."""
import numpy as np
from scipy.optimize import brentq
c44=1.0; rho=1.0; eps=1.0; k=1.0
def secular(v,K2,r0,metal=False):
    e=np.sqrt(K2*c44*eps); cb=c44+e**2/eps; vb=np.sqrt(cb/rho)
    a=k*np.sqrt(1-v**2/vb**2)
    # unknowns A,B,C ; eqs: sigma_yz=0, phi continuity, D_y continuity (or phi=0 for metallised)
    # sigma = c44 u_y + e phi_y ; u_y=-aA ; phi_y=(e/eps)(-aA)-kB
    r1=[-(c44*a)+e*(-(e/eps)*a),  -e*k, 0]
    if metal: r2=[e/eps,1,0]; r3=[0,0,1]       # phi(0)=0 ; C=0 (no vacuum field) 
    else:
        r2=[e/eps,1,-1]                            # phi continuity
        r3=[0,eps*k,r0*eps*k]                      # D_y: eps k B = -eps0 k C -> eps k B + eps0 k C = 0
    return np.linalg.det(np.array([r1,r2,r3]))
for K2 in [0.05,0.2,0.5]:
    cb2=1+K2; vb=np.sqrt(cb2)
    vm=vb*np.sqrt(1-(K2/(1+K2))**2)
    f=lambda v: secular(v,K2,0,True); 
    root=brentq(f,0.3,vb*0.99999) if f(0.3)*f(vb*0.99999)<0 else None
    print('K2=%.2f vbar=%.5f  closed-form metallised v=%.5f  numeric root=%s'%(K2,vb,vm,root))
    for r0 in [0.01,0.1,1.0]:
        al_k=(r0/(1+r0))*K2/(1+K2); vf=vb*np.sqrt(1-al_k**2)
        g=lambda v: secular(v,K2,r0,False); rt=brentq(g,0.3,vb*0.999999) if g(0.3)*g(vb*0.999999)<0 else None
        print('    eps0/eps=%.2f closed v=%.5f numeric=%s'%(r0,vf,rt))
