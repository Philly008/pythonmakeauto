'''
Created on 2017年2月21日

@author: admin
'''
#coding=utf-8
import unittest
import HTMLTestRunner
import os, time, datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
# 这里需要导入测试文件
import pythonmakeauto.pythonBase.selenium.baidu as baidu, pythonmakeauto.pythonBase.selenium.youdao as youdao

# 定义发送邮件
def sentmail(file_new):
    # 发信邮箱
    mail_from = 'fnngj@126.com'
    # 收信邮箱
    mail_to = '123456@qq.com'
    # 定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg=MIMEText(mail_body, _subtype='html', _charset='utf-8')
    # 定义标题
    msg['Subject']=u'私有云测试报告'
    # 定义发送时间
    msg['date']=time.strftime('%a, %d %b %Y %H:%M%S %z')
    smtp=smtplib.SMTP()
    # 连接 SMTP 服务器
    smtp.connect('smtp.126.com')
    # 用户名密码
    smtp.login('fnngj@126.com', '123456')
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print('email has send out !')
# 查找测试报告，调用发邮件功能
def sendreport():
    result_dir = 'D:\\selenium_python\\report'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not
               os.path.isdir(result_dir+"\\" +fn) else 0)
    print(u'上一次测试生成的报告：' +lists[-2])
    # 找到上一次测试生成的文件
    file_new = os.path.join(result_dir, lists[-2])
    print(file_new)
    # 调用发邮件模块
    sentmail(file_new)

testunit = unittest.TestSuite()
# 将测试用例加入到测试容器（套件）中
testunit.addTest(unittest.makeSuite(baidu.Baidu))
testunit.addTest(unittest.makeSuite(youdao.Youdao))
# 执行测试套件
runner = unittest.TextTestRunner()
runner.run(testunit)

if __name__ == "__main__":
    # 执行发邮件
    sendreport()




