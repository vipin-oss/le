import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fig_common import *
from interface_te import Med, solve
# ---- (A) oblique P incidence, welded elastic-elastic interface, P-SV, energy partition ----
def zoeppritz(th, m1, m2):
    r1,a1,b1=m1; r2,a2,b2=m2
    l1=r1*(a1**2-2*b1**2); mu1=r1*b1**2; l2=r2*(a2**2-2*b2**2); mu2=r2*b2**2
    p=np.sin(th)/a1
    def kz(v): return np.sqrt((1/v**2-p**2)+0j)
    w=1.0
    # wave vectors (omega=1): kx=p
    def wave(rho,lam,mu,v,kzv,kind,sign):
        kvec=np.array([p,sign*kzv]); 
        if kind=='P': pol=kvec/np.linalg.norm(kvec)
        else: pol=np.array([-kvec[1],kvec[0]])/np.linalg.norm(kvec)    # perpendicular (SV)
        return kvec,pol,lam,mu
    def fields(kvec,pol,lam,mu):
        ux,uz=pol
        div=1j*(kvec@pol)
        # strain components
        exx=1j*kvec[0]*ux; ezz=1j*kvec[1]*uz; exz=0.5j*(kvec[1]*ux+kvec[0]*uz)
        szz=lam*(exx+ezz)+2*mu*ezz; sxz=2*mu*exz
        return np.array([ux,uz,szz,sxz]),(szz,sxz)
    inc=wave(r1,l1,mu1,a1,kz(a1),'P',+1); rp=wave(r1,l1,mu1,a1,kz(a1),'P',-1); rs=wave(r1,l1,mu1,b1,kz(b1),'S',-1)
    tp=wave(r2,l2,mu2,a2,kz(a2),'P',+1); ts=wave(r2,l2,mu2,b2,kz(b2),'S',+1)
    F=lambda wv,rho: fields(wv[0],wv[1],wv[2],wv[3])[0]
    fi=F(inc,r1); frp=F(rp,r1); frs=F(rs,r1); ftp=F(tp,r2); fts=F(ts,r2)
    A=np.column_stack([frp,frs,-ftp,-fts]); x=np.linalg.solve(A,-fi)
    def flux(f,amp):  # time-avg z-flux into +z:  P_z = -1/2 Re(sigma_zj * conj(udot_j)), udot=-i w u (w=1)
        u=amp*f[:2]; szz=amp*f[2]; sxz=amp*f[3]; ud=-1j*u
        return -0.5*np.real(sxz*np.conj(ud[0])+szz*np.conj(ud[1]))
    Pin=flux(fi,1); 
    out=dict(RPP=-flux(frp,x[0])/Pin,RPS=-flux(frs,x[1])/Pin,TPP=flux(ftp,x[2])/Pin,TPS=flux(fts,x[3])/Pin)
    # total fluxes with cross-terms
    left=fi+x[0]*frp+x[1]*frs; right=x[2]*ftp+x[3]*fts
    def tot(f): u=f[:2]; ud=-1j*u; return -0.5*np.real(f[3]*np.conj(ud[0])+f[2]*np.conj(ud[1]))
    out['tot_left']=tot(left)/Pin; out['tot_right']=tot(right)/Pin
    return out
m1=(2.5,5.0,2.8); m2=(3.0,8.0,4.5)
ang=np.radians(np.linspace(0.5,89.5,300)); R=[zoeppritz(a,m1,m2) for a in ang]
sumnaive=np.array([r['RPP']+r['RPS']+r['TPP']+r['TPS'] for r in R])
print('max |sum-1| elastic oblique (naive sum):',np.max(abs(sumnaive-1)),' continuity of total flux:',max(abs(r['tot_left']-r['tot_right']) for r in R))
# normal incidence check vs impedance formula
n=zoeppritz(np.radians(0.01),m1,m2); Z1=m1[0]*m1[1]; Z2=m2[0]*m2[1]
print('normal incidence: RPP',n['RPP'],' impedance formula',((Z1-Z2)/(Z1+Z2))**2)
# ---- (B) thermoelastic normal incidence ----
m1t=Med(1.0,1.0,1.0,1.0,np.sqrt(0.1),tq=0.25); m2t=Med(2.0,1.2,0.8,0.6,np.sqrt(0.3),tq=0.15)
ws=np.logspace(-2,1.0,120); res=[solve(m1t,m2t,w) for w in ws]
# elastic-limit check: tiny coupling
m1e=Med(1.0,1.0,1.0,1.0,1e-6,tq=0.25); m2e=Med(2.0,1.2,0.8,0.6,1e-6,tq=0.15)
r0=solve(m1e,m2e,0.5); Zs=(1.0*1.0,2.0*1.2); print('eps->0 Re=',r0['Re'],' impedance',((Zs[0]-Zs[1])/(Zs[0]+Zs[1]))**2)
fig,ax=plt.subplots(1,3,figsize=(7.4,2.7))
deg=np.degrees(ang)
for key,lab,ls in [('RPP','R(P→P)','-'),('RPS','R(P→SV)','--'),('TPP','T(P→P)','-'),('TPS','T(P→SV)','--')]:
    ax[0].plot(deg,[r[key] for r in R],ls=ls,label=lab)
ax[0].plot(deg,sumnaive,color='k',lw=0.8,ls=':',label='sum')
ax[0].set_xlabel('incidence angle (deg)'); ax[0].set_ylabel('energy fraction'); ax[0].legend(frameon=False,fontsize=6); ax[0].set_title('(a) elastic, oblique P',fontsize=9,loc='left')
for key,lab,col in [('Re','reflected elastic','#0072B2'),('Te','transmitted elastic','#D55E00'),('Rt','reflected thermal','#009E73'),('Tt','transmitted thermal','#CC79A7')]:
    ax[1].semilogx(ws,[r[key] for r in res],label=lab,color=col)
ax[1].set_xlabel(r'$\omega/\omega_*$'); ax[1].set_ylabel('mode energy fraction'); ax[1].legend(frameon=False,fontsize=6); ax[1].set_title('(b) thermoelastic, normal',fontsize=9,loc='left')
ax[2].semilogx(ws,[r['naive_sum'] for r in res],color='k',label='sum of mode fractions')
ax[2].semilogx(ws,[1-(r['total_left']-r['total_right']) for r in res],color='#E69F00',ls='--',label='1 + (net flux left − right)')
ax[2].axhline(1,color='k',lw=0.5,ls=':'); ax[2].set_xlabel(r'$\omega/\omega_*$'); ax[2].legend(frameon=False,fontsize=6); ax[2].set_title('(c) energy bookkeeping',fontsize=9,loc='left')
fig.tight_layout(); save(fig,'fig_interface_energy')
print('thermoelastic: max deviation of naive sum from 1 over omega:',max(abs(r['naive_sum']-1) for r in res),' continuity of net flux max:',max(abs(r['total_left']-r['total_right']) for r in res))
for w,r in zip(ws[::30],res[::30]): print(round(w,3),round(r['naive_sum'],4))
