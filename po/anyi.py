from common.tools import ui, tools
from po import page
from common.globall import g
import time


class AnYi(page.Page):
    '''
    天府安逸首页第一屏
    '''

    @ui("AnYi")
    def enterMyself(self):
        '''
        :return:点击我的
        '''
        self._click(g().get_resource_infor('主页面导航栏第五个按钮我的'))

    @ui("AnYi")
    def scan(self,assertDict=None):
        '''
        :return: 点击扫一扫
        '''
        self._click(g().get_resource_infor('安逸页面扫一扫按钮'))
        self._performAssert('断言启动扫一扫成功',assertDict)
        self._click_back()

    @ui("AnYi")
    def sendMessage(self,sendTo):
        '''
        :return: 发送消息
        '''
        #点击添加
        self._click(g().get_resource_infor('安逸页面添加按钮'))
        #点击添加联系人
        self._click(g().get_resource_infor('添加联系人按钮'))
        #点击按姓名查找
        self._click(g().get_resource_infor('按姓名查找按钮'))
        #输入姓名
        self._click(g().get_resource_infor('按姓名查找输入框'))
        self._text(sendTo)
        #点击查找
        self._click(g().get_resource_infor('查找按钮'))
        self._wait_ui_apper(g().get_resource_infor('查找用户'))
        self._click(g().get_resource_infor('查找用户'))
        #点击发消息
        time.sleep(2)
        self._click(g().get_resource_infor('发消息按钮'))

    @ui("AnYi")
    def sendLinkMessage(self):
        '''
        :return: 发送链接消息
        '''
        # 点击消息输入框
        self._click(g().get_resource_infor('消息输入框'))
        self._text('http://www.baidu.com')
        # 点击发送
        self._click(g().get_resource_infor('消息发送按钮'))

    @ui("AnYi")
    def sendTextMessage(self,sendContent,assertDict=None):
        '''
        :param sendTo:
        :param assertDict:
        :return: 发送文本消息
        '''
        # 点击消息输入框
        self._click(g().get_resource_infor('消息输入框'))
        self._text(sendContent)
        # 点击发送
        self._click(g().get_resource_infor('消息发送按钮'))
        self._performAssert('发送的文本消息', assertDict)
        # self._click_back()
        # self._click_back()

    @ui("AnYi")
    def sendExpressionMessage(self,assertDict=None):
        '''
        :return: 发送表情消息
        '''
        # 点击表情图标
        self._click(g().get_resource_infor('表情图标'))
        #点击要发送的表情
        self._text('/::)')
        # 点击发送
        self._click(g().get_resource_infor('消息发送按钮'))
        self._performAssert('断言发送表情消息成功', assertDict)
        self._click_back()
        self._click_back()

    @ui("AnYi")
    def sendVoiceMessage(self,assertDict=None):
        '''
        :param sendTo:
        :param assertDict:
        :return: 发送语音消息
        '''
        #点击语音图标
        self._click(g().get_resource_infor('语音图标'))
        #长按按住说话
        self._click(g().get_resource_infor('按住说话按钮'),times=3)
        time.sleep(2)
        self._performAssert('断言发送语音消息成功',assertDict)
        self._click_back()

    @ui("AnYi")
    def sendPictureMessage(self,assertDict=None):
        '''
        :param sendTo:
        :param assertDict:
        :return: 发送语音消息
        '''
        # 点击+号
        self._click(g().get_resource_infor('聊天界面加号图标'))
        self._wait_ui_apper(g().get_resource_infor('聊天界面拍摄按钮'))
        #点击拍摄
        self._click(g().get_resource_infor('聊天界面拍摄按钮'),focus=(0.5,-0.5))
        #等待拍照按钮出现，出现后点击
        #如果还是出错
        #采用固定坐标点击的方式
        self._flushUiTree()
        self._click(g().get_resource_infor('手机自带相机拍照按钮'))
        #点击拍摄页确定按钮
        self._click(g().get_resource_infor('拍摄页确定按钮'))
        self._performAssert('断言发送图片消息成功', assertDict)
        self._click_back()
        self._click_back()

    @ui("AnYi")
    def sendVideoMessage(self,assertDict=None):
        '''
        :param sendTo:
        :param assertDict:
        :return: 发送视频消息
        '''
        #初始化
        tools.pushInitFile()
        # 点击+号
        self._click(g().get_resource_infor('聊天界面加号图标'))
        #点击录像按钮
        self._click(g().get_resource_infor('聊天界面录像按钮'),focus=(0.5,-0.5))
        #点击录像
        self._click(g().get_resource_infor('手机自带相机录像按钮'))
        self._wait_ui_apper(g().get_resource_infor('手机自带相机停止录像按钮'))
        #点击停止录像
        self._click(g().get_resource_infor('手机自带相机停止录像按钮'))
        #点击发送
        self._wait_ui_apper(g().get_resource_infor('录像页发送按钮'))
        self._click(g().get_resource_infor('录像页发送按钮'))
        #等待发送成功
        self._wait_ui_apper(g().get_resource_infor('发送的视频消息'))
        self._performAssert('断言发送视频消息成功', assertDict)
        self._click_back()
        self._click_back()

    @ui("AnYi")
    def sendFileMessage(self,assertDict=None):
        '''
        :param sendTo:
        :param assertDict:
        :return: 发送文件消息
        '''
        # 初始化
        tools.pushInitFile()
        # 点击+号
        self._click(g().get_resource_infor('聊天界面加号图标'))
        #点击文件按钮
        self._click(g().get_resource_infor('聊天界面文件按钮'),focus=(0.5,-0.5))
        #点击本机文件
        self._click(g().get_resource_infor('选择文件页本机按钮'))
        self._click(g().get_resource_infor('本机文件夹'))
        checkBox=g().get_resource_infor('本机文件夹多选框')
        self._wait_ui_apper(checkBox)
        self._click(g().get_resource_infor('Excel文件'))
        self._click(g().get_resource_infor('PDF文件'))
        self._click(g().get_resource_infor('PPT文件'))
        self._click(g().get_resource_infor('Txt文件'))
        wordFile=g().get_resource_infor('Word文件')
        self._wait_ui_apper(wordFile, lambda ui: ui._swipe((0.6, 0.7), (0.6, 0.4)))
        self._click(g().get_resource_infor('Word文件'))
        # while self._exists(checkBox):
        #     self._click(checkBox)
        # self._click(g().get_resource_infor('本机文件'))
        #点击确定按钮
        self._click(g().get_resource_infor('选择文件页确定按钮'))
        self._click_back()
        self._performAssert('断言发送文件消息成功',assertDict)
        self._click_back()

    @ui("AnYi")
    def viewFileMessage(self,fileType,assertDict=None):
        '''
        :param sendTo:
        :param asserDict:
        :return: 查看Excel文件消息
        '''
        # 初始化
        tools.pushInitFile()
        if fileType=='Excel':
            #点击Excel文件
            self._click(g().get_resource_infor('Excel文件'))
            #点击预览
            self._click(g().get_resource_infor('文件预览按钮'))
            #等待文件加载完成
            self._wait_ui_apper(g().get_resource_infor('Excel文件正文'))
            self._performAssert('断言查看Excel文件消息成功',assertDict)
        elif fileType=='Word':
            # 点击Word文件
            self._click(g().get_resource_infor('Word文件'))
            # 点击预览
            self._click(g().get_resource_infor('文件预览按钮'))
            # 等待文件加载完成
            self._wait_ui_apper(g().get_resource_infor('Word文件正文'))
            self._performAssert('断言查看Word文件消息成功', assertDict)
        elif fileType=='Txt':
            # 点击Txt文件
            self._click(g().get_resource_infor('Txt文件'))
            # 点击预览
            self._click(g().get_resource_infor('文件预览按钮'))
            # 等待文件加载完成
            self._wait_ui_apper(g().get_resource_infor('Txt文件正文'))
            self._performAssert('断言查看Txt文件消息成功', assertDict)
        elif fileType=='PDF':
            # 点击PDF文件
            self._click(g().get_resource_infor('PDF文件'))
            # 点击预览
            self._click(g().get_resource_infor('文件预览按钮'))
            # 等待文件加载完成
            self._flushUiTree()
            self._wait_ui_apper(g().get_resource_infor('PDF文件正文'))
            self._performAssert('断言查看PDF文件消息成功', assertDict)
        elif fileType=='PPT':
            # 点击PPT文件
            self._click(g().get_resource_infor('PPT文件'))
            # 点击预览
            self._click(g().get_resource_infor('文件预览按钮'))
            # 等待文件加载完成
            self._wait_ui_apper(g().get_resource_infor('PPT文件正文'))
            self._performAssert('断言查看PPT文件消息成功', assertDict)
        self._click_back()

    @ui("AnYi")
    def sendPositionMessage(self,assertDict=None):
        '''
        :param sendTo:
        :param assertDict:
        :return:发送位置消息
        '''
        # 点击+号
        self._click(g().get_resource_infor('聊天界面加号图标'))
        #点击位置
        self._click(g().get_resource_infor('聊天界面位置图标'),focus=(0.5,-0.5))
        #点击发送
        # self._click(g().get_resource_infor('位置发送按钮'))
        #点击取消
        self._click(g().get_resource_infor('位置取消按钮'))
        time.sleep(1)
        self._performAssert('断言取消发送位置消息成功',assertDict)
        self._click_back()

    @ui("AnYi")
    def sendContactMessage(self,contactType,assertDict=None):
        '''
        :param assertDict:
        :return: 发送企业通讯录名片消息
        '''
        #为手机添加联系人
        tools.importAContact(self)
        # 点击+号
        self._click(g().get_resource_infor('聊天界面加号图标'))
        #点击名片
        self._click(g().get_resource_infor('聊天界面名片图标'),focus=(0.5,-0.5))
        if contactType=='企业通讯录名片':
            #点击企业通讯录
            self._click(g().get_resource_infor('企业通讯录'))
            self._click(g().get_resource_infor('公司通讯录按钮'))
            self._click(g().get_resource_infor('通讯录联系人ui_test2'))
            #点击确定
            self._click(g().get_resource_infor('发送名片确定按钮'))
            self._performAssert('断言发送企业通讯录名片消息成功',assertDict)
        elif contactType=='手机通讯录名片':
            #点击手机通讯录
            self._click(g().get_resource_infor('手机通讯录'))
            #点击手机联系人
            self._wait_ui_apper(g().get_resource_infor('手机联系人'))
            self._click(g().get_resource_infor('手机联系人'))
            #点击确定
            self._click(g().get_resource_infor('手机通讯录确定按钮'))
            self._performAssert('断言发送手机通讯录名片消息成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("AnYi")
    def serachMessage(self,searchContent,assertDict=None):
        '''
        :param assertDict:
        :return: 搜索会话内容
        '''
        self._wait_ui_apper(g().get_resource_infor('安逸页面搜索按钮'),lambda ui:ui._click_back())
        #点击搜索
        self._click(g().get_resource_infor('安逸页面搜索按钮'))
        #输入搜索关键字
        self._click(g().get_resource_infor('搜索输入框'))
        self._text(searchContent)
        self._performAssert('断言搜索会话内容成功', assertDict)
        self._click_back()
        self._click_back()

    @ui("AnYi")
    def groupChat(self,assertDict=None):
        '''
        :param assertDict:
        :return: 发起群聊
        '''
        # 点击添加
        self._click(g().get_resource_infor('安逸页面添加按钮'))
        #点击发起群聊
        self._click(g().get_resource_infor('发起群聊按钮'))
        #点击公司通讯录
        self._wait_ui_apper(g().get_resource_infor('公司通讯录按钮'))
        self._click(g().get_resource_infor('公司通讯录按钮'))
        #选择群聊用户
        self._click(g().get_resource_infor('通讯录联系人ui_test2'))
        self._click(g().get_resource_infor('通讯录联系人ui_test3'))
        #点击确定
        self._click(g().get_resource_infor('选择人员页确定按钮'))
        #等待群聊出现
        self._wait_ui_apper(g().get_resource_infor('群聊页'))
        self._performAssert("断言发起群聊成功",assertDict)

    @ui("AnYi")
    def enterGroupChat(self,assertDict):
        '''
        :param assertDict:
        :return: 删除聊天会话，保存到通讯录进入群聊成功
        '''
        # 点击群组图标
        self._click(g().get_resource_infor('群聊页右上角群组图标'))
        # 点击群聊名称
        self._click(g().get_resource_infor('群聊名称按钮'))
        # 输入群聊名称
        self._click(g().get_resource_infor('群聊名称输入框'))
        self._text('enterGroupChat')
        # 点击保存群聊名称
        self._click(g().get_resource_infor('群聊名称页保存按钮'))
        self._wait_ui_apper(g().get_resource_infor('群管理按钮'))
        saveToContact=g().get_resource_infor('保存到通讯录按钮')
        self._wait_ui_apper(saveToContact,lambda ui:ui._swipe((0.6, 0.8), (0.6, 0.4)))
        # 点击保存到通讯录
        self._click(g().get_resource_infor('保存到通讯录按钮'))
        self._click_back()
        self._click_back()
        # 关闭天府安逸
        self._stopTFAnYi()
        time.sleep(2)
        # 运行天府安逸
        self._startTFAnYi()
        homeUi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_apper(homeUi)
        # 长按群聊
        self._click(g().get_resource_infor('群聊'),times=3)
        # 点击删除该聊天
        self._click(g().get_resource_infor('删除该聊天按钮'))
        # 点击通讯录
        self._click(g().get_resource_infor('主页面导航栏第二个按钮通讯录'))
        # 点击群聊
        self._click(g().get_resource_infor('通讯录页群聊按钮'))
        self._click(g().get_resource_infor('群聊'))
        self._performAssert('断言删除聊天会话，保存到通讯录群聊进入成功',assertDict)

    @ui("AnYi","Contact")
    def deleteSaveToContactGroupChat(self):
        '''
        :return: 删除保存到通讯录的群聊
        '''
        # 点击通讯录
        self._click(g().get_resource_infor('主页面导航栏第二个按钮通讯录'))
        # 点击群聊
        self._click(g().get_resource_infor('通讯录页群聊按钮'))
        # 长按群聊
        self._click(g().get_resource_infor('群聊'), times=3)
        self._click(g().get_resource_infor('删除群聊确认按钮'))
        self._click_back()

    @ui("AnYi")
    def saveToContact(self,groupChatName):
        '''
        :return: 保存群聊到通讯录
        '''
        # 点击群组图标
        self._click(g().get_resource_infor('群聊页右上角群组图标'))
        # 点击群聊名称
        self._click(g().get_resource_infor('群聊名称按钮'))
        # 输入群聊名称
        self._click(g().get_resource_infor('群聊名称输入框'))
        self._text(groupChatName)
        # 点击保存群聊名称
        self._click(g().get_resource_infor('群聊名称页保存按钮'))
        self._wait_ui_apper(g().get_resource_infor('群管理按钮'))
        saveToContact = g().get_resource_infor('保存到通讯录按钮')
        self._wait_ui_apper(saveToContact,lambda ui:ui._swipe((0.6, 0.8), (0.6, 0.4)))
        # 点击保存到通讯录
        self._click(g().get_resource_infor('保存到通讯录按钮'))
        self._click_back()
        self._click_back()

    @ui("AnYi")
    def inviteContactJoinGroupChat(self,assertDict=None):
        '''
        :param assertDict:
        :return: 邀请联系人加入群聊
        '''
        # 等待群聊出现
        self._wait_ui_apper(g().get_resource_infor('群聊页'))
        # 点击群组图标
        self._click(g().get_resource_infor('群聊页右上角群组图标'))
        #点击加号邀请联系人
        self._click(g().get_resource_infor('聊天信息页邀请联系人+号图标'))
        #点击公司通讯录
        self._click(g().get_resource_infor('公司通讯录按钮'))
        #点击邀请的联系人
        self._click(g().get_resource_infor('通讯录联系人ui_test'))
        #点击确定按钮
        self._click(g().get_resource_infor('公司通讯录选择人员页确定按钮'))
        self._wait_ui_apper(g().get_resource_infor('群聊人数显示'))
        self._performAssert('断言邀请联系人加入群聊成功',assertDict)
        self._click_back()

    @ui("AnYi")
    def deleteGroupChatContact(self,assertDict=None):
        '''
        :param assertDict:
        :return: 移除群聊人员
        '''
        # 等待群聊出现
        self._wait_ui_apper(g().get_resource_infor('群聊页'))
        # 点击群组图标
        self._click(g().get_resource_infor('群聊页右上角群组图标'))
        #点击减号移除群聊人员
        self._click(g().get_resource_infor('聊天信息页移除联系人-号图标'))
        #点击联系人移除图标
        self._click(g().get_resource_infor('群聊联系人左上角移除图标'))
        self._performAssert('断言移除群聊人员成功',assertDict)
        self._click_back()

    @ui("AnYi")
    def serachGroupChatContact(self,assertDict=None):
        '''
        :param assertDict:
        :return:搜索群聊成员
        '''
        # 等待群聊出现
        self._wait_ui_apper(g().get_resource_infor('群聊页'))
        # 点击群组图标
        self._click(g().get_resource_infor('群聊页右上角群组图标'))
        #点击全部群成员
        self._click(g().get_resource_infor('聊天信息页全部群成员'))
        #点击搜索框
        self._click(g().get_resource_infor('全部群成员页搜索框'))
        self._text("ui_test1")
        self._performAssert('断言搜索群聊成员成功',assertDict)
        self._click_back()
        self._click_back()
        self._click_back()

    @ui("AnYi")
    def setGroupChatName(self,setGroupChatName,assertDict=None):
        '''
        :param setGroupName:
        :param assertDict:
        :return: 设置群聊名称
        '''
        # 点击群组图标
        self._click(g().get_resource_infor('群聊页右上角群组图标'))
        # 点击群聊名称
        self._click(g().get_resource_infor('群聊名称按钮'))
        # 输入群聊名称
        self._click(g().get_resource_infor('群聊名称输入框'))
        self._text(setGroupChatName)
        # 点击保存群聊名称
        self._click(g().get_resource_infor('群聊名称页保存按钮'))
        # 等待群管理图标出现
        self._wait_ui_apper(g().get_resource_infor('群管理按钮'))
        self._performAssert('断言设置群聊名称成功',assertDict)

    @ui("AnYi")
    def cancelSetGroupChatName(self,setGroupChatName,assertDict):
        '''
        :param assertDict:
        :return: 取消设置群聊名称
        '''
        # 点击群组图标
        self._click(g().get_resource_infor('群聊页右上角群组图标'))
        # 点击群聊名称
        self._click(g().get_resource_infor('群聊名称按钮'))
        # 输入群聊名称
        self._click(g().get_resource_infor('群聊名称输入框'))
        self._text(setGroupChatName)
        # 点击返回按钮
        self._click(g().get_resource_infor('群聊名称设置页返回按钮'))
        self._performAssert('断言取消设置群名称成功',assertDict)

    @ui("AnYi")
    def sendGroupChatNotice(self,sendContent,assertDict):
        '''
        :param sendContent:
        :param assertDict:
        :return: 发送群公告
        '''
        # 等待群聊出现
        self._wait_ui_apper(g().get_resource_infor('群聊页'))
        # 点击群组图标
        self._click(g().get_resource_infor('群聊页右上角群组图标'))
        # 点击群公告
        self._click(g().get_resource_infor('聊天信息页群公告按钮'))
        # 点击群公告输入框
        self._click(g().get_resource_infor('群公告页输入框'))
        self._text(sendContent)
        # 点击完成
        self._click(g().get_resource_infor('群公告页完成按钮'))
        # 点击发布
        self._click(g().get_resource_infor('群公告发布按钮'))
        self._wait_ui_apper(g().get_resource_infor('群管理按钮'))
        self._performAssert('断言发送群公告成功', assertDict)
        self._click_back()
        # 等待群聊出现
        self._wait_ui_apper(g().get_resource_infor('群聊页'))

    @ui("AnYi")
    def cancelSendGroupChatNotice(self,sendContent,assertDict):
        '''
        :param assertDict:
        :return: 取消发送群公告
        '''
        # 等待群聊出现
        self._wait_ui_apper(g().get_resource_infor('群聊页'))
        # 点击群组图标
        self._click(g().get_resource_infor('群聊页右上角群组图标'))
        # 点击群公告
        self._click(g().get_resource_infor('聊天信息页群公告按钮'))
        # 点击群公告输入框
        self._click(g().get_resource_infor('群公告页输入框'))
        self._text(sendContent)
        # 点击取消
        self._click(g().get_resource_infor('取消发送公告按钮'))
        # 点击退出
        self._click(g().get_resource_infor('取消发送公告退出按钮'))
        self._performAssert('断言取消发送群公告成功',assertDict)

    @ui("AnYi")
    def addGroupChatSpecialContact(self,assertDict):
        '''
        :param assertDict:
        :return: 添加群特别关注人员
        '''
        # 等待群聊出现
        self._wait_ui_apper(g().get_resource_infor('群聊页'))
        # 点击群组图标
        self._click(g().get_resource_infor('群聊页右上角群组图标'))
        # 点击特别关注人员
        self._click(g().get_resource_infor('聊天信息页特别关注人员按钮'))
        # 点击+号添加特别关注人员
        self._click(g().get_resource_infor('特别关注人员页+号'))
        # 点击特别关注人员
        self._click(g().get_resource_infor('通讯录联系人ui_test2'))
        self._performAssert('断言添加群特别关注人员成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("AnYi")
    def setGroupChatInviteConfirm(self,assertDict):
        '''
        :param assertDict:
        :return:设置群聊邀请确认
        '''
        # 等待群聊出现
        self._wait_ui_apper(g().get_resource_infor('群聊页'))
        # 点击群组图标
        self._click(g().get_resource_infor('群聊页右上角群组图标'))
        # 点击群管理
        self._click(g().get_resource_infor('群管理按钮'))
        # 点击群聊邀请确认
        self._click(g().get_resource_infor('群管理页群聊邀请确认按钮'))
        self._click_back()
        # 点击群聊二维码
        self._click(g().get_resource_infor('聊天信息页群聊二维码'))
        self._wait_ui_apper(g().get_resource_infor('群聊邀请提示语'))
        self._performAssert('断言设置群聊邀请确认成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("AnYi")
    def setGroupChatOnlyAdminCanSetName(self,assertDict):
        '''
        :param assertDict:
        :return:设置仅允许群管理员修改群聊名称
        '''
        # 等待群聊出现
        self._wait_ui_apper(g().get_resource_infor('群聊页'))
        # 点击群组图标
        self._click(g().get_resource_infor('群聊页右上角群组图标'))
        # 点击群管理
        self._click(g().get_resource_infor('群管理按钮'))
        # 点击仅允许群管理员修改群聊名称
        self._click(g().get_resource_infor('群管理仅允许群管理修改群聊名称按钮'))
        self._click(g().get_resource_infor('群管理仅允许群管理修改群聊名称按钮'))
        self._performAssert('断言设置仅允许群管理员修改群聊名称成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("AnYi")
    def deleteGroupChat(self,assertDict):
        '''
        :return: #解散群聊
        '''
        if not self._exists(g().get_resource_infor('群管理按钮')):
            # 点击群组图标
            self._click(g().get_resource_infor('群聊页右上角群组图标'))
        #等待群管理图标出现
        self._wait_ui_apper(g().get_resource_infor('群管理按钮'))
        #点击群管理
        self._click(g().get_resource_infor('群管理按钮'))
        #等待解散群聊图标出现
        self._wait_ui_apper(g().get_resource_infor('群管理页解散群聊按钮'))
        #点击解散群聊
        self._click(g().get_resource_infor('群管理页解散群聊按钮'))
        #点击解散群聊确认框确认
        self._click(g().get_resource_infor('解散群聊确认框确认按钮'))
        #等待回到安逸页
        self._wait_ui_apper(g().get_resource_infor('主页面导航栏第一个按钮安逸'))
        #判断解散群聊是否仍显示在安逸页
        deleteGroupChatName=g().get_resource_infor('发起群聊名称')
        if self._exists(deleteGroupChatName):
            self._click(deleteGroupChatName,times=3)
            if self._exists(g().get_resource_infor('删除该聊天按钮')):
                self._click(g().get_resource_infor('删除该聊天按钮'))
        self._performAssert("断言解散群聊成功",assertDict)

    @ui("AnYi")
    def logOutGroupChat(self,assertDict):
        '''
        :param assertDict:
        :return:删除并退出群聊
        '''
        #滑动到删除并退出按钮出现
        logOut = g().get_resource_infor('聊天信息页删除并退出群聊按钮')
        self._wait_ui_apper(logOut,lambda ui:ui._swipe((0.6, 0.8), (0.6, 0.4)))
        # 点击删除并退出
        self._click(logOut)
        # 点击确定
        self._click(g().get_resource_infor('删除并退出群聊确定按钮'))
        self._performAssert('断言删除并退出群聊成功',assertDict)

    @ui("AnYi")
    def groupChatManagementTransfer(self,assertDict):
        '''
        :param assertDict:
        :return: 群管理转让
        '''
        # 等待群聊出现
        self._wait_ui_apper(g().get_resource_infor('群聊页'))
        # 点击群组图标
        self._click(g().get_resource_infor('群聊页右上角群组图标'))
        # 点击群管理
        self._click(g().get_resource_infor('群管理按钮'))
        # 点击群管理转让
        self._click(g().get_resource_infor('群管理页群管理转让按钮'))
        # 选择新管理员
        self._click(g().get_resource_infor('通讯录联系人ui_test2'))
        # 点击确定
        self._click(g().get_resource_infor('群管理转让确定按钮'))
        time.sleep(2)
        self._performAssert('断言群管理转让成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("AnYi")
    def forwardMessage(self,assertDict):
        '''
        :param assertDict:
        :return: 转发消息
        '''
        # 点击联系人
        # self._click(g().get_resource_infor('通讯录联系人ui_test2'))
        # 长按要转发的消息
        self._click(g().get_resource_infor('转发的消息'),times=3)
        # 点击转发
        self._click(g().get_resource_infor('消息转发按钮'))
        # 点击创建新聊天
        self._click(g().get_resource_infor('创建新聊天按钮'))
        # 点击公司通讯录
        self._click(g().get_resource_infor('公司通讯录按钮'))
        # 选择要转发消息的联系人
        self._click(g().get_resource_infor('通讯录联系人ui_test3'))
        # 点击确定
        self._click(g().get_resource_infor('公司通讯录选择人员页确定按钮'))
        time.sleep(2)
        anYi=g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_apper(anYi,lambda ui:ui._click_back())
        # 点击已转发消息的联系人
        self._click(g().get_resource_infor('联系人ui_test3'))
        self._performAssert('断言转发消息成功',assertDict)
        self._click_back()

    @ui("AnYi")
    def collectMessage(self,assertDict):
        '''
        :param assertDict:
        :return:收藏消息
        '''
        # 点击联系人
        # self._click(g().get_resource_infor('通讯录联系人ui_test2'))
        # 长按要收藏的消息
        self._click(g().get_resource_infor('收藏的消息'),times=3)
        # 点击收藏
        self._click(g().get_resource_infor('消息收藏按钮'))
        anYi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_apper(anYi, lambda ui: ui._click_back())
        # 点击我的
        self._click(g().get_resource_infor('主页面导航栏第五个按钮我的'))
        # 点击我的收藏
        self._click(g().get_resource_infor('我的页面我的收藏按钮'))
        time.sleep(5)
        # self._performAssert('断言收藏消息成功',assertDict)
        # # 点击收藏的消息
        # self._click(g().get_resource_infor('收藏的消息内容'),times=3)
        # # 点击删除确定按钮
        # self._click(g().get_resource_infor('删除收藏消息确定按钮'))
        # self._click_back()

    @ui("AnYi")
    def recallMessage(self,assertDict):
        '''
        :param assertDict:
        :return:撤回消息
        '''
        # 点击联系人
        # self._click(g().get_resource_infor('通讯录联系人ui_test2'))
        # 长按要撤回的消息
        self._click(g().get_resource_infor('撤回的消息'), times=3)
        # 点击撤回
        self._click(g().get_resource_infor('消息撤回按钮'))
        self._wait_ui_apper(g().get_resource_infor('消息撤回成功提示'))
        self._performAssert('断言撤回消息成功',assertDict)
        anYi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_apper(anYi, lambda ui: ui._click_back())

    @ui("AnYi")
    def deleteMessage(self,assertDict):
        '''
        :param assertDict:
        :return: 删除消息
        '''
        # 点击联系人
        # self._click(g().get_resource_infor('通讯录联系人ui_test2'))
        # 长按要删除的消息
        self._click(g().get_resource_infor('删除的消息'), times=3)
        # 点击删除
        self._click(g().get_resource_infor('消息删除按钮'))
        self._performAssert('断言删除消息成功',assertDict)
        anYi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_apper(anYi, lambda ui: ui._click_back())

    @ui("AnYi")
    def deleteManyMessage(self,assertDict):
        '''
        :param assertDict:
        :return: 删除多条消息
        '''
        # 点击消息输入框
        self._click(g().get_resource_infor('消息输入框'))
        self._text('firstMessage')
        # 点击发送
        self._click(g().get_resource_infor('消息发送按钮'))
        # 点击消息输入框
        self._click(g().get_resource_infor('消息输入框'))
        self._text('secondMessage')
        # 点击发送
        self._click(g().get_resource_infor('消息发送按钮'))
        # 长按第一条消息
        self._click(g().get_resource_infor('删除的第一条消息'),times=3)
        # 点击更多
        self._click(g().get_resource_infor('消息页面更多按钮'))
        # 点击第二条信息
        self._click(g().get_resource_infor('删除的第二条消息'))
        # 点击删除
        self._click(g().get_resource_infor('消息页面更多删除按钮'))
        # 点击确认删除
        self._click(g().get_resource_infor('确认删除按钮'))
        self._performAssert('断言删除多条消息成功',assertDict)
        anYi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_apper(anYi, lambda ui: ui._click_back())

    @ui("AnYi")
    def forwardManyMessage(self,assertDict):
        '''
        :param assertDict:
        :return: 转发多条消息
        '''
        # 点击消息输入框
        self._click(g().get_resource_infor('消息输入框'))
        self._text('forwardFirstMessage')
        # 点击发送
        self._click(g().get_resource_infor('消息发送按钮'))
        # 点击消息输入框
        self._click(g().get_resource_infor('消息输入框'))
        self._text('forwardSecondMessage')
        # 点击发送
        self._click(g().get_resource_infor('消息发送按钮'))
        # 长按第一条消息
        self._click(g().get_resource_infor('转发的第一条消息'),times=3)
        # 点击更多
        self._click(g().get_resource_infor('消息页面更多按钮'))
        # 点击第二条信息
        self._click(g().get_resource_infor('转发的第二条消息'))
        # 点击转发
        self._click(g().get_resource_infor('消息页面更多转发按钮'))
        # 点击创建新聊天
        self._click(g().get_resource_infor('创建新聊天按钮'))
        # 点击公司通讯录
        self._click(g().get_resource_infor('公司通讯录按钮'))
        # 选择要转发消息的联系人
        self._wait_ui_apper(g().get_resource_infor('通讯录联系人ui_test3'))
        self._click(g().get_resource_infor('通讯录联系人ui_test3'))
        # 点击确定
        self._click(g().get_resource_infor('公司通讯录选择人员页确定按钮'))
        # 点击发送
        self._click(g().get_resource_infor('转发多条消息发送按钮'))
        time.sleep(2)
        anYi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_apper(anYi, lambda ui: ui._click_back())
        # 点击已转发消息的联系人
        self._click(g().get_resource_infor('联系人ui_test3'))
        self._performAssert('断言转发多条消息成功', assertDict)
        anYi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_apper(anYi, lambda ui: ui._click_back())

    @ui("AnYi")
    def shareLinkMessage(self,assertDict):
        '''
        :param assertDict:
        :return: 分享链接消息给同事
        '''
        # 点击链接消息
        self._click(g().get_resource_infor('分享的链接消息'))
        # 点击菜单选项
        self._wait_ui_apper(g().get_resource_infor('链接消息正文内容'))
        self._wait_ui_apper(g().get_resource_infor('链接消息操作菜单图标'))
        self._click(g().get_resource_infor('链接消息操作菜单图标'))
        # 点击分享给同事
        self._click(g().get_resource_infor('分享给同事按钮'))
        # 点击创建新聊天
        self._click(g().get_resource_infor('创建新聊天按钮'))
        # 点击公司通讯录
        self._click(g().get_resource_infor('公司通讯录按钮'))
        # 选择要分享消息的联系人
        self._click(g().get_resource_infor('通讯录联系人ui_test3'))
        # 点击确定
        self._click(g().get_resource_infor('公司通讯录选择人员页确定按钮'))
        time.sleep(2)
        anYi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_apper(anYi, lambda ui: ui._click_back())
        # 点击已分享消息的联系人
        self._click(g().get_resource_infor('联系人ui_test3'))
        self._performAssert('断言分享链接消息给同事成功', assertDict)
        anYi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_apper(anYi,lambda ui:ui._click_back())

    @ui("AnYi")
    def shareLinkMessageToWorkCicle(self,assertDict):
        '''
        :param assertDict:
        :return: 分享链接消息到工作圈
        '''
        # 点击联系人
        self._click(g().get_resource_infor('联系人ui_test2'))
        # 点击链接消息
        self._click(g().get_resource_infor('分享的链接消息'))
        # 点击菜单选项
        self._wait_ui_apper(g().get_resource_infor('链接消息正文内容'))
        self._wait_ui_apper(g().get_resource_infor('链接消息操作菜单图标'))
        self._click(g().get_resource_infor('链接消息操作菜单图标'))
        # 点击分享到工作圈
        self._click(g().get_resource_infor('分享到工作圈按钮'))
        # 点击分享
        self._click(g().get_resource_infor('分享按钮'))
        # 点击确定
        self._click(g().get_resource_infor('分享到工作圈确定按钮'))
        anYi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_apper(anYi,lambda ui:ui._click_back())
        # 点击工作圈
        self._click(g().get_resource_infor('主页面导航栏第四个按钮工作圈'))
        self._wait_ui_apper(g().get_resource_infor('分享的链接消息内容'))
        self._performAssert('断言分享链接消息到工作圈成功',assertDict)
        #点击删除
        self._click(g().get_resource_infor('工作圈删除消息按钮'))
        self._click(g().get_resource_infor('工作圈删除消息确认按钮'))

    @ui("AnYi")
    def openLinkMessage(self,assertDict):
        '''
        :param assertDict:
        :return: 在浏览器中打开链接消息
        '''
        # 点击联系人
        self._click(g().get_resource_infor('联系人ui_test2'))
        # 点击链接消息
        self._click(g().get_resource_infor('分享的链接消息'))
        # 点击菜单选项
        self._wait_ui_apper(g().get_resource_infor('链接消息正文内容'))
        self._click(g().get_resource_infor('链接消息操作菜单图标'))
        #点击在浏览器中打开
        self._click(g().get_resource_infor('在浏览器中打开按钮'))
        time.sleep(2)
        if self._exists(g().get_resource_infor('允许按钮')):
            self._click(g().get_resource_infor('允许按钮'))
        if self._exists(g().get_resource_infor('浏览器官方推荐图标')):
            self._click(g().get_resource_infor('浏览器官方推荐图标'))
        if self._exists(g().get_resource_infor('浏览器确定按钮')):
            self._click(g().get_resource_infor('浏览器确定按钮'))
        if self._exists(g().get_resource_infor('确定按钮')):
            self._click(g().get_resource_infor('确定按钮'))
        self._performAssert('断言在浏览器中打开链接消息成功',assertDict)

    @ui("AnYi")
    def copyLinkMessage(self,assertDict):
        '''
        :param assertDict:
        :return: 复制链接消息
        '''
        # 点击联系人
        self._click(g().get_resource_infor('联系人ui_test2'))
        # 点击链接消息
        self._click(g().get_resource_infor('分享的链接消息'))
        # 点击菜单选项
        self._wait_ui_apper(g().get_resource_infor('链接消息正文内容'))
        self._click(g().get_resource_infor('链接消息操作菜单图标'))
        # 点击复制链接
        self._click(g().get_resource_infor('复制链接按钮'))
        time.sleep(1)
        self._performAssert('断言复制链接消息成功', assertDict)
        self._click_back()
        # 点击输入框
        # self._click(g().get_resource_infor('消息输入框'))
        # self._click(g().get_resource_infor('消息输入框'),times=3)
        # # 点击粘贴
        # self._click(g().get_resource_infor('粘贴按钮'))
        # # 点击发送
        # self._click(g().get_resource_infor('消息发送按钮'))
        self._click_back()

    @ui("AnYi")
    def collectLinkMessage(self,assertDict):
        '''
        :param assertDict:
        :return: 收藏链接消息
        '''
        # 点击联系人
        self._click(g().get_resource_infor('联系人ui_test2'))
        # 点击链接消息
        self._click(g().get_resource_infor('分享的链接消息'))
        # 点击菜单选项
        self._wait_ui_apper(g().get_resource_infor('链接消息正文内容'))
        self._click(g().get_resource_infor('链接消息操作菜单图标'))
        # 点击收藏
        self._click(g().get_resource_infor('收藏按钮'))
        anYi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_apper(anYi,lambda ui:ui._click_back())
        # 点击我的
        self._click(g().get_resource_infor('主页面导航栏第五个按钮我的'))
        # 点击我的收藏
        self._click(g().get_resource_infor('我的页面我的收藏按钮'))
        # self._performAssert('断言收藏链接消息成功', assertDict)
        # # 点击收藏的消息
        # self._click(g().get_resource_infor('收藏的链接消息'), times=3)
        # # 点击删除确定按钮
        # self._click(g().get_resource_infor('删除收藏消息确定按钮'))
        # self._click_back()

    @ui("AnYi")
    def searchContact(self,assertDict):
        '''
        :param assertDict:
        :return: 发送名片详细页关键字搜索成功
        '''
        # 点击+号
        self._click(g().get_resource_infor('聊天界面加号图标'))
        # 点击名片
        self._click(g().get_resource_infor('聊天界面名片图标'),focus=(0.5,-0.5))
        # 点击企业通讯录
        self._click(g().get_resource_infor('企业通讯录'))
        # 点击搜索
        self._click(g().get_resource_infor('发送名片页搜索图标'))
        self._click(g().get_resource_infor('联系人搜索框'))
        self._text('ui_test2')
        self._performAssert('断言发送名片详细页关键字搜索成功',assertDict)
        anYi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_apper(anYi,lambda ui:ui._click_back())

    @ui("AnYi")
    def searchDownloadFile(self,assertDict):
        '''
        :param assertDict:
        :return: 我的下载搜索关键字成功
        '''
        # 初始化
        tools.pushInitFile()
        # 点击+号
        self._click(g().get_resource_infor('聊天界面加号图标'))
        # 点击文件按钮
        self._click(g().get_resource_infor('聊天界面文件按钮'),focus=(0.5,-0.5))
        # 点击本机文件
        self._click(g().get_resource_infor('选择文件页本机按钮'))
        self._click(g().get_resource_infor('本机文件夹'))
        self._click(g().get_resource_infor('Excel文件'))
        # 点击确定按钮
        self._click(g().get_resource_infor('选择文件页确定按钮'))
        # 点击头像图标
        self._click(g().get_resource_infor('右上角头像图标'))
        # 点击聊天文件与图片
        self._click(g().get_resource_infor('聊天文件与图片按钮'))
        # 点击搜索
        self._click(g().get_resource_infor('聊天文件与图片页搜索图标'))
        # 输入搜索关键字
        self._click(g().get_resource_infor('聊天文件与图片搜索框'))
        self._text('测试EXCEL文件')
        self._performAssert('断言我的下载搜索关键字成功',assertDict)
        anYi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_apper(anYi, lambda ui: ui._click_back())

    @ui("AnYi")
    def sendLargeFileMessage(self,assertDict):
        '''
        :param assertDict:
        :return: 发送文件大于50M失败，提示正确
        '''
        # 初始化
        tools.pushInitFile()
        # 点击+号
        self._click(g().get_resource_infor('聊天界面加号图标'))
        # 点击文件按钮
        self._click(g().get_resource_infor('聊天界面文件按钮'),focus=(0.5,-0.5))
        # 点击本机文件
        self._click(g().get_resource_infor('选择文件页本机按钮'))
        self._click(g().get_resource_infor('本机大文件存放夹'))
        # 点击大文件
        self._click(g().get_resource_infor('本机大于50M文件'))
        # 点击确定按钮
        # self._click(g().get_resource_infor('选择文件页确定按钮'))
        self._performAssert('断言发送文件大于50M失败，提示成功',assertDict)
        anYi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_apper(anYi,lambda ui:ui._click_back())

    @ui("AnYi")
    def setMessageOnTop(self,assertDict):
        '''
        :param assertDict:
        :return: 置顶消息
        '''
        # 长按已发送消息的联系人
        self._click(g().get_resource_infor('联系人ui_test2'),times=3)
        # 点击置顶消息
        self._click(g().get_resource_infor('置顶聊天按钮'))
        # 长按已发送消息的联系人
        self._click(g().get_resource_infor('联系人ui_test2'), times=3)
        self._performAssert('断言置顶聊天消息成功',assertDict)
        self._click_back()

    @ui("AnYi")
    def setMessageNotOnTop(self,assertDict):
        '''
        :param assertDict:
        :return: 取消置顶聊天消息
        '''
        # 长按已发送消息的联系人
        self._click(g().get_resource_infor('联系人ui_test2'), times=3)
        # 点击取消置顶消息
        self._click(g().get_resource_infor('取消置顶按钮'))
        # 长按已发送消息的联系人
        self._click(g().get_resource_infor('联系人ui_test2'), times=3)
        self._performAssert('断言取消置顶聊天消息成功', assertDict)
        self._click_back()

    @ui("AnYi")
    def joinConversationChangeToGroupChat(self,assertDict):
        '''
        :param assertDict:
        :return: 个人聊天加入人员自动生成群
        '''
        # 点击头像图标
        self._click(g().get_resource_infor('右上角头像图标'))
        # 点击加号
        self._click(g().get_resource_infor('个人聊天信息页+号'))
        # 点击公司通讯录
        self._wait_ui_apper(g().get_resource_infor('公司通讯录按钮'))
        self._click(g().get_resource_infor('公司通讯录按钮'))
        # 选择群聊用户
        self._click(g().get_resource_infor('通讯录联系人ui_test3'))
        # 点击确定
        self._click(g().get_resource_infor('选择人员页确定按钮'))
        # 等待群聊出现
        self._wait_ui_apper(g().get_resource_infor('群聊页'))
        self._performAssert('断言个人聊天加入人员自动生成群成功',assertDict)
        self._click_back()

    @ui("AnYi")
    def searchGroupChat(self,assertDict):
        '''
        :param assertDict:
        :return: 发起群聊人员选择页关键字搜索
        '''
        # 点击添加
        self._click(g().get_resource_infor('安逸页面添加按钮'))
        # 点击发起群聊
        self._click(g().get_resource_infor('发起群聊按钮'))
        # 点击搜索
        self._click(g().get_resource_infor('选择人员页搜索图标'))
        self._click(g().get_resource_infor('联系人搜索框'))
        self._text('ui_test2')
        self._performAssert('断言发起群聊人员选择页关键字搜索成功',assertDict)
        self._click_back()
        self._click_back()
        self._click_back()

    @ui("AnYi")
    def deleteInputContent(self,inputContent,assertDict=None):
        '''
        :param assetDict:
        :return: 按姓名查找，清除输入内容成功
        '''
        # 点击添加
        self._click(g().get_resource_infor('安逸页面添加按钮'))
        # 点击添加联系人
        self._click(g().get_resource_infor('添加联系人按钮'))
        # 点击按姓名查找
        self._click(g().get_resource_infor('按姓名查找按钮'))
        # 输入姓名
        self._click(g().get_resource_infor('按姓名查找输入框'))
        self._text(inputContent)
        # 点击清除按钮
        self._click(g().get_resource_infor('清除按钮'))
        self._performAssert('断言按姓名查找，清除输入内容成功',assertDict)
        anYi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_apper(anYi,lambda ui:ui._click_back())

    @ui("AnYi")
    def findContact(self,contactName,assertDict):
        '''
        :return: #查找联系人
        '''
        # 点击添加
        self._click(g().get_resource_infor('安逸页面添加按钮'))
        # 点击添加联系人
        self._click(g().get_resource_infor('添加联系人按钮'))
        # 点击按姓名查找
        self._click(g().get_resource_infor('按姓名查找按钮'))
        # 输入姓名
        self._click(g().get_resource_infor('按姓名查找输入框'))
        self._text(contactName)
        # 点击查找
        self._click(g().get_resource_infor('查找按钮'))
        self._performAssert('断言查找联系人成功',assertDict)
        self._wait_ui_apper(g().get_resource_infor('主页面导航栏第一个按钮安逸'), lambda ui: ui._click_back())

    @ui("AnYi")
    def findCompanyContacts(self,assertDict):
        '''
        :param assertDict:
        :return: #查看公司通讯录
        '''
        # 点击添加
        self._click(g().get_resource_infor('安逸页面添加按钮'))
        # 点击添加联系人
        self._click(g().get_resource_infor('添加联系人按钮'))
        #点击公司通讯录
        self._click(g().get_resource_infor('添加联系人页公司通讯录按钮'))
        #等待进入通讯录页
        self._wait_ui_apper(g().get_resource_infor('公司通讯录详情页'))
        siChuanTFBank=g().get_resource_infor('公司通讯录四川天府银行机构')
        self._wait_ui_apper(siChuanTFBank,lambda ui:ui._swipe((0.6,0.9),(0.6,0.4)))
        self._performAssert('断言查看公司通讯录成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("AnYi")
    def sendCircleMessage(self,sendContent,assertDict):
        '''
        :param assertDict:
        :return: #工作分享，发布消息到工作圈
        '''
        # 点击添加
        self._click(g().get_resource_infor('安逸页面添加按钮'))
        #点击工作分享
        self._click(g().get_resource_infor('工作分享按钮'))
        #输入内容
        self._click(g().get_resource_infor('发布内容输入框'))
        self._text(sendContent)
        #点击发布
        self._click(g().get_resource_infor('发送按钮'))
        #点击发送确认框确认
        self._click(g().get_resource_infor('发送确认框确认按钮'))
        #等待发送成功，回到主页面
        self._wait_ui_apper(g().get_resource_infor('主页面导航栏第一个按钮安逸'))
        #点击工作圈
        self._click(g().get_resource_infor('主页面导航栏第四个按钮工作圈'))
        self._performAssert('断言工作分享成功',assertDict)
        #点击删除
        self._click(g().get_resource_infor('工作圈删除消息按钮'))
        self._click(g().get_resource_infor('工作圈删除消息确认按钮'))

    @ui("AnYi")
    def cancelSendCircleMessage(self, sendContent, assertDict=None):
        '''
        :param assertDict:
        :return: 取消工作分享
        '''
        # 点击添加
        self._click(g().get_resource_infor('安逸页面添加按钮'))
        # 点击工作分享
        self._click(g().get_resource_infor('工作分享按钮'))
        # 输入内容
        # self._click(g().get_resource_infor('发布内容输入框'))
        # self._text(sendContent)
        # 点击返回
        self._click(g().get_resource_infor('工作分享页返回按钮'))
        self._performAssert('断言取消工作分享成功', assertDict)

    @ui("AnYi")
    def deleteConversation(self,assertDict):
        '''
        :param assertDict:
        :return: 删除会话
        '''
        if self._exists(g().get_resource_infor('联系人ui_test2')):
            # 长按消息会话的联系人
            self._click(g().get_resource_infor('联系人ui_test2'), times=3)
            # 点击删除该聊天
            self._click(g().get_resource_infor('删除该聊天按钮'))
            self._performAssert('断言删除会话成功',assertDict)

    @ui("AnYi")
    def recoverDeleteConversation(self,assertDict):
        '''
        :param assertDict:
        :return: 恢复已删除会话
        '''
        anYi = g().get_resource_infor('主页面导航栏第一个按钮安逸')
        self._wait_ui_apper(anYi,lambda ui:ui._click_back())
        self._performAssert('断言恢复已删除会话成功',assertDict)

    @ui("AnYi")
    def sendMessageByFileAssistant(self,assertDict=None):
        '''
        :param assertDict:
        :return: 通过文件助手发送文件
        '''
        # 初始化
        tools.pushInitFile()
        # 点击我的应用
        self._click(g().get_resource_infor('主页面导航栏第三个按钮我的应用'))
        self._scrollDown()
        # 点击文件助手
        self._click(g().get_resource_infor('我的应用文件助手'))
        # 点击+号
        self._click(g().get_resource_infor('聊天界面加号图标'))
        # 点击文件按钮
        self._click(g().get_resource_infor('聊天界面文件按钮'), focus=(0.5, -0.5))
        # 点击本机文件
        self._click(g().get_resource_infor('选择文件页本机按钮'))
        self._click(g().get_resource_infor('本机文件夹'))
        checkBox = g().get_resource_infor('本机文件夹多选框')
        self._wait_ui_apper(checkBox)
        self._click(g().get_resource_infor('Excel文件'))
        # 点击确定按钮
        self._click(g().get_resource_infor('选择文件页确定按钮'))
        self._performAssert('断言通过文件助手发送文件成功', assertDict)
        self._click_back()
        self._click_back()

    @ui("AnYi")
    def sendLimitByFileAssistant(self,assertDict):
        '''
        :param assertDict:
        :return: 通过文件助手发送文件不能超过50M
        '''
        # 初始化
        tools.pushInitFile()
        # 点击我的应用
        self._click(g().get_resource_infor('主页面导航栏第三个按钮我的应用'))
        self._scrollDown()
        # 点击文件助手
        self._click(g().get_resource_infor('我的应用文件助手'))
        # 点击+号
        self._click(g().get_resource_infor('聊天界面加号图标'))
        # 点击文件按钮
        self._click(g().get_resource_infor('聊天界面文件按钮'), focus=(0.5, -0.5))
        # 点击本机文件
        self._click(g().get_resource_infor('选择文件页本机按钮'))
        self._click(g().get_resource_infor('本机大文件存放夹'))
        # 点击大文件
        self._click(g().get_resource_infor('本机大于50M文件'))
        self._performAssert('断言通过文件助手发送文件不能超过50M成功', assertDict)

    @ui("AnYi")
    def sendExpressionMessageByFileAssistant(self):
        '''
        :return: 通过文件助手发送表情消息
        '''
        # 点击我的应用
        self._click(g().get_resource_infor('主页面导航栏第三个按钮我的应用'))
        # 点击文件助手
        self._scrollDown()
        self._click(g().get_resource_infor('我的应用文件助手'))
        # 点击表情图标
        self._click(g().get_resource_infor('表情图标'))
        # 点击要发送的表情
        self._text('/::)')
        # 点击发送
        self._click(g().get_resource_infor('消息发送按钮'))
        self._click_back()
        self._click_back()
        # 点击安逸
        self._click(g().get_resource_infor('主页面导航栏第一个按钮安逸'))

    @ui("AnYi")
    def enterFileAssistant(self,assertDict):
        '''
        :param assertDict:
        :return: 删除文件助手会话框，重新进入文件助手生成新的对话框
        '''
        if self._exists(g().get_resource_infor('文件助手会话')):
            # 长按文件助手对话框
            self._click(g().get_resource_infor('文件助手会话'),times=3)
            # 点击删除该聊天
            self._click(g().get_resource_infor('删除该聊天按钮'))
            # 点击我的应用
            self._click(g().get_resource_infor('主页面导航栏第三个按钮我的应用'))
            #下滑
            self._scrollDown()
            # 点击文件助手
            self._click(g().get_resource_infor('我的应用文件助手'))
            # 点击表情图标
            self._click(g().get_resource_infor('表情图标'))
            # 点击要发送的表情
            self._text('/::)')
            # 点击发送
            self._click(g().get_resource_infor('消息发送按钮'))
            self._click_back()
            self._click_back()
            # 点击安逸
            self._click(g().get_resource_infor('主页面导航栏第一个按钮安逸'))
            self._performAssert('断言删除文件助手会话框，重新进入文件助手生成新的对话框成功',assertDict)

    @ui("AnYi")
    def setFileAssistantOnTop(self,assertDict):
        '''
        :param assertDict:
        :return: 置顶文件助手会话框
        '''
        # 长按文件助手对话框
        self._click(g().get_resource_infor('文件助手会话'), times=3)
        # 点击置顶消息
        self._click(g().get_resource_infor('置顶聊天按钮'))
        # 长按文件助手对话框
        self._click(g().get_resource_infor('文件助手会话'), times=3)
        self._performAssert('断言置顶文件助手会话框成功', assertDict)
        self._click_back()

    @ui("AnYi")
    def setFileAssistantNotOnTop(self, assertDict):
        '''
        :param assertDict:
        :return: 取消置顶文件助手会话框
        '''
        # 长按文件助手对话框
        self._click(g().get_resource_infor('文件助手会话'), times=3)
        # 点击取消置顶消息
        self._click(g().get_resource_infor('取消置顶按钮'))
        # 长按文件助手对话框
        self._click(g().get_resource_infor('文件助手会话'), times=3)
        self._performAssert('断言取消置顶文件助手会话框成功', assertDict)
        self._click_back()

    @ui("AnYi")
    def cancelSendVideoMessageByFileAssistant(self,assertDict):
        '''
        :param assertDict:
        :return:
        '''
        # 点击文件助手对话框
        self._click(g().get_resource_infor('文件助手会话'))
        # 点击+号
        self._click(g().get_resource_infor('聊天界面加号图标'))
        # 点击录像按钮
        self._click(g().get_resource_infor('聊天界面录像按钮'), focus=(0.5, -0.5))
        # 点击录像
        self._click(g().get_resource_infor('手机自带相机录像按钮'))
        time.sleep(2)
        # 点击停止录像
        self._click(g().get_resource_infor('手机自带相机停止录像按钮'))
        # 点击返回
        self._click(g().get_resource_infor('录像返回按钮'))
        # 点击确定
        self._click(g().get_resource_infor('录像取消确定按钮'))
        self._performAssert('断言通过文件助手取消发送视频消息成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("AnYi")
    def enterOfficialAccount(self,assertDict):
        '''
        :param assertDict:
        :return: 进入公众号对话框
        '''
        # 点击通讯录
        self._click(g().get_resource_infor('主页面导航栏第二个按钮通讯录'))
        # 点击公众号
        self._click(g().get_resource_infor('通讯录页公众号按钮'))
        # 点击会议室公众号
        self._click(g().get_resource_infor('会议室公众号'))
        # 点击设置
        self._click(g().get_resource_infor('会议室公众号设置按钮'))
        # 点击进入公众号
        self._click(g().get_resource_infor('进入公众号按钮'))
        self._performAssert('断言进入公众号对话框成功',assertDict)
        self._wait_ui_apper(g().get_resource_infor('主页面导航栏第二个按钮通讯录'), lambda ui: ui._click_back())

    @ui("AnYi")
    def viewOfficialAccount(self,assertDict):
        '''
        :param assertDict:
        :return: 查看公众号历史消息
        '''
        # 点击通讯录
        self._click(g().get_resource_infor('主页面导航栏第二个按钮通讯录'))
        # 点击公众号
        self._click(g().get_resource_infor('通讯录页公众号按钮'))
        # 点击会议室公众号
        self._click(g().get_resource_infor('会议室公众号'))
        # 点击设置
        self._click(g().get_resource_infor('会议室公众号设置按钮'))
        # 点击查看历史消息
        self._click(g().get_resource_infor('查看历史消息'))
        self._wait_ui_apper(g().get_resource_infor('公众号历史消息'))
        self._performAssert('断言查看公众号历史消息成功',assertDict)
        self._wait_ui_apper(g().get_resource_infor('主页面导航栏第二个按钮通讯录'), lambda ui: ui._click_back())

    @ui("AnYi")
    def cancelSubscribOfficialAccount(self,assertDict):
         '''
         :param assertDict:
         :return: 取消订阅公众号
         '''
         # 点击通讯录
         self._click(g().get_resource_infor('主页面导航栏第二个按钮通讯录'))
         # 点击公众号
         self._click(g().get_resource_infor('通讯录页公众号按钮'))
         # 点击会议室公众号
         self._click(g().get_resource_infor('会议室公众号'))
         # 点击设置
         self._click(g().get_resource_infor('会议室公众号设置按钮'))
         # 点击取消订阅
         self._click(g().get_resource_infor('取消订阅按钮'))
         self._performAssert('断言取消订阅公众号成功',assertDict)
         self._wait_ui_apper(g().get_resource_infor('主页面导航栏第二个按钮通讯录'), lambda ui: ui._click_back())

    @ui("AnYi")
    def addApplication(self,assertDict):
        '''
        :param assertDict:
        :return: 添加应用
        '''
        # 点击我的应用
        self._click(g().get_resource_infor('主页面导航栏第三个按钮我的应用'))
        # 点击全部应用
        self._click(g().get_resource_infor('全部应用按钮'))
        # 点击编辑
        self._click(g().get_resource_infor('全部应用编辑按钮'))
        #下滑
        self._scrollDown()
        # 点击+号
        self._click(g().get_resource_infor('添加应用按钮'))
        # 点击完成
        self._click(g().get_resource_infor('全部应用完成按钮'))
        time.sleep(3)
        self._click_back()
        self._scrollDown()
        # 点击业务审批应用
        self._click(g().get_resource_infor('业务审批应用'))
        self._performAssert('断言添加应用成功',assertDict)
        self._click_back()

    @ui("AnYi", "Contact")
    def deleteApplication(self,assertDict):
        '''
        :param assertDict:
        :return: 删除应用
        '''
        # 点击我的应用
        self._click(g().get_resource_infor('主页面导航栏第三个按钮我的应用'))
        # 点击业务审批应用
        self._scrollDown()
        self._click(g().get_resource_infor('业务审批应用'))
        # 长按已添加的应用
        self._click(g().get_resource_infor('添加的应用'),times=3)
        # 点击删除
        self._click((186/1080,774/1920))
        # 点击确定
        self._click(g().get_resource_infor('删除应用确定按钮'))
        time.sleep(2)
        # 点击完成
        self._click((1014/1080,118/1920))
        self._performAssert('断言删除应用成功',assertDict)
        self._click_back()

if __name__ == '__main__':
    AnYi().enterMyself()
