#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/13 13:33
# @Author : Kitty
# @File   : get_driver.py
# @SoftWare: PyCharm
from selenium import webdriver


class GetDriver:
    driver = None

    @classmethod
    def get_driver(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://www.baidu.com")
        return cls.driver

    @classmethod
    def driver_quit(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
