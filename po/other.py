import time
from common.tools import ui
from po import page
from common.globall import g

class Other(page.Page):
    '''
    除天府安逸的其他页面
    '''

    @ui("other","anyi","login","myself","setting")
    def enterLoginPage(self):   #进入欢迎回来登录页面
        '''
        :return:登录页
        '''
        #关闭天府手机银行
        self._stopTFBank()
        #运行天府手机银行
        self._startTFBank()
        #等待【主界面】出现
        time.sleep(2)
        self._wait_ui_appear(g().get_resource_infor("手机银行首页定位按钮"))        #手机银行首页
        self._click(g().get_resource_infor('主页面导航栏第五个按钮我的'))           # 点击 我的跳到登录页面
        loginUi = g().get_resource_infor('登录页面手机号')                         # 未登录-有手机号
        welcomeLoginUi = g().get_resource_infor("登录页面欢迎回来")                 # 未登录-欢迎回来

        appearUi = self._wait_multiple_ui_appear([loginUi,welcomeLoginUi])
        if appearUi==loginUi:
            self._click(g().get_resource_infor("登录页面更多登录按钮"))            # 点击 更多登录 按钮
            self._click(g().get_resource_infor("登录页面切换账户按钮"))  # 点击 切换账户

        #如果是欢迎登录页面，则直接返回登录页面
        from po.login import Login
        return Login()

    @ui("mall")
    def enterMallPage(self):
        '''
        :return: 商城页
        '''
        # # 关闭天府安逸
        # self._stopTFBank()
        # # 运行天府安逸
        # self._startTFBank()
        # 等待【商城主界面】
        self._click(g().get_resource_infor('手机银行主导航界面商城按钮'))
        from po.mall import Mall
        return Mall()

    @ui("AnYi")
    def enterContactPage(self):
        '''
        :return: 通讯录页
        '''
        # 关闭天府安逸
        self._stopTFAnYi()
        # 运行天府安逸
        self._startTFAnYi()
        # 等待【主界面】
        homeUi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_appear(homeUi)
        # 点击通讯录
        self._click(g().get_resource_infor('主页面导航栏第二个按钮通讯录'))
        from po.contact import Contact
        return Contact()

    @ui("AnYi")
    def logout(self):
        '''
        :return: 退出登录
        '''
        # 关闭天府安逸
        self._stopTFAnYi()
        # 运行天府安逸
        self._startTFAnYi()
        # 等待【主界面】
        homeUi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_appear(homeUi)
        # 点击我的
        self._click(g().get_resource_infor('主页面导航栏第五个按钮我的'))
        # 点击设置
        self._click(g().get_resource_infor('我的页面设置'))
        # 点击退出登录
        self._click(g().get_resource_infor('设置退出登录按钮'))
        # 点击确定
        self._click(g().get_resource_infor('退出登录确认按钮'))

    @ui("AnYi","attendance")
    def enterAttendancePage(self):
        '''
        :return: 我的应用页
        '''
        # 关闭天府安逸
        self._stopTFAnYi()
        # 运行天府安逸
        self._startTFAnYi()
        # 等待【主界面】
        homeUi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_appear(homeUi)
        # 点击我的应用
        self._click(g().get_resource_infor('主页面导航栏第三个按钮我的应用'))
        # 点击智能考勤
        self._click(g().get_resource_infor('我的应用智能考勤'))
        if self._exists(g().get_resource_infor('安装应用确定按钮')):
            self._click(g().get_resource_infor('安装应用确定按钮'))
            time.sleep(10)
            # 点击智能考勤
            self._click(g().get_resource_infor('我的应用智能考勤'))
        from po.attendance import Attendance
        return Attendance()

    @ui("AnYi","creditCard")
    def enterCreditCardPage(self):
        '''
        :return: 信用卡页
        '''
        # 关闭天府安逸
        self._stopTFAnYi()
        # 运行天府安逸
        self._startTFAnYi()
        # 等待【主界面】
        homeUi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_appear(homeUi)
        # 点击我的应用
        self._click(g().get_resource_infor('主页面导航栏第三个按钮我的应用'))
        # 点击信用卡
        self._click(g().get_resource_infor('我的应用信用卡'))
        time.sleep(1)
        if self._exists(g().get_resource_infor('安装应用确定按钮')):
            self._click(g().get_resource_infor('安装应用确定按钮'))
            time.sleep(10)
            # 点击信用卡
            self._click(g().get_resource_infor('我的应用信用卡'))
        elif self._exists(g().get_resource_infor('升级应用确定按钮')):
            self._click(g().get_resource_infor('升级应用确定按钮'))
            time.sleep(10)
            # 点击信用卡
            self._click(g().get_resource_infor('我的应用信用卡'))
        from po.creditCard import CreditCard
        return CreditCard()

    @ui("AnYi","OA")
    def enterOAPage(self):
        '''
        :return: OA应用页
        '''
        # 关闭天府安逸
        self._stopTFAnYi()
        # 运行天府安逸
        self._startTFAnYi()
        # 等待【主界面】
        homeUi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_appear(homeUi)
        # 点击我的应用
        self._click(g().get_resource_infor('主页面导航栏第三个按钮我的应用'))
        # 点击OA
        self._click(g().get_resource_infor('我的应用OA'))
        if self._exists(g().get_resource_infor('安装应用确定按钮')):
            self._click(g().get_resource_infor('安装应用确定按钮'))
            time.sleep(10)
            # 点击信用卡
            self._click(g().get_resource_infor('我的应用OA'))
        # 等待OA首页
        self._wait_ui_appear(g().get_resource_infor('OA首页'))
        from po.oa import OA
        return OA()

    @ui("AnYi")
    def test(self):
        '''
        测试
        :return:
        '''
        self._multiple_points_swipe(('poot(clazz="android.widget.ImageView")[0]','poot(clazz="android.widget.ImageView")[1]','poot(clazz="android.widget.ImageView")[2]'))

    @ui("anyi")
    def LaunchApp(self):
        # 关闭天府安逸
        self._stopTFAnYi()
        # 运行天府安逸
        self._startTFAnYi()

    @ui("AnYi")
    def enterMyAppPage(self):
        '''
        :return: OA应用页
        '''
        # 关闭天府安逸
        self._stopTFAnYi()
        # 运行天府安逸
        self._startTFAnYi()
        # 等待【主界面】
        homeUi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_appear(homeUi)
        # 点击我的应用
        self._click(g().get_resource_infor('主页面导航栏第三个按钮我的应用'))

    @ui("AnYi", "work")
    def enterworkPage(self):
        '''
        :return: OA应用页
        '''
        # 关闭天府安逸
        self._stopTFAnYi()
        # 运行天府安逸
        self._startTFAnYi()
        # 等待【主界面】
        homeUi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_appear(homeUi)
        # 点击我的应用
        self._click(g().get_resource_infor('主页面导航栏第四个按钮工作圈'))

if __name__ == '__main__':
    Other().enterLoginPage()


