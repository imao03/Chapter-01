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
    需求：
        1. 点击 alert按钮
        2. 输入用户名 admin
"""

driver.find_element_by_css_selector("#alerta").click()
sleep(2)

# 切换到 alert
to_alert = driver.switch_to.alert

# to_alert.accept()
to_alert.dismiss()


driver.find_element_by_css_selector("#userA").send_keys("Kitty")

sleep(2)

driver.quit()

