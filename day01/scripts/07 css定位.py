# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome()

# 打开url
driver.get('https://gssdev.haoshengy.com/pc_workbench/login')

# 查找用户名
# 使用属性选择
# driver.find_element_by_css_selector('[placeholder="请输入账号"]').send_keys('93300000000')

# 使用class选择
# input_list = driver.find_elements_by_css_selector('.el-input__inner')   # 返回一个列表
# input_list[1].send_keys('93300000000')
driver.find_elements_by_css_selector('.el-input__inner')[1].send_keys('93300000000')

# 查找密码
driver.find_elements_by_css_selector('.el-input__inner')[2].send_keys('12345678')

# 点击登录
# driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/button').click()
driver.find_element_by_tag_name('button').click()

# 暂停3秒
sleep(3)

# 退出浏览器
driver.quit()