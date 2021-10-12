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

    # 方法的组装
    def pageLogin(self, userName, pwd):
        self.pageInputUserName(userName)
        self.pageInputPassWord(pwd)
        self.pageClickLoginBtn()