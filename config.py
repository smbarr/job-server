import os
import subprocess
import pandas as pd

root_dir = ...

# Define which sets of cases will be run on this machine
_set = "set1"
priority = 0

# Set the maximum number of concurrent jobs to the single integer in "max_nodes"
with open("max_nodes") as f:
  max_concurrent_cases = int(f.read().strip())

# Load case matrix
case_matrix = pd.read_csv("case-matrix.csv", index_col=0)
# Get subset of cases for to be run on this machine
my_cases = case_matrix.loc[(case_matrix["set"] == _set) & (case_matrix["priority"] == priority)]

# Get number of currently running cases
# This will be dependent on your queue system
def getNRunning():
  n_running = 0
  res = subprocess.run(["squeue", "-o%.25j %.8u %.2t"], capture_output=True)
  jobs = [[n for n in l.split()] for l in res.stdout.decode().split("\n")][1:-1]
  for j in jobs:
    if "RUN-" in j[0] and j[1] == os.getlogin() and (j[2] == "R" or j[2] == "PD"):
      n_running += 1
  return n_running

n_running = getNRunning()
