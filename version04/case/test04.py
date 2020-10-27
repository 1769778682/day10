# 1.导包
import time

from version04.base.base_page import HandlesTools
from version04.page.login_page import LoginProxy
from version04.utils04 import Driver, get_element_msg


class CaseLogin:

    def setup_class(self):
        self.driver = Driver().get_driver()
        self.login_proxy = LoginProxy()
        self.handles = HandlesTools()

    def setup(self):
        # 3.打开测试网址       --> 输入网址
        time.sleep(1)
        self.driver.get("http://localhost/")
        # 4.业务操作
        # 1) 点击首页的‘登录’链接，进入登录页面
        self.driver.find_element_by_class_name("red").click()
        # self.handles.to_window(-1)
        # self.driver.switch_to.window(self.driver.window_handles[-1])

    # 用户名不存在
    def test_username_not_in(self):
        self.login_proxy.test_login("13413413489", "123456", "8888")
        # 6) 获取错误提示信息
        msg = get_element_msg("//div[@id]/div[2]")
        assert "账号不存在" in msg

    def test_password(self):
        self.login_proxy.test_login("13812341234", "123457", "8888")
        # 6) 获取错误提示信息
        msg = get_element_msg("//div[@id]/div[2]")
        assert "密码错误" in msg

    @staticmethod
    def teardown_class():
        Driver.quit_driver()
