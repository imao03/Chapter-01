# coding=utf-8
"""
    抽取公共的方法
	如：初始化方法，查找元素，点击方法，输入方法，获取文本信息，截图
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化方法
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://cal.apple886.com/")

    # 查找元素方法
    def base_find(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(
            self.driver,
            timeout=timeout,
            poll_frequency=poll
        ).until(
            lambda x: x.find_element(*loc)
        )

    # 点击元素
    def base_click(self, loc):
        self.base_find(loc).click()

    # 获取 文本框值
    def base_get_value(self, loc):
        # 获取 input输入框值，必须使用value获取
        return self.base_find(loc).get_attribute("value")
