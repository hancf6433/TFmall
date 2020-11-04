from common.globall import g
from common.tools import ui
from po import page
import time


class EnterLoginPage(page.Page):
    '''
    进入天府手机银行登录页面
    '''
    @ui("myself","mall")
    def  enterLoginPage(self):
        '''
        :return:登录页
        '''
        #关闭天府手机银行
        self._stopTFBank()
        #运行天府手机银行
        self._startTFBank()
        #等待【主界面】出现
        time.sleep(3)
        self._wait_ui_appear(g().get_resource_infor("手机银行首页定位按钮"))        #手机银行首页

        #self._click(g().get_resource_infor('手机银行主导航界面我的按钮'),focus=(0.8, 0.5))          # 点击 我的跳到登录页面
        time.sleep(3)
        #self._wait_ui_appear(g().get_resource_infor("手机银行主导航界面我的按钮"))
        #self._click(g().get_resource_infor('手机银行首页退出按钮'))
        self._click((0.909,2063/2244))
        loginUi = g().get_resource_infor('登录页面手机号')                         # 未登录-有手机号
        welcomeLoginUi = g().get_resource_infor("登录页面欢迎回来")                 # 未登录-欢迎回来

        appearUi = self._wait_multiple_ui_appear([loginUi,welcomeLoginUi])
        if appearUi==loginUi:
            self._click(g().get_resource_infor("登录页面更多登录按钮"))            # 点击 更多登录 按钮
            self._click(g().get_resource_infor("登录页面切换账户按钮"))  # 点击 切换账户

        #如果是欢迎登录页面，则直接返回登录页面
        return Login()

class Login(page.Page):
    '''
    天府手机银行的登录页面
    '''
    @ui("myself","mall")
    def __init__(self):
        #调用父类构造方法
        super(Login, self).__init__()
        # #等待当前界面出现
        # self._wait_ui_appear(g().get_resource_infor('登录页面注册按钮'))

    @ui("myself","mall")
    def login(self,userName:str,vagueUserName:str,pwd:str,assertDict=None):
        '''
        :return:
        '''

        # 关闭天府手机银行
        self._stopTFBank()
        # 运行天府手机银行
        self._startTFBank()
        # 等待【主界面】出现
        time.sleep(4)
        self._wait_ui_appear(g().get_resource_infor('手机银行首页定位按钮'))  # 手机银行首页
        time.sleep(3)
        #self._click(g().get_resource_infor('手机银行首页退出按钮'))
        self._click((0.909, 2063 / 2244))        #点击手机银行主页面“我的”按钮

        # loginUi = g().get_resource_infor('登录页面手机号')  # 未登录-有手机号
        # welcomeLoginUi = g().get_resource_infor("登录页面欢迎回来")  # 未登录-欢迎回来
        #
        # appearUi = self._wait_multiple_ui_appear([loginUi, welcomeLoginUi])
        # if appearUi == loginUi:
        #     self._click(g().get_resource_infor("登录页面更多登录按钮"))  # 点击 更多登录 按钮
        #     self._click(g().get_resource_infor("登录页面切换账户按钮"))  # 点击 切换账户
        exisitAccount = self._get_text(g().get_resource_infor('登录页面已存账号'))
        print("--------------------")
        print(exisitAccount)
        print("--------------------")

        if not exisitAccount == vagueUserName:
            self._set_text(g().get_resource_infor('登录页用户名输入框'),userName)
        #输入密码
        self._click(g().get_resource_infor('登录页密码输入框'))
        self._inputPwdForLatter(pwd)  #输入密码
        # 点击完成
        # self._click(g().get_resource_infor('密码输入完成按钮'))

        #勾选同意协议
        if not exisitAccount == "185****0096":
            self._click(g().get_resource_infor("登录页同意协议按钮"))
        #点击登录
        self._click(g().get_resource_infor('登录页登录按钮'))

        if self._exists(g().get_resource_infor('登录成功不再提醒按钮')):
            self._click(g().get_resource_infor('登录成功不再提醒按钮'))
        #self._click((0.909, 2063 / 2244))        #点击手机银行主页面“我的”按钮
        #time.sleep(2)

        self._performAssert('断言登录成功',assertDict)
