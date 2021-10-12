#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/1 09:03
# @Author : Kitty
# @File   : page_calc.py

from selenium.webdriver.common.by import By
from po_calculator_demo_report import page
from po_calculator_demo_report.base.base import Base
from po_calculator_demo_report.base.get_logger import GetLogger

logger = GetLogger.get_logger()


class PageCalc(Base):
    calc = None

    # 点击数字
    def page_click_num(self, num):
        logger.info("正在对{}元素进行点击".format(num))
        for i in str(num):
            loc = By.CSS_SELECTOR, "#simple{}".format(i)
            self.base_click(loc)

    # click +
    def page_click_add(self):
        logger.info("正在点击 + 元素进行点击")
        self.base_click(page.calc_add)

    def page_click_sub(self):
        logger.info("正在点击 - 元素进行点击")
        self.base_click(page.calc_sub)

    def page_click_mul(self):
        logger.info("正在点击 * 元素进行点击")
        self.base_click(page.calc_mul)

    def page_click_div(self):
        logger.info("正在点击 / 元素进行点击")
        self.base_click(page.calc_div)

    # click =
    def page_click_eq(self):
        logger.info("正在点击 = 元素进行点击")
        self.base_click(page.calc_eq)

    # get text
    def page_get_text(self):
        logger.info("正在获取元素的文本信息")
        return self.base_get_text(page.calc_result)

    def page_click_clear(self):
        logger.info("正在点击元素进行点击")
        self.base_click(page.calc_clear)

    def page_sc_img(self):
        logger.info("正在截图...")
        self.base_sc_img()

    # 业务组合
    def page_two_add(self, a, b):
        logger.info("正在{} + {} 的相加".format(a, b))
        self.page_click_clear()
        self.page_click_num(a)
        self.page_click_add()
        self.page_click_num(b)
        self.page_click_eq()

    def page_two_sub(self, a, b):
        logger.info("正在{} - {} 的相减".format(a, b))
        self.page_click_clear()
        self.page_click_num(a)
        self.page_click_sub()
        self.page_click_num(b)
        self.page_click_eq()

    def page_two_mul(self, a, b):
        logger.info("正在{} * {} 的相乘".format(a, b))
        self.page_click_clear()
        self.page_click_num(a)
        self.page_click_mul()
        self.page_click_num(b)
        self.page_click_eq()

    def page_two_div(self, a, b):
        logger.info("正在{} / {} 的相除".format(a, b))
        self.page_click_clear()
        self.page_click_num(a)
        self.page_click_div()
        self.page_click_num(b)
        self.page_click_eq()
