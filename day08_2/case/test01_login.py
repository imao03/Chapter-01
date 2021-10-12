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
    arrays = []
    for data in read_txt("login.txt"):
        arrays.append(tuple(data.strip().split(",")))
    return arrays[1:]


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
        GetDriver.driver_quit()

    # 新建 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, username, pwd, code, expect_result, status):
        try:
            # 2.调用登录组合业务方法
            self.login.page_login(username, pwd, code)

            # 3.判断是否为正向用例
            if status == 'true':
                try:
                    # 获取登陆成功的 提示信息
                    assert_msg = self.login.page_if_login_is_ok()
                    # 断言是否成功
                    self.assertTrue(assert_msg)

                except Exception as e:
                    self.login.base_sc_img()

                # 点击安全退出
                self.login.page_click_logout_link()
                # 点击登录链接
                self.login.page_click_login_link()

            # 逆向用例：
            else:
                # 获取错误提示信息
                error_info = self.login.page_get_error_info()
                # print("error_info:", error_info)

                try:
                    self.assertEqual(error_info, expect_result)

                except Exception as e:
                    self.login.base_sc_img()
                    # 点击错误提示框中的确认按钮
                self.login.page_error_box_btn()

        except Exception as e:
            self.login.base_sc_img()