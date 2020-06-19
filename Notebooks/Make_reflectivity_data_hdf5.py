# Make reflectivity_data.hdf5
# @Milo

import glob
import numpy as np
import h5py
auxR, auxA = [], []


rm 'reflectivity_data.hdf5'

for file in glob.glob('Iridium/*.txt'):
    auxR.append(np.loadtxt(file)[:,1])
    auxA.append(np.loadtxt(file)[:,0])

f = h5py.File('reflectivity_data.hdf5', 'a')
datar = f.create_dataset('reflectivity/ir', (30, 500), dtype='f',data=np.array(auxR))
dataa = f.create_dataset('angle', (500,), dtype='f',data=auxA[0]*0.18/np.pi)
dataa = f.create_dataset('energy', (30,), dtype='f',data=np.arange(1,31,1))
