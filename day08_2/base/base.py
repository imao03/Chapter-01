#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/3 09:45
# @Author : Kitty
# @File   : base.py
# @Software:
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from day08_2 import page
from day08_2.base.get_logger import GetLogger

log = GetLogger().get_logger()


class Base:

    def __init__(self, driver):
        log.info("[base]将要获取初始化driver".format())
        self.driver = driver

    def base_find_ele(self, loc, timeout=30, poll_frequency=0.5):
        log.info("[base]正在执行查找元素{},等待时间{}".format(loc, timeout))
        return WebDriverWait(
            self.driver,
            timeout=timeout,
            poll_frequency=poll_frequency
        ).until(
            lambda x: x.find_ele(*loc)
        )

    def base_click(self, loc):
        log.info("[base]正在执行点击事件{}".format(loc))
        self.base_find_ele(loc).click()

    def base_input(self, loc, value):
        ele = self.base_find_ele(loc)
        log.info("[base]正在执行清空输入框事件{}".format(loc))
        ele.clear()
        log.info("[base]正在执行输入框事件{}".format(loc))
        ele.send_keys(value)

    def base_get_text(self, loc):
        log.info("[base]正在执行获取文本事件{}".format(loc))
        text = self.base_find_ele(loc).text
        return text

    def base_sc_img(self):
        log.info("[base]正在执行截图事件")
        self.driver.get_screenshot_as_file(
            "../image/{}.png".format(
                time.strftime("%Y_%m_%d %H_%M_%S")
            )
        )

    def base_ele_is_exist(self, loc):
        try:
            self.base_find_ele(loc, timeout=2)
            log.info("[base]:{}元素查找成功,存在于页面".format(loc))
            return True
        except:
            return False

    # ------------------------购物车base模块--------------------------------

    #   1.回到 index.html —> 购物车、下订单、支付都要用到
    def base_index(self):
        # 暂停2s,正在进行登录 就跳转 报错
        time.sleep(2)
        self.driver.get(page.URL)

    # 	2.切换到frame表单方法
    def base_switch_frame(self, name):
        self.driver.switch_to.frame(name)

    # 	3.回到默认目录方法
    def base_default_content(self):
        self.driver.switch_to.default_content()
