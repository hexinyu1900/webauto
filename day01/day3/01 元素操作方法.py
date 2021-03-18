# 导包
from time import sleep
from selenium import webdriver

# 获取浏览器对象
driver = webdriver.Chrome()

# 打开url
driver.get('https://gssdev.haoshengy.com/pc_workbench/login')

# 查找用户名并输入
username = driver.find_elements_by_css_selector('.el-input__inner')[1]
username.send_keys('93300000000')
# 查找密码并输入
password = driver.find_elements_by_css_selector('.el-input__inner')[2]
password.send_keys('12345678')

# 间隔3秒，修改电话号码
sleep(3)
username.clear()
username.send_keys('18113748898')

# 间隔3秒，点击注册按钮
sleep(3)
driver.find_element_by_tag_name('button').click()

# 间隔3秒，关闭浏览器
sleep(3)
driver.quit()