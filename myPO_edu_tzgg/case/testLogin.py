# 导包
from myPO_edu_tzgg.page import page_login
import unittest
from parameterized import parameterized


def get_data():
    # userName, pwd, tzgg_add_ggst_values, tzgg_add_gget_values,tzgg_add_input_content_value
    return [('admin', 'admin123', "2021-09-09", "2021-09-30", "914-公告标题")]


# 新建测试类并继承
class TestLogin(unittest.TestCase):

    # setUp
    def setUp(self):
        # 实例化获取页面对象PageLogin
        self.login = page_login.PageLogin()

    # tearDown
    def tearDown(self):
        # 关闭driver驱动对象
        self.login.driver.quit()

    # 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, userName, pwd, tzgg_add_ggst_values, tzgg_add_gget_values, tzgg_add_input_content_value):
        # 调用登录方法

        # # 获取登录提示信息
        # self.info = self.login.pageGetErrorInfo()

        # 截图
        self.login.pageScreenShotImg()

        self.login.pageTzggAdd(userName, pwd, tzgg_add_ggst_values, tzgg_add_gget_values, tzgg_add_input_content_value)

        # 截图
        self.login.pageScreenShotImg()
