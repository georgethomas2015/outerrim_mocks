import numpy as np
import os
import glob
import sys
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
#import matplotlib.cm as mplcm
#import matplotlib.colors as colors


doplot = True
docheck = False

halodir = '/mnt/lustre/eboss/OuterRim/OuterRim_sim/'
mfile = halodir + 'hmf.txt'
mlow, mhigh = np.loadtxt(mfile, usecols= (0, 1), unpack=True)


path = "/users/ghthomas/outerrim_mocks/george_thomas_project/"
pathtemp = path+'/xi_mass_bin/tmp/'
ocat = '/users/ghthomas/output_catalogues/'
oplot = '/users/ghthomas/output_plots/'
lbox = 1000.
maxnumjobs = 5000
outdir = '/users/ghthomas/junk_directory/queuetest'
joblist = '/users/ghthomas/jobs_id.txt'

space = 'rspace'
#space = 'zspace'

nameroot = path + 'Testboxawk'
massroot = path + 'Testbox'

path2plot = "/users/ghthomas/output_plots/"
NUM_COLOURS = 24

if doplot:
	for ix in range(3):
		for iy in range(3):
			for iz in range(3):
				namebox = str(ix) + str(iy) + str(iz)
				cm = plt.get_cmap('gist_rainbow')
				fig = plt.figure(figsize = (8., 9.))
				ax = fig.add_subplot(111)
				ax.set_color_cycle([cm(1.*i/NUM_COLOURS) for i in range(NUM_COLOURS)])
				xtit = '${\\rm r}$'
				ytit = '${\\rm \\epsilon(r)}$'
				plt.xlabel(xtit)
				plt.ylabel(ytit)
				plt.xlim([-1, 3])
				plotname = "2PCF" + str(namebox) + ".png"
				for i, imlow in enumerate(mlow):
					boxfile = ocat + space + namebox + '_' + str(imlow) + '.txt'
					if (not os.path.exists(boxfile)):
						print ('This file does not exist:' + boxfile)
						continue
				
					r, xi, error = np.loadtxt(boxfile, usecols=(0,1,2), unpack=True)
#					print (r)
					ind = np.where(xi>0.)

					ax.plot(np.log10(r[ind]), np.log10(xi[ind]), label='$log(mass) =$' + str(imlow))

				leg = ax.legend(loc=1)
				leg.draw_frame(False)
				fig.savefig(path2plot + plotname)
				print ('Ouput: ', path2plot + plotname)

if docheck:
	for line in joblist:
		if os.path.exists(line):
			searchfile = open(line, 'r')
			namebox = str(ix) + str(iy) + str(iz)
			for i, imlow in enumerate(mlow):
				paramfile = pathtemp+'paramfile_'+namebox+'_'+str(imlow)+'.txt'
				runfile = pathtemp+'runfile_'+namebox+'_'+str(imlow)+'.sh'
				if 'Done !!!' in searchfile:
					os.remove(runfile)
					os.remove(paramfile)
				else:
					print ("Problem with files", runfile + paramfile) 
			searchfile.close()
