'''
Created on 2017年1月18日

@author: admin
'''
from asyncore import dispatcher
import asyncore
class ChatServer(dispatcher): pass
s = ChatServer()
asyncore.loop()