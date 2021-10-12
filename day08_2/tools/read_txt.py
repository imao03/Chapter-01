#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/6 15:38
# @Author : Kitty
# @File   : read_txt.py
# @SoftWare: PyCharm
# version=''


def read_txt(filename):
    filepath = "../data/" + filename
    with open(
            filepath,
            "r",
            encoding="utf-8"
    )as f:
        return f.readlines()


if __name__ == '__main__':

    print(read_txt("login.txt"))
    arrays = []
    for data in read_txt("login.txt"):
        arrays.append(tuple(data.strip().split(",")))
    print(arrays[1:])
