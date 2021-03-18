# 导包
import unittest
from day01.day6_2.v4.page.page_login import PageLogin
from parameterized import parameterized


# 新建测试类并继承
class TestLogin(unittest.TestCase):

    # setUp
    def setUp(self):
        # 实例化获取页面对象PageLogin
        self.login = PageLogin()

    # tearDown
    def tearDown(self):
        # 关闭driver驱动对象
        self.login.driver.quit()

    # 登录测试方法
    # @parameterized.expand([('18113748898', '11111')])
    def test_login(self):
        # 调用登录方法
        username = 18113748898
        pwd = 12345678
        self.login.page_login(username, pwd)

