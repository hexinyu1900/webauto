# 导包
import unittest
from parameterized import parameterized
from day01.day6_2.v3.page.page_login import PageLogin


# 新建测试类
class TestLogin(unittest.TestCase):
    # 初始化方法
    def setUp(self):
        # 获取登录页面对象
        self.login = PageLogin()

    # 结束方法
    def tearDown(self):
        # 关闭驱动对象
        self.login.driver.quit()

    # 新建测试方法
    @parameterized.expand([('18113748898', '12345678')])
    def test_login(self, username, password):
        # 调用测试登录方法
        self.login.page_login(username, password)