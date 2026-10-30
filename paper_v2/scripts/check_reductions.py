"""Symbolic checks of the reductions of the heat-flux function G(s) (template)."""
import sympy as sp
s,k,ks,tq,tT,tv,t0=sp.symbols('s k ks tq tT tv t0',positive=True)
G=(k*(1+tT*s)+ks*(1+tv*s)/s)/(1+tq*s)
def lim(expr,**kw):
    e=expr.subs(kw); return sp.simplify(e)
LS=k/(1+t0*s)
res={}
res['DPL -> LS : tT->0, tq=t0 ']=sp.simplify(G.subs({ks:0,tT:0,tq:t0})-LS)==0
res['DPL tq->0 (tT fixed) = Fourier with rate term k(1+tT s)']=sp.simplify(G.subs({ks:0,tq:0})-k*(1+tT*s))==0
res['TPL -> DPL : ks->0']=sp.simplify(sp.limit(G,ks,0)-G.subs(ks,0))==0
res['GN-II: k=0,tq=tT=tv=0 -> ks/s']=sp.simplify(G.subs({k:0,tq:0,tT:0,tv:0})-ks/s)==0
res['GN-III: tq=tT=tv=0 -> k+ks/s']=sp.simplify(G.subs({tq:0,tT:0,tv:0})-(k+ks/s))==0
res['TPL -> classical needs ks->0 and all lags->0']=sp.simplify(G.subs({ks:0,tq:0,tT:0,tv:0})-k)==0
res['G(0): finite iff ks=0 (else ~ ks/s)']=(sp.limit(G.subs(ks,0),s,0)==k) and (sp.limit(s*G,s,0)==ks)
res['DPL G(inf)=k tT/tq']=sp.limit(G.subs({ks:0}),s,sp.oo)==k*tT/tq
res['LS G(inf)=0']=sp.limit(LS,s,sp.oo)==0
for kk,v in res.items(): print(('OK   ' if v else 'FAIL ')+kk)
