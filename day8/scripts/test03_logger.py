"""
    目标：学习logging底层 模块实现
        1.logger
"""
import logging

# 获取logger
logger = logging.getLogger()
# 设置级别
logger.setLevel(logging.DEBUG)
# 获取控制台 处理器
sh = logging.StreamHandler()
# 将处理器添加到logger
logger.addHandler(sh)
# 输入信息
logging.info("info")
logging.debug("debug")