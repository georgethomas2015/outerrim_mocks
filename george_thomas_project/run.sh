#!/bin/bash 
#PBS -l walltime=24:00:00 
#PBS -o /users/ghthomas/junk_directory/queuetest.o.${PBS_JOBID}
#PBS -e /users/ghthomas/junk_directory/queuetest.e.${PBS_JOBID}
#PBS -q sciama1.q

 path='/users/ghthomas/outerrim_mocks/george_thomas_project/'
 prog='test.py'
 python $path$prog
