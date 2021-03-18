# 导包
import unittest

# 定义测试类并继承
class Test02(unittest.TestCase):
    # 定义测试 注意：以test字母开头
    def test001(self):
        print("一个测试罢了")


if __name__ == '__main__':
    unittest.main()