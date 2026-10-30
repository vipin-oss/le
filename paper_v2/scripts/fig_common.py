import matplotlib as mpl
mpl.rcParams.update({'pdf.fonttype':42,'font.size':9,'axes.labelsize':9,'legend.fontsize':8,'xtick.labelsize':8,'ytick.labelsize':8,
 'figure.dpi':150,'savefig.dpi':300,'axes.spines.top':False,'axes.spines.right':False,'axes.linewidth':0.7,
 'lines.linewidth':1.5,'font.family':'serif','mathtext.fontset':'cm','axes.grid':True,'grid.alpha':0.25,'grid.linewidth':0.5})
C={'CD':'#444444','LS':'#0072B2','DPL':'#D55E00','GN':'#009E73','MGT':'#CC79A7','accent':'#E69F00'}
import os
FIG=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','figs')
def save(fig,name):
    fig.savefig(f'{FIG}/{name}.pdf',bbox_inches='tight'); fig.savefig(f'{FIG}/{name}.png',bbox_inches='tight')
