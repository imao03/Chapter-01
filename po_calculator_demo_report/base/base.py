#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/1 08:52
# @Author : Kitty
# @File   : base.py
# @Software:
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from po_calculator_demo_report.base.get_driver import GetDriver
from po_calculator_demo_report.base.get_logger import GetLogger

logger = GetLogger.get_logger()


class Base:
    # 1.init
    def __init__(self):
        logger.info("[base]正在初始化driver...")
        self.driver = GetDriver.get_driver()

    # 2. 查找元素的方法
    def base_find_element(self, loc, timeout=30, pull=0.5):
        logger.info("[base]正在查找元素{},响应时间为{}".format(loc, timeout))
        return WebDriverWait(
            self.driver,
            timeout=timeout,
            poll_frequency=pull
        ).until(
            lambda x: x.find_element(*loc)
        )

    # 3. click ele
    def base_click(self, loc):
        logger.info("[base]正在对{}元素进行点击".format(loc))
        self.base_find_element(loc).click()

    # 4. 获取文本
    def base_get_text(self, loc):
        logger.info("[base]正在获取文本信息{}".format(loc))
        element = self.base_find_element(loc)
        get_attribute = element.get_attribute("value")
        return get_attribute

    # 5.截图
    def base_sc_img(self):
        logger.info("[base]正在进行截图")
        self.driver.get_screenshot_as_file(
            "../img/{}.png".format(
                time.strftime("%Y_%m_%d %H_%M_%S")
            )
        )
