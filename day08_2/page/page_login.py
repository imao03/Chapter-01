#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/3 13:35
# @Author : Kitty
# @File   : page_login.py
# @Software:
from day08_2 import page
from day08_2.base.base import Base


class PageLogin(Base):

    # 点击登录链接
    def page_click_login_link(self):
        self.base_click(page.login_link)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 输入验证码
    def page_input_verify_code(self, code):
        self.base_input(page.login_verify_code, code)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 获取错误提示信息
    def page_get_error_info(self):
        info = self.page_get_error_info()
        return info

    # 点击错误提示框确定btn
    def page_error_box_btn(self):
        self.base_click(page.login_err_ok_btn)

    # 判断是否登录成功
    def page_if_login_is_ok(self):
        return self.base_ele_is_exist(page.login_logout_link)

    # 点击安全退出
    def page_click_logout_link(self):
        self.base_click(page.login_logout_link)

    # 判断是否退出成功
    def page_if_logout_is_ok(self):
        return self.base_ele_is_exist(page.login_link)

    # 业务组合方法
    def page_login(self, username, pwd, code):
        self.page_click_login_link()
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_verify_code(code)
        self.page_click_login_btn()

    # 业务组合方法 给依赖登录模块使用
    def page_login_success(self, username="13800001111", pwd="123456", code="8888"):
        self.page_click_login_link()
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_verify_code(code)
        self.page_click_login_btn()