#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/2 10:48
# @Author : Kitty
# @File   : test03_log_bottom.py
# @Software:

# 导包
import logging.handlers
from time import sleep


def log_utils():
    logger = logging.getLogger()

    logger.setLevel(logging.DEBUG)

    # 添加格式器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
    fm = logging.Formatter(fmt)

    sh = logging.StreamHandler()
    th = logging.handlers.TimedRotatingFileHandler(
        filename="../log/until_log.log",
        when="midnight",
        interval=1,
        backupCount=30,
        encoding="UTF-8"
    )

    sh.setFormatter(fm)
    th.setFormatter(fm)

    logger.handlers.append(sh)
    logger.handlers.append(th)

    return logger


if __name__ == '__main__':
    while 1:
        logger = log_utils()
        logger.info("加利福尼亚州")
        logger.error("德克萨斯州")
        logger.warning("阿拉斯加州")
        logger.error("華盛頓州")
        logger.debug("弗洛里达州")
        sleep(1)
