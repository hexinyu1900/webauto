# 导包
import time
from time import sleep
from selenium import webdriver

# 获取浏览器对象
driver = webdriver.Chrome()

# 最大化浏览器
driver.maximize_window()

# 设置cookie
driver.get('https://gssdev.haoshengy.com/pc_workbench/workbench/overview')
driver.add_cookie({'name':'jwt_dev','value':''})

# 间隔3秒，关闭浏览器
sleep(3)
driver.quit()