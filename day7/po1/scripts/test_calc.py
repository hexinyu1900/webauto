import unittest
from parameterized import parameterized
from day7.po1.base.get_logger_ok import GetLogger
from day7.po1.page.page_calc import PageCalc
from day7.po1.base.get_driver import GetDriver
from day7.po1.tool.read_json import read_json
from day7.po1.base.get_logger import get_logger

# 没有使用单例
# log = get_logger()
# 使用单例
log = GetLogger().get_logger()


def get_data():
    datas = read_json("calc.json")
    # 新建空列表
    arrs = []
    for data in datas.values():
        arrs.append((data['num1'], data['num2'], data['num3']))
    return arrs


class TestCalc(unittest.TestCase):

    # setupclass
    @classmethod
    def setUpClass(cls):
        # 获取driver
        cls.driver = GetDriver().get_driver()
        # 初始化计算页面对象
        cls.calc = PageCalc(cls.driver)

    # teardown
    @classmethod
    def tearDownClass(cls):
        # 关闭driver
        GetDriver().quit_driver()

    # 测试加法方法
    @parameterized.expand(get_data())
    def test_add_calc(self, num1, num2, num3):
        # 调用计算业务方法
        self.calc.page_add_calc(num1, num2)
        print("预期结果为：", num3, "实际结算结果为", self.calc.page_get_result() )
        try:
            # 断言
            self.assertEqual(self.calc.page_get_result(), str(num3))
        except:
            # 截图
            self.calc.page_screenshot()
            raise
