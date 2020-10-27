import logging

# 设置日志标识
logging.basicConfig(level=logging.DEBUG, filename="../log/test.log")
logging.debug("我")
logging.info("是")
logging.warning("warning")
logging.error("error")
logging.critical("critical")