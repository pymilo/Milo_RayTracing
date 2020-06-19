#!/usr/bin/env python
#from foxsisim.module import Module
from foxsisim.detector import Detector
from foxsisim.source import Source
from foxsisim.plotting import plot,scatterHist
import matplotlib.pyplot as plt
import numpy as np

#!/usr/bin/env python
from foxsisim.module import Module
from foxsisim.detector import Detector
from foxsisim.source import Source
from foxsisim.plotting import plot,scatterHist
import matplotlib.pyplot as plt
import numpy as np

max_energy = 30.0
def spectrum(z):
        if (type(z) is not type([1])) and (type(z) is not type(np.array(1))):
            x = np.array([z])
        else:
            x = np.array(z)
        return np.piecewise(x, [x < 0, ((x < max_energy) & (x > 0)), (x >= max_energy)], [0, 1./max_energy, 0])

source_distance = -1e4 ##cm
source = Source(type='point', center=[0, 0, source_distance])
source.loadSpectrum(spectrum)
energies = np.arange(-10, 60, 0.1)
plt.plot(energies, source._spectrum(energies))
plt.xlabel('Energy [keV]')
plt.title('Source Spectrum')
#plt.show()
print('teo-input-spect.png')
plt.savefig('teo-input-spect.png')

module = Module(radii=[5.151,4.9],focal=200.0)
detector = Detector(width=8,
                    height=8,
                    normal = [0,0,1],
                    center = [0,0,230],
                    reso = [1024,1024])

rays = source.generateRays(module.targetFront, 7) 

print('rays generated')

plt.figure()
plt.hist([ray.energy for ray in rays], normed=True, label='generated rays')
plt.xlabel('Energy [keV]')
plt.title('Histogram generated rays')
plt.legend()
#plt.show()
print('gen-input-spect.png')
plt.savefig('gen-input-spect.png')


from datetime import datetime
tstart = datetime.now()

print('pasing rays')
# pass rays through module
module.passRays(rays, robust=True)
# catch rays at detector
detector.catchRays(rays)
