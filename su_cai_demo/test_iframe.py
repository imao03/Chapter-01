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

url = "file:///Users/kitty/PycharmProjects/Chapter01/su_cai/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html"
driver.get(url)

"""
    目标： 为什么要切换frame表单
    需求：
        1. 打开注册实例.html
        2. 填写主页面 页面信息
        3. 填写注册A 页面信息
        4. 填写注册B 页面信息
    
"""
"""填写主页面"""
# 用户名
driver.find_element_by_css_selector("#user").send_keys("admin")
# 密码
driver.find_element_by_css_selector("#password").send_keys("admin")
# 电话
driver.find_element_by_css_selector(".tel").send_keys("18611112222")
# 邮件
driver.find_element_by_css_selector("#email").send_keys("123@qq.com")

driver.switch_to.frame("idframe1")

"""填写注册A"""
# 用户名
driver.find_element_by_css_selector("#userA").send_keys("admin")
# 密码
driver.find_element_by_css_selector("#passwordA").send_keys("admin")
# 电话
driver.find_element_by_css_selector(".telA").send_keys("18611112222")
# 邮件
driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")

# 切回默认目录
driver.switch_to.default_content()

# 切换到注册B 使用name
frame2 = driver.find_element_by_css_selector("[name='myframe2']")
driver.switch_to.frame(frame2)

"""填写注册B"""
# 用户名
driver.find_element_by_css_selector("#userB").send_keys("admin")
# 密码
driver.find_element_by_css_selector("#passwordB").send_keys("admin")
# 电话
driver.find_element_by_css_selector(".telB").send_keys("18611112222")
# 邮件
driver.find_element_by_css_selector("#emailB").send_keys("123@qq.com")

sleep(2)
driver.quit()
