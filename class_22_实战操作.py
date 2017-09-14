__author__ = 'Administrator'
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#完成登录
url="http://www.lemfix.com/signin"
browser=webdriver.Chrome()
browser.get(url)
browser.find_element_by_id("name").send_keys("sally")
browser.find_element_by_id("pass").send_keys("123456")
browser.find_element_by_class_name("span-primary").submit()

#浏览器最大化
time.sleep(2)
browser.maximize_window()

#链接访问
time.sleep(2)
browser.find_element_by_link_text("【Python：获取时间戳】").click()

#返回上一页
time.sleep(2)
browser.back()

#返回到上次阅读的文章
time.sleep(2)
browser.forward()

#评论
# text=browser.find_element_by_xpath(".//*[@id='reply_form']/div/div/div[2]/div[6]/div[1]/div/div/div/div[3]/pre")
# ActionChains(browser).click(text).perform()
# but=browser.find_element_by_xpath(".//*[@id='reply_form']/div/div/div[3]/input")
# ActionChains(browser).click(but).perform()

#点赞
zan=browser.find_element_by_xpath(".//*[@id='594220c33eb7d7be23c27659']/div[1]/div[2]/span[1]/i")
ActionChains(browser).click(zan).perform()
#退出浏览器
browser.quit()




