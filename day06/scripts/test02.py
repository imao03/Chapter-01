"""
    目标：unittest skip 与 skipif功能
    语法：
        @unittest.skip("原因")
        @unittest.skipIf(条件，原因)
"""

# 导包
import unittest

version = 30


# 新建测试类


class Test01(unittest.TestCase):

    def test01(self):
        print("test01")

    def test02(self):
        print("test02")
