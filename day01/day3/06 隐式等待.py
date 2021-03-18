# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome()

# 设置隐式等待10s
driver.implicitly_wait(10)

# 打开url
driver.get('https://gssdev.haoshengy.com/pc_workbench/login')

# 最大化浏览器
driver.maximize_window()

# 给一个错误id，如果直接抛出异常，说明等待失效，反之生效
driver.find_element_by_css_selector('#user')
# 暂停3秒
sleep(3)

# 退出浏览器
driver.quit()