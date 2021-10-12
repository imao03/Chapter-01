"""
    目标：基于unittest框架执行生成html版报告
    操作：
        1. 复制HtmlTestRunner.py文件到指定目录
        2. 导包 from HTMLTestRunner import HTMLTestRunner
        3. 获取报告存放文件流，并实例化HTMLTestRunner类，执行run方法
"""

import unittest
import time


# 定义测试套件
from po_calculator_demo_report.tools.HTMLTestRunner import HTMLTestRunner

test_suite = unittest.defaultTestLoader.discover(
    "../case",  # 加载的测试用例
    pattern="case_*.py"
)

# 定义测试报告的文件目录和名称
reportDir = "../htmlPaper/{}.html".format(
    time.strftime("%Y_%m_%d %H_%M_%S")
)

# 获取测试报告 并执行
with open(reportDir, 'wb') as f:
    HTMLTestRunner(
        stream=f,
        title="calculator case 正在进行 项目测试报告",
        description="操作系统:MacOS,    浏览器:Chrome浏览器"
    ).run(test_suite)
