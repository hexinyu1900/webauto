"""
    目标：基于unittest框架执行生成html报告
    操作：
        1. 复制HtmlTestRunner.py文件到指定目录
        2. 导包 from HTMLTestRunner import HTMLTestRunner
        3. 获取报告存放文件流，并实例化HTMLTestRunner类，执行run方法
"""
# 导包
import unittest
import time
from day01.tools.HTMLTestRunner import HTMLTestRunner

# 定义测试套件
suite = unittest.defaultTestLoader.discover("./", pattern='test01_skip*.py')
# 定义报告存放路径及文件名称
report_dir = '../report/{}.html'.format(time.strftime('%Y_%m_%d_%H_%M_%S'))
# 获取报告文件流并执行
with open(report_dir, 'wb') as f:
    HTMLTestRunner(stream=f, verbosity=2, title="自动化测试报告", description="操作系统win10").run(suite)
