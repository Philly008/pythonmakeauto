'''
Created on 2017年1月3日

@author: admin
'''
import socket
s = socket.socket()
host = socket.gethostname()
port = 1234
s.connect((host, port))
print(s.recv(1024))