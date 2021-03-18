"""
    目标：断言练习
    案例：
        输入：正确的用户名 密码为空
        断言：提示信息是否为“密码不能为空”
        要求：如果断言出错，截屏保存
"""

# 导包
import unittest
from selenium import webdriver
from time import sleep


# 定义测试类
class GssLogin(unittest.TestCase):
    # 定义初始化方法
    def setUp(self):
        # 获取浏览器驱动对象
        self.driver = webdriver.Chrome()
        # 打开url
        self.driver.get("https://gssdev.haoshengy.com/pc_workbench/login")
        # 最大化浏览器
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(30)

    # 定义teardown
    def tearDown(self):
        # 关闭浏览器驱动
        sleep(2)
        self.driver.quit()

    # 定义登录测试方法,密码为空
    def test_login_code_null(self):
        # 输入用户名
        self.driver.find_elements_by_css_selector('.el-input__inner')[1].send_keys('18113748898')
        # 输入密码
        self.driver.find_elements_by_css_selector('.el-input__inner')[2].send_keys(' ')
        # 点击登录
        self.driver.find_element_by_tag_name('button').click()
        # 获取登录后提示
        result = self.driver.find_element_by_css_selector('.el-notification__group.is-with-icon').text
        try:
            # 断言
            self.assertIn('账号或密码错误', result)
        except AssertionError:
            # 截图
            self.driver.get_screenshot_as_file('../image/error.png')
            # 抛异常
            raise

