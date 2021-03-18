# 导包
import time
from time import sleep
from selenium import webdriver

# 获取浏览器对象
driver = webdriver.Chrome()

# 打开url
driver.get('https://gssdev.haoshengy.com/pc_workbench/login')


# 最大化浏览器
driver.maximize_window()

# 查找用户名并输入
username = driver.find_elements_by_css_selector('.el-input__inner')[1]
username.send_keys('93300000000')
# 查找密码并输入
password = driver.find_elements_by_css_selector('.el-input__inner')[2]
password.send_keys('12345678')

# 调用截图方法
# driver.get_screenshot_as_file('./admin.png')

# 存放指定目录
# driver.get_screenshot_as_file('../image/admin.png')

# 动态获取文件名称 使用时间戳
driver.get_screenshot_as_file('../image/%s.png' % (time.strftime('%Y_%m_%d_%H_%M_%S')))

# 间隔3秒，点击登录按钮
sleep(3)
driver.find_element_by_tag_name('button').click()


# 间隔3秒，关闭浏览器
sleep(3)
driver.quit()