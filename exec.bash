#!/bin/bash

##SBATCH --nodes=1
#SBATCH --time=2-10:59:59
#SBATCH --job-name=10-6KT

#SBATCH --mem=64Gb
##SBATCH --gres=gpu:k40m:1
#SBATCH --output=Output.%j.out

## Choose one of these methods
#SBATCH --partition=general
##SBATCH -p long

## legacy option for specifying CPU architecture
###SBATCH --constraint=E5-2690v3@2.60GHz

module load python/3.8.1
source /work/props/yourusername/HOOMDblue/VirtEnv/bin/activate
/work/props/yourusername/HOOMDblue/VirtEnv/bin/python3  simulation.py
