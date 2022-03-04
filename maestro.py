import os
import json
import threading
import time
import pandas as pd
from case import case
import config
from server import server

## This starts a daemon thread running the server function
thread = threading.Thread(target=server)
thread.daemon = True
thread.start()

n = 0
while n < len(config.my_cases):
  ## Get the max_nodes each time to see if it changed
  with open("%s/max_nodes"%(config.root_dir)) as f:
    config.max_concurrent_cases = int(f.read().strip())
  n_running = config.getNRunning()
  if n_running < config.max_concurrent_cases:
    c = case(config.my_cases.iloc[n].to_json())
    run_num = config.my_cases.iloc[n]["run_num"]
    if not c.isCompleted():
      if not os.path.isfile("%s/RUNNING"%(c.case_dir)):
        print("Submitting case: %d"%(run_num))
        c.run()
    n += 1
  else:
    time.sleep(5)
