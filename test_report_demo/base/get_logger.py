#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/13 14:06
# @Author : Kitty
# @File   : get_logger.py
# @SoftWare: PyCharm
import logging.handlers


class GetLogger:
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.logger = logging.getLogger()
            cls.logger.setLevel(logging.INFO)

            sh = logging.StreamHandler()
            th = logging.handlers.TimedRotatingFileHandler(
                filename="../log/baidu.log",
                when="midnight",
                interval=1,
                backupCount=30,
                encoding="utf-8"
            )

            # 获取格式器
            fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fmt = logging.Formatter(fm)

            sh.setFormatter(fmt)
            th.setFormatter(fmt)

            cls.logger.addHandler(th)
            cls.logger.addHandler(sh)

        return cls.logger


if __name__ == '__main__':
    def xoxo():
        GetLogger().get_logger().info("xoxo")