import  unittest
"""
    目标：unittest常用断言
        1.assertTrue：如果结果为True通过，否则失败
"""
class Test01(unittest.TestCase):
    def test001(self):
        flag = True

# 断言是否为True
        self.assertTrue(flag)
        # 判断两个字符串是否相等
        self.assertEqual("晚安，打工人", "晚安，打工人")
        # 判断后边的字符串是否包含前边的字符串
        self.assertIn("hello world", "hello world,hi")
        # 判断是否为None
        flag = None
        self.assertIsNone(flag)
        self.assertIsNotNone(flag)