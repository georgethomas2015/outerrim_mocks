#! /bin/bash
#PBS -l walltime=24:00:00
#PBS -l nodes=1

logpath=/mnt/lustre/$(whoami)/Junk/tar1

qsub -q sciama1.q -o $logpath -j oe run.sh 

