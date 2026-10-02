import json,traceback,csv,numpy as np
from src.common import ROOT,Stage,INPUT
from src.physics import SCALES,FIELDS,off_front,front_positions
from src.fvm import solve
stage=Stage('P02_FINITE_VOLUME')
try:
 runs=[];rows=[];curves={}
 def interp(q,x,field):
  u0=-q['dx']*float(np.sum(q['strain']))
  lv={'theta':q['boundary']['theta_left'],'sigma':q['boundary']['sigma_left'],'u':u0}[field]
  return np.interp(x,np.r_[0,q['x'],1],np.r_[lv,q[field],0])
 for model in INPUT['models']:
  for nx in INPUT['numerics']['FVM_cells']:
   stage.check();q=solve(model,nx,stage);curves[(model,nx)]=q
   np.savez_compressed(ROOT/'data'/f'FVM_{model}_N{nx}.npz',**{k:v for k,v in q.items() if isinstance(v,np.ndarray)})
   run={'run_id':f'P02_{model}_N{nx}','model':model,'cells':nx,'dx':q['dx'],'dt':q['dt'],'steps':q['steps'],'boundary':q['boundary'],'speeds':q['speeds'].tolist(),'tau_channels':q['tau_channels'].tolist(),'weights':q['weights'].tolist(),'wall_seconds':q['wall_seconds'],'origin':'ACTUALLY_EXECUTED_PILOT_NUMERICAL_RESULT','finite':all(np.all(np.isfinite(q[f])) for f in FIELDS)};runs.append(run);print('FVM',model,nx,run['steps'],'BC',run['boundary'],flush=True)
  ns=INPUT['numerics']['FVM_cells']
  for nco,nfi in zip(ns[:-1],ns[1:]):
   qc=curves[(model,nco)];qf=curves[(model,nfi)];x=qf['x'];mask=off_front(x)
   for f in FIELDS:
    diff=np.abs(interp(qc,x,f)-qf[f])/SCALES[f]
    rows.append({'model':model,'field':f,'coarse_cells':nco,'fine_cells':nfi,'scaled_offfront_max_change':float(np.max(diff[mask])),'scaled_global_L1_change':float(np.trapezoid(diff,x)),'scope':'PILOT — NOT FINAL VALIDATION'})
 result={'runs':runs,'refinement':rows,'front_exclusion':front_positions(),'no_parameter_fitting':True,'status':'RUN_SUCCESS','label':'PILOT — NOT FINAL VALIDATION','acceptance':'Independent-method comparison not yet executed; report refinement metrics without declaring physical validation'}
 (ROOT/'data/FVM_RUNS_AND_REFINEMENT.json').write_text(json.dumps(result,indent=2))
 print(json.dumps({'refinement':rows},indent=2));stage.finish('RUN_SUCCESS',{'run_count':len(runs)})
except Exception as e:
 (ROOT/'logs/P02_ERROR.txt').write_text(traceback.format_exc());stage.finish('RUN_FAILED',{'error':str(e)});raise
