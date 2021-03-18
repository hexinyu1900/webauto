# 导包
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 获取浏览器对象
driver = webdriver.Chrome()
# 实例化并获取ActionChains类
action = ActionChains(driver)

# 打开url
driver.get('https://gssdev.haoshengy.com/pc_workbench/login')

# 最大化浏览器
driver.maximize_window()

# 定位用户名，右击鼠标   预期：粘贴
username = driver.find_elements_by_css_selector('.el-input__inner')[1]
action.context_click(username).perform()

# 查找用户名并输入
username.send_keys('93300000000')

# 双击用户名    预期：选择
action.double_click(username).perform()

# 查找密码并输入
password = driver.find_elements_by_css_selector('.el-input__inner')[2]
password.send_keys('12345678')

# 点击登录按钮
driver.find_element_by_css_selector('button').click()


# 悬停
sleep(3)
action = ActionChains(driver)
hover = driver.find_element_by_css_selector('.role-names-button')
action.move_to_element(hover).perform()
# stop.click()

# 间隔3秒，关闭浏览器
sleep(3)
driver.quit()