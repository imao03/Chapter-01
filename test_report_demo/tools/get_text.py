#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/13 14:07
# @Author : Kitty
# @File   : get_text.py
# @SoftWare: PyCharm

def get_text(filename):
    filepath = "../data/" + filename
    with open(
            filepath,
            "r",
            encoding="utf-8"
    ) as f:
        return f.readlines()


if __name__ == '__main__':
    text = get_text("test_text.txt")
    print(text)
    print("* *" * 50)

    arrays_xo = []
    for data in get_text("test_text.txt"):
        str_tup = tuple(data.strip().split(","))
        arrays_xo.append(str_tup)

    print(arrays_xo[0:])
    print(str(text))
    print(type(str(text)))

    for data in get_text("test_text.txt"):
        print(data)