"""Post-failure reporting of ALREADY COMPUTED data only; no additional solver runs."""
import json,numpy as np,csv
from src.common import ROOT,Stage,INPUT
from src.physics import FIELDS,SCALES,off_front,front_positions,PARAMS
stage=Stage('P04_EXISTING_DATA_DIAGNOSTIC_SUMMARY')
pro=json.loads((ROOT/'data/INVERSION_PROBES.json').read_text());x=np.asarray(pro['x']);mask=off_front(x);rows=[];cohen=[]
for model in INPUT['models']:
 nx=6400 if model=='CV' else 3200;fv=np.load(ROOT/'data'/f'FVM_{model}_N{nx}.npz');dx=1/nx;u0=-dx*float(np.sum(fv['strain']))
 for f in FIELDS:
  dh=np.asarray(pro['values'][model][f]['dehoog_64']);ch=np.asarray(pro['values'][model][f]['cohen_80'])
  lv={'theta':1.,'sigma':0.,'u':u0}[f];interp=np.interp(x,np.r_[0,fv['x'],1],np.r_[lv,fv[f],0])
  diff=np.abs(interp-dh)/SCALES[f];imax=np.where(mask)[0][np.argmax(diff[mask])]
  rows.append({'model':model,'field':f,'FV_cells':nx,'scaled_offfront_probe_max_difference':float(diff[imax]),'x_worst':float(x[imax]),'criterion_frozen':3e-3,'probe_only_diagnostic_pass':bool(diff[imax]<=3e-3),'scope':'POST_FAILURE_DIAGNOSTIC — selected probes, NOT full-profile acceptance'})
  cd=np.abs(ch-dh)/SCALES[f];ii=np.where(mask)[0][np.argmax(cd[mask])]
  cohen.append({'model':model,'field':f,'x_worst':float(x[ii]),'dehoog64':float(dh[ii]),'cohen80':float(ch[ii]),'scaled_difference':float(cd[ii]),'root_cause':'NOT_ESTABLISHED; unsuitable/unstable inversion for these delayed/oscillatory responses is a hypothesis, not proven'})
res={'label':'PILOT — NOT FINAL VALIDATION','overall_status':'BLOCKED after two pilot iterations did not meet frozen inversion cross-check','primary_dehoog_probe_refinement':'PASS on specified off-front probes','independent_time_solver_probe_comparison':rows,'Cohen_failure_examples':cohen,'source_graphical_comparison':'NOT_EXECUTED: prerequisite numerical inversion gate unresolved','full_profile_Laplace_FV_comparison':'NOT_EXECUTED','physical_validation':'NOT_RUN','source_parameters_changed':False,'criteria_changed':False,'code_changes':'Analytic zero-stress endpoint handling; CV6400 post-result numerical refinement, both logged','next_action':'STOP solver runs; require user decision/authorization for diagnostic-only follow-up or logged method-plan revision'}
(ROOT/'data/DIAGNOSTIC_SUMMARY.json').write_text(json.dumps(res,indent=2))
with (ROOT/'data/EXISTING_PROBE_METHOD_COMPARISON.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print(json.dumps(res,indent=2));stage.finish('RUN_SUCCESS',{'kind':'Postprocessing existing data only; no solver execution'})
