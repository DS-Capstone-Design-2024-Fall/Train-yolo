#!/usr/bin/bash

#SBATCH -J yolov8
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-gpu=8
#SBATCH --mem-per-gpu=30G
#SBATCH -p batch_ugrad
#SBATCH -t 1-0
#SBATCH -o logs/slurm-%A.out

pwd
which python
hostname
python test.py

exit 0
