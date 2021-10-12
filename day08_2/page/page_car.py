#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/15 11:21
# @Author : Kitty
# @File   : page_car.py
# @SoftWare: PyCharm
from day08_2 import page
from day08_2.base.base import Base


class PageCar(Base):

    # #1. 登录操作：
    # 	在page——login.py 中组装一个登录方法

    # # 2. 打开首页
    def page_car_open_index(self):
        # 坑:暂停两秒钟
        self.base_click(page.cart_back_index)

    # 3. 输入内容
    def page_car_input_search_content(self, values="小米手机"):
        self.base_input(page.cart_search, values)

    # # 4. 点击搜索按钮
    def page_car_click_search_btn(self):
        self.base_click(page.cart_search_btn)

    # 5.点击添加购物车 —跳转到商品详情页
    def page_car_click_add_good_car_info(self):
        self.base_click(page.cart_add_info)

    #  6. 点击添加购物车
    def page_car_click_add_good_car_btn(self):
        self.base_click(page.cart_add)

    #  7.获取添加结果
    def page_car_get_text(self):
        # 	切换frame表单
        self.base_switch_frame(self.base_find_ele(page.cart_frame_id))
        # 获取结果 并返回
        return self.base_get_text(page.cart_add_result)

    # 8.关闭窗口
    def page_car_close_window(self):
        # 回到默认目录
        self.base_default_content()
        # 关闭操作
        self.base_click(page.cart_close_window)

    # 组合调用
    def page_car_add_good(self):
        self.page_car_input_search_content()
        self.page_car_click_search_btn()
        self.page_car_click_add_good_car_info()
        self.page_car_click_add_good_car_btn()
