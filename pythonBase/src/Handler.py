'''
Created on 2017年1月3日
一个基于 SocketServer 的小型服务器
@author: admin
'''
from socketserver import TCPServer, StreamRequestHandler
class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('Got connection from ', addr)
        self.wfile.write('Thank you for connecting')
server = TCPServer(('', 1234), Handler)
server.serve_forever()