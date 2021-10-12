#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/1 09:59
# @Author : Kitty
# @File   : case_calc.py
# @Software:
import unittest

from parameterized import parameterized

from po_calculator_demo_report.base.get_logger import GetLogger
from po_calculator_demo_report.page.page_calc import PageCalc
from po_calculator_demo_report.base.get_driver import GetDriver
from po_calculator_demo_report.tools.read_txt import read_txt

logger = GetLogger().get_logger()


def get_data_two_add():
    arrays = []
    for data in read_txt():
        arrays.append(tuple(data.strip().split(",")))
    return arrays[1:]


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

    # 1.setUp
    @classmethod
    def setUpClass(cls) -> None:
        try:
            cls.driver = GetDriver().get_driver()
            cls.calc = PageCalc()
        except Exception as e:
            logger.info("截图报错:".format(e))
            cls.calc.page_sc_img()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().driver_quit()

    @parameterized.expand(get_data_two_add())
    def test_calc_two_add(self, a, b, expect_result):
        try:
            self.calc.page_two_add(a, b)  # 这里是调用的计算方法
            ac_result = self.calc.page_get_text()

            print(
                "{}+{}={}".format(a, b, ac_result)
            )

            try:
                self.assertEqual(
                    expect_result, ac_result
                )
            except Exception as e:
                logger.info("断言报错{}:".format(e))
                self.assertEqual(
                    expect_result,
                    ac_result
                )

        except Exception as e:
            logger.info("截图报错{}:".format(e))
            self.calc.base_sc_img()

    @parameterized.expand(get_data_two_sub())
    def test_calc_two_sub(self, a, b, expect_result):
        try:
            self.calc.page_two_sub(a, b)
            ac_result = self.calc.page_get_text()

            print(
                "{}+{}={}".format(a, b, ac_result)
            )

            try:
                self.assertEqual(
                    expect_result,
                    int(ac_result)
                )
            except Exception as e:
                logger.info("断言报错{}:".format(e))

        except Exception as e:
            logger.info("截图报错{}:".format(e))
            self.calc.base_sc_img()

    @parameterized.expand(get_data_two_mul())
    def test_calc_two_mul(self, a, b, expect_result):

        try:
            self.calc.page_two_mul(a, b)
            ac_result = self.calc.page_get_text()

            print(
                "{}+{}={}".format(a, b, ac_result)
            )
            try:
                self.assertEqual(
                    expect_result,
                    int(ac_result)
                )
            except Exception as e:
                logger.info("断言报错{}:".format(e))

        except Exception as e:
            logger.info("截图报错{}:".format(e))
            self.calc.base_sc_img()

    @parameterized.expand(get_data_two_div())
    def test_calc_two_div(self, a, b, expect_result):
        try:
            self.calc.page_two_div(a, b)
            ac_result = self.calc.page_get_text()

            print(
                "{}+{}={}".format(a, b, ac_result)
            )
            try:
                self.assertEqual(
                    expect_result,
                    int(ac_result)
                )
            except Exception as e:
                logger.info("断言报错{}:".format(e))

        except Exception as e:
            logger.info("截图报错{}:".format(e))
            self.calc.base_sc_img()
