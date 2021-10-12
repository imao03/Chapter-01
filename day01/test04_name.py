# 导包
from selenium import webdriver
from time import sleep


# 获取浏览器对象
driver = webdriver.Firefox()
# 打开url
url = r"E:\课堂\北京\北京十期\Day01\02_其他资料\浏览器\课堂素材\注册A.html"
driver.get(url)

# 查找用户名 输入admin
driver.find_element_by_name("userA").send_keys("admin")
# 查找密码 输入123456
driver.find_element_by_name("passwordA").send_keys("123456")

# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()