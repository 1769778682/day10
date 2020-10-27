import logging.handlers

# 创建日志器
import time

logger = logging.getLogger("mylogger")
logger.setLevel(level=logging.DEBUG)
# 创建处理器
log1 = logging.StreamHandler()
log2 = logging.handlers.TimedRotatingFileHandler(
    filename="../log/test_01.log", when="M", interval=1, backupCount=2, encoding="utf-8")

# 创建格式化器
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s [%(name)s] '
                                  '[%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s')

# 给处理器设置
log1.setFormatter(formatter)
log2.setFormatter(formatter)

logger.addHandler(log1)
logger.addHandler(log2)
while True:
    logger.debug("哈哈哈哈哈！！！！！！！")
    time.sleep(1)
