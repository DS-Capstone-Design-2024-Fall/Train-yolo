#!/usr/bin/bash

#SBATCH -J v8m-tune
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-gpu=8
#SBATCH --mem-per-gpu=30G
#SBATCH -p batch_ugrad
#SBATCH -t 1-0
#SBATCH -o logs/slurm-%A.out

pwd
which python
hostname
python tune.py

exit 0
