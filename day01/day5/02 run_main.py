'''
    目标：unittest框架--TestSuite使用
    步骤：
        1.导包 import unittest
        2.实例化获取 TestSuite对象
        3.调用addTest方法添加用例到指定套件中
    案例：
        编写求和测试函数
'''

# 导包
import unittest
from day5.tas01_case import Test01
from day5.test02_case import Test02
# 实例化 suite
suite = unittest.TestSuite()


# 调用添加方法
# 写法1 类名("方法名")
suite.addTest(Test01('test_add'))
suite.addTest(Test01('test_add1'))

# 扩展 添加测试类中所有test开头的方法
suite.addTest(unittest.makeSuite(Test02))

# 执行测试套件
runner = unittest.TextTestRunner()
runner.run(suite)