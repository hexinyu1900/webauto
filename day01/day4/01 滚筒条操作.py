# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome()

# 打开url
driver.get('https://www.cnblogs.com/wangcp-2014/p/10907725.html')

# 最大化浏览器
driver.maximize_window()

# 设置js控制滚动语句
# js = 'window.scrollTo(0,1000)'
# 调用执行js语句方法
driver.execute_script('window.scrollTo(0,10000)')

# 暂停3秒
sleep(3)

# 退出浏览器
driver.quit()