#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/2 10:48
# @Author : Kitty
# @File   : test03_log_bottom.py
# @Software:

import logging

logger = logging.getLogger()

# Level
logger.setLevel(logging.DEBUG)

# 将处理器Handler 添加到logger中
sh = logging.StreamHandler()
logger.addHandler(sh)

logger.info("info... 凯蒂~")
logger.debug("debug...咪咪")
logger.critical("critical...米奇")
logger.error("error...明明")