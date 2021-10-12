#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/1 09:03
# @Author : Kitty
# @File   : page_calc.py
# @Software:
from selenium.webdriver.common.by import By

import po_calculator_demo.page
from po_calculator_demo import page
from po_calculator_demo.base.base import Base


class PageCalc(Base):
    calc = None

    # 点击数字
    def page_click_num(self, num):
        for i in str(num):
            loc = By.CSS_SELECTOR, "#simple{}".format(i)
            self.base_click(loc)

    # click +
    def page_click_add(self):
        self.base_click(page.calc_add)

    def page_click_sub(self):
        self.base_click(page.calc_sub)

    def page_click_mul(self):
        self.base_click(page.calc_mul)

    def page_click_div(self):
        self.base_click(page.calc_div)

    # click =
    def page_click_eq(self):
        self.base_click(page.calc_eq)

    # get text
    def page_get_text(self):
        return self.base_get_text(page.calc_result)

    def page_click_clear(self):
        self.base_click(page.calc_clear)

    # 业务组合
    def page_two_add(self, a, b):
        self.page_click_clear()
        self.page_click_num(a)
        self.page_click_add()
        self.page_click_num(b)
        self.page_click_eq()

    def page_two_sub(self, a, b):
        self.page_click_clear()
        self.page_click_num(a)
        self.page_click_sub()
        self.page_click_num(b)
        self.page_click_eq()

    def page_two_mul(self, a, b):
        self.page_click_clear()
        self.page_click_num(a)
        self.page_click_mul()
        self.page_click_num(b)
        self.page_click_eq()

    def page_two_div(self, a, b):
        self.page_click_clear()
        self.page_click_num(a)
        self.page_click_div()
        self.page_click_num(b)
        self.page_click_eq()
