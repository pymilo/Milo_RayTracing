import numpy as np
from foxsisim.source import Source
from foxsisim.module import Module
from foxsisim.util import load_rays, save_rays
from foxsisim.detector import Detector

n = 100000                 ## number of rays
Sdist = -1.5e13        ## cm
offaxisAngle = 0.0     ## arcmin

fbrs = np.arange(2.623,3.29,0.05) # Front blocker radius ranging from 2.623 cm to 3.273

#Create Source : 
source = Source(type='point',center=[0, -Sdist * np.sin(np.deg2rad(offaxisAngle / 60.0)), Sdist ])


for fbr in fbrs:
    print('Front radius: %f' % fbr)
    module = Module(radii = [3.17], core_radius=(fbr,0.))
    rays = source.generateRays(module.targetFront,n)
    module.passRays(rays)
    Rrays = [ray for ray in rays if (ray.tag != 'Source')] #kills the passthrough rays
    save_rays(Rrays,filename='/Users/Kamilobu/Desktop/Developer/Milo_RayTracing/blockers/rays_FB/rays_FBR_=_'+str(fbr)+'.csv')
