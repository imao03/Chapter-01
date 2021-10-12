# coding:UTF-8

import unittest

from parameterized import parameterized

"""
    问题：
        如果有三组数据需要测试？
        [(1,1,2), (1,2,3), (0,3,3)]
"""


def add(x, y):
    return x + y


def get_data():
    return [(1, 2, 3), (3, 0, 3), (2, 1, 3)]


# 定义测试类,并集成
class Test01(unittest.TestCase):

    @parameterized.expand(get_data())
    def test_add(self, a, b, expect):
        result = add(a, b)
        assert result == expect

    def testStr_Int(self):
        print("")
        i = 10
        s = str(i)
        print(s)

        s = '1'
        i = int(s)
        print(i)


if __name__ == '__main__':
    print("")
