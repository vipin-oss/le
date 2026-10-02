"""Source-figure digitization only; run before new model results are computed.
Extracts coloured curves from embedded Figure-5 rasters, not experimental data.
"""
from pathlib import Path
import json,csv,hashlib,resource,time
import numpy as np
from PIL import Image
ROOT=Path(__file__).parent;REF=ROOT/'reference_local'
# Axis ranges and image mapping read from supplied B01 Figure5.
panels={'theta':('embedded_2.png',0.0,1.0),'sigma':('embedded_1.png',-0.05,0.01),'u':('embedded_0.png',-6e-4,2e-4)}
colors={'CV':np.array([0.32449835538864136,0.32750439643859863,0.3350728750228882])*255,
        'MCV3':np.array([0.2683146297931671,0.661448061466217,0.44966810941696167])*255}
rows=[];meta=[]
for field,(filename,ymin,ymax) in panels.items():
 rgb=np.asarray(Image.open(REF/filename).convert('RGB')).astype(float);H,W=rgb.shape[:2]
 black=(np.max(rgb,axis=2)<40)
 cols=np.where(black.sum(axis=0)>0.85*H)[0]; rr=np.where(black.sum(axis=1)>0.85*W)[0]
 left=cols[cols<W/2].mean();right=cols[cols>W/2].mean();top=rr[rr<H/2].mean();bottom=rr[rr>H/2].mean()
 assert right-left>0.9*W and bottom-top>0.9*H
 dx=1/(right-left);dy=(ymax-ymin)/(bottom-top)
 meta.append({'field':field,'filename':filename,'width':W,'height':H,'frame':[left,right,top,bottom],'x_range':[0,1],'y_range':[ymin,ymax],'delta_x_two_pixels':2*dx,'delta_y_two_pixels':2*dy,'origin':'GRAPHICAL_REFERENCE_DIGITIZATION — not original raw solver data/experiment'})
 for model,col in colors.items():
  distance=np.linalg.norm(rgb-col,axis=2);mask=distance<25
  pts=[]
  for ix in range(int(left)+5,int(right)-4,4):
   ys=np.where(mask[:,ix])[0];ys=ys[(ys>top+3)&(ys<bottom-3)]
   if not len(ys):continue
   # Exclude columns with separated segments/vertical fronts; no solver-dependent selection.
   if ys.max()-ys.min()>8:continue
   py=float(np.median(ys));x=(ix-left)*dx;y=ymax-(py-top)*dy
   pts.append((x,y,max(2.0,0.5*(ys.max()-ys.min()+1))*dy,ix,py))
  pts.sort()
  for i,(x,y,yerr,ix,py) in enumerate(pts):
   if len(pts)>1:
    ia=max(0,i-1);ib=min(len(pts)-1,i+1)
    slope=(pts[ib][1]-pts[ia][1])/(pts[ib][0]-pts[ia][0]) if ib!=ia else 0.
   else:slope=0.
   rows.append({'model':model,'field':field,'x_ref':x,'value_ref':y,'x_bound':2*dx,'y_bound':yerr,'source_slope':slope,'pixel_x':ix,'pixel_y_median':py,'origin':'SOURCE_FIGURE_DERIVED — NOT_OUR_RESULT — NOT_EXPERIMENT'})
with (REF/'figure5_digitized.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
(REF/'DIGITIZATION_PROVENANCE.json').write_text(json.dumps({'source_id':'B01','doi':'10.1007/s10483-025-3280-7','pdf_page':12,'figure':'5','source_sha256':hashlib.sha256(Path('/home/user/RESEARCH_PROJECT_INPUT/LITERATURE/USER_SUPPLIED_BENCHMARKS/ALIT_01/s10483-025-3280-7 (1).pdf').read_bytes()).hexdigest(),'method':'Raster colour mask, known axis endpoints, median pixels; 4-pixel column sampling; colour tolerance25 fixed before solver output','uncertainty':'Conservative representation bounds: at least2pixels y and2pixels x, propagated with source local slope; not statistical CI; source solver uncertainty unknown','panels':meta,'counts':{m+'_'+f:sum(r['model']==m and r['field']==f for r in rows) for m in colors for f in panels},'redistribution':'Private reference extraction; not included in public/final recovery archive pending rights review'},indent=2))
print(json.dumps({'digitized_counts':{m+'_'+f:sum(r['model']==m and r['field']==f for r in rows) for m in colors for f in panels},'frames':meta},indent=2))
print('SOURCE_PROCESSING_CPU_SECONDS',resource.getrusage(resource.RUSAGE_SELF).ru_utime+resource.getrusage(resource.RUSAGE_SELF).ru_stime)
