#!/bin/bash 
#PBS -l walltime=24:00:00 
#PBS -o /users/ghthomas/junk_directory/input.o.${PBS_JOBID}
#PBS -e /users/ghthomas/junk_directory/input.e.${PBS_JOBID}
#PBS -q sciama1.q

 path='/users/ghthomas/outerrim_mocks/george_thomas_project/'
# prog='test.py'
 prog='write_input.py'
 python $path$prog
