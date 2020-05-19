
WORKFLOW='inversion'    # inversion, migration, modeling
SOLVER='specfem3d'      # specfem2d, specfem3d
SYSTEM='tiger_lg'       # serial, pbs, slurm
OPTIMIZE='LBFGS'        # base
PREPROCESS='base'       # base
POSTPROCESS='base'      # base

MISFIT='Waveform'
MATERIALS='Acoustic'
DENSITY='Constant'
PRECOND=None


# WORKFLOW
BEGIN=1                 # first iteration
END=1                   # last iteration
NREC=729                # number of receivers
NSRC=1                  # number of sources


# PREPROCESSING
FORMAT='su'             # data file format
CHANNELS='z'            # data channels
NORMALIZE=0             # normalize
MUTE=0                  # mute direct arrival
MUTECONST=0.            # mute constant
MUTESLOPE=0.            # mute slope


# POSTPROCESSING
SMOOTH=0.               # smoothing radius
SCALE=1.                # scaling factor


# OPTIMIZATION
STEPMAX=10              # maximum trial steps
STEPINIT=0.25           # step length safeguard
STEPFACTOR=0.75


# SOLVER
NT=800                  # number of time steps
DT=0.0025               # time step
F0=2.5                  # dominant frequency


# SYSTEM
NTASK=NSRC              # number of tasks
NPROC=16                # number of processers
WALLTIME=10             # walltime

