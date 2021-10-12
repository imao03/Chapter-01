#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/10/9 14:11
# @Author : Kitty
# @File   : test_select.py
# @SoftWare: PyCharm
from selenium import webdriver

from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

# 注册A.html
url = "file:///Users/kitty/PycharmProjects/Chapter01/su_cai/%E6%B3%A8%E5%86%8CA.html"
driver.get(url)

"""
    默认为 北京
    暂停
    定为上海
    暂停
    定为广州
"""

sleep(2)
driver.find_element_by_css_selector("#selectA > option:nth-child(2)").click()

sleep(2)
driver.find_element_by_css_selector("#selectA > option:nth-child(3)").click()

sleep(2)

driver.quit()
