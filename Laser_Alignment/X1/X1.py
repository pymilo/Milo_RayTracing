## X1 - New 1-shell module

import numpy as np
from foxsisim.source import Source
from foxsisim.module import Module
from foxsisim.util import load_rays, save_rays
from foxsisim.detector import Detector

n = 40000               ## number of rays
fbr = 3.75             ## front blocker radius
rbr = 3.135             ## rear blocker radius
Sdist = -2000.0        ## cm
#offaxisAngle = 0.0     ## arcmin
offaxisAngles = np.arange(0.0,2.,0.2)     ## arcmin


for angle in offaxisAngles:
    #Create Source :
    Xs = -Sdist * np.sin(np.deg2rad(angle / 60.0))
    Ys = 0.0
    source = Source(type='point',center=[Xs, Ys, Sdist ])
    print('Off-axis Angle: %f' % angle)
    '''This needs to be modified for each module'''
    module = Module(radii = [5.151, 4.9, 4.659, 4.429, 4.21, 4.0, 3.799], core_radius=(fbr,rbr))
    rays = source.generateRays(module.targetFront,n)
    module.passRays(rays)
    Rrays = [ray for ray in rays if (ray.tag != 'Source')] #kills the passthrough rays
    save_rays(Rrays,filename='/Users/Kamilobu/Desktop/Developer/Milo_RayTracing/Laser_Alignment/X1/rays/rays_Angle_=_'+'{:.1f}'.format(angle)+'.csv')


