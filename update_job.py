import os, sys
import json
import struct
import pickle
import socket

def send_msg(msg):
  host = # Enter the hostname here
  port = 12345
  s = socket.socket()
  s.connect((host, port))
  data = pickle.dumps(msg)
  data_size = sys.getsizeof(data)
  s.send(struct.pack('!i',data_size))
  res = s.recv(1024)
  s.send(data)
  res = s.recv(1024)

  s.close()

## This dictionary can have some case-specific data
data{
  "value": 1.0
}
send_msg(data)
