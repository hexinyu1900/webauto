# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome()

# 打开url
driver.get('https://gssdev.haoshengy.com/pc_workbench/login')

# 查找用户名
# 绝对路径
# driver.find_element_by_xpath('/html/body/div/div/div/form/div/div/div/input').send_keys('18113748898')
# 相对路径
driver.find_element_by_xpath('''//input[@placeholder='请输入账号']''').send_keys('18113748898')

# 查找密码
driver.find_element_by_xpath('/html/body/div/div/div/form/div[2]/div/div/input').send_keys('12345678')

# 点击登录
# driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/button').click()
driver.find_element_by_tag_name('button').click()

# 暂停3秒
sleep(3)

# 退出浏览器
driver.quit()