#!/bin/bash 
#PBS -l walltime=24:00:00
#PBS -o /users/ghthomas/junk_directory/queuetest.o.${PBS_JOBID}
#PBS -e /users/ghthomas/junk_directory/queuetest.e.${PBS_JOBID}
#PBS -l nodes=1:ppn=1
#PBS -q sciama1.q
 cute='/users/ghthomas/CUTE/CUTE_box/CUTE_box'  
 path='/users/ghthomas/outerrim_mocks/george_thomas_project/'
 prog='paramstes2.txt'
 $cute $path$prog
