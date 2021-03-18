import time
from selenium.webdriver.support.wait import WebDriverWait
from day7.po1.base.get_logger import get_logger
from day7.po1.base.get_logger_ok import GetLogger
from day7.po1.tool.get_log import get_logging

# log = get_logging()
# 没有使用单例
# log = get_logger()
# 使用单例
log = GetLogger().get_logger()

class Base:
    # 初始化方法
    def __init__(self, driver):
        log.info("初始化driver{}".format(driver))
        self.driver = driver

    # 查找元素
    def base_find_element(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元素的定位信息，格式为元组
        :param timeout: 默认超时时间30s
        :param poll: 访问频率，默认0.5s查找一次元素
        :return: 返回查找到的元素
        """
        # 显示等待
        log.info("正在查找元素{}".format(loc))
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击
    def base_click(self, loc):
        # 调用查找元素并进行点击
        log.info("正在点击元素{}".format(loc))
        self.base_find_element(loc).click()

    # 获取value属性方法封装
    def base_get_value(self, loc):
        # 使用get_attribute()方法获取指定的元素属性值
        log.info("正在获取元素{}value属性".format(loc))
        return self.base_find_element(loc).get_attribute("value")

    # 截图
    def base_screenshot(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))
