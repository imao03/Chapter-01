# 导包
from selenium import webdriver
from time import sleep

# 获取 浏览器对象
driver = webdriver.Firefox()

# 打开url
# 注意：\反斜杠在python是转义字符  r:修饰的字符串，如果字符串中有转义字符，不进行转义使用
url = r"E:\课堂\北京\北京十期\Day01\02_其他资料\浏览器\课堂素材\注册A.html"

# 使用双反斜杠 进行转义操作
# url = "E:\\课堂\\北京\\北京十期\\Day01\\02_其他资料\\浏览器\\课堂素材\\注册A.html"

# 使用本地浏览模式 前缀必须添加 file:///
# url = "file:///E:/课堂/北京/北京十期/Day01/02_其他资料/浏览器/课堂素材/注册A.html"

# 复制浏览器地址
# url = "file:///E:/%E8%AF%BE%E5%A0%82/%E5%8C%97%E4%BA%AC/%E5%8C%97%E4%BA%AC%E5%8D%81%E6%9C%9F/Day01/02_%E5%85%B6%E4%BB%96%E8%B5%84%E6%96%99/%E6%B5%8F%E8%A7%88%E5%99%A8/%E8%AF%BE%E5%A0%82%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html"
driver.get(url)

# 查找 用户名元素
username = driver.find_element_by_id("userA")

# 查找 密码元素
password = driver.find_element_by_id("passwordA")

# 用户名输入 admin  send_keys("内容")
username.send_keys("admin")

# 密码 输入 123456
password.send_keys("123456")

# 暂停3秒
sleep(3)

# 退出浏览器驱动
driver.quit()
