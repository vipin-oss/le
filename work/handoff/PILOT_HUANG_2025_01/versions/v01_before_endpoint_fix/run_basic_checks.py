import json,numpy as np,sys,traceback
from src.common import ROOT,Stage,sha
from src.physics import *
stage=Stage('P01_BASIC_CHECKS')
try:
 samples=[complex(1,1),complex(10,20),complex(60,80),complex(200,400)]
 rows=[]
 for model in INPUT['models']:
  for s in samples:
   for x in [0.,.025,.1,.24,.4]:
    q=laplace_np(model,s,x,derivatives=True);M,N=operator(model,s);p=PARAMS
    def res(a,b,c=0):return abs(a+b+c)/max(abs(a)+abs(b)+abs(c),1e-300)
    mom=res(p['beta2']*q['u_xx'],-p['b']*q['theta_x'],-p['beta2']*s*s*q['u'])
    ene=res(N*q['theta_xx'],-M*s*p['g']*q['u_x'],-M*s*q['theta'])
    con=res(q['sigma'],-p['beta2']*q['u_x'],p['b']*q['theta'])
    mat=laplace_matrix_np(model,s,x);sw=laplace_np(model,s,x,swap=True)
    scales={'theta':1/abs(s),'sigma':p['b']/abs(s),'u':p['b']/p['beta2']/abs(s)**2}
    md=max(abs(q[f]-mat[f])/scales[f] for f in FIELDS);sd=max(abs(q[f]-sw[f])/scales[f] for f in FIELDS)
    rows.append({'model':model,'s_real':s.real,'s_imag':s.imag,'x':x,'momentum_residual':mom,'energy_residual':ene,'constitutive_residual':con,'matrix_mode_scaled_difference':md,'root_swap_scaled_difference':sd})
  bdy=[laplace_np(model,s,0.) for s in samples]
  assert max(abs(z['theta']*s-1) for z,s in zip(bdy,samples))<=1e-10
  assert max(abs(z['sigma']) for z in bdy)<=1e-10*PARAMS['b']
  for s in samples:
   taus,w=cv_channels(model);rr=sum(wj/(1+tj*s) for wj,tj in zip(w,taus));M,N=operator(model,s)
   assert abs(rr-N/M)/max(abs(N/M),1e-30)<=1e-12
  A,vel,R,Ri,taus,w=transport(model)
  assert np.all(taus>0) and np.all(w>0) and abs(sum(w)-1)<1e-12
  assert np.max(np.abs(A@R-R*vel[None,:]))/np.max(np.abs(A))<1e-10
 # Decoupled alpha=0 control: mathematically recover pure thermal response (not a new specimen).
 pp=derived_np(alpha=0.)
 for model in INPUT['models']:
  for s in samples:
   M,N=operator(model,s);expected=np.exp(-np.sqrt(s*M/N)*.1)/s;got=laplace_np(model,s,.1,params=pp)
   assert abs(got['theta']-expected)<1e-10/max(abs(s),1)
   assert abs(got['u'])<1e-15 and abs(got['sigma'])<1e-15
 maxima={k:max(r[k] for r in rows) for k in rows[0] if 'residual' in k or 'difference' in k}
 passed=all(maxima[k]<=1e-10 for k in ['momentum_residual','energy_residual','constitutive_residual','root_swap_scaled_difference']) and maxima['matrix_mode_scaled_difference']<=1e-9
 # Minimal arbitrary-precision execution checks after basic algebra.
 mp_probe={model:{f:inverse(model,.1,f,degree=32) for f in FIELDS} for model in INPUT['models']}
 for v in mp_probe.values():assert all(np.isfinite(list(v.values())))
 result={'status':'PASS' if passed else 'FAIL','label':'PILOT — NOT FINAL VALIDATION','parameters_derived':PARAMS,'normalization_scales':SCALES,'front_positions_derived':front_positions(),'maxima':maxima,'case_count':len(rows),'MP_probe_not_a_reference_measurement':mp_probe,'limited_scope':'Constitutive/PDE/BC/representation implementation checks; no physical validation or source-curve agreement yet'}
 (ROOT/'data/BASIC_CHECKS.json').write_text(json.dumps(result,indent=2));(ROOT/'data/LAPLACE_RESIDUALS.json').write_text(json.dumps(rows,indent=2))
 print(json.dumps(result,indent=2));stage.finish('RUN_SUCCESS',{'scientific_check_status':result['status']})
 if not passed:sys.exit(2)
except Exception as e:
 (ROOT/'logs/P01_ERROR.txt').write_text(traceback.format_exc());stage.finish('RUN_FAILED',{'error':str(e)});raise
