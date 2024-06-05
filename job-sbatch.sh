#!/bin/bash
#SBATCH --job-name=pcrystal
#SBATCH --partition=bluemoon
#SBATCH --array=1-100  # Change this to the desired array size
#SBATCH --ntasks=256
#SBATCH --time=8:00:00  # Adjust the time limit as needed



cd run_${SLURM_ARRAY_TASK_ID}

source /users/r/s/rschirem/intel/oneapi/setvars.sh
/users/r/s/rschirem/CRYSTAL_23/ompi/bin/mpirun /users/r/s/rschirem/CRYSTAL_23/bin/Linux-ifort_openmpi_i64_clut/std/Pcrystal </dev/null &> output_${SLURM_ARRAY_TASK_ID}.out
