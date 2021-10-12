#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/6 13:54
# @Author : Kitty
# @File   : get_driver.py
# @SoftWare: PyCharm
# version=''
from selenium import webdriver
from day08_2 import page


class GetDriver:
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(page.URL)
        return cls.driver

    @classmethod
    def driver_quit(cls):
        if cls.driver:
            cls.driver.quit()

            # 退出后,必须清空driver
            cls.driver = None


if __name__ == '__main__':
    g = GetDriver()
    g.driver_quit()
    # AttributeError: 'NoneType' object has no attribute 'quit'

    info = None
    if info:
        print("不为空")
    else:
        print("为空")
