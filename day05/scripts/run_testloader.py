"""
    目标：演示TestLoader()类的用法
    作用：搜索指定目录下指定开头的py文件，在Py文件中搜索test开头测试方法，并且将这些方法添加到测试套件中，最后返回测试套件
    需求：
        运行 cases目录下test01.py~test05.py文件
    操作：
        1. 导包 unittest
        2. 调用TestLoader类下discaver方法
        3. 执行测试用例
"""
# 导包
import unittest
# 调用方法
# suite = unittest.TestLoader().discover("../cases")

# 扩展 指定 tpshop开头的模块
# suite = unittest.TestLoader().discover("../cases", pattern="tpshop*.py")

# 扩展 使用 推荐使用
suite = unittest.defaultTestLoader.discover("../cases")

# 执行 套件 方法 TextTestRunner
unittest.TextTestRunner().run(suite)

