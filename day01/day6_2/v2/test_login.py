# 导包
import unittest
from selenium import webdriver
from time import sleep


# 新建测试类并继承
class TestLogin(unittest.TestCase):
    # 初始化 setUp
    def setUp(self):
        # 获取浏览器对象
        self.driver = webdriver.Chrome()
        # 打开url
        self.driver.get('https://gssdev.haoshengy.com/pc_workbench/login')
        # 最大化浏览器
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(30)

    # 结束 tearDown
    def tearDown(self):
        # 关闭浏览器
        sleep(2)
        self.driver.quit()

    # 新建测试方法 用户名错误
    def test_login_username_not_exist(self):
        # 输入用户名
        self.driver.find_elements_by_css_selector('.el-input__inner')[1].send_keys('18512568595')
        # 输入密码
        self.driver.find_elements_by_css_selector('.el-input__inner')[2].send_keys('123')
        # 点击登录按钮
        self.driver.find_element_by_tag_name('button').click()
        # 获取错误提示信息
        msg = self.driver.find_element_by_css_selector('.el-notification__group').get_attribute('innerText')
        print(msg)
        try:
            # 断言
            self.assertIn('账号或密码错误', msg)
            # 点击提示框确定按钮
            element = self.driver.find_element_by_css_selector('.el-notification__closeBtn.el-icon-close')
            self.driver.execute_script('arguments[0].click();', element)
        except AssertionError:
            # 截图
            self.driver.get_screenshot_as_file('../image/fail.png')

    # 新建测试方法 密码错误
    def test_login_password_error(self):
        # 输入用户名
        self.driver.find_elements_by_css_selector('.el-input__inner')[1].send_keys('18113748898')
        # 输入密码
        self.driver.find_elements_by_css_selector('.el-input__inner')[2].send_keys('123')
        # 点击登录按钮
        self.driver.find_element_by_tag_name('button').click()
        # 获取错误提示信息
        msg = self.driver.find_element_by_css_selector('.el-notification__group').get_attribute('innerText')
        print(msg)
        try:
            # 断言
            self.assertIn('账号或密码错误', msg)
            # 点击提示框确定按钮
            element = self.driver.find_element_by_css_selector('.el-notification__closeBtn.el-icon-close')
            self.driver.execute_script('arguments[0].click();', element)
        except AssertionError:
            # 截图
            self.driver.get_screenshot_as_file('../image/fail_1.png')