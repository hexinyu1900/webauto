# 导包
from selenium import webdriver
from time import sleep
# 获取driver对象
driver = webdriver.Chrome()
# 最大化浏览器
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(30)
# 打开url
driver.get('https://gssdev.haoshengy.com/pc_workbench/login')
# 输入用户名
driver.find_elements_by_css_selector('.el-input__inner')[1].send_keys('18113748898')
# 输入密码
driver.find_elements_by_css_selector('.el-input__inner')[2].send_keys('12345678')
# 点击登录按钮
driver.find_element_by_tag_name('button').click()
# 获取错误提示信息
# msg = driver.find_element_by_css_selector('.el-notification__group.is-with-icon').text     内容被隐藏，msg内容返回为空
msg = driver.find_element_by_css_selector('.el-notification__group').get_attribute('innerText')
print(msg)
# 断言
assert '账号或密码错误' in msg
# 点击提示框确定按钮
# driver.find_element_by_css_selector('.el-notification__closeBtn.el-icon-close').click()     会报错
element = driver.find_element_by_css_selector('.el-notification__closeBtn.el-icon-close')
driver.execute_script('arguments[0].click();', element)
sleep(2)
driver.close()