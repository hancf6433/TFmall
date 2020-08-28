import time
from common.tools import ui
from po import page
from common.globall import g


class Myself(page.Page):
    '''
    天府安逸首页第五屏：我的页面
    '''

    @ui("myself","anyi")
    def enterSetting(self):
        '''
        :return:进入设置页面
        '''
        self._click(g().get_resource_infor('主页面导航栏第五个按钮我的'))

    @ui("myself")
    def entermyinfo(self,assertDict=None):
        self._click(g().get_resource_infor('我的页面我的消息按钮'))
        self._performAssert('成功进入我的消息页面', assertDict)

    @ui("myself")
    def entermycelect(self,assertDict=None):
        self._click(g().get_resource_infor('我的页面我的收藏按钮'))
        self._performAssert('成功进入我的收藏页面', assertDict)

    @ui("myself")
    def uploadfile(self,assertDict=None):
        self._click(g().get_resource_infor('我的页面我上传的文件'))
        self._performAssert('成功进入我上传的文件页面', assertDict)

    @ui("myself")
    def downloadfile(self,assertDict=None):
        self._click(g().get_resource_infor('我的页面我下载的文件'))
        self._performAssert('进入我下载的文件页面', assertDict)

    @ui("myself")
    def myAvator(self,assertDict=None):
        self._click(g().get_resource_infor('我的页面我的头像'))
        self._performAssert('成功进入个人信息页面', assertDict)
        self._performAssert('我的姓名', assertDict)

    @ui("myself")
    def myQRcode(self, assertDict=None):
        self._click(g().get_resource_infor('我的页面我的二维码'))
        self._performAssert('二维码加载成功', assertDict)
    @ui("myself")
    def changeAvator(self,assertDict=None):
        self._click(g().get_resource_infor('头像'))
        self._click(g().get_resource_infor('右上角更多按钮'))
        self._click(g().get_resource_infor('拍照'))
        time.sleep(2)
        self._click(g().get_resource_infor('拍照按钮'))
        time.sleep(2)
        self._click(g().get_resource_infor('拍照完成按钮'))
        time.sleep(1)
        self._click(g().get_resource_infor('保存'))
        time.sleep(15)
        self._performAssert('成功进入个人信息页面', assertDict)

    @ui("myself")
    def clickSettings(self, assertDict=None):
        self._click(g().get_resource_infor('点击设置按钮'))
        self._wait_ui_appear(g().get_resource_infor('安全密码'))
        self._click(g().get_resource_infor('安全密码'))
        self._click(g().get_resource_infor('手势解锁'))

    @ui("myself")
    def closesafepassword(self, assertDict=None):
        self._click(g().get_resource_infor('点击设置按钮'))
        self._wait_ui_appear(g().get_resource_infor('安全密码'))
        self._click(g().get_resource_infor('安全密码'))
        self._click(g().get_resource_infor("打开天府安逸"))

    @ui("myself")
    def setguestureLess(self, assertDict=None):
        self._wait_ui_appear(g().get_resource_infor('设置手势密码'))
        self._multiple_points_swipe(('poot(clazz="android.widget.ImageView")[0]','poot(clazz="android.widget.ImageView")[1]','poot(clazz="android.widget.ImageView")[2]'))
        self._performAssert('最少连接4个点', assertDict)

    @ui("myself")
    def setguestureFail(self, assertDict=None):
        self._wait_ui_appear(g().get_resource_infor('设置手势密码'))
        self._multiple_points_swipe(('poot(clazz="android.widget.ImageView")[0]',
                                     'poot(clazz="android.widget.ImageView")[1]',
                                     'poot(clazz="android.widget.ImageView")[2]',
                                     'poot(clazz="android.widget.ImageView")[6]'))
        self._wait_ui_appear(g().get_resource_infor('请再次绘制解锁图案'))
        self._multiple_points_swipe(('poot(clazz="android.widget.ImageView")[0]',
                                     'poot(clazz="android.widget.ImageView")[1]',
                                     'poot(clazz="android.widget.ImageView")[2]'))
        self._performAssert('请再次绘制解锁图案', assertDict)

    @ui("myself")
    def setguestureSuccess(self, assertDict=None):
        self._wait_ui_appear(g().get_resource_infor('设置手势密码'))
        self._multiple_points_swipe(('poot(clazz="android.widget.ImageView")[0]',
                                     'poot(clazz="android.widget.ImageView")[1]',
                                     'poot(clazz="android.widget.ImageView")[2]',
                                     'poot(clazz="android.widget.ImageView")[6]'))
        self._wait_ui_appear(g().get_resource_infor('请再次绘制解锁图案'))
        self._multiple_points_swipe(('poot(clazz="android.widget.ImageView")[0]',
                                     'poot(clazz="android.widget.ImageView")[1]',
                                     'poot(clazz="android.widget.ImageView")[2]',
                                     'poot(clazz="android.widget.ImageView")[6]'))
        self._performAssert('手势解码', assertDict)

    @ui("myself")
    def guestureverify(self, assertDict=None):
        #等待手势验证出现
        self._wait_ui_appear(g().get_resource_infor('手势验证'))
        self._multiple_points_swipe(('poot(clazz="android.widget.ImageView")[0]',
                                     'poot(clazz="android.widget.ImageView")[1]',
                                     'poot(clazz="android.widget.ImageView")[2]'))
        self._performAssert('手势验证', assertDict)

    @ui("myself","anyi")
    def guestureverifysuccess(self, assertDict=None):
        self._wait_ui_appear(g().get_resource_infor('手势验证'))
        self._multiple_points_swipe(('poot(clazz="android.widget.ImageView",clickable="false",index="0")',
                                     'poot(clazz="android.widget.ImageView",clickable="false",index="1")',
                                     'poot(clazz="android.widget.ImageView",clickable="false",index="2")',
                                     'poot(clazz="android.widget.ImageView",clickable="false",index="6")'))
        homeUi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_appear(homeUi)
        from po.anyi import AnYi
        return AnYi()

    @ui("myself", "anyi")
    def guestureverifyfail(self, assertDict=None):
        self._wait_ui_appear(g().get_resource_infor('手势验证'))
        self._multiple_points_swipe(('poot(clazz="android.widget.ImageView",clickable="false",index="0")',
                                     'poot(clazz="android.widget.ImageView",clickable="false",index="1")',
                                     'poot(clazz="android.widget.ImageView",clickable="false",index="2")',
                                     'poot(clazz="android.widget.ImageView",clickable="false",index="6")'))
        self._performAssert('手势验证', assertDict)

    @ui("myself", "anyi")
    def modifyguesturepassword(self, assertDict=None):
        self._wait_ui_appear(g().get_resource_infor('手势验证'))
        self._multiple_points_swipe(('poot(clazz="android.widget.ImageView",clickable="false",index="0")',
                                     'poot(clazz="android.widget.ImageView",clickable="false",index="1")',
                                     'poot(clazz="android.widget.ImageView",clickable="false",index="2")'))
        self._performAssert('手势解码', assertDict)

    @ui("myself", "anyi")
    def modifyguesturepasswordsuccess(self, assertDict=None):
        self._wait_ui_appear(g().get_resource_infor('手势验证'))
        self._multiple_points_swipe(('poot(clazz="android.widget.ImageView",clickable="false",index="0")',
                                     'poot(clazz="android.widget.ImageView",clickable="false",index="1")',
                                     'poot(clazz="android.widget.ImageView",clickable="false",index="2")',
                                     'poot(clazz="android.widget.ImageView",clickable="false",index="6")'))
        self._wait_ui_appear(g().get_resource_infor('安全密码'))
        self._click(g().get_resource_infor('手势解锁'))
        self._wait_ui_appear(g().get_resource_infor('设置手势密码'))
        self._multiple_points_swipe(('poot(clazz="android.widget.ImageView")[0]',
                                     'poot(clazz="android.widget.ImageView")[1]',
                                     'poot(clazz="android.widget.ImageView")[2]',
                                     'poot(clazz="android.widget.ImageView")[8]'))
        self._wait_ui_appear(g().get_resource_infor('请再次绘制解锁图案'))
        self._multiple_points_swipe(('poot(clazz="android.widget.ImageView")[0]',
                                     'poot(clazz="android.widget.ImageView")[1]',
                                     'poot(clazz="android.widget.ImageView")[2]',
                                     'poot(clazz="android.widget.ImageView")[8]'))
        self._performAssert('手势解码', assertDict)

    @ui("myself", "anyi")
    def newguesturepasswordsuccess(self, assertDict=None):
        self._wait_ui_appear(g().get_resource_infor('手势验证'))
        self._multiple_points_swipe(('poot(clazz="android.widget.ImageView",clickable="false",index="0")',
                                     'poot(clazz="android.widget.ImageView",clickable="false",index="1")',
                                     'poot(clazz="android.widget.ImageView",clickable="false",index="2")',
                                     'poot(clazz="android.widget.ImageView",clickable="false",index="8")'))
        homeUi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_appear(homeUi)
        from po.anyi import AnYi
        return AnYi()

    @ui("myself", "anyi")
    def swipeguesture(self, assertDict=None):
        self._wait_ui_appear(g().get_resource_infor('手势验证'))
        self._multiple_points_swipe(('poot(clazz="android.widget.ImageView",clickable="false",index="0")',
                                     'poot(clazz="android.widget.ImageView",clickable="false",index="1")',
                                     'poot(clazz="android.widget.ImageView",clickable="false",index="2")',
                                     'poot(clazz="android.widget.ImageView",clickable="false",index="8")'))
        self._wait_ui_appear(g().get_resource_infor('安全密码'))

    @ui("myself")
    def clearcache(self, assertDict=None):
        self._click(g().get_resource_infor('点击设置按钮'))
        self._wait_ui_appear(g().get_resource_infor('安全密码'))
        self._click(g().get_resource_infor('清理缓存'))
        self._click(g().get_resource_infor("清理缓存按钮"))
        self._click(g().get_resource_infor("确认清空"))