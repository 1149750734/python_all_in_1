__author__ = 'Administrator'
#谷歌浏览器，就要用到chromedriver需要去下载安装
import time
from selenium import webdriver
browser=webdriver.Chrome()
browser.get("http://www.baidu.com")

browser.maximize_window()#窗口最大化
browser.set_window_size(400,400)#设置窗口尺寸

time.sleep(5)#等待5秒
browser.maximize_window()

#前进后退键的使用和模拟
url_1="http://www.baidu.com"
url_2="http://www.lemfix.com"

#访问百度首页
print("访问百度首页：%s"%(url_1))
browser.get(url_1)
time.sleep(5)

#前进到社区页面
print("前进：%s"%(url_2))
browser.forward()
time.sleep(5)

browser.refresh()
browser.get_screenshot_as_file("jietu.jpg")

