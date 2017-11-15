'''
Created on 2017年2月4日

@author: admin

#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time, os
import userinfo # 导入函数

# 通过两个变量，来接收调用函数获得用户名&密码
us, pw = userinfo.fun()
# 打印两个变量
print(us, pw)

source = open("F:\\workspace\\hola world\\selenium\\username.txt","r")
un = source.read() # 读取用户名
source.close()
source2 = open("F:\\workspace\\hola world\\selenium\\password.txt","r")
pw = source2.read() # 读取密码
source2.close()
def login(self):
    driver = self.driver
    driver.maximize_window()
    driver.find_element_by_id("user_name").clear()
    driver.find_element_by_id("user_name").send_keys(un)
    driver.find_element_by_id("user_pwd").clear()
    driver.find_element_by_id("user_pwd").send_keys(pw)
    driver.find_element_by_id("dl_an_submit").click()
    time.sleep(3)
 '''
 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
 
driver = webdriver.Firefox()
driver.get("http://passport.kuaibo.com")
driver.maximize_window()    # 浏览器最大化
# 登录快播私有云
driver.find_element_by_id("user_name").send_keys("testing360")
driver.find_element_by_id("user_pwd").send_keys("198876")
driver.find_element_by_id("dl_an_submit").click()
time.sleep(3)
# 获取用户名
now_user = driver.find_element_by_xpath("//div[@id='Nav']/ul/li[4]/a[1]/span").text
# 用户名是否等于虫师，不等于将抛出异常
if now_user == u'虫师':
    print('登录成功')
else:
    raise NameError('user name error!')
# 退出
driver.find_element_by_class_name("Usertoot").click()
time.sleep(2)
driver.find_element_by_link_text("退出").click()
time.sleep(2)
driver.close()

# 判断当前文件个数
inputs = driver.find_element_by_tag_name('input')
n = 0
for i in inputs:
    if i.get_attribute('type') == "checkbox":
        n=n+1
print(u"当前列表文件为 %d" %n)
# 收藏用户分享文件
driver.find_element_by_class_name("collect").click()
time.sleep(3)
# 再次获取当前文件的个数
inputs=driver.find_element_by_tag_name('input')
ns=0
for ii in inputs:
    if ii.get_attribute('type')=="checkbox":
        ns=ns+1
print(u"当前列表文件为  %d" %ns)
# 判断执行收场文件之后比手擦很难过之前文件加1， 否则抛异常
if ns==n+1:
    print("ok!")
else:
    raise NameError('添加文件失败！')

# 判断当前文件个数
inputs = driver.find_element_by_tag_name('input')
n=0
for i in inputs:
    if i.get_attribute('type')=="checkbox":
        n=n+1
print(u"当前列表文件为  %d" %n)
# 删除操作
driver.find_element_by_xpath("/html/body/div/div[2]/table/input").click()
driver.find_element_by_class_name("dele").click()
driver.find_element_by_xpath("/html/body/div[2]/div").click()
time.sleep(4)
# 再次获取当前文件的个数
inputs = driver.find_element_by_tag_name('input')
ns=0
for ii in inputs:
    if ii.get_attribute('type')=="checkbox":
        ns=ns+1
print(u"当前列表文件为  %d" %ns)
# 判断执行删除单个文件之后比删除之前文件减 1，否则抛异常
if ns==n-1:
    print("ok!")
else:
    raise NameError('删除文件失败！')
# 收藏用户分享单个文件
driver.find_element_by_class_name("collect").click()
time.sleep(3)

 # 勾选重命名的文件
driver.find_element_by_xpath("/html/body/div/table/input").click()
time.sleep(3)
# 鼠标移动到“更多”按钮弹下拉框
element = driver.find_element_by_class_name("more-fe")
ActionChains(driver).move_to_element(element).perform()
time.sleep(2)
# 在 li 标签（更多 下拉框）中筛选到 data-action==rename(重命名)选项点击
lis=driver.find_element_by_class_name('li')
for li in lis:
    if li.get_attribute('data-action')=='rename':
        li.click()
time.sleep(2)
# input 标签中筛选 type==text 的重命名输入框
inputs = driver.find_element_by_tag_name('input')
for input in inputs:
    if input.get_attribute('type') == 'text':
        input.send_keys(u"新文件名")    # 进行重名操作
        input.send_keys(Keys.ENTER) #回车确认重命名
        time.sleep(2)
   






