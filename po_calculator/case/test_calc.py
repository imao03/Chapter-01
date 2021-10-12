#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/8/31 13:51
# @Author : Kitty
# @File   : test_calc.py
# @Software:
import unittest

from parameterized import parameterized
from po_calculator.base.read_txt import read_txt
from po_calculator.page.page_calc import PageCalc


def get_data():
    data = []
    for list_content in read_txt():
        data.append(tuple(list_content.strip().split(",")))
    return data[1:]


class TestCalc(unittest.TestCase):
    calc = None

    @classmethod
    def setUpClass(cls):
        cls.calc = PageCalc()

    @classmethod
    def tearDownClass(cls):
        cls.calc.driver.quit()

    @parameterized.expand(get_data())
    def test_calc_add(self, a, b, expect_result):
        self.calc.page_two_add(a, b)
        actual_result = self.calc.page_get_result()
        print(
            "{}+{}={}".format(a, b, actual_result)
        )
        self.assertEqual(expect_result, actual_result)


"""
    @parameterized.expand(get_data())
    def test_calc_sub(self, a, b, expect_result):
        self.calc.page_two_sub(a, b)
        actual_result = self.calc.page_get_result()
        print(
            "{}+{}={}".format(a, b, int(actual_result))
        )
        self.assertEqual(
            expect_result, actual_result
        )

    @parameterized.expand(get_data())
    def test_calc_mul(self, a, b, expect_result):
        actual_result = self.calc.page_two_mul(a, b)
        print(
            "{}+{}={}".format(a, b, int(actual_result))
        )
        self.assertEqual(
            expect_result, actual_result
        )

    @parameterized.expand(get_data())
    def test_calc_div(self, a, b, expect_result):
        actual_result = self.calc.page_two_div(a, b)
        print(
            "{}+{}={}".format(a, b, int(actual_result))
        )
        self.assertEqual(
            expect_result, actual_result
        )
"""
