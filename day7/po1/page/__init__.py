from selenium.webdriver.common.by import By

"""以下为服务器域名配置地址"""
url = "http://tools.jb51.net/static/api/js_kexue_jsq/index.html"

"""以下为计算器配置数据"""
# 由于数字键，有一定的规律，所以暂时先不用定位此键，用到的时候再考虑怎么解决
# calc_num = By.CSS_SELECTOR, "simple"
# 加号
calc_add = By.CSS_SELECTOR, "#simpleAdd"
# 等号
calc_equal = By.CSS_SELECTOR, "#simpleEqual"
# 获取结果
calc_result = By.CSS_SELECTOR, "#resultIpt"
# 清屏
calc_clear = By.CSS_SELECTOR, "#simpleClearAllBtn"