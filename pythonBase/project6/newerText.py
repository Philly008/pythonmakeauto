#coding=UTF-8
'''
Created on 2017年3月13日

@author: admin
'''
import os, os.path, datetime, locale
locale.setlocale(locale.LC_CTYPE, 'chinese')
base_dir = "D:\\apache-tomcat-7.0.6\\webapps\\"
l=os.listdir(base_dir)
l.sort(key=lambda fn: os.path.getmtime(base_dir+fn) if not os.path.isdir(base_dir+fn) else 0)
d=datetime.datetime.fromtimestamp(os.path.getmtime(base_dir+l[-1]))
print('最后改动的文件是'+l[-1]+",时间："+d.strftime("%Y年%m月%d日  %H时%M分%S秒"))