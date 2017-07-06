from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://113.108.207.92:8899/PG/login.action')
userName = browser.find_element_by_id('userName').send_keys('xxb')
password = browser.find_element_by_id('password').send_keys('daan123')
login = browser.find_element_by_class_name('login_go').click()
sleep(5)
moveto = browser.find_element_by_xpath('//*[@id="menu"]/li[4]/a')
ActionChains(browser).move_to_element(moveto).perform()
sleep(15)
pg_input = browser.find_element_by_xpath('//*[@id="menu"]/li[4]/ul/li[1]/a').click()

sleep(10)

browser.switch_to.frame('menu3001')

# 201705030100
browser.find_element_by_xpath('//*[@id="txtBarCode"]').clear()
browser.find_element_by_xpath('//*[@id="txtBarCode"]').send_keys('201705030100')    # Ctrl + Alt + 向下键，复制内容到下一行
browser.find_element_by_xpath('//*[@id="txtBarCode"]').send_keys(Keys.ENTER)    # Ctrl + Alt + 向下键，复制内容到下一行
# logout = browser.find_element_by_link_text('注销').click()
browser.find_element_by_id('btnSave').click()
browser.find_element_by_id('popup_ok').click()