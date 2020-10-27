# 定义浏览器驱动的工具类
import json
import time
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

dir_path = os.path.dirname(os.path.abspath(__file__))
print(dir_path)

# 读取文件函数
def get_data(file_path):
    text_data = []
    # 打开文件
    with open(file_path, encoding="utf-8") as f:
        # 加载文件内容
        json_data = json.load(f)
        # 遍历文件
        for i in json_data.values():
            text_data.append(list(i.values()))
    print(text_data)
    return text_data


# 获取弹出框文本信息函数
def get_element_msg(xpath):
    time.sleep(3)
    try:
        msg = WebDriverWait(Driver.get_driver(), 10, 1).until(lambda x: x.find_element_by_xpath(xpath)).text
        print(msg)
        return msg
    except Exception as e:
        NoSuchElementException(f"no such element, can not find {xpath} element")


class Driver(object):
    __driver = None

    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()  # 窗口最大化
            cls.__driver.implicitly_wait(30)  # 隐式等待
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None:
            time.sleep(3)
            cls.__driver.quit()
            cls.__driver = None

# if __name__ == '__main__':
#     Driver().get_driver()
#     Driver().quit_driver()
