from selenium.webdriver.common.by import By
"""以下为登录页面元素配置信息，临时存放地"""
# 用户名
login_username = [(By.CSS_SELECTOR, '.el-input__inner'), 1]
# 密码
login_pwd = [(By.CSS_SELECTOR, '.el-input__inner'), 2]
# 登录按钮"
login_button = [(By.TAG_NAME, 'button'),0]