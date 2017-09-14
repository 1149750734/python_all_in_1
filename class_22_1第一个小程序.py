__author__ = 'Administrator'
import time
from selenium import webdriver
#打开浏览器，访问百度，该操作是固定的
url="http://www.lemfix.com/signin"
browser=webdriver.Chrome()#打开谷歌浏览器,即创造浏览器对象
browser.get(url)

browser.find_element_by_id("name").send_keys("summer")

time.sleep(5)
browser.find_element_by_id("name").clear()

browser.find_element_by_name("name").send_keys("sally")

time.sleep(5)
browser.find_element_by_class_name("span-primary").click()

browser.quit()#用完后退出浏览器