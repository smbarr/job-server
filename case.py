import json
import config
import os

class case:
  params = {}
  finished = False
  def __init__(self, params):
    ## Initialize the case
    params = json.loads(params)
    self.case_number = params["run_num"]
    self.params = params
    self.root_dir = config.root_dir
    self.case_dir = ""

    self.case_dir = "CASES/CASE-%0.5d"%(self.case_number)
    if not os.path.isdir(self.case_dir):
      ## Make new case directory and copy input files to it
      os.system("mkdir %s"%(self.case_dir))
      os.system("cp INPUTS/* %s/."%(self.case_dir))

  def run(self):
    ## Run job
    os.chdir(self.case_dir)
    os.system("sbatch job.scr")
    os.chdir(self.root_dir)

  def isCompleted(self):
    ## Add some logic here to check if case completed or not
    completed = False
    return completed

  def getFitness(self):
    ## Get fitness value for the case
    fitness = 0.0
    return fitness
