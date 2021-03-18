# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome()

# 打开url
driver.get('')

# 查找用户名 输入admin
driver.find_element_by_name('').send_keys('admin')

# 查找密码 输入123456
driver.find_element_by_name('').send_keys('123456')

# 暂停3s
sleep(3)

# 退出浏览器
driver.quit()