'''
Created on 2017年2月28日

@author: admin
'''

#!D:\python35\python.exe
#encoding=UTF-8

print ('Content-type: text/html\n')
from os.path import join, abspath
import cgi, sys

BASE_DIR = abspath('data')
form = cgi.FieldStorage()
filename = form.getvalue('filename')
if not filename:
    print('Please enter a file name')
    sys.exit()
text = open(join(BASE_DIR, filename)).read()
 
 
 
 
 
 
 
    

