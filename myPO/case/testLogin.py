# 导包
from myPO.page import page_login
import unittest
from parameterized import parameterized


def get_data():
    return [("13822223333", "123456", "8888", "账号不存在!"),
            ("13800001111", "123123", "8888", "密码错误!")]


# 新建测试类并继承
class TestLogin(unittest.TestCase):

    # setUp
    def setUp(self):
        # 实例化获取页面对象PageLogin
        self.login = page_login.PageLogin()

        # 点击登录连接
        self.login.pageClickLoginLink()

    # tearDown
    def tearDown(self):
        # 关闭driver驱动对象
        self.login.driver.quit()

    # 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, userName, pwd, code, errorMsg):
        # 调用登录方法
        self.login.pageLogin(userName, pwd, code)
        # 获取登录提示信息
        self.info = self.login.pageGetErrorInfo()
        try:
            # 并断言
            self.assertEqual(self.info, errorMsg)
        except AssertionError:
            # 截图
            self.login.pageScreenShotImg()
