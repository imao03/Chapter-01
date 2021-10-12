from PO_Test.base.base import Base
from PO_Test import page


class PageLogin(Base):
    base = Base()

    # 1.封装登录链接
    def page_login_link(self):
        self.base_click(page.loginLink)

    # 2.封装UserName
    def page_input_username(self, username):
        self.base_input(page.loginUserName, username)

    # 3.封装psw
    def page_input_pwd(self, pwd):
        self.base_input(page.loginPassword, pwd)

    # 4.封装code
    def page_input_code(self, code):
        self.base_input(page.loginVerifyCode, code)

    # 5.封装登录按钮
    def page_click_login_btn(self):
        self.page_login_link()
        # 6.组合方法

    def page_login_method(self, username, pwd, code):
        self.page_login_link()
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_code(code)
        self.page_click_login_btn()
