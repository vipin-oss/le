"""Post-result diagnostic mesh extension. Original results/criteria preserved."""
import json,numpy as np,traceback
from src.common import ROOT,Stage
from src.physics import SCALES,FIELDS,off_front
from src.fvm import solve
stage=Stage('P02B_CV_POST_RESULT_6400')
try:
 q=solve('CV',6400,stage);np.savez_compressed(ROOT/'data/FVM_CV_N6400.npz',**{k:v for k,v in q.items() if isinstance(v,np.ndarray)})
 c=np.load(ROOT/'data/FVM_CV_N3200.npz');dx=1/3200;u0=-dx*float(np.sum(c['strain']));x=q['x'];mask=off_front(x);rows=[]
 for f in FIELDS:
  lv={'theta':1.,'sigma':0.,'u':u0}[f];cc=np.interp(x,np.r_[0,c['x'],1],np.r_[lv,c[f],0]);diff=np.abs(q[f]-cc)/SCALES[f]
  rows.append({'model':'CV','field':f,'coarse_cells':3200,'fine_cells':6400,'scaled_offfront_max_change':float(np.max(diff[mask])),'scaled_global_L1_change':float(np.trapezoid(diff,x)),'criterion':3e-3,'point_refinement_pass':bool(np.max(diff[mask])<=3e-3),'analysis_kind':'POST_RESULT_DIAGNOSTIC — original mask/criterion/source unchanged'})
 result={'run_id':'P02B_CV_N6400','model':'CV','cells':6400,'steps':q['steps'],'dt':q['dt'],'boundary':q['boundary'],'metrics':rows,'status':'PASS' if all(z['point_refinement_pass'] for z in rows) else 'PARTIAL','label':'PILOT — NOT FINAL VALIDATION'}
 (ROOT/'data/FVM_CV_6400_POST_RESULT_DIAGNOSTIC.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2));stage.finish('RUN_SUCCESS',{'scientific_check_status':result['status']})
except Exception as e:
 (ROOT/'logs/P02B_ERROR.txt').write_text(traceback.format_exc());stage.finish('RUN_FAILED',{'error':str(e)});raise
