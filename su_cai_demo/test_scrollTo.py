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

url = "file:///Users/kitty/PycharmProjects/Chapter01/su_cai/%E6%B3%A8%E5%86%8CA.html"
driver.get(url)

"""
    滚动条操作:
      
    需求：
        1. 启动暂停2秒
        2. 滚动条拉倒最底下
"""

sleep(2)

# 1.设置就是 控制滚动条语句
js = "window.scrollTo(0,10000)"

# 2.调用执行js
driver.execute_script(js)

sleep(2)
driver.quit()
