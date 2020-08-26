import time
from common.tools import ui
from po import page
from common.globall import g

class vconference(page.Page):
    '''
    天府安逸首页第五屏：我的页面
    '''

    @ui("vconference","anyi")
    def enterVconfrence(self,assertDict=None):
        '''
        :return:进入设置页面
        '''
        self._scrollDown()
        self._click(g().get_resource_infor('我的应用视频会议'))
        if self._exists(g().get_resource_infor('安装应用确定按钮')):
            self._click(g().get_resource_infor('安装应用确定按钮'))
            time.sleep(10)
            # 点击视频客服
            self._click(g().get_resource_infor('我的应用视频会议'))
        # 等待视频会议首页
        self._wait_ui_apper(g().get_resource_infor('加入视频会议'))

    @ui("vconference")
    def enterVconfrenceFail(self,assertDict=None):
        '''
        :return:进入设置页面
        '''
        self._click(g().get_resource_infor('视频会议首页'))
        self._performAssert('视频会议首页', assertDict)

    @ui("vconference")
    def enterVconfrencesuccess(self, assertDict=None):
        '''
        :return:进入设置页面
        '''
        self._set_text(g().get_resource_infor('请输入视频会议号输入框'),'1101')
        self._click(g().get_resource_infor('视频会议首页'))
        self._click(g().get_resource_infor('呼叫'))
        if self._exists(g().get_resource_infor('证书无效')):
            self._click(g().get_resource_infor('接受'))
        time.sleep(10)
        self._performAssert('摄像头转换按钮', assertDict)

    @ui("vconference")
    def pausevideo(self, assertDict=None):
        self._click(g().get_resource_infor('摄像头转换按钮'))
        self._click((467 / 1080, 1815 / 1920))
        self._performAssert("视频已停止",assertDict)

    @ui("vconference")
    def stopVideo(self,assertDict=None):
        self._click(g().get_resource_infor('摄像头转换按钮'))
        self._click((793/1080,1798/1920))
        time.sleep(5)
        self._performAssert("视频已挂断", assertDict)

