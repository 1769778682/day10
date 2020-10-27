# 1.导包

import time
import logging
import pytest
from version04.base.base_page import HandlesTools

from version04.page.login_page import LoginProxy
from version04.utils04 import Driver, get_element_msg, get_data


class TestLogin:

    def setup_class(self):
        self.driver = Driver().get_driver()
        self.login_proxy = LoginProxy()
        self.handles = HandlesTools()

    def setup(self):
        # 3.打开测试网址       --> 输入网址
        time.sleep(1)
        self.driver.get("http://localhost/")
        # 4.业务操作,点击首页的‘登录’链接，进入登录页面
        self.driver.find_element_by_class_name("red").click()

    @pytest.mark.parametrize(('username', 'password', 'verify', 'message', "is_success"),
                             get_data("../data/login.json"))
    def test_login(self, username, password, verify, message, is_success):
        logging.info("start->proxy--->{}{}{}{}{}".format(username, password, verify, message, is_success))
        self.login_proxy.test_login(username, password, verify)
        # 6) 获取错误提示信息
        if is_success:
            logging.warning("start-catch---->result")
            msg = get_element_msg("//*[@title='退出']")
        else:
            msg = get_element_msg("//div[@id]/div[2]")
        assert message in msg

    @staticmethod
    def teardown_class():
        Driver.quit_driver()
