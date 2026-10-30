import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fig_common import *
# rounded handbook values (SI): c11,c12,c44 [GPa], alpha [1/K], rho, cp [J/kg/K]; T0=300 K
MAT={'Cu':dict(c=(168.4,121.4,75.4),al=16.5e-6,rho=8960,cp=385),'Si':dict(c=(165.7,63.9,79.6),al=2.6e-6,rho=2329,cp=700),
     'Al':dict(c=(108.2,61.3,28.5),al=23.1e-6,rho=2700,cp=897)}
T0=300.
def stiff(c11,c12,c44):
    C=np.zeros((3,3,3,3)); v={(0,0):0,(1,1):1,(2,2):2,(1,2):3,(2,1):3,(0,2):4,(2,0):4,(0,1):5,(1,0):5}
    M=np.zeros((6,6)); 
    for i in range(3):
        for j in range(3): M[i,j]=c11 if i==j else c12
    for i in range(3,6): M[i,i]=c44
    for (i,j),a in v.items():
        for (k,l),b in v.items(): C[i,j,k,l]=M[a,b]
    return C*1e9
def speeds(mat,n,coupled):
    p=MAT[mat]; C=stiff(*p['c']); rho=p['rho']; cv=rho*p['cp']; beta0=(p['c'][0]+2*p['c'][1])*1e9*p['al']
    G=np.einsum('ijkl,j,l->ik',C,n,n)
    if coupled: G=G+beta0**2*T0/cv*np.outer(n,n)
    w,v=np.linalg.eigh(G); return np.sqrt(w/rho)
res={}
for mat in MAT:
    p=MAT[mat]; cv=p['rho']*p['cp']; b0=(p['c'][0]+2*p['c'][1])*1e9*p['al']
    out=[]
    for name,n in [('[100]',np.array([1,0,0.])),('[110]',np.array([1,1,0.])/np.sqrt(2)),('[111]',np.array([1,1,1.])/np.sqrt(3))]:
        vi=speeds(mat,n,False)[-1]; va=speeds(mat,n,True)[-1]
        M=vi**2*p['rho']; out.append((name,vi,va,(va/vi-1)*100,b0**2*T0/(cv*M)))
    res[mat]=out
    print(mat,'beta0=%.3g Pa/K cv=%.3g'%(b0,cv)); 
    for o in out: print('  %s v_iso=%.0f v_ad=%.0f m/s  shift=%.3f%%  eps=%.4g'%o)
fig,ax=plt.subplots(1,2,figsize=(7.2,2.9))
th=np.linspace(0,np.pi/2,400)
for mat,col in [('Cu',C['LS']),('Si',C['DPL']),('Al',C['GN'])]:
    d=[]
    for t in th:
        n=np.array([np.cos(t),np.sin(t),0]); vi=speeds(mat,n,False)[-1]; va=speeds(mat,n,True)[-1]; d.append((va/vi-1)*100)
    ax[1].plot(np.degrees(th),d,color=col,label=mat)
    if mat=='Cu':
        for t in th[::40]: pass
ax[1].set_xlabel('propagation angle from [100] in (001) plane (deg)'); ax[1].set_ylabel(r'$(v_{\rm ad}/v_{\rm iso}-1)$ (\%) quasi-L'); ax[1].legend(frameon=False); ax[1].set_title('(b) adiabatic stiffening',fontsize=9,loc='left')
for mat,col in [('Cu',C['LS'])]:
    vi=[];va=[]
    for t in th:
        n=np.array([np.cos(t),np.sin(t),0]); vi.append(speeds(mat,n,False)); va.append(speeds(mat,n,True))
    vi=np.array(vi);va=np.array(va)
    for j,ls in zip(range(3),[':','--','-']): ax[0].plot(np.degrees(th),va[:,j]/1e3,color=col,ls=ls,label=['slow shear','fast shear','quasi-L'][j])
ax[0].set_xlabel('angle from [100] (deg)'); ax[0].set_ylabel('adiabatic speed in Cu (km/s)'); ax[0].legend(frameon=False,fontsize=7); ax[0].set_title('(a) Cu, (001) plane',fontsize=9,loc='left')
fig.tight_layout(); save(fig,'fig_aniso')
import json; json.dump({m:[list(map(float,o[1:])) for o in res[m]] for m in res},open('aniso_out.json','w'))
