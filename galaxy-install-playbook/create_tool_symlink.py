#!/usr/env/python

import sys
import os
from subprocess import call

# This script create symlinks used by conda to activate certain environments.


# NOTE YOU MUST EXPORT CONDA_PATH IN YOUR .bashrc file
# i.e export CONDA_ROOT_PATH=/cvmfs/soft.galaxy/v2/tool-dependency/_conda

# Call this script without Arguments

conda_env_path = os.path.join(os.environ['CONDA_ROOT_PATH'], 'envs')
envs = []

for f in os.listdir(conda_env_path):
  if not f.startswith('.'):
    envs.append(f)

for env in envs:
  flist = []
  for folder  in os.listdir(os.path.join(conda_env_path, os.path.join(env, '/bin/'))):
    if not folder.startswith('.'):
      flist.append(folder)

  if not "conda" in flist:
    str1 = os.path.join(os.environ['CONDA_ROOT_PATH'], "bin/conda")
    str2 = os.path.join(os.environ['CONDA_ENV_PATH'],  os.path.join(env,"/bin/"))

    call(["ln", "-s", str1, str2 + "conda"])
    call(["ln", "-s", str1, str2 + "activate"])
    call(["ln", "-s", str1, str2 + "deactivate"])
    print "created for " + env

  #sys.exit()
