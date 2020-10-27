import logging

# 设置日志标识
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s [%(name)s] '
                           '[%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s')
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
