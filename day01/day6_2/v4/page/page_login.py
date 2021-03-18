from day01.day6_2.v4 import page
from day01.day6_2.v4.base.base import Base
from time import sleep


class PageLogin(Base):
    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_username[0], username, page.login_username[1])

    # 输入密码
    def page_input_password(self, pwd):
        self.base_input(page.login_pwd[0], pwd, page.login_pwd[1])

    # 点击登录
    def page_click_login_button(self):
        self.base_click(page.login_button[0], page.login_button[1])

    # 组合业务方法
    def page_login(self, username, pwd):
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_click_login_button()
        sleep(2)
