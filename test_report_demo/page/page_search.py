#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/13 13:53
# @Author : Kitty
# @File   : page_search.py
# @SoftWare: PyCharm
import time

from test_report_demo import page
from test_report_demo.base.base import Base
from test_report_demo.base.get_logger import GetLogger

logger = GetLogger().get_logger()


class PageSearch(Base):

    def page_input_text(self, values):
        logger.info("[page]正在对元素{}输入,value{}".format(page.baidu_input, values))
        self.base_input(page.baidu_input, values)

    def page_click_search_btn(self):
        logger.info("[page]正在对元素{}点击".format(page.baidu_search_btn))
        self.base_click(page.baidu_search_btn)

    def page_sc_img(self):
        logger.info("[page] 截图")
        self.base_sc_img()

    def page_search(self, values):
        logger.info("[page] page_search 搜索操作,values={}".format(values))
        self.page_input_text(values)
        self.page_click_search_btn()
        time.sleep(2)
        self.page_sc_img()
