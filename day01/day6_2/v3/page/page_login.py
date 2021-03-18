"""
页面对象层：
    页面对象编写技巧：
        类名：使用大驼峰命名模块名称
        方法：根据业务需求，每个操作步骤单独封装一个方法
"""
import unittest
from selenium import webdriver


class PageLogin:
    def __init__(self):
        # 获取浏览器对象
        self.driver = webdriver.Chrome()
        # 打开url
        self.driver.get('https://gssdev.haoshengy.com/pc_workbench/login')
        # 最大化浏览器
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(30)

    # 输入用户名
    def page_input_username(self, username):
        self.driver.find_elements_by_css_selector('.el-input__inner')[1].send_keys(username)

    # 输入密码
    def page_input_password(self, password):
        self.driver.find_elements_by_css_selector('.el-input__inner')[2].send_keys(password)

    # 点击登录
    def page_login_click(self):
        self.driver.find_element_by_tag_name('button').click()

    # 组合登录业务方法，给业务层调用
    def page_login(self, username, password):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_login_click()
