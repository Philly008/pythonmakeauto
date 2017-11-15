'''
Created on 2017年1月9日

@author: admin
'''
from xml.sax.handler import ContentHandler
from xml.sax import parse

class TestHandler(ContentHandler): 
    def startElement(self, name, attrs):
        print(name, attrs.keys())
parse('website.xml', TestHandler())