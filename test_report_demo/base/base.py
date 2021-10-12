#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/13 13:37
# @Author : Kitty
# @File   : base.py
# @SoftWare: PyCharm
import time

from selenium.webdriver.support.wait import WebDriverWait

from test_report_demo.base.get_driver import GetDriver
from test_report_demo.base.get_logger import GetLogger

logger = GetLogger().get_logger()


class Base:

    @classmethod
    def __init__(cls):
        logger.info("[base]正在初始化driver....")
        cls.driver = GetDriver().get_driver()

    def base_find_element(self, loc, timeout=30, poll_frequency=0.5):
        logger.info("[base]正在查找元素{},timeout={}".format(loc, timeout))
        return WebDriverWait(
            self.driver,
            timeout=timeout,
            poll_frequency=poll_frequency
        ).until(
            lambda x: x.find_element(*loc)
        )

    def base_click(self, loc):
        logger.info("[base]正在click element{}".format(loc))
        self.base_find_element(loc).click()

    def base_input(self, loc, value):
        element = self.base_find_element(loc)
        logger.info("[base]正在clear element{}".format(loc))
        element.clear()
        logger.info("[base]正在 input element{},values={}".format(loc, value))
        element.send_keys(value)

    def base_sc_img(self):
        logger.info("[base]正在 截图")
        self.driver.get_screenshot_as_file(
            "../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S"))
        )
