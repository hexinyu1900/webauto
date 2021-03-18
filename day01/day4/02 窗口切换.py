# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome()

# 打开url
driver.get('https://dev.xiaojing0.com/admin/login?staff=1111')

# 最大化浏览器
driver.maximize_window()

# 获取当前窗口句柄  -->目的：判断只要不是当前主窗口句柄，就一定是新开的窗口句柄
current_handle = driver.current_window_handle
print("当前窗口句柄为：", current_handle)

# 登录账号
driver.find_elements_by_css_selector('.el-input__inner')[0].send_keys('Molly')
driver.find_elements_by_css_selector('.el-input__inner')[1].send_keys('xiao123456')
driver.find_element_by_tag_name('button').click()

# 进入课表中心
sleep(2)
driver.find_elements_by_css_selector('.el-submenu__title')[1].click()
sleep(2)
driver.find_elements_by_css_selector('.el-menu-item')[8].click()

# 获取所有窗口句柄
handles = driver.window_handles
print("所有窗口句柄：", handles)

# 判断是否是当前窗口句柄
for h in handles:
    if h != current_handle:
        # 切换
        driver.switch_to.window(h)

# driver.find_element_by_css_selector('.el-button.el-button--default.xjl-button-item"').click()
driver.find_element_by_xpath('//button[@class="el-button el-button--default xjl-button-item"]').click()
# 暂停3秒
sleep(3)

# 退出浏览器
driver.quit()