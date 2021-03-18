# 导包
import logging


# 定义获取logging函数
def get_logging():
    fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)]] - %(message)s"
    logging.basicConfig(level=logging.INFO, filename="../log/log01.log", format=fm)
    return logging