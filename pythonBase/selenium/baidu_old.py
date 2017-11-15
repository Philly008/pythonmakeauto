'''
Created on 2017年1月18日

@author: admin
'''
from time import sleep
'''
# import selenium
# print(selenium.__file__)    # 查看调用的selenium路径
# 获取 https://github.com/mozilla/geckodriver/releases 放到Python 路径下
from lib2to3.tests.support import driver

from selenium import webdriver

browser = webdriver.Firefox()
#browser = webdriver.Chrome()


browser.get("http://www.baidu.com")

print("浏览器最大化")
browser.maximize_window()   # 将浏览器最大化显示

browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()


browser.get("http://m.mail.10086.cn")
# 参数数字为像素点
print("设置浏览器宽 480、高 800 显示")
browser.set_window_size(480, 800)
#browser.quit()


#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
# 访问百度首页
first_url = 'http://www.baidu.com'
print("now access %s" % (first_url))
driver.get(first_url)

# 访问新闻页
second_url = 'http://news.baidu.com'
print("now access %s" % (second_url))
driver.get(second_url)

# 返回（后退）到百度首页
print("back to %s " % (first_url))
driver.back()

# 前进到新闻页
print("forward to %s" % (second_url))
driver.forward()

#driver.quit()


from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://mail.163.com/index_alternate.htm")

driver.find_element_by_id("idInput").clear()
driver.find_element_by_id("idInput").send_keys("liuup66")
driver.find_element_by_id("pwdInput").clear()
driver.find_element_by_id("pwdInput").send_keys("163liu")
driver.find_element_by_id("loginBtn").click()

size = driver.find_element_by_id("idInput").size
print(size)

# 返回百度页面底部备案信息
text = driver.find_element_by_id("cp").text
print(text)

# 返回元素的属性值，可以是 id, name, type 或元素拥有的其它任意属性
attribute = driver.find_element_by_id("kw").get_attribute('type')
print(attribute)

result = driver.find_element_by_id("kw").is_displayed()
print(result)
# 通过 submit() 来提交操作
# driver.find_element_by_id("dl_an_submit").submit()
#driver.quit()


# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# 定位到要右击的元素
right = driver.find_element_by_xpath("xx")
# 对定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(right).perform()

# 定位到要双击的元素
double = driver.find_element_by_xpath("xxx")
# 对定位到的元素执行鼠标双击操作
ActionChains(driver).double_click(double).perform()

# 定位元素的原位置
element = driver.find_element_by_name("xxx")
# 定位元素要移动到的目标位置
target = driver.find_element_by_name("xxx")
# 执行元素的移动操作
ActionChains(driver).drag_and_drop(element, target).perform()

# 定位到鼠标移动到上面的元素
above = driver.find_element_by_xpath("xxx")
# 对定位到的元素执行鼠标移动到上面的操作
ActionChains(driver).move_to_element(above).perform()

# 定位到鼠标按下左键的元素
left = driver.find_element_by_xpath("xxx")
# 对定位到的元素执行鼠标左键按下的操作
ActionChains(driver).click_and_hold(left).perform()


#coding=utf-8
from selenium import webdriver
# 引入 Keys 类包
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# 输入框输入内容
driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(3)
# 删除多输入的一个 m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(3)
# 输入空格键+“教程”
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys(u"教程")
time.sleep(3)
#ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
time.sleep(3)
# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
time.sleep(3)
# 输入框重新输入内容，搜索
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
time.sleep(3)
# 通过回车键盘来代替点击事件
driver.find_element_by_id("su").send_keys(Keys.ENTER)
time.sleep(3)

# 登录
driver.find_element_by_id("user_name").clear()
driver.find_element_by_id("user_name").send_keys("username")
driver.find_element_by_id("user_pwd").clear()
driver.find_element_by_id("user_pwd").send_keys("password")
driver.find_element_by_id("dl_an_submit").click()

# 获得前面 title, 打印
title = driver.title
print(title)
# 拿当前URL 与预期 URL 做比较
if title == u"快播私有云":
    print("title ok!")
else:
    print("title on!")
# 获得前面URL，打印
now_url = driver.current_url
print(now_url)
# 拿当前URL 与预期URL 做比较
if now_url == "http://webcloud.kuaibo.com/":
    print("url ok!")
else:
    print("url on!")
# 获得登录成功的用户， 打印
now_user = driver.find_element_by_xpath("//div[@id='Nav']/ul/li[4]/a[1]/span").text 
print(now_user)

driver.quit()


from selenium import webdriver
# 导入 WebDriverWait 包
from selenium.webdriver.support.ui import WebDriverWait
# 导入 time 包
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# WebDriverWait() 方法使用
element = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("kw"))
element.send_keys("selenium")
# 添加智能等待
driver.implicitly_wait(30)
driver.find_element_by_id("su").click()
# 添加固定休眠时间
time.sleep(5)


from selenium import webdriver
import os

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)
# 选择页面上所有的 tag name 为 input 的元素
inputs = driver.find_elements_by_tag_name('input')
# 然后从中过滤出 type 为 checkbox 的元素，单击为勾选
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()

# 选择所有的 type 为 checkbox 的元素并单击勾选
checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes :
    checkbox.click()
# 打印当前页面上 type 为 checkbox 的个数
print(len(driver.find_elements_by_css_selector('input[type=checkbox]')))
# 把页面上最后一个 checkbox 的勾选去掉
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()

 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('level_locate.html')
driver.get(file_path)
# 点击 Link1 链接（弹出下拉列表）
driver.find_element_by_link_text('Link1').click()
# 在父亲元件下找到 link 为 Action 的子元素
menu = driver.find_element_by_id('dropdown1').find_element_by_link_text('Another action')
# 鼠标移动到子元素上
ActionChains(driver).move_to_element(menu).perform()
time.sleep(5)     
 
 
from selenium import webdriver
import time
import os

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('frame.html')
driver.get(file_path)
driver.implicitly_wait(30)
# 先找到 iframe1 (id=f1)
driver.switch_to_frame("f1")
# 再找到其下面的 iframe2 (id=f2)
driver.switch_to_frame("f2")
# 下面就可以正常的操作元素了
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)


from selenium import webdriver
import time 

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# 点击登录链接
#driver.find_element_by_name("tj_login").click()
driver.find_element_by_css_selector("a.lb:nth-child(7)").click()
time.sleep(10)

# 通过二次定位找到用户名输入框
div = driver.find_element_by_class_name("tang-content").find_element_by_name("userName")
#div = driver.find_element_by_id("TANGRAM__PSP_2__content").find_element_by_name("userName")
div.send_keys("liushuiliu3")
# 输入登录密码
driver.find_element_by_name("password").send_keys("liushuiliu3")
# 点击登录
driver.find_element_by_id("TANGRAM__PSP_8__submit").click()


from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# # 获得当前窗口
# nowhandle = driver.current_window_handle
# # 打开注册新窗口
# driver.find_element_by_name("tj_reg").click()
# # 获得所有窗口
# allhandles = driver.window_handles
# # 循环判断窗口是否为当前窗口
# for handle in allhandles:
#     if handle != nowhandle:
#         driver.switch_to_window(handle)
#         print('now register window!')
#         # 切换到邮箱注册标签
#         driver.find_element_by_id("mailRegTab").click()
#         time.sleep(5)
#         driver.close()
# # 回到原先的窗口
# driver.switch_to_window(nowhandle)
# driver.find_element_by_id("kw").send_keys(u"注册成功！")
# time.sleep(3)

# 点击打开搜索设置
driver.find_element_by_name("tj_settingicon").click()
driver.find_element_by_id("SL_1").click()
# 点击保存设置
driver.find_element_by_xpath("//div[@id='gxszButton']/input").click()
# 获取网页上的警告信息
alert = driver.switch_to_alert()
# 接收警告信息
alert.accept()
# 得到文本信息并打印
print(alert.text())
# 取消对话框
alert.dismiss()
# 输入值
alert.send_keys("xxx")


from selenium import webdriver
import os,time

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('drop_down.html')
driver.get(file_path)
time.sleep(2)
# 先定位到下拉框
m = driver.find_element_by_id("ShippingMethod")
# 再点击下拉框下的选项
m.find_element_by_xpath("//option[@value='10.69']").click()
time.sleep(3)


from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://passport.kuaibo.com/login")
# 登录系统
driver.find_element_by_id("user_name").clear()
driver.find_element_by_id("user_name").send_keys("username")
driver.find_element_by_id("user_pwd").clear()
driver.find_element_by_id("user_pwd").send_keys("password")
driver.find_element_by_id("dl_an_submit").click()
sleep(2)
# 获取所有分页的数量，并打印
total_pages = len(driver.find_element_by_tag_name("select").find_elements_by_tag_name("option"))
print("total page is %s" % (total_pages))
sleep(3)
# 再次获取分页，并执行循环翻页操作
pages = driver.find_element_by_tag_name("select").find_elements_by_tag_name("option")
for page in pages:
    page.click()
    sleep(2)
sleep(3)


from selenium import webdriver
import os, time

driver = webdriver.Firefox()
# 打开上传文件页面
file_path = 'file:///' + os.path.abspath('upload_file.html')
driver.get(file_path)
# 定位上传按钮，添加本地文件
driver.find_element_by_name("file").send_keys('F:\\新建文本文档2.txt')
time.sleep(2)


import requests
print(requests.head('http://www.baidu.com').headers['content-type'])


import os,time
from selenium import webdriver

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
browser = webdriver.Firefox(firefox_profile=fp)
browser.get("http://pypi.python.org/pypi/selenium")
time.sleep(10)
browser.find_element_by_partial_link_text("selenium").click()

print("Done!")


from selenium import webdriver
import time, os

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('js.html')
driver.get(file_path)
####通过 JS 隐藏选中的元素###第一种方法：
# 隐藏文字信息
driver.execute_script('$("#tooltip").hide();')
time.sleep(5)
print("wenzixinxi")
# 隐藏按钮：
button = driver.find_element_by_class_name('btn')
driver.execute_script('$(arguments[0]).hide()', button)
time.sleep(5)
print("anniu")


from selenium import webdriver
import time
# 访问百度
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# 搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
# 将页面滚动条拖到底部
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)
# 将滚动条移动到页面的顶部
js_ = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js_)
time.sleep(3)


from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")
# 获得 cookie 信息
cookie = driver.get_cookies()
# 将获得 cookie 的信息打印
print(cookie)
# 向cookie 的name 和 value 添加会话信息
driver.add_cookie({'name':'key-aaa', 'value':'value-bbb'})
# 遍历 cookie 中的 name 和 value 信息打印
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))
####下面可以通过来年高中方式删除 cookie
# 删除一个特定的 cookie
driver.delete_cookie("key-aaa")
print("deleteone")
# 删除所有 cookie
driver.delete_all_cookies()
print("deleteall")
time.sleep(2)
driver.close()


# 选择页面上所有的 tag name 为 input 的元素
inputs = driver.find_element_by_tag_name('input')
# 然后循环遍历出 data-node 为 555 的元素，单击勾选
for input in inputs :
    if input.get_attribute('data-node') == '555':
        input.click()
        
# 访问 xxx 网站
driver.get("http://www.xxx.cn/")
# 将用户名密码写入浏览器 cookie
driver.add_cookie({'name':'login_username', 'value':'username'})
driver.add_cookie({'name':'login_passwd','value':'password'})
# 再次访问 xxx 网站，将会自动登录
driver.get("http://www.xxx.cn/")
time.sleep(3)
       
  
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.xxx.com")
        
driver.find_element_by_id("tbUserName").send_keys("username")      
driver.find_element_by_id("tbPassword").send_keys("123456")
driver.find_element_by_id("btnLogin").click()
# 执行具体用例操作
#...
driver.quit()        


# 登录模块 login.py
def login():
    driver.find_element_by_id("tbUserName").send_keys("username")
    driver.find_element_by_id("tbPassword").send_keys("456123")
    driver.find_element_by_id("btnLogin").click()

# 退出模块 quit.py
def quit_():
    ... 
    
# 测试用例
from selenium import webdriver
import login, quit_     # 调用登录、退出模块         

driver = webdriver.Firefox()
driver.get("http://www.xxx.com")
# 调用登录模块
login.login()
# 其它个性化操作
...
# 调用退出模块
quit.quit()    
 
 
#coding=utf-8
from selenium import webdriver
import time
values = ['selenium', 'webdriver', u'充实']
# 执行循环
for search in values:
    driver = webdriver.Firefox()
    driver.get("http://www.xxx.com")
    driver.find_element_by_id("kw").send_keys(search)
    time.sleep(3)
    ...        
''' 

from selenium import webdriver
browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
# 捕捉百度输入框异常
try:
    browser.find_element_by_id("kwsss").send_keys("selenium")
    browser.find_element_by_id("su").click()
except:
    browser.get_screenshot_as_file("./error_png.png")
#browser.quit()
        
        
        


