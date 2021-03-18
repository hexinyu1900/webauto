from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    # 初始化
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://gssdev.haoshengy.com/pc_workbench/login')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    # 查找元素方法（提供：点击、输入、获取文本）使用
    def base_find_element(self, loc, num, timeout=5, poll=0.5):
        # 使用显示等待
        '''
        :param loc: 元素的配置信息，格式为元组，如：login_link = By.PartialLink, "登录"
        :param num:
        :param timeout: 默认超时时间为10，可以通过传入参数进行修改
        :param poll: 默认访问频率0.5秒
        :return: 查找到的元素
        '''
        z = WebDriverWait(self.driver,
                          timeout=timeout,
                          poll_frequency=poll).until(lambda x: x.find_elements(*loc))
        # print(z[40])
        return z[num]

    # 点击方法
    def base_click(self, loc, num):
        self.base_find_element(loc, num).click()

    # 输入方法
    def base_input(self, loc, value, num):
        el = self.base_find_element(loc, num)
        # 清空
        # el.clear()
        # 输入
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc, num):
        return self.base_find_element(loc, num).text

    # 截图方法
    def base_get_image(self):
        self.driver.get_screenshot_as_file('../image/fail.png')
