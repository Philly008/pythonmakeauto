'''
Created on 2017年2月4日

@author: admin

import userinfo # 导入函数
# 获取字典数据
info = userinfo.zidian()
# 通过 items() 循环读取元组（键/值对）
for us, pw in info.items():
    print(us)
    print(pw)
'''

import csv # 导入 csv 包
from _csv import Dialect
# 读取本地 CSV 文件
my_file = 'F:\\workspace\\hola world\\selenium\\userinfo.csv'
data=csv.reader(file(my_file,'rb'))
print(data)
# 循环输出每一行信息
for user in data:
    print(user[0])
    print(user[1])
    print(user[2])
    print(user[3])









