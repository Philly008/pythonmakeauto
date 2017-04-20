'''
Created on 2016年12月28日

@author: admin
'''
import fileinput, random 
fortunes = list(fileinput.input())
print(random.choice(fortunes))