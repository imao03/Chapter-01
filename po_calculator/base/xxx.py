#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/8/31 13:33
# @Author : Kitty
# @File   : xxx.py
# @File   :

# 点击数字方法
from selenium.webdriver.common.by import By


def page_click_num(num):
    for i in str(num):
        loc = By.CSS_SELECTOR, "#simple{}".format(i)
        print(loc)


page_click_num(1314)

