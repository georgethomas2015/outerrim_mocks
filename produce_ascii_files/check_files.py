import sys, os, glob, getpass
import numpy as np

steps = np.array([203, 266, 300])

check_fof = False
check_particle = False

for istep in steps:
    halodir = '/mnt/lustre/eboss/OuterRim/OuterRim_sim/'
    nroot = halodir+'HaloCatalog/STEP'+str(istep)  

    # FoF
    files = glob.glob(nroot+'/*'+str(istep)+'*.fofproperties#*')
    print len(files),' fof input files, step=',istep
    nums = [int(i.split('#', 1)[1]) for i in files]
    print '      from',min(nums),' to ',max(nums)

    # Particles
    files = glob.glob(nroot+'/*'+str(istep)+'*.haloparticles#*')
    print len(files),' particles input files, step=',istep
    nums = [int(i.split('#', 1)[1]) for i in files]
    print '      from',min(nums),' to ',max(nums)
