'''
Created on 2017年1月3日

@author: admin
'''
import socket
s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from ', addr)
    c.send(bytes('Thank you for connecting'))
    c.close()