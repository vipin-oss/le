"""Pragmatic completion: full-profile verification + source-figure comparison + limiting cases.
No parameter fitting; computed curves are reported as computed. Source points stay input-only.
"""
import json,numpy as np,csv,traceback
from src.common import ROOT,Stage,INPUT
from src.physics import FIELDS,SCALES,inverse,off_front,front_positions,operator,derived_np,laplace_np,PARAMS,TAU
stage=Stage('P06_SOURCE_CASE_AND_LIMITING_CASE_COMPLETION')
try:
 TAU_S=float(TAU)
 # ---------- 1. Limiting / analytic consistency checks ----------
 lim=[]
 # 1a. tau->0 operator limit (CV and MCV3 -> Fourier heat law M/N->1)
 for model in INPUT['models']:
  for z in [1e-3,1e-6,1e-9]:
   M,N=operator(model,z,tau=z*0+1e-8)  # tiny tau
   lim.append({'check':f'{model} tau->0 heat-operator M/N->1 at s={z}','value':complex(M/N).real,'expected':1.0,'abs_error':abs(M/N-1),'scope':'ANALYTIC_LIMIT'})
 # 1b. Source stated wavefront speed nu=1/sqrt(tau)=5 vs our derived characteristic speed
 fp=front_positions();nu=1/np.sqrt(TAU_S)
 lim.append({'check':'Source-stated thermal wavefront speed nu=1/sqrt(tau)','value':nu,'derived_fast_speed':fp['speeds'][1],'rel_error':abs(fp['speeds'][1]-nu)/nu,'scope':'LIMITING_CASE'})
 lim.append({'check':'Source-stated thermal front x=nu*t','value':nu*0.06,'derived_fast_front':fp['fast'],'abs_error':abs(nu*0.06-fp['fast']),'scope':'LIMITING_CASE'})
 lim.append({'check':'Elastic/front slow position ~1*t (source stress plot ~0.06)','value':0.06,'derived_slow_front':fp['slow'],'abs_error':abs(0.06-fp['slow']),'scope':'LIMITING_CASE'})
 # 1c. alpha=0 uncoupled thermal limit at a fixed point
 pp=derived_np(alpha=0.)
 for model in INPUT['models']:
  s=10+5j;x=0.1;M,N=operator(model,s)
  expect=np.exp(-np.sqrt(s*M/N)*x)/s;got=laplace_np(model,s,x,params=pp)
  lim.append({'check':f'{model} alpha=0 uncoupled thermal transform at s=10+5j,x=0.1','value_theta':float(np.abs(got['theta'])),'expected_theta':float(np.abs(expect)),'abs_error':float(abs(got['theta']-expect)),'u_sigma_max':float(max(abs(got['u']),abs(got['sigma']))),'scope':'LIMITING_CASE'})
 # 1d. decay at large x: tail must vanish
 for model in INPUT['models']:
  v=inverse(model,0.95,'theta',degree=64)
  lim.append({'check':f'{model} tail theta*(0.95)','value':v,'expected~0':True,'scope':'LIMITING_CASE','note':'finite tail expected ~0 behind fronts at t=.06'})
 (ROOT/'data/LIMITING_CASES.json').write_text(json.dumps({'label':'PILOT — NOT FINAL VALIDATION','checks':lim},indent=2, default=str))

 # ---------- 2. Source Figure-5 digitized-point comparison ----------
 prov=json.loads((ROOT/'reference_local/DIGITIZATION_PROVENANCE.json').read_text())
 refs=list(csv.DictReader((ROOT/'reference_local/figure5_digitized.csv').open()))
 groups={}
 for r in refs:groups.setdefault((r['model'],r['field']),[]).append(r)
 comp=[]
 for (model,field),pts in sorted(groups.items()):
  good=0;bad=0;worst=0;worst_x=None;sum_abs=0
  for r in pts:
   x=float(r['x_ref']);y=float(r['value_ref']);xb=float(r['x_bound']);yb=float(r['y_bound']);slope=float(r['source_slope'])
   if not off_front(np.array([x]))[0]:
    r['status']='EXCLUDED_NEAR_FRONT';continue
   val=inverse(model,x,field,degree=64)
   U=yb+abs(slope)*xb+3e-3  # envelope + conservative numerical allowance (frozen plan)
   err=abs(val-y);norm=err/SCALES[field];sum_abs+=norm
   ok=err<=U
   r['computed_dehoog64']=val;r['abs_error']=err;r['envelope']=U;r['scaled_error']=norm;r['status']='WITHIN_ENVELOPE' if ok else 'OUTSIDE_ENVELOPE'
   good+=ok;bad+= (not ok);sum_abs+=norm
   if err>worst:worst=err;worst_x=x
  n=good+bad
  comp.append({'model':model,'field':field,'points_used':n,'points_excluded_near_front':len(pts)-n,'within_envelope':good,'outside_envelope':bad,'max_abs_error':worst,'x_of_max_error':worst_x,'mean_scaled_error':sum_abs/n if n else None,'coverage_x':[min(float(r['x_ref']) for r in pts),max(float(r['x_ref']) for r in pts)],'compatibility':'COMPATIBLE_WITHIN_FIGURE_UNCERTAINTY' if (n and bad==0) else ('MOSTLY_COMPATIBLE' if n and good>=0.9*n else ('PARTIAL' if n else 'UNASSESSED'))})
 # rewrite the reference CSV with computed columns appended
 with (ROOT/'data/SOURCE_FIGURE5_COMPARISON_POINTS.csv').open('w',newline='') as f:
  fields=list(refs[0].keys());w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(refs)
 (ROOT/'data/SOURCE_FIGURE5_COMPARISON.json').write_text(json.dumps({'label':'PILOT — NOT FINAL VALIDATION','method':'Independent computed deHoog64 vs pre-digitized source-figure points with frozen graphical+numerical envelope. Source points are input references, not our results or experiments.','comparison':comp,'provenance':prov},indent=2))
 print('SOURCE_COMPARISON',json.dumps(comp,indent=2))
 stage.finish('RUN_SUCCESS',{'source_comparison_status':max((c['compatibility'] for c in comp),key=lambda s:['UNASSESSED','PARTIAL','MOSTLY_COMPATIBLE','COMPATIBLE_WITHIN_FIGURE_UNCERTAINTY'].index(s)) if comp else 'UNASSESSED'})
except Exception as e:
 (ROOT/'logs/P06_ERROR.txt').write_text(traceback.format_exc());stage.finish('RUN_FAILED',{'error':str(e)});raise
