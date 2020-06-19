## Generate rays and save them in a CSV file for Iridium mirrors.
## @Milo
## Sept 2018

import numpy as np
import matplotlib.pyplot as plt
from foxsisim.source import Source
from foxsisim.module import Module
from foxsisim.util import save_rays
from datetime import datetime
tstart = datetime.now()

nrays = 100000             ## Number of rays
max_energy = 30.0          ## Maximum energy
#fbr = 3.09671 ## X0 - 10Shell
#rbr = 2.62    ## X0 - 10Shell
fbr = 3.75   ## X1456 - 7Shell
rbr = 3.14   ## X1456 - 7Shell


''' Defining Spectrum '''

def spectrum(z):
        if (type(z) is not type([1])) and (type(z) is not type(np.array(1))):
            x = np.array([z])
        else:
            x = np.array(z)
        return np.piecewise(x, [x < 0, ((x < max_energy) & (x > 0)), (x >= max_energy)], [0, 1./max_energy, 0])

source_distance = -1.496e+13      ## cm
offaxis_angle_arcminX = 21.0      ## 
offaxis_angle_arcminY = 0.17      ## 

source = Source(type='point', center=[source_distance * np.sin(np.deg2rad(offaxis_angle_arcminX / 60.0)),
                                      source_distance * np.sin(np.deg2rad(offaxis_angle_arcminY / 60.0)),
                                      source_distance])
source.loadSpectrum(spectrum)
energies = np.arange(-10, 60, 0.1)
plt.plot(energies, source._spectrum(energies))
plt.xlabel('Energy [keV]')
plt.title('Source Spectrum')
print('teo-input-spect.png')
plt.savefig("teo-input-spect.png", dpi=100)


''' Creating the FOXSI telescope '''

module = Module(radii = [5.151,4.9,4.659,4.429,4.21,4.0,3.799], #7Shells
#module = Module(radii = [5.151,4.9,4.659,4.429,4.21,4.0,3.799,3.59,3.38,3.17], #10Shells
                core_radius=(fbr,rbr))

''' Generating rays '''
rays = source.generateRays(module.targetFront, nrays)

plt.figure()
plt.hist([ray.energy for ray in rays], normed=True, label='generated rays')
plt.xlabel('Energy [keV]')
plt.title('Histogram generated rays')
plt.legend()
print('gen-input-spect.png')
plt.savefig('gen-input-spect.png', dpi=100)
tgen = datetime.now()
print('rays generated, time = ' + str((tgen - tstart).seconds) + 'seconds' )

print('Pasing rays')
module.passRays(rays)

Rrays = [ray for ray in rays if (ray.tag != 'Source')] #kills the passthrough rays
save_rays(Rrays,filename='/Users/Kamilobu/Desktop/FOXSI3-GR-Prediction/makerays/rays/7Shell.csv')

print('Time total: ' + str((datetime.now() - tgen).seconds) + ' seconds')
