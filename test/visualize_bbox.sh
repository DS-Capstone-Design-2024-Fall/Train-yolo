#!/usr/bin/bash

#SBATCH -J viz_bbox
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-gpu=8
#SBATCH --mem-per-gpu=30G
#SBATCH -p batch_ugrad
#SBATCH -t 1-0
#SBATCH -o logs/slurm-%A.out

pwd
which python
hostname
# python 코드 실행 순서는 꼭 다음의 순서를 지켜야 한다.
python visualize_pred_bbox.py
python visualize_ans_bbox.py

exit 0
