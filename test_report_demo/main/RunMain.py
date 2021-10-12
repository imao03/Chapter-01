"""
    目标：基于unittest框架执行生成html版报告
    操作：
        1. 复制HtmlTestRunner.py文件到指定目录
        2. 导包 from HTMLTestRunner import HTMLTestRunner
        3. 获取报告存放文件流，并实例化HTMLTestRunner类，执行run方法
"""

import unittest
import time

from myHTML_report.myTools.HTMLTestRunner import HTMLTestRunner

# 定义测试套件

test_suite = unittest.defaultTestLoader.discover(
    "../case/",  # 加载的测试用例
    pattern="test*.py"
)

# 定义测试报告的文件目录和名称
reportDir = "../report/{}.html".format(
    time.strftime("%Y_%m_%d %H_%M_%S")
)

# 获取测试报告 并执行
current_time = format(time.strftime("%Y_%m_%d %H_%M_%S"))
with open(reportDir, 'wb') as f:
    HTMLTestRunner(
        stream=f,
        title="test_report_demo 项目测试报告",
        description="MacOS 操作系统"
    ).run(test_suite)
