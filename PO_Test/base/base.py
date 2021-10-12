from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    # 初始化方法
    def __int__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")

    # tearDown:
    def tearDown(self):
        self.driver.quit()

    # 查找元素
    def base_find_element(self, loc, timeout=30, poll_frequency=0.5):
        WebDriverWait(
            self.driver,
            timeout=timeout,
            poll_frequency=poll_frequency
        ).until(
            lambda x: x.find_element(*loc)
        )

    # click
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # input
    def base_input(self, loc, value):
        element = self.base_find_element(loc)
        element.clear()
        element.send_keys(value)

    # 获取文本
    def base_get_text(self, loc):
        text = self.base_find_element(loc).text()
        return text

    # 截图
    def base_sc_img(self):
        self.driver.get_screenshot_as_file("../image/fail.png")
