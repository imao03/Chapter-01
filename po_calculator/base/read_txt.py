#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/1 13:42
# @Author : Kitty
# @File   : read_txt.py
# @Software:

def read_txt():
    with open(
            "../data/calc.txt",
            "r",
            encoding="UTF-8"
    ) as f:
        return f.readlines()
        # 读出来是 <class 'list'>


if __name__ == '__main__':
    print(read_txt())
    print()
    # str.split(read_txt())
    # Expected type 'str', got 'List[bytes]' instead

    my_arrays = []
    for list_content in read_txt():
        my_arrays.append(tuple(list_content.strip().split(",")))

    print(my_arrays)
    print(my_arrays[1:])
