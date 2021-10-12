import time

from myPO_edu_tzgg import page
from myPO_edu_tzgg.base.base import Base


class PageLogin(Base):

    # click login link
    def pageClickLoginLink(self):
        self.base_click(page.loginLink)

    # inputUserName
    def pageInputUserName(self, userName):
        self.base_input(page.loginUserName, userName)

    # inputPassWord
    def pageInputPassWord(self, pwd):
        self.base_input(page.loginPassword, pwd)

    # inputVerifyCode
    def pageInputVerifyCode(self, code):
        self.base_input(page.loginVerifyCode, code)

    # clickLoginBtn
    def pageClickLoginBtn(self):
        self.base_click(page.loginBtn)

    # 获取登录提示信息
    def pageGetErrorInfo(self):
        return self.base_click(page.loginTextErrorInfo)

    # 点击异常信息框 确定
    def pageClickErrorInfoBox(self):
        self.base_click(page.loginClickErrorInfoBox)

    # 截图
    def pageScreenShotImg(self):
        self.base_getScImg()

    # ------------------------------------------------------

    # 点击考试学习导航栏
    def page_click_menu_edu(self):
        self.base_click(page.menu_edu)

    # 点击基础平台菜单栏
    def page_click_menu_jcpt(self):
        self.base_click(page.menu_jcpt)

    # 系统管理 左侧菜单栏
    def page_click_menu_xxgl(self):
        self.base_click(page.menu_xxgl)

    # 点击通知公告
    def page_click_menu_tzgg(self):
        self.base_click(page.menu_tzgg)

    # 点击李泽坤测试 tabbar
    def page_click_menu_tabbar(self):
        self.base_click(page.menu_tabbar)

    # 新增按钮
    def page_click_tzgg_add_btn(self):
        self.base_click(page.tzgg_add_btn)

    # 点击新增按钮后,跳转到另一个新增的标签页
    def page_click_tzgg_add_new_tab_page(self):
        self.base_click(page.tzgg_add_new_tab_page)

    # 公告标题
    def page_input_tzgg_add_ggbt(self, values="test-913"):
        self.base_input(page.tzgg_add_ggbt, values)

    # 点击开始时间
    def page_click_tzgg_add_ggst(self):
        self.base_click(page.tzgg_add_ggst)

    # 点击选择开始时间
    def page_input_tzgg_add_ggst_input(self, tzgg_add_ggst_values="2021-9-14"):
        self.base_input(page.tzgg_add_ggst, tzgg_add_ggst_values)

    # 点击结束时间
    def page_click_tzgg_add_gget(self):
        self.base_click(page.tzgg_add_ggst)

    # 点击选择结束时间
    def page_click_tzgg_add_gget_input(self, tzgg_add_gget_values="2021-9-30"):
        self.base_input(page.tzgg_add_gget, tzgg_add_gget_values)

    # 点击文本内容框
    def page_tzgg_click_add_input_content(self):
        self.base_click(page.tzgg_click_add_input_content)

    # 输入内容
    def page_input_tzgg_add_input_content(self, tzgg_add_input_content_value="输入内容----"):
        self.base_input(page.tzgg_add_input_content, tzgg_add_input_content_value)

    # 点击确认按钮
    def page_click_tzgg_add_submit_btn(self):
        self.base_click(page.tzgg_add_submit_btn)

    # 方法的组装
    def pageLogin(self, userName, pwd):
        self.pageInputUserName(userName)
        self.pageInputPassWord(pwd)
        self.pageClickLoginBtn()

    def pageTzggAdd(self, userName, pwd, tzgg_add_ggst_values, tzgg_add_gget_values, tzgg_add_input_content_value):
        self.pageLogin(userName, pwd)
        time.sleep(5)
        self.page_click_menu_edu()
        self.page_click_menu_jcpt()
        self.page_click_menu_xxgl()
        self.page_click_menu_tzgg()
        self.page_click_menu_tabbar()
        self.page_click_tzgg_add_btn()
        self.page_click_tzgg_add_new_tab_page()

        # 输入公告标题
        self.page_input_tzgg_add_ggbt()
        self.page_click_tzgg_add_ggst()
        self.page_input_tzgg_add_ggst_input(tzgg_add_ggst_values)
        self.page_click_tzgg_add_gget()
        self.page_click_tzgg_add_gget_input(tzgg_add_gget_values)

        # 点击文本框
        self.page_tzgg_click_add_input_content()
        time.sleep(1)

        self.page_input_tzgg_add_input_content(tzgg_add_input_content_value)
        self.page_click_tzgg_add_submit_btn()
