# 导包
from time import sleep
from selenium import webdriver

# 获取浏览器对象
driver = webdriver.Chrome()

# 打开url
driver.get('https://gssdev.haoshengy.com/pc_workbench/login')

# 设置浏览器窗口大小
driver.set_window_size(500, 500)

# 设置浏览器窗口位置
driver.set_window_position(100,500)

# 最大化浏览器
sleep(3)
driver.maximize_window()

# 查找用户名并输入
username = driver.find_elements_by_css_selector('.el-input__inner')[1]
username.send_keys('93300000000')
# 查找密码并输入
password = driver.find_elements_by_css_selector('.el-input__inner')[2]
password.send_keys('12345678')

# 间隔3秒，点击登录按钮
sleep(3)
driver.find_element_by_tag_name('button').click()

# 后退
sleep(3)
driver.back()

# 前进
sleep(3)
driver.forward()

# 获取title
title = driver.title
print("当前页面title为：", title)

# 获取当前url
current_url = driver.current_url
print("当前页面url为：", current_url)

# 刷新浏览器
sleep(3)
driver.refresh()

# 间隔3秒，关闭浏览器
sleep(3)
driver.quit()