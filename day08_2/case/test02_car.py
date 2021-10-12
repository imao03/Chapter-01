#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/15 13:52
# @Author : Kitty
# @File   : test02_car.py
# @SoftWare: PyCharm

import unittest

from day08_2.base.get_driver import GetDriver
from day08_2.page.page_car import PageCar
from day08_2.page.page_login import PageLogin


class TestCar(unittest.TestCase):

    def setUp(self):
        # 获取driver
        self.driver = GetDriver().get_driver()
        # 1.实例化PageCar
        self.car = PageCar(self.driver)
        # 调用成功登录的依赖
        PageLogin(self.driver).page_login_success()
        # 跳转到首页 坑~
        self.car.base_index()

    def tearDown(self):
        GetDriver().get_driver()

    def test_car(self):
        # 调用组合添加购物车的方法
        self.car.page_car_add_good()
        # 断言是否成功
        get_text = self.car.page_car_get_text()
        self.assertEqual(get_text, "添加成功")
        # 关闭窗口
        self.car.page_car_close_window()
