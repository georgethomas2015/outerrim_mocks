#!/bin/bash 
#PBS -l walltime=24:00:00 
#PBS -o /users/ghthomas/junk_directory/queuetest.o.${PBS_JOBID}
#PBS -e /users/ghthomas/junk_directory/queuetest.e.${PBS_JOBID}
#PBS -q sciama1.q
#module load apps/anaconda3/5.2.0
path='/users/ghthomas/outerrim_mocks/george_thomas_project/'
prog='script_Bigbox.py'
python3 $path$prog
