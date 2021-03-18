"""
    目标：unittest中fixture用法
    fixture就是两个函数，这个函数可以一起使用，也可以单独使用
        1.初始化函数：def setUp()
        2.结束函数：def tearDown()

    fixture级别：
        1.函数级别
        2.类级别
        3.模块级别
"""
import unittest

def setUpmodule():
    print("setupmodule被执行")

def tearDownModule():
    print("teardownmodule被执行")

class Test03(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupclass被执行")

    @classmethod
    def tearDownClass(cls):
        print("teardownclass被执行")

    def setUp(self):
        print("setup被执行")

    def tearDown(self):
        print("teardown被执行")

    def test01(self):
        print("test01被执行")

    def test02(self):
         print("test02被执行")