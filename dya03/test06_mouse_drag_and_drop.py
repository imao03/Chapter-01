# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器驱动对象
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
# 打开url
url = "file:///Users/kitty/PycharmProjects/Chapter01/su_cai/drop.html"
driver.get(url)

# 实例化并获取 ActionChains类
action = ActionChains(driver)
# 获取源元素
source = driver.find_element_by_css_selector("#div1")
# 获取目标元素
target = driver.find_element_by_css_selector("#div2")
sleep(2)
action.drag_and_drop(source, target).perform()

# 扩展 通过坐标偏移量执行
# action.drag_and_drop_by_offset(source, xoffset=360, yoffset=180).perform()

# 暂停 2
sleep(2)
# 关闭驱动对象
driver.quit()