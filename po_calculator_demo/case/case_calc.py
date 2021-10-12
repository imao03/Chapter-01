#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/1 09:59
# @Author : Kitty
# @File   : case_calc.py
# @Software:
import unittest

from parameterized import parameterized
from po_calculator_demo.page.page_calc import PageCalc


def get_data_two_add():
    return [
        (1, 1, 2),
        (1314, 520, 1834),
        (7758, 521, 8279),
        (1113, 1, 1114),
    ]


def get_data_two_sub():
    return [
        (2, 1, 1),
        (4, 2, 2),
        (888, 1, 889)
    ]


def get_data_two_mul():
    return [
        (22, 2, 44),
        (512, 2, 1024)
    ]


def get_data_two_div():
    return [
        (22, 2, 11),
        (1024, 2, 512)
    ]


class CaseCalc(unittest.TestCase):
    calc = None

    # 1.setUp
    @classmethod
    def setUpClass(cls) -> None:
        cls.calc = PageCalc()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.calc.driver.quit()

    @parameterized.expand(get_data_two_add())
    def test_calc_two_add(self, a, b, expect_result):
        self.calc.page_two_add(a, b)  # 这里是调用的计算方法
        ac_result = self.calc.page_get_text()

        print(
            "{}+{}={}".format(a, b, ac_result)
        )

        self.assertEqual(
            expect_result,
            int(ac_result)
        )

    @parameterized.expand(get_data_two_sub())
    def test_calc_two_sub(self, a, b, expect_result):
        self.calc.page_two_sub(a, b)
        ac_result = self.calc.page_get_text()

        print(
            "{}+{}={}".format(a, b, ac_result)
        )
        self.assertEqual(
            expect_result,
            int(ac_result)
        )

    @parameterized.expand(get_data_two_mul())
    def test_calc_two_mul(self, a, b, expect_result):
        self.calc.page_two_mul(a, b)
        ac_result = self.calc.page_get_text()

        print(
            "{}+{}={}".format(a, b, ac_result)
        )

        self.assertEqual(
            expect_result,
            int(ac_result)
        )

    @parameterized.expand(get_data_two_div())
    def test_calc_two_div(self, a, b, expect_result):
        self.calc.page_two_div(a, b)
        ac_result = self.calc.page_get_text()

        print(
            "{}+{}={}".format(a, b, ac_result)
        )
        self.assertEqual(
            expect_result,
            ac_result
        )
