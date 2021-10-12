from time import sleep
# 导包 webdriver
from selenium import webdriver

# 获取 火狐浏览器对象
driver = webdriver.Chrome()

# 获取 谷歌浏览器对象
# driver = webdriver.Chrome()

# 获取 Ie
# driver = webdriver.Ie()

# 打开 百度
driver.get('http://www.baidu.com')

# 暂停 3秒
sleep(3)

# 
driver.quit()
