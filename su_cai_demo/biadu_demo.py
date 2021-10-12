#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/10/11 14:31
# @Author : Kitty
# @File   : test_up_file.py
# @SoftWare: PyCharm

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

# 注册实例A.html
url = "https://www.baidu.com"
driver.get(url)

"""
    目标： 截屏
    方法：
        driver.get_screenshot_as_file()
    需求：
        1. 输入用户名
        2. 截图 当前目录下 admin.png
"""

driver.get(url)
driver.add_cookie(
    {
        "name": "BDUSS",
        "value": "lBzNUN1N0NGWEhMdDJxVWF-Rzlzay1IRG4xNHdMYm14OWdNT0RJflkzZDZ3M3RoRVFBQUFBJCQAAAAAAAAAAAEAAAAOSXb0RkxYX1N1bnNoaW5lAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHo2VGF6NlRhU"
    }
)

sleep(1)

driver.find_element_by_css_selector(
    "#kw"
).send_keys("kitty")

driver.find_element_by_css_selector(
    "#su"
).click()
sleep(2)

# 点击进入我的个人中心
driver.find_element_by_css_selector(
    "#user"
).click()
sleep(2)

# 获取当前窗口句柄
current_window_handle = driver.current_window_handle
print("当前窗口-个人中心的句柄:", current_window_handle)

title = driver.title
print("当前窗口-个人中心-title:", title)

# 点击关注 ".siderbar-info-title_645Y4"
driver.find_element_by_css_selector(
    ".siderbar-info-title_645Y4"
).click()
sleep(2)

# 点击收藏
# .active_JwncH
driver.find_element_by_css_selector(
    ".active_JwncH"
).click()
sleep(2)

# 切换会个人中心主界面
driver.switch_to.window(current_window_handle)
sleep(2)

# 点击关注 ".siderbar-info-title_645Y4"
driver.find_element_by_css_selector(
    ".siderbar-info-title_645Y4"
).click()
sleep(2)

sleep(10)
driver.quit()
