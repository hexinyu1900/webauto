from time import sleep
# 导包 webdriver
from selenium import webdriver

# 获取谷歌浏览器对象
driver = webdriver.Chrome()
# 打开百度
driver.get('https://www.baidu.com/')
# 暂停3秒
sleep(3)
# 退出浏览器驱动
driver.quit()
