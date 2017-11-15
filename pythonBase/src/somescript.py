'''
Created on 2016年12月30日

@author: admin
'''
import sys 
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print('Wordcount: ', wordcount)