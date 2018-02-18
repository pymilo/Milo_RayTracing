import numpy as np
from foxsisim.source import Source
from foxsisim.module import Module
from foxsisim.util import load_rays, save_rays
from foxsisim.detector import Detector

n = 10000                 ## number of rays
Sdist = -1.5e13        ## cm
offaxisAngle = 0.0     ## arcmin
fbr = 3.17

rbrs = np.arange(2.6,2.855,0.02) # Rear blocker radius ranging from 0.0cm to 2.8 in steps of 0.2

#Create Source : 
source = Source(type='point',center=[0, -Sdist * np.sin(np.deg2rad(offaxisAngle / 60.0)), Sdist ])


for rbr in rbrs:
    print('Rear radius: %f' % rbr)
    module = Module(radii = [3.17], core_radius=(fbr,rbr))
    rays = source.generateRays(module.targetFront,n)
    module.passRays(rays)
    Rrays = [ray for ray in rays if (ray.tag != 'Source')] #kills the passthrough rays
    save_rays(Rrays,filename='/Users/Kamilobu/Desktop/Developer/Milo_RayTracing/blockers/rays_RB/test/rays_RBR_=_'+str(rbr)+'.csv')
