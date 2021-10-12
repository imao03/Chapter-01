from selenium.webdriver.common.by import By

"""计算器配置数据"""
# 加号
calc_add = By.CSS_SELECTOR, "#simpleAdd"

# 减号
calc_sub = By.CSS_SELECTOR, "#simpleSubtr"

# 乘号
calc_mul = By.CSS_SELECTOR, "#simpleMulti"

# 除号
calc_div = By.CSS_SELECTOR, "#simpleDivi"

# 等号
calc_eq = By.CSS_SELECTOR, "#simpleEqual"

# 获取计算结果
calc_result = By.CSS_SELECTOR, "#resultIpt"

# 清屏
calc_clear = By.CSS_SELECTOR, "#simpleClearAllBtn"
