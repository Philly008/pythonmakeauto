from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://113.108.207.92:8899/PG/login.action')
userName = browser.find_element_by_id('userName').send_keys('xxb')
password = browser.find_element_by_id('password').send_keys('daan123')
login = browser.find_element_by_class_name('login_go').click()
sleep(2)
moveto = browser.find_element_by_xpath('//*[@id="menu"]/li[4]/a')
print(moveto)
ActionChains(browser).move_to_element(moveto).perform()
sleep(3)


# logout = browser.find_element_by_link_text('注销').click()