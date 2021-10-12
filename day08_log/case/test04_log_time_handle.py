#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/2 10:48
# @Author : Kitty
# @File   : test03_log_bottom.py
# @Software:

import logging.handlers

logger = logging.getLogger()

# Level
logger.setLevel(logging.DEBUG)

# 设置格式器---给处理器-美化
fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
fm = logging.Formatter(fmt)

# 控制台处理器Handler
sh = logging.StreamHandler()

# 时间处理器Handler
th = logging.handlers.TimedRotatingFileHandler(
    filename="../log/time_log.log",
    when="midnight",
    interval=1,
    backupCount=30  # 项目开发中 一夜,30个log文件
)

# 将格式器添加到 处理器中
sh.setFormatter(fm)
th.setFormatter(fm)

# 将任务处理器Handler 添加到logger中
logger.addHandler(sh)

# 将时间处理器Handler 添加到logger中
logger.addHandler(th)

logger.info("info... 凯蒂~")
logger.debug("debug...咪咪")
logger.critical("critical...米奇")
logger.error("error...唐老鸭")
