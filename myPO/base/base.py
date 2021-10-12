import time

from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait


class Base:

    # 定义initdriver
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost')

    # 定义公共查找元素的方法
    def base_findElement(self, loc, timeout=30, poll_frequency=0.5):
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll_frequency).until(lambda x: x.find_element(*loc))

    # 点击
    def base_click(self, loc):
        self.base_findElement(loc).click()

    # 输入
    def base_input(self, loc, value):
        elementSendKeys = self.base_findElement(loc)
        elementSendKeys.clear()
        elementSendKeys.send_keys(value)

    # 获取文本
    def base_getText(self, loc):
        elementText = self.base_findElement(loc)
        return elementText.text()

    # 截图
    def base_getScImg(self):
        self.driver.get_screenshot_as_file(
            "../sc_img/{}.png".format(
                time.strftime("%Y_%m_%d_%H_%M_%S")
            )
        )
