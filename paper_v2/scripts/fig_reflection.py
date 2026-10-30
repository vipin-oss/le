import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fig_common import *
nu=0.3; cs2=(1-2*nu)/(2-2*nu); mu=cs2; lam=1-2*mu     # c1=1, rho=1, c_v=1, k_cond=1, T0=1
def cols(w,kx,eps,G,bc):
    s=-1j*w; beta=np.sqrt(eps)
    a=G; b=-(G*s**2+s+eps*s); c=s**3
    d=np.sqrt(b*b-4*a*c+0j); kap=[(-b+d)/(2*a),(-b-d)/(2*a)]
    kap.sort(key=lambda z:abs(z+w**2))      # elastic-type root first (kappa ~ -w^2)
    ms=[np.sqrt(kk+kx**2+0j) for kk in kap]; ms=[m if m.real>0 else -m for m in ms]
    msh=np.sqrt(s**2/cs2+kx**2+0j); msh=msh if msh.real>0 else -msh
    th=[(kk-s**2)/beta for kk in kap]
    def col_dil(j,sg):
        m=sg*ms[j]
        return np.array([lam*kap[j]+2*mu*m**2-beta*th[j], -2*mu*1j*kx*m, (-m*th[j]) if bc=='ins' else th[j]])
    def col_sh(sg):
        m=sg*msh
        return np.array([2*mu*1j*kx*m, mu*(m**2+kx**2), 0.0])
    return col_dil,col_sh,kap,ms,msh
def refl(w,theta,eps,G,bc='ins'):
    # incident elastic-type P at angle theta: kx = Re k1 sin(theta)
    s=-1j*w
    _,_,kap0,_,_=cols(w,1e-9,eps,G,bc); k1=np.sqrt(-kap0[0]) if False else None
    kP=np.sqrt(-kap0[0]+0j)                       # complex wavenumber magnitude of elastic-type wave (kappa=-kP^2)
    kx=kP.real*np.sin(theta)
    cd,cs_,kap,ms,msh=cols(w,kx,eps,G,bc)
    inc=cd(0,-1)                                   # incoming: reversed y-dependence
    M=np.column_stack([cd(0,+1),cd(1,+1),cs_(+1)])
    x=np.linalg.solve(M,-inc)
    return x, kP, kx
def run(w,eps,G,bc,thetas):
    RPP=[];RPS=[];RT=[]
    for t in thetas:
        x,kP,kx=refl(w,t,eps,G,bc); RPP.append(abs(x[0])); RPS.append(abs(x[2])*(np.sqrt(1/cs2))); 
    return np.array(RPP),np.array(RPS)
def elastic(theta):
    c12=cs2   # (c2/c1)^2
    r=1/np.sqrt(cs2); sphi=np.sin(theta)*np.sqrt(cs2); phi=np.arcsin(sphi)
    D=np.sin(2*theta)*np.sin(2*phi)+r**2*np.cos(2*phi)**2
    return abs((np.sin(2*theta)*np.sin(2*phi)-r**2*np.cos(2*phi)**2)/D), abs(2*r*np.sin(2*theta)*np.cos(2*phi)/D)
th=np.radians(np.linspace(1,70,69))
# validation: elastic limit (tiny eps, low frequency) vs closed-form free-surface coefficients
rp,rs=run(0.5,1e-10,1.0,'ins',th); ep=np.array([elastic(t)[0] for t in th]); es=np.array([elastic(t)[1] for t in th])
print('validation max|R_PP diff|=%.2e  max|R_PS diff| (potential->disp scaling)=%.2e'%(np.max(abs(rp-ep)),np.max(abs(rs-es))))
print('sample: theta=30deg  numeric RPP %.4f RPS %.4f ; closed form %.4f %.4f'%(rp[29],rs[29],ep[29],es[29]))
fig,ax=plt.subplots(1,2,figsize=(7.2,2.9)); eps=0.1
for lab,Gf,col,ls in [('classical',lambda s:1.0,C['CD'],'-'),('LS $\\tau\\omega_*=0.25$',lambda s:1/(1+0.25*s),C['LS'],'--')]:
    for w,al in [(1.0,1.0),(0.1,0.45)]:
        G=Gf(-1j*w); rp_,rs_=run(w,eps,G,'ins',th)
        ax[0].plot(np.degrees(th),rp_,color=col,ls=ls,alpha=al,label=lab+r', $\omega/\omega_*=%g$'%w); ax[1].plot(np.degrees(th),rs_,color=col,ls=ls,alpha=al)
ax[0].plot(np.degrees(th),ep,'k:',lw=0.8,label='elastic'); ax[1].plot(np.degrees(th),es,'k:',lw=0.8)
ax[0].set_xlabel('incidence angle (deg)'); ax[0].set_ylabel('$|R_{PP}|$'); ax[0].legend(frameon=False,fontsize=6); ax[0].set_title('(a) P$\\to$P',fontsize=9,loc='left')
ax[1].set_xlabel('incidence angle (deg)'); ax[1].set_ylabel('$|R_{PS}|$'); ax[1].set_title('(b) P$\\to$SV conversion',fontsize=9,loc='left')
fig.tight_layout(); save(fig,'fig_reflection')
for w in [0.1,1.0]:
    for lab,G in [('classical',1.0),('LS',1/(1+0.25*(-1j*w)))]:
        rp_,rs_=run(w,eps,G,'ins',th); print('w=%.1f %s: |RPP| at 20,45,60 deg:'%(w,lab),np.round(rp_[[19,44,59]],4),' |RPS|',np.round(rs_[[19,44,59]],4))
