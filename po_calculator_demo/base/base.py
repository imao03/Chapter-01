#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/1 08:52
# @Author : Kitty
# @File   : base.py
# @Software:
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 1.init
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://cal.apple886.com/")

    # 2. 查找元素的方法
    def base_find_element(self, loc, timeout=30, pull=0.5):
        return WebDriverWait(
            self.driver,
            timeout=timeout,
            poll_frequency=pull
        ).until(
            lambda x: x.find_element(*loc)
        )

    # 3. click ele
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 4. 获取文本
    def base_get_text(self, loc):
        element = self.base_find_element(loc)
        get_attribute = element.get_attribute("value")
        return get_attribute
