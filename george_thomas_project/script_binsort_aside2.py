import numpy as np
import os
import glob
import sys

halodir = '/mnt/lustre/eboss/OuterRim/OuterRim_sim/'
mfile = halodir + 'hmf.txt'
mlow, mhigh = np.loadtxt(mfile, usecols= (0, 1), unpack=True)
#mlow = np.array([10.58])

path = "/users/ghthomas/outerrim_mocks/george_thomas_project/"
pathtemp = path+'/xi_mass_bin/tmp/'
ocat = '/users/ghthomas/output_catalogues/'
lbox = 1000.
maxnumjobs = 5000
outdir = '/users/ghthomas/junk_directory/queuetest'

space = 'rspace'
#space = 'zspace'

nameroot = path + 'Testboxawk'
massroot = path + 'Testbox'

#Take the columns from a CUTEbox fle and plot them.
