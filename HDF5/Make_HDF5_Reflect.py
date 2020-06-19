from astropy import units as u
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import h5py

def HDF5_Creation(Emax,Dir,filename_Ir,filename_Ni,OutFile):
    header_list = ["Angle (mrad)", "Energy (eV)", "Reflectivity"]
    Ir = pd.read_csv(Dir+filename_Ir,header=2,sep='\s+',names=header_list)
    Ni = pd.read_csv(Dir+filename_Ni,header=2,sep='\s+',names=header_list)
    # Define Energy, Angles and Reflectivity for Ir and Ni
    Energy = np.arange(1,Emax+1) # in keV
    Angles = Ir[0:499]['Angle (mrad)'].values * u.milliradian.to('deg') #original file comes in mrad
    Reflectivity_Ir=[]
    Reflectivity_Ni=[]
    for i in Energy:
        Reflectivity_Ir.append(Ir[(i-1)*500:(i-1)*500+499]['Reflectivity'].values)
        Reflectivity_Ni.append(Ni[(i-1)*500:(i-1)*500+499]['Reflectivity'].values)

    # HDF5 File creation:
    #!rm OutFile # removes any existing mytestfile.hdf5 file
    f = h5py.File(OutFile, "w") # creates hdf5 with write permissions
    fenergy = f.create_dataset("energy", data=Energy) # load energy
    fangle = f.create_dataset("angle", data=Angles) # load angles list
    # load reflectivity for for Ir and Ni as HDF5 groups
    # http://docs.h5py.org/en/stable/high/group.html
    reflec_ir = f.create_dataset("reflectivity/ir", data=np.array(Reflectivity_Ir))
    reflec_ni = f.create_dataset("reflectivity/ni", data=np.array(Reflectivity_Ni))
    f.close()

# 1-100 keV file
Dir = './'
filename_Ir = 'Ir_1-100keV.txt'
filename_Ni = 'Ni_1-100keV.txt'
OutFile = "reflectivity_data_100keV.hdf5"
HDF5_Creation(100,Dir,filename_Ir,filename_Ni,OutFile)

# 1-30 keV for sanity check
Dir = './'
filename_Ir = 'Ir_30.txt'
filename_Ni = 'Ni_30.txt'
OutFile = "reflectivity_data_30keV.hdf5"
HDF5_Creation(30,Dir,filename_Ir,filename_Ni,OutFile)
