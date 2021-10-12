#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/1 15:32
# @Author : Kitty
# @File   : read_txt.py
# @Software:

def read_txt():
    with open(
            "../data/calc_add.txt",
            encoding="UTF-8"
    ) as f:
        return f.readlines()


if __name__ == '__main__':
    print(read_txt())

    arrays = []
    for data in read_txt():
        l = data.strip().split(",")
        my_tuple = tuple(l)
        append = arrays.append(my_tuple)
    arrays_ = arrays[1:]
    print(arrays_)
