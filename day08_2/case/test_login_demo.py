#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/6 09:40
# @Author : Kitty
# @File   : test01_login.py
# @SoftWare: PyCharm
# version=''

import unittest

from day08_2.base.get_driver import GetDriver
from day08_2.page.page_login import PageLogin
from parameterized import parameterized

from day08_2.tools.read_txt import read_txt


def get_data():
    return [
        # username, pwd, code, status
        # 17891209824,123456,8888,,true
        # ,123456,8888,用户名不能为空!,false
        ("17891209824", "123456", "8888", "true"),
        ("", "123456", "8888", "false")
    ]


# 新建 登录测试类 并 继承 unittest.TestCase
class TestLogin(unittest.TestCase):

    # 新建 setupClass
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.login = PageLogin(cls.driver)
        cls.login.page_click_login_link()

    # 新建 tearDownClass
    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().driver_quit()

    # 新建 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, username, pwd, code, status):
        # 调用 组合登录方法
        self.login.page_login(username, pwd, code)

        if status == "true":
            login_ok_msg = self.login.page_if_login_is_ok()
            self.assertTrue(login_ok_msg)

            self.login.page_click_logout_link()
            self.login.page_click_login_link()

        else:
            error_info = self.login.page_get_error_info()
            print(error_info)
            self.login.page_error_box_btn()
