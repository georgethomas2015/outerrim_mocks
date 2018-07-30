import numpy as np
import os
import glob


halodir = '/mnt/lustre/eboss/OuterRim/OuterRim_sim/'
mfile = halodir + 'hmf.txt'
mlow, mhigh = np.loadtxt(mfile, usecols= (0, 1), unpack=True)


path = "/users/ghthomas/outerrim_mocks/george_thomas_project/massbins_Testbox1.txt"

def checkdir(indir):
	if os.path.isdir(indir)==False:
		os.mkdir(indir)

def writeScript(listdir,box,nfil,outdir,oeroot):                        
	ff = listdir+box+'.txt'
	outplate = outdir+box+'/'
	checkdir(outplate)
	f=open(listdir+box+'runbins.sh','w')                                    
	f.write('#!/bin/bash \n')
	f.write('#PBS -l walltime=260:00:00 \n')
	f.write('#PBS -t 1-'+nfil+' \n')
	f.write('#PBS -o '+oeroot+'ff.o.${PBS_JOBID} \n')
	f.write('#PBS -e '+oeroot+'ff.e.${PBS_JOBID} \n')
	f.write(' \n')
	f.write('echo "+++++++++++" \n')
	f.write('listF='+ff+'\n')
	f.write(' \n')
	f.write('INPUT_FILE=`awk "NR==$PBS_ARRAYID" ${listF}` \n')
	f.write('#echo $INPUT_FILE \n')
	f.write(' \n')
	f.write('python '+os.getcwd()+'/firefly_run.py ', '$INPUT_FILE'+' '+outplate+' \n')
	f.write(' \n')
	f.close()

def testFiles(listdir,box,outdir):
	ff = listdir+box+'.txt'
	with open(ff) as f: 
		lines = f.readlines()

	num = 0 	
	badf = listdir+box+badfil
	ff = open(Testbox1.txt, 'w')
	for line in lines:
		endf = 'Testbox1'+line.split('spec-')[6]
		outf = outdir+plate+endf.strip()

		if os.path.isfile(outf):
			header = fits.open(outf)
			nofit = header[0].header['not_galaxy_bad_z']
			if (not nofit):
				if (len(header)<2):
					num += 1
					print >> ff, outf,' : NOT enough tables have been produced.'
				else:
					list_keys = header[1].header.keys()
					if (len(list_keys)<2):
						num += 1
						print >> ff, outf,' : NOT enough columns have been produced.'
			header.close()
		else:
			print >> ff, outf,' does NOT exist'
			num += 1
	ff.close()
	print "%i jobs did something out of %i, check %s" % (num,len(lines),badf)

def resubmitFiles(listdir,plate,indir):
	ff = listdir+plate+'.txt'
	if os.path.exists(ff):
		os.remove(ff)

	badf = listdir+plate+badfil 
	if (os.path.isfile(badf)):
		with open(badf) as f:
			lines = f.readlines()
		
		if (len(lines)>0):
			print 'WRITING input from ', badf 
			output = open(ff,'w') 
			for line in lines:
				endf = (line.split('/spFly-')[1]).split('.fits')[0]
				el = indir+plate+'/spec-'+endf+'.fits' #; print el 
				output.write(el+' \n')				
			output.close()	
	else:
		print badf,' NOT FOUND'

maxnumjobs = 4000

# Directory with input files
indir = os.path.join('/users/ghthomas/outerrim_mocks/george_thomas_project/')
checkdir(indir)
print ('Input: ',indir)

# Directory for scripts to be submitted
jobsdir = os.path.join('/users/ghthomas/outerrim_mocks/george_thomas_project/')
checkdir(jobsdir)
print 'Run scripts: ',jobsdir

# Directory for output files
outdir = '/users/ghthomas/output_catalogues'
checkdir(outdir)
print 'Output: ',outdir


# Directory for input lists
listdir = outdir
checkdir(listdir)
print 'Input lists: ',listdir

boxes = []
path2boxes = glob.glob(indir+'*')
for path2box in path2boxes:
	box = path2box.split('spectra/')[6]
	boxes.append(box)
print 'Number of boxes =',len(boxes) 

# Test on box
for box in boxes: # Full run
	ff = listdir+box+'.txt' #; print ff

	qsub_command = 'qsub '+listdir+box+'run.sh' # Runs 
	#qsub_command = 'qsub -q sciama1.q '+listdir+plate+'run.sh' 

	write_inputlist = False
	write_inputlist_resubmit = False

	if write_inputlist: 	# Generate lists with input files
		print 'WRITTING ',ff
		fileList = glob.glob(indir+box+'/spec-*.fits')
		fileList.sort()

		with open(ff, 'w') as output:
	                #for el in fileList[12:14]: # Test
			for el in fileList: # Full run
				output.write(el+' \n')

	elif write_inputlist_resubmit:
		resubmitFiles(listdir,plate,indir)

	if (os.path.isfile(ff)): # Find the number of input files
		with open(ff) as f: nfil = str(len(f.readlines()))
		# Write the submission script *run.sh
		writeScript(listdir,box,nfil,outdir)

                #-------------------------
		submit_scripts = False
	        #-------------------------
		if (submit_scripts):
			print 'SUBMIT: ',qsub_command      
			time.sleep(10.) ; trysubmit(maxnumjobs)
			os.system(qsub_command) ; time.sleep(10.)

                #-------------------------
		test_newfiles  = True
                #-------------------------
		if test_newfiles:
			print 'TESTING box ',box      
			testFiles(listdir,box,outdir)

sys.exit()

ff = open('Testbox1.txt')

logM = np.zeros(num)

for line in ff:
	logmass = float(line.split()[6])
	tag = float(line.split()[7])
	print (logmass)

	for i, ed in enumerate(edges[:-1]):
		mmin = ed
		mmax = edges[i + 1]
		if ((logmass <= mmax) and (logmass >= mmin)):
			tofile = zip(logmass, tag)
			if os.path.exists(outfile):
				with open(outfile, 'a') as outf:
					np.savetxt(outf,tofile,fmt=('%10.5f %i'))
					outf.closed
			else:
				with open(outfile, 'w') as outf:
					np.savetxt(outf,tofile,fmt=('%10.5f %i'))
					outf.closed

 
ff.close()
