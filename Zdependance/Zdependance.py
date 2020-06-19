## Generating Rays for assessing the Z dependance of the PSF for a 10-shell module 
## and new blockers. Z ranging from -5mm to +5mm in steps of 1/2 a mm.
## @Milo, UC Berkeley. June 2018

# Packages:
import numpy as np
from foxsisim.source import Source
from foxsisim.module import Module
from foxsisim.util import load_rays, save_rays
from foxsisim.detector import Detector

n = 100000                  ## Number of rays
Sdist = -1.496e13       ## 1AU in cm 
## 10-Shell Blocker:
fbr = 3.0985            ## Ideal front blocker radius
rbr = 2.62              ## Ideal rear blocker radius
## 7-Shell Blocker:
#fbr = 3.74936           ## Ideal front blocker radius
#rbr = 3.14              ## Ideal rear blocker radius


#Create Source :
Xs = 0.0
Ys = 0.0
source = Source(type='point',center=[Xs, Ys, Sdist ])
#print('Simulating Z = : %f' % z)
'''This needs to be modified for each module'''
## 10-Shell Module:
module = Module(radii = [5.151, 4.9, 4.659, 4.429, 4.21, 4.0, 3.799, 3.59, 3.38, 3.17], core_radius=(fbr,rbr))
## 7-Shell Module:
#module = Module(radii = [5.151, 4.9, 4.659, 4.429, 4.21, 4.0, 3.799], core_radius=(fbr,rbr))
rays = source.generateRays(module.targetFront,n)
module.passRays(rays)
Rrays = [ray for ray in rays if (ray.tag != 'Source')] #kills the passthrough rays
save_rays(Rrays,filename='/Users/Kamilobu/Desktop/Developer/Milo_RayTracing/Zdependance/rays/Z_=_10Shell_1AU.csv')


