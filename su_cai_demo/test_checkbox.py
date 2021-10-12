#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/10/11 17:59
# @Author : Kitty
# @File   : test_checkbox.py
# @SoftWare: PyCharm

"""
    测试多选框:若果当前为全选则全选
"""


from selenium import webdriver

from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

# 注册A.html
url = "file:///Users/kitty/PycharmProjects/Chapter01/su_cai/%E6%B3%A8%E5%86%8CA.html"
driver.get(url)


