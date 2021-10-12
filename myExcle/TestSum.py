# coding:utf-8

import unittest


def mySum(a, b):
    return a + b


class TestSum(unittest.TestCase):

    def testCase01(self):
        my_sum = mySum(1, 1)
        print('testCase01:', my_sum)

    def testCase02(self):
        a = 2
        b = 2
        my_sum = mySum(a, b)
        print("testCase02:", my_sum)

    def testCase03(self, a=3, b=3):
        print("testCase03:", mySum(a, b))


if __name__ == '__main__':
    print("main函数")
