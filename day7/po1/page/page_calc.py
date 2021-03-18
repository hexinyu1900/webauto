from day7.po1.base.base import Base
from selenium.webdriver.common.by import By
from day7.po1 import page


class PageCalc(Base):

    # 点击数字方法
    def page_click_number(self, num):
        for n in str(num):
            # 拆开单个按钮的定位方式
            loc = By.CSS_SELECTOR, "#simple{}".format(n)
            self.base_click(loc)

    # 点击加号
    def page_click_add(self):
        self.base_click(page.calc_add)

    # 点击等号
    def page_click_eq(self):
        self.base_click(page.calc_equal)

    # 获取结果方法
    def page_get_result(self):
        return self.base_get_value(page.calc_result)

    # 点击清屏
    def page_click_clear(self):
        self.base_click(page.calc_clear)

    # 截屏
    def page_screenshot(self):
        self.base_screenshot()

    # 组装加法业务方法
    def page_add_calc(self, num1, num2):
        self.page_click_number(num1)
        self.page_click_add()
        self.page_click_number(num2)
        self.page_click_eq()

