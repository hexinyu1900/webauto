"""
    目标：unittest skip 与 skipif功能
    语法：
        @unittest.skip("原因")
        @unittest.skipif(条件,原因)
"""

# 导包
import unittest

version = 10
# 新建测试类
# @unittest.skip("Test01方法功能暂未实现")
class Test01(unittest.TestCase):
    # 新建测试方法1
    @unittest.skip("test01方法功能暂未实现")
    def test01(self):
        print("test01")

    # 新建测试方法2
    @unittest.skipIf(version > 25, "版本大于25，跳过此用例")
    def test02(self):
        print("test02")