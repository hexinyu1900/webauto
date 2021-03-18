# 导包
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


# 获取浏览器对象
driver = webdriver.Chrome()

# 打开url
driver.get('https://gssdev.haoshengy.com/pc_workbench/login')

# 最大化浏览器
driver.maximize_window()

# 实例化WebDriverWait()并调用until方法
# 注意：调用until方法返回的一定是一个元素
WebDriverWait(driver, timeout=30, poll_frequency=0.5).until(lambda x:x.find_element_by_id('userA')).send_keys('123')
# 此时el还不是元素，只有代码运行起来才是元素


# 给一个错误id，如果直接抛出异常，说明等待失效，反之生效
driver.find_element_by_css_selector('#user')
# 暂停3秒
sleep(3)
# 退出浏览器
driver.quit()