# 导包
from selenium import webdriver
from time import sleep


# 获取浏览器对象
driver = webdriver.Firefox()
# 打开url
url = r"E:\课堂\北京\北京十期\Day01\02_其他资料\浏览器\课堂素材\注册A.html"
driver.get(url)

# 查找电话 输入 18611111111
driver.find_element_by_class_name("telA").send_keys("18611111111")


# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()