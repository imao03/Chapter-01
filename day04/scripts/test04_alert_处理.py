# 导包
from selenium import webdriver
from time import sleep
# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 最大化浏览器
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(3)
# 打开url
url = "file:///Users/kitty/PycharmProjects/Chapter01/su_cai/%E6%B3%A8%E5%86%8CA.html"
driver.get(url)

"""
    需求：
        1. 点击 alert按钮
        2. 输入用户名 admin
"""
# 定位 alert按钮 并 点击
driver.find_element_by_css_selector("#alerta").click()

# 切换 到alert
# 默认返回的alert对话框对象
at = driver.switch_to.alert

# 处理 对话框
# 同意
at.accept()

# 获取文本
# print("警告信息：", at.text)

# 取消
# at.dismiss()

# 定位 用户名 输入admin
driver.find_element_by_css_selector("#userA").send_keys("admin")

# 暂停 2
sleep(2)
# 关闭驱动对象
driver.quit()