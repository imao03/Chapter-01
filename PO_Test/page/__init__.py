from selenium.webdriver.common.by import By

# 登录链接
loginLink = By.CSS_SELECTOR, "body > div.tpshop-tm-hander > div.top-hander.clearfix > div > div > div.fl.nologin > a.red"

# 用户名
loginUserName = By.CSS_SELECTOR, "#username"

# 密码
loginPassword = By.CSS_SELECTOR, '#password'

# 验证码
loginVerifyCode = By.CSS_SELECTOR, '#verify_code'

# 登录按钮
loginBtn = By.CSS_SELECTOR, '#loginform > div > div.login_bnt > a'

# 获取文本异常信息
loginTextErrorInfo = By.CSS_SELECTOR, '.layui-layer-content'

# 点击异常提示框 按钮
loginClickErrorInfoBox = By.CSS_SELECTOR, '.layui-layer-btn0'
