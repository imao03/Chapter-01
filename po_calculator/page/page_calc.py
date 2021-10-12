# coding=utf-8
from selenium.webdriver.common.by import By

from po_calculator import page
from po_calculator.base.base import Base


class PageCalc(Base):

    # 点击数字方法
    def page_click_num(self, num):
        for i in str(num):
            loc = By.CSS_SELECTOR, "#simple{}".format(i)
            self.base_click(loc)

    # 点击 加号
    def page_click_add(self):
        self.base_click(page.calc_add)

    # -
    def page_click_sub(self):
        self.base_click(page.calc_sub)

    # *
    def page_click_mul(self):
        self.base_click(page.calc_mul)

    # /
    def page_click_div(self):
        self.base_click(page.calc_div)

    # 点击 等号
    def page_click_eq(self):
        self.base_click(page.calc_eq)

    # 获取 结果方法
    def page_get_result(self):
        return self.base_get_value(page.calc_result)

    # 清屏
    def page_click_clear(self):
        self.base_click(page.calc_clear)

    # 组合业务方法
    def page_two_add(self, a, b):
        self.page_click_clear()
        self.page_click_num(a)
        self.page_click_add()
        self.page_click_num(b)
        self.page_click_eq()

    def page_two_sub(self, a, b):
        self.page_click_clear()
        self.page_click_num(a)
        self.page_click_sub()
        self.page_click_num(b)
        self.page_click_eq()

    def page_two_mul(self, a, b):
        self.page_click_clear()
        self.page_click_num(a)
        self.page_click_mul()
        self.page_click_num(b)
        self.page_click_eq()

    def page_two_div(self, a, b):
        self.page_click_clear()
        self.page_click_num(a)
        self.page_click_div()
        self.page_click_num(b)
        self.page_click_eq()


if __name__ == '__main__':
    #   5. 请合并 [1, 3, 5 ,7] 和 [2, 4, 6, 8] , 保持有序
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]

    new_list = list1 + list2
    print("sore-before:", new_list)

    new_list.sort()
    print("sore-after:", new_list)
    # 默认是降序

    new_list.sort(reverse=True)
    print("sore-after:", new_list)
