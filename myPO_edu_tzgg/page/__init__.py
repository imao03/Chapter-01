from selenium.webdriver.common.by import By

# 登录链接
loginLink = By.CSS_SELECTOR, "body > div.tpshop-tm-hander > div.top-hander.clearfix > div > div > div.fl.nologin > a.red"

# 用户名
loginUserName = By.CSS_SELECTOR, "#app > div > form > div:nth-child(2) > div > div > input"

# 密码
loginPassword = By.CSS_SELECTOR, '#app > div > form > div:nth-child(3) > div > div > input'

# 验证码
loginVerifyCode = By.CSS_SELECTOR, '#verify_code'

# 登录按钮
loginBtn = By.CSS_SELECTOR, '#app > div > form > div:nth-child(6) > div > button'

# 获取文本异常信息
loginTextErrorInfo = By.CSS_SELECTOR, '.layui-layer-content'

# 点击异常提示框 按钮
loginClickErrorInfoBox = By.CSS_SELECTOR, '.layui-layer-btn0'

# ---------------------
# 考试学习
menu_edu = By.CSS_SELECTOR, "#breadcrumb-container > div > div:nth-child(4) > div > div > a > div"

# 基础平台
menu_jcpt = By.CSS_SELECTOR, "#breadcrumb-container > div > div:nth-child(1) > div > div > a > div"

# 系统管理 左侧菜单栏
menu_xxgl = By.CSS_SELECTOR, "#app > div > div.sidebar-container.has-logo > div.el-scrollbar.theme-dark > div.scrollbar-wrapper.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > ul > div:nth-child(3) > li > div"

# 通知公告
menu_tzgg = By.CSS_SELECTOR, "#app > div > div.sidebar-container.has-logo > div.el-scrollbar.theme-dark > div.scrollbar-wrapper.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > ul > div:nth-child(3) > li > ul > div:nth-child(10) > a > li"

# 李泽坤测试 tabbar
menu_tabbar = By.CSS_SELECTOR, "#app > div > div.main-container.hasTagsView > section > div > div.el-row > div.el-col.el-col-4.el-col-xs-24 > div:nth-child(2) > div > div.el-tree-node.is-expanded.is-focusable > div.el-tree-node__children > div:nth-child(3) > div.el-tree-node__children > div > div.el-tree-node__children > div:nth-child(3) > div.el-tree-node__children > div:nth-child(6)"

# 新增按钮
tzgg_add_btn = By.CSS_SELECTOR, "#app > div > div.main-container.hasTagsView > section > div > div.el-row > div.el-col.el-col-20.el-col-xs-24 > div.mb8.el-row > div:nth-child(1) > button"

# 点击新增按钮后,跳转到另一个新增的标签页
tzgg_add_new_tab_page = By.CSS_SELECTOR, "#tags-view-container > div > div.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > span.tags-view-item.router-link-exact-active.router-link-active.active"

# 公告标题
tzgg_add_ggbt = By.CSS_SELECTOR, "#app > div > div.main-container.hasTagsView > section > div > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input"


# 点击选中的公告类型
tzgg_add_gglx_click = By.CSS_SELECTOR, ".vue-treeselect__control-arrow-container"

# 选中 李泽坤测试
tzgg_add_gglx_lzk_click = By.CSS_SELECTOR, ".vue-treeselect__control-arrow-container"


# 开始时间
tzgg_add_ggst = By.CSS_SELECTOR, "#app > div > div.main-container.hasTagsView > section > div > form > div:nth-child(2) > div:nth-child(1) > div > div > div > input"
# 点击开始时间
tzgg_add_ggst_input = By.CSS_SELECTOR, "body > div:nth-child(9) > div.el-picker-panel__body-wrapper > div > div.el-picker-panel__content > table.el-date-table > tbody > tr:nth-child(2) > td.available.current > div"

# 结束时间
tzgg_add_gget = By.CSS_SELECTOR, "#app > div > div.main-container.hasTagsView > section > div > form > div:nth-child(2) > div:nth-child(2) > div > div > div > input"
# 点击结束时间
tzgg_add_gget_input = By.CSS_SELECTOR, "body > div:nth-child(9) > div.el-picker-panel__body-wrapper > div > div.el-picker-panel__content > table.el-date-table > tbody > tr:nth-child(6) > td.available.current > div"

# 点击文本内容框
tzgg_click_add_input_content = By.CSS_SELECTOR, ".w-e-text"

# 输入内容
tzgg_add_input_content = By.CSS_SELECTOR, ".w-e-text"

# 点击确认按钮
tzgg_add_submit_btn = By.CSS_SELECTOR, "#app > div > div.main-container.hasTagsView > section > div > div > button.el-button.el-button--primary.el-button--medium"
