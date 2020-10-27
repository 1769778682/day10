# 登录页面
from selenium.webdriver.common.by import By

from version04.base.base_page import BasePage, ActionPage


# 对象库层
class LoginPage(BasePage):

    def __init__(self):
        super().__init__()
        """定义浏览器驱动对象"""
        self.username = (By.XPATH, "//input[@id='username']")
        self.password = (By.XPATH, "//*[@name='password']")
        self.verify_code = (By.XPATH, "//*[@placeholder='验证码']")
        self.login = (By.XPATH, "//*[@name='sbtbutton']")

    def find_username(self):
        """查找用户名输入框"""
        return self.find_element(self.username)

    def find_password(self):
        """查找密码输入框"""
        return self.find_element(self.password)

    def find_verify_code(self):
        """查找验证码输入框"""
        return self.find_element(self.verify_code)

    def find_login(self):
        """查找登录按钮"""
        return self.find_element(self.login)


# 操作层
class LoginHandle(ActionPage):
    def __init__(self):
        """实例化驱动对象"""
        self.driver = LoginPage()

    def input_username(self, username):
        """输入用户名"""
        self.input_text(self.driver.find_username(), username)
        # self.driver.find_username().clear()
        # self.driver.find_username().send_keys(username)

    def input_password(self, password):
        """输入密码"""
        self.input_text(self.driver.find_password(), password)
        # self.driver.find_password().clear()
        # self.driver.find_password().send_keys(password)

    def input_verify_code(self, verify_code):
        """输入验证码"""
        self.input_text(self.driver.find_verify_code(), verify_code)
        # self.driver.find_verify_code().clear()
        # self.driver.find_verify_code().send_keys(verify_code)

    def click_login(self):
        """点击登录"""
        self.driver.find_login().click()


# 业务层
class LoginProxy:
    def __init__(self):
        """实例化对象"""
        self.login = LoginHandle()

    def test_login(self, username, password, verify_code):
        # 输入用户名
        self.login.input_username(username)
        # 输入密码
        self.login.input_password(password)
        # 输入验证码
        self.login.input_verify_code(verify_code)
        # 点击登录
        self.login.click_login()
