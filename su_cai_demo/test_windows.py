#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/10/9 17:43
# @Author : Kitty
# @File   : test_windows.py
# @SoftWare: PyCharm

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(30)

url = "file:///Users/kitty/PycharmProjects/Chapter01/su_cai/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html"
driver.get(url)

"""
    目标： 为什么要切换窗口
    需求：
        1. 打开注册实例.html
        2. 点击 注册A网页
        3. 填写 注册A网页 内容
"""

# 获取当前创库哦句柄
# 获取当前窗口句柄  -->目的：判断只要不是当前主窗口句柄，
#  就一定时新开的窗口句柄
current_window_handle = driver.current_window_handle
print("当前窗口句柄:", current_window_handle)

# 点击注册A网页
driver.find_element_by_partial_link_text("A网页").click()
# sleep(2)


# 获取所有窗口句柄
handles = driver.window_handles
print("窗口句柄:", handles)
# 窗口句柄: ['CDwindow-649A9023D2CDEEC9354E79834B971387',
# 'CDwindow-52BC35BDC8C13CB6FF0310E0894210A5']


# 判断是不是当前创库哦的句柄
for h in handles:
    if h != current_window_handle:
        driver.switch_to.window(h)

        """填写注册A"""
        # 用户名
        driver.find_element_by_css_selector("#userA").send_keys("admin")
        # 密码
        driver.find_element_by_css_selector("#passwordA").send_keys("admin")
        # 电话
        driver.find_element_by_css_selector(".telA").send_keys("18611112222")
        # 邮件
        driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")

sleep(2)
driver.quit()

"""
前有阳台
后有花园
站着S型
躺下山水画
前面波涛汹涌
后面悬崖峭壁
横看成岭侧成峰
远近高低各不同
肥不露赘瘦不露骨
曲线有致婀娜多姿
女人看了想拥有
男人看了想占有

"""
