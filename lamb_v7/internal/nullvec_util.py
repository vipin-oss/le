import mpmath as mp, mpmats, numpy as np
import section8_tests as _T
def T_mp_roots(model,k,w,**kw):
    return _T.mp_roots(model,k,w,**kw)

def nullvec_mp(M):
    best=None
    for i in range(5):
        cof=[]
        for j in range(5):
            sub=mp.matrix(4,4)
            rows=[r for r in range(5) if r!=i]; cols=[c for c in range(5) if c!=j]
            for a,r in enumerate(rows):
                for b,c in enumerate(cols): sub[a,b]=M[r][c]
            cof.append(((-1)**(i+j))*mp.det(sub))
        n=max(abs(x) for x in cof)
        if best is None or n>best[0]: best=(n,cof,i)
    n,cof,i=best
    return [x/n for x in cof]

def rows_mp(p, eta, kk, a, lg, lnl):
    G=1+lg**2*(kk**2-eta**2); N=1+lnl**2*(kk**2-eta**2)
    X,Z,Ph,Nu,Th=a
    I=mp.mpc(0,1)
    szz=G*(I*kk*p.c13*X+eta*p.c33*Z)+eta*p.e33*Ph-p.b3*Th
    sxz=G*p.c44*(eta*X+I*kk*Z)+I*kk*p.e15*Ph
    l2=lg**2
    return [ (szz - l2*I*kk*eta*p.c44*(eta*X+I*kk*Z))/N,
             (sxz - l2*I*kk*eta*(I*kk*p.c11*X+eta*p.c13*Z))/N,
             l2*eta*p.c44*(eta*X+I*kk*Z)/N,
             l2*eta*(I*kk*p.c13*X+eta*p.c33*Z)/N,
             I*kk*p.e31*X+eta*p.e33*Z-eta*p.eps33*Ph+p.p3*Th,
             -p.Dn*eta*Nu+p.bn*p.n0*eta*Ph-p.beta_th*eta*Th,
             eta*Th]

def build_B_mp(model, k, w, h, lg=None, lnl=None):
    prm=mpmats.prm_from(model); kk=mp.mpf(repr(float(k))); ww=mp.mpf(repr(float(w)))
    lgv=mp.mpf(repr(model.lg)) if lg is None else mp.mpf(repr(lg))
    lnlv=mp.mpf(repr(model.lnl)) if lnl is None else mp.mpf(repr(lnl))
    fun={'Sumit':mpmats.sumit_M,'Neha':mpmats.neha_M,'Anu':mpmats.anu_M}[model.name]
    _,etas_mp=T_mp_roots(model,k,w,lg=lg,lnl=lnl)
    etas=[mp.mpc(x) for x in etas_mp]
    vecs=[nullvec_mp(fun(e,kk,ww,prm,lg=lgv,lnl=lnlv)) for e in etas]
    nb=7
    B=mp.matrix(2*nb,len(etas))
    hh=mp.mpf(repr(h))
    for fi,face in enumerate((1,-1)):
        for m,(eta,a) in enumerate(zip(etas,vecs)):
            b=rows_mp(model,eta,kk,a,lgv,lnlv)
            sc=mp.e**(eta*face*hh-abs(mp.re(eta))*hh)
            for r in range(nb): B[fi*nb+r,m]=b[r]*sc
    for i in range(B.rows):
        n=mp.sqrt(sum(abs(B[i,j])**2 for j in range(B.cols)))
        if n>0:
            for j in range(B.cols): B[i,j]=B[i,j]/n
    return B, etas
