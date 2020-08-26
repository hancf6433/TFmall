import time

from common.globall import g
from common.tools import ui
from po import page


class Login(page.Page):
    '''
    天府手机银行的登录页面
    '''
    @ui("myself")
    def __init__(self):
        #调用父类构造方法
        super(Login, self).__init__()
        # #等待当前界面出现
        # self._wait_ui_appear(g().get_resource_infor('登录页面注册按钮'))

    # @ui("login","anyi")
    @ui("myself")
    def login(self,userName:str,pwd:str,assertDict=None):
        '''
        :return:
        '''

        #输入用户名
        self._set_text(g().get_resource_infor('登录页用户名输入框'),userName)
        #输入密码
        self._click(g().get_resource_infor('登录页密码输入框'))
        self._inputPwdForLatter(pwd)  #输入密码
        # 点击完成
        # self._click(g().get_resource_infor('密码输入完成按钮'))

        #勾选同意协议
        self._click(g().get_resource_infor("登录页同意协议按钮"))
        #点击登录
        self._click(g().get_resource_infor('登录页登录按钮'))

        if self._exists(g().get_resource_infor('登录成功不再提醒按钮')):
            self._click(g().get_resource_infor('登录成功不再提醒按钮'))
        self._performAssert('断言登录成功',assertDict)
        self._performAssert('断言登录失败',assertDict)

if __name__ == '__main__':
    Login().login()




