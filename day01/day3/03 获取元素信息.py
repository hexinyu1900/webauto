# 导包
from time import sleep
from selenium import webdriver

# 获取浏览器对象
driver = webdriver.Chrome()

# 打开url
driver.get('https://gssdev.haoshengy.com/pc_workbench/login')

# 最大化浏览器
driver.maximize_window()

# 获取用户名文本框大小
size = driver.find_elements_by_css_selector('.el-input__inner')[1].size
print("用户名大小为：", size)

# 查找用户名并输入
username = driver.find_elements_by_css_selector('.el-input__inner')[1]
username.send_keys('93300000000')
# 查找密码并输入
password = driver.find_elements_by_css_selector('.el-input__inner')[2]
password.send_keys('12345678')

# 间隔3秒，点击登录按钮
sleep(3)
driver.find_element_by_css_selector('button').click()

# 获取页面上第一个超文本链接内容
sleep(2)
text = driver.find_elements_by_css_selector('a')[0].text
print("页面中第一个a标签为：", text)

# 获取页面上第一个超文本链接地址
sleep(2)
att = driver.find_elements_by_css_selector('a')[0].get_attribute('href')
print("页面上第一个a标签的href属性值为：", att)

# 判断span元素是否可见
display = driver.find_elements_by_css_selector('span')[0].is_displayed()
print("span元素是否可见：", display)

# 间隔3秒，关闭浏览器
sleep(3)
driver.quit()