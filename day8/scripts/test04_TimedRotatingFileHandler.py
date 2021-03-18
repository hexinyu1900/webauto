"""
    目标：学习logging底层 模块实现
        1.logger
"""
# import logging

# 导包时导入logging.handlers  推荐原因：logging是包名，导入包名时会自动执行包下面的__init__文件，所以这样导入，相当于导入了logging
import logging.handlers

# 获取logger
# logger = logging.getLogger()

# 修改名称
logger = logging.getLogger()

# 设置级别
logger.setLevel(logging.DEBUG)

# 获取控制台 处理器
sh = logging.StreamHandler()
# 到文件 根据时间切割
th = logging.handlers.TimedRotatingFileHandler(filename="../log/logtime.log",
                                               when="M",
                                               interval=1,
                                               backupCount=3)

# 设置处理器级别
th.setLevel(logging.ERROR)

# 添加格式器
fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)]] - %(message)s"
fm = logging.Formatter(fmt)

# 将格式器添加到处理器中
sh.setFormatter(fm)
th.setFormatter(fm)

# 将处理器添加到logger
logger.addHandler(sh)
logger.addHandler(th)

# 输入信息
logging.info("info")
logging.debug("debug")
logging.error("error")
logging.warning("warning")
