import logging.handlers
# 创建日志器
logger = logging.getLogger()
logger.setLevel(level=logging.DEBUG)  # 设置日志级别
# 创建处理器对象
# -->输出控制台的处理器
ls = logging.StreamHandler()
# --> 输出到文件的处理器
lst = logging.handlers.TimedRotatingFileHandler(filename="../log/test.log", encoding="utf-8", )
# 创建格式化器对象
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s [%(name)s] '
                                  '[%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s')
# 添加格式化器到处理器中
ls.setFormatter(formatter)
lst.setFormatter(formatter)
# 添加处理器到日志器中
logger.addHandler(ls)
logger.addHandler(lst)
# 打印日志
logger.debug("啦啦啦啦啦啦啦")
