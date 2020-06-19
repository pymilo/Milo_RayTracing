from astropy import units as u
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import h5py

# Readind LBL Data
'''
This corresponds to Ni Rho=8.902, Sig=0.nm, P=1., E=1000.eV
'''
Dir = './'
filename = 'Reflectivity_Nickel_01keV.txt'
header_list = ["Angle (deg)", "Reflectivity"]
lbl = pd.read_csv(Dir+filename,header=2,sep='\s+',names=header_list)

# Readind XOP Data [Windt model]
'''
This corresponds to Ni Rho=8.902\AA, P=0., E=1000.eV
'''
file_unpol= 'unpol.txt'
unpol = pd.read_csv(Dir+file_unpol,sep='\s+',names=header_list)

fig, axs = plt.subplots(2, 1, sharex=True, figsize=(12,6))
fig.subplots_adjust(hspace=0)
axs[0].set_title('Ir, 10keV, Roughness=0.0, Unpolarized',fontsize=26)
axs[0].plot(lbl[lbl.keys()[0]],lbl[lbl.keys()[1]],label='NLBL',linewidth=4,alpha=.8,
       color='tab:blue')
axs[0].plot(unpol[unpol.keys()[0]] * u.milliradian.to('deg'),unpol[unpol.keys()[1]],
       label='XOP',linewidth=4,alpha=.8,linestyle='-',color='tab:orange')
axs[0].legend(fontsize=16)
axs[0].set_ylabel(lbl.keys()[1],fontsize=20)
axs[0].set_yscale('log')
axs[0].tick_params(labelsize=20)
axs[1].plot(lbl[lbl.keys()[0]],unpol[unpol.keys()[1]]-lbl[lbl.keys()[1]],label='XOP-NLBL',linewidth=4,alpha=.8,
       color='tab:red')
axs[1].set_xlabel(lbl.keys()[0],fontsize=20)
axs[1].tick_params(labelsize=20,axis='y')
axs[1].tick_params(labelsize=20,axis='x')
axs[1].set_ylabel('Residual',fontsize=20)
axs[1].legend(fontsize=16)
axs[1].set_yscale('log')
#axs[1].ticklabel_format(axis='y',style='sci',scilimits=(0,-6))
plt.show()
