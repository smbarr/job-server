import pickle
import struct
import config
import socket

def server():
  port = 12345
  s = socket.socket()
  
  s.bind(('', port))
  print("Opened socket on port %d"%(port))
  
  s.listen()
  
  while True:
    c, addr = s.accept()
    print("Got a connection from ", addr)
  
    buf = b''
    while len(buf) < 4:
      buf += c.recv(8)
    datasize = struct.unpack('!i', buf[:4])[0]
    c.send(b"Received")
    data = c.recv(datasize)
    msg_p = pickle.loads(data)
    c.send(b"Received")

    ## Get the value from the received message
    config.case_matrix.loc[config.case_matrix["run_num"] == msg_p["run_num"],"value"] = msg_p["value"]

    config.my_cases = config.case_matrix.loc[(config.case_matrix["set"] == config._set) & (config.case_matrix["priority"] == config.priority)]
    config.case_matrix.to_csv("case-matrix.csv")
  
    c.close()
