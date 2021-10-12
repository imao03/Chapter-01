# coding:utf-8

import unittest


class MyAssert(unittest.TestCase):

    def test01(self):
        flag = True
        self.assertTrue(flag)

    def test02(self):
        # 判断字符串是否相等
        self.assertEqual("xoxo", "XOXO")
        self.assertEqual("xoxo", "xoxo")

        # 包含
        self.assertIn("xo", "xoxo")


if __name__ == '__main__':
    print("...")
