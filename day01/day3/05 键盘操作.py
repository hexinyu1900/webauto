# 导包
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 获取浏览器对象
driver = webdriver.Chrome()

# 打开url
driver.get('https://gssdev.haoshengy.com/pc_workbench/login')

# 最大化浏览器
driver.maximize_window()

# 定位用户名
username = driver.find_elements_by_css_selector('.el-input__inner')[1]

# 输入用户名9330000000001
username.send_keys('93300000000')

# 删除用户名1
sleep(2)
username.send_keys(Keys.BACK_SPACE)

# 全选用户名
sleep(2)
username.send_keys(Keys.CONTROL, 'a')

# 复制用户名
username.send_keys(Keys.CONTROL, 'c')

# 查找密码并输入
password = driver.find_elements_by_css_selector('.el-input__inner')[2]

# 粘贴到密码框
password.send_keys(Keys.CONTROL, 'v')

# 点击登录按钮
driver.find_element_by_css_selector('button').click()


# 间隔3秒，关闭浏览器
sleep(3)
driver.quit()