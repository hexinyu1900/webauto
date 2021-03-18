# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome()

# 打开url
driver.get('https://passport.bilibili.com/login')

# 查找用户名元素
username = driver.find_element_by_id('login-username')

# 查找密码元素
password = driver.find_element_by_id('login-passwd')

# 用户名输入 send_keys('内容')
username.send_keys('1297560025@qq.com')

# 密码输入
password.send_keys('123456')

# 暂停3秒
sleep(3)

# 退出浏览器
driver.quit()