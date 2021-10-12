# coding:UTF-8
import time
import unittest
from time import sleep

import selenium
from selenium import webdriver


class TestLogin(unittest.TestCase):

    # init
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://xdclass.net/#/index")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_css_selector(
            "#app > div > div.get_main > div > div.closed"
        ).click()

    #
    def tearDown(self) -> None:
        sleep(2)
        self.driver.quit()

    # 定义登录测试方法 验证码为空
    def testLogin(self):
        driver = self.driver
        driver.find_element_by_css_selector(
            "#app > div > div:nth-child(1) > div.header > div.r_userinfo.f_r > div.login > span:nth-child(2)"
        ).click()

        driver.find_element_by_css_selector(
            "#app > div > div:nth-child(1) > div.header > div.main > div.login > div > div.mobienum > input[type=text]"
        ).send_keys("15535160433")
        sleep(2)

        driver.find_element_by_css_selector(
            "#app > div > div:nth-child(1) > div.header > div.main > div.login > div > div.psw > input[type=password]"
        ).send_keys("li796093")
        sleep(2)

        driver.find_element_by_css_selector(
            "#app > div > div:nth-child(1) > div.header > div.main > div.login > div > div.login_btn > button"
        ).click()
        sleep(5)

        driver.get_screenshot_as_file("sc_img/{}.png".format(
            time.strftime("%Y_%m_%d_%H_%M_%S")))

    if __name__ == '__main__':
        print("")
