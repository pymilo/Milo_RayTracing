'''
Generate rays and save them into CSVs file for Iridium mirrors.
Parallel code using multiprocessing
Author  : Milo
Created : Jun 2020

Parameters:  - angle : Off-axis angle [arcmin]
             - nrays : Number of rays per process
             - proc  : Number of processes
             - max_energy : Max energy for input spectrum
Output : 
             - CSV files with format: rays_Angle_=_angle_proc.csv
'''
# Packages:
import multiprocessing
import numpy as np
import matplotlib.pyplot as plt
import time
from foxsisim.module import Module
from foxsisim.source import Source
from foxsisim.util import save_rays

# Input parameters : 
angle = 0.0    # Off-axis angle [arcmin]
nrays = 1600   # Number of rays
Nproc = 4      # Number of Process in Parallel

# Defining Input Spectrum
def spectrum(z):
        max_energy = 100.0 # Maximum energy
        if (type(z) is not type([1])) and (type(z) is not type(np.array(1))):
            x = np.array([z])
        else:
            x = np.array(z)
        return np.piecewise(x, [x < 0, ((x < max_energy) & (x > 0)), (x >= max_energy)], 
                            [0, 1./max_energy, 0])

# Main function which creates rays and save them into CSV files
def make_rays(angle,nrays,proc):
    fbr = 6.296              ## Front blocker radius
    rbr = 5.99               ## Rear blocker radius

    # Creating the FOXSI telescope
    module = Module(radii = [9.333,9.153,8.973,8.793,8.613,8.434,8.255,
                             8.076,7.897,7.718,7.540,7.362,7.184,7.006,
                             6.828,6.650,6.473,6.296], focal=1400.0, core_radius=(fbr,rbr))

    Sdist = -1.5e13         ## Source distance in cm
    Xs = -Sdist * np.sin(np.deg2rad(np.sqrt(2.) * angle / 120.0))
    Ys = -Sdist * np.sin(np.deg2rad(np.sqrt(2.) * angle / 120.0))
    source = Source(type='point', center=[Xs, Ys, Sdist ])
    source.loadSpectrum(spectrum)

    # Generating rays
    rays = source.generateRays(module.targetFront, nrays)
    # Passing rays
    module.passRays(rays)
    Trays = [ray for ray in rays if (ray.dead==False)] ## save only those alive rays
    save_rays(Trays,filename=f'rays_Angle_=_{angle}_{proc}.csv')

processes = []
start = time.perf_counter()
for proc in range(Nproc):
    p = multiprocessing.Process(target=make_rays, args=[angle,nrays,proc+1])
    p.start()
    processes.append(p)
for process in processes: process.join()
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
