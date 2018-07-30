import numpy as np
import os
import glob
import sys


def writeScriptParams(paramfile, infile, outfile, lbox):
	f=open(paramfile,'w')
	f.write('data_filename= '+infile+'\n')
	f.write('num_lines= all \n')
	f.write('input_format= 0 \n')
	f.write('output_filename= '+outfile+'\n')
	f.write('box_size= '+lbox+'\n')
#	f.write(' \n')
	f.write('use_tree= 0 \n')
	f.write('max_tree_order= 6 \n')
	f.write('max_tree_nparts= 100 \n')
#	f.write(' \n')
	f.write('use_pm= 0 \n')
	f.write('n_grid_side= 256 \n')
#	f.write(' \n')
	f.close()


def writeScriptRun(runfile, paramfile, outdir):
	f=open(runfile,'w')                                    
	f.write('#!/bin/bash \n')
	f.write('#PBS -l walltime=24:00:00 \n')
	logid = outdir+'.o.${PBS_JOBID}'
	f.write('#PBS -o '+logid+' \n')
	f.write('#PBS -e '+outdir+'.e.${PBS_JOBID} \n')
	f.write('#PBS -l nodes=1:ppn=1 \n')
	f.write('#PBS -q sciama1.q \n')
	f.write(' \n')
	f.write('echo '+logid+' >> jobs_id.txt \n')
	f.write('cute=/users/ghthomas/CUTE/CUTE_box/CUTE_box \n')
#	f.write('cute=/users/ghthomas/outerrim_mocks/george_thomas_project/test.py \n')
	f.write('path='+paramfile+' \n')
	f.write(' \n')
	f.write('$cute $path \n')
#	f.write('python $cute \n')
	f.write(' \n')
	f.close()

dodeltemp = False

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

for ix in range(3):
	for iy in range(3):
		for iz in range(3):
			namebox = str(ix) + str(iy) + str(iz)
			boxfile = nameroot + namebox + '.txt'
			fullboxfile = massroot + namebox + '.txt'
#			print (boxfile)

			if (not os.path.exists(boxfile)):
				print ('This file does not exist,', boxfile)
				continue
			print (ix, iy, iz, namebox)
			for i, imlow in enumerate(mlow):
				imhigh = mhigh[i]

				massfile = pathtemp + space + namebox + '_' + 'xyz' + '_' + str(imlow) + '.txt'
#				print (massfile)
				print (fullboxfile)
				ff =open(fullboxfile, 'r')
				for line in ff:
					
					
					massh = float(line.split()[6])
					
					

					if ((massh>=imlow) & (massh<imhigh)):
#						print (imlow, massh, imhigh)
						x = (line.split()[0])
						y = (line.split()[1])
						z = (line.split()[2])

						if os.path.exists(massfile):
							with open(massfile, 'a') as outf:
								outf.write(x+' '+y+' '+z+' \n')
								outf.closed
						else:	
							with open(massfile, 'w') as outf:
								outf.write(x+' '+y+' '+z+' \n')
								outf.closed
				ff.close()
				paramfile = pathtemp+'paramfile_'+namebox+'_'+str(imlow)+'.txt'
				outfile = ocat+space+namebox+'_'+str(imlow)+'.txt'
				runfile = pathtemp+'runfile_'+namebox+'_'+str(imlow)+'.sh'
				writeScriptParams(paramfile,massfile,outfile, str(lbox))
				writeScriptRun(runfile, paramfile, outdir)

				qsub_command = 'qsub '+runfile

				print (qsub_command)
				submit_scripts = True

				if (submit_scripts):
					print ('SUBMIT: ',qsub_command)
					os.system(qsub_command)

				if dodeltemp:
					if os.path.exists(paramfile):
						os.remove(paramfile)

					if os.path.exists(runfile):
						os.remove(runfile)
