import numpy as np
from foxsisim.source import Source
from foxsisim.module import Module
from foxsisim.util import load_rays, save_rays
from foxsisim.detector import Detector

n = 100000               ## number of rays
fbr = 3.17
rbr = 0.00
Sdist = -1.5e13        ## cm
#offaxisAngle = 0.0     ## arcmin
offaxisAngles = np.arange(0.0,30.,2.)     ## arcmin


for angle in offaxisAngles:
    #Create Source : 
    source = Source(type='point',center=[0, -Sdist * np.sin(np.deg2rad(angle / 60.0)), Sdist ])
    print('Off-axis Angle: %f' % angle)
    module = Module(radii = [3.17], core_radius=(fbr,rbr))
    rays = source.generateRays(module.targetFront,n)
    module.passRays(rays)
    Rrays = [ray for ray in rays if (ray.tag != 'Source')] #kills the passthrough rays
    save_rays(Rrays,filename='/Users/Kamilobu/Desktop/Developer/Milo_RayTracing/blockers/Off-axis/F317R000/rays_Angle_=_'+str(angle)+'.csv')


