#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/13 13:48
# @Author : Kitty
# @File   : test_search.py
# @SoftWare: PyCharm
import time
import unittest

from test_report_demo.base.get_driver import GetDriver
from test_report_demo.page.page_search import PageSearch
from parameterized import parameterized

from test_report_demo.tools.get_text import get_text


def get_data():
    return get_text("test_text.txt")


class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.search = PageSearch()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().driver_quit()

    @parameterized.expand(get_data())
    def test_search(self, values):
        self.search.page_search(values)

