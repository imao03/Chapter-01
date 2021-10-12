#!/usr/bin/env python3.7.9
# -*- coding:utf-8 -*-
# @Time   : 2021/9/7 09:15
# @Author : Kitty
# @File   : get_logger.py
# @SoftWare: PyCharm
# version=''
import logging.handlers


class GetLogger:
    logger = None

    @classmethod
    # 1.获取logger
    def get_logger(cls):
        # 如果logger为空
        if cls.logger is None:
            # 1、获取日志器
            cls.logger = logging.getLogger()
            # 2、设置日志器的默认级别
            cls.logger.setLevel(logging.INFO)
            # 3、获取处理器 （th，sh）
            sh = logging.StreamHandler()
            # 4、获取处理文件时间
            th = logging.handlers.TimedRotatingFileHandler(
                filename="../log/tpshop.log",
                when="midnight",
                interval=1,
                backupCount=30,
                encoding="utf-8"
            )

            # 5、获取格式器
            fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fmt = logging.Formatter(fm)

            # 6、将格式器设置在处理器中
            sh.setFormatter(fmt)
            th.setFormatter(fmt)

            # 7、将处理器添加到日志器中
            cls.logger.addHandler(th)
            cls.logger.addHandler(sh)
        # 8、返回日志器
        return cls.logger
