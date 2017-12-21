import numpy as np
from foxsisim.source import Source
from foxsisim.module import Module
Sdist = -1.5e13           ## cm
offaxisAngle = 30.0     ## arcmin
source = Source(type='point',center=[0, -Sdist * np.sin(np.deg2rad(offaxisAngle / 60.0)), Sdist ])
module = Module(core_radius=3.36)
n = 1000000
rays = source.generateRays(module.targetFront,n)
module.passRays(rays)
Rrays = [ray for ray in rays if (ray.tag != 'Source')] #kills the passthrough rays
from foxsisim.util import save_rays
save_rays(Rrays,filename='rays_on_module.csv')
print(len(Rrays),' rays saved')
print('Done!')


