# 定义对象库层的父类
from version04.utils04 import Driver


class BasePage(object):

    def __init__(self):
        self.driver = Driver.get_driver()


    # 公用元素定位方法
    def find_element(self, location):
        # return self.driver.find_element(By.XPATH, "//input[@id='username']")
        return self.driver.find_element(*location)


# 定义操作层父类
class ActionPage(object):

    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)


class HandlesTools:

    def to_window(self, n):
        handles = Driver.get_driver().window_handles
        Driver.get_driver().switch_to.window(handles[n])
