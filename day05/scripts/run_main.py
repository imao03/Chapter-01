"""
    目标：unittest框架  - TestSuite使用
    操作：
        1. 导包
        2. 实例化获取 TestSuite对象
        3. 调用addTest方法添加用例 到指定套件中
"""

# 导包
import unittest

from scripts.test02 import Test02

# 实例化 suite
suite = unittest.TestSuite()

# 调用添加方法
# 写法1  类名("方法名") 注意：方法名称使用双引号
# suite.addTest(Test01("test_add"))
# suite.addTest(Test01("test_add02"))

# 扩展 添加测试类中所有test开头的方法
suite.addTest(unittest.makeSuite(Test02))

# 执行测试套件
runner = unittest.TextTestRunner()
runner.run(suite)