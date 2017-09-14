__author__ = 'Administrator'
import time
from selenium import webdriver
url="http://www.lemfix.com/signin"
browser=webdriver.Chrome()
browser.get(url)
browser.find_element_by_link_text("忘记密码了？").click()
browser.back()
time.sleep(3)
browser.quit()