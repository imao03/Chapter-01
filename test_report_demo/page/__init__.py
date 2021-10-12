#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/13 13:49
# @Author : Kitty
# @File   : __init__.py
# @SoftWare: PyCharm

from selenium.webdriver.common.by import By

# 输入框
baidu_input = By.CSS_SELECTOR, "#kw"

# 点击百度一下
baidu_search_btn = By.CSS_SELECTOR, "#su"
