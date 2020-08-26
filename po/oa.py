import time

from common.tools import ui
from po import page
from common.globall import g
import time

class OA(page.Page):
    '''
    天府安逸首页第三屏OA应用
    '''

    @ui("OA")
    def enterOA(self):
        '''
        :return:点击OA应用
        '''
        self._click(g().get_resource_infor('我的应用OA'))

    @ui("OA")
    def cancelSendXieTong(self,assertDict):
        '''
        :param assertDict:
        :return: 放弃新建协同
        '''
        # 点击协同
        self._click(g().get_resource_infor('OA首页协同按钮'))
        # 点击+号新建协同
        self._click(g().get_resource_infor('协同页搜索图标'),focus=(0.8,0.5))
        # 点击自由协同
        self._click(g().get_resource_infor('自由协同'))
        # 点击关闭
        self._click(g().get_resource_infor('关闭按钮'))
        # 点击放弃新建
        self._click(g().get_resource_infor('放弃新建按钮'))
        self._performAssert('断言放弃新建协同成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("OA")
    def editXieTongApprovalProcess(self,assertDict):
        '''
        :param assertDict:
        :return: 编辑协同审批流程
        '''
        # 点击协同
        self._click(g().get_resource_infor('OA首页协同按钮'))
        # 点击+号新建协同
        self._click(g().get_resource_infor('协同页搜索图标'), focus=(0.8, 0.5))
        # 点击自由协同
        self._click(g().get_resource_infor('自由协同'))
        # 点击添加审批人员+号
        self._click(g().get_resource_infor('接收人员+号图标'))
        # 点击联系人
        self._click(g().get_resource_infor('联系人ui_test2'))
        # 点击确认
        self._click(g().get_resource_infor('确认按钮'))
        # 点击联系人
        self._click(g().get_resource_infor('联系人ui_test2'))
        # 点击替换
        self._click(g().get_resource_infor('编辑流程替换选项'))
        # 点击联系人
        self._click(g().get_resource_infor('联系人ui_test3'))
        # 点击确认
        self._click(g().get_resource_infor('确认按钮'))
        self._performAssert('断言编辑协同审批流程成功',assertDict)
        # 点击联系人
        self._click(g().get_resource_infor('联系人ui_test3'))
        # 点击删除
        self._click(g().get_resource_infor('编辑流程删除选项'))
        # 点击联系人
        self._click(g().get_resource_infor('联系人ui_test1'))
        # 点击新增
        self._click(g().get_resource_infor('编辑流程新增选项'))
        # 点击联系人
        self._click(g().get_resource_infor('联系人ui_test2'))
        # 点击确认
        self._click(g().get_resource_infor('确认按钮'))
        # 点击联系人
        self._click(g().get_resource_infor('联系人ui_test2'))
        # 点击修改节点权限
        self._click(g().get_resource_infor('编辑流程修改节点权限'))
        # 选择审批
        self._click(g().get_resource_infor('审批按钮'))
        # 点击完成
        self._click(g().get_resource_infor('修改节点权限完成按钮'))
        # 点击完成
        self._click(g().get_resource_infor('编辑流程完成按钮'))
        # 点击关闭
        self._click(g().get_resource_infor('关闭按钮'))
        # 点击放弃新建
        self._click(g().get_resource_infor('放弃新建按钮'))
        self._click_back()

    @ui("OA")
    def sendXieTong(self,titleName,firstReceiver,secondReceiver,content,assertDict=None):
        '''
        :return: 发送自由协同
        '''
        if not self._exists(g().get_resource_infor('协同页搜索图标')):
            # 点击协同
            self._click(g().get_resource_infor('OA首页协同按钮'))
        # 点击+号新建协同
        self._click(g().get_resource_infor('协同页搜索图标'), focus=(0.8, 0.5))
        # 点击自由协同
        self._click(g().get_resource_infor('自由协同'))
        # 点击标题输入框
        self._click(g().get_resource_infor('标题输入框'))
        time.sleep(2)
        self._text(titleName,enter=False)
        # 点击接收人输入框
        self._click(g().get_resource_infor('接收人输入框'))
        self._text(firstReceiver)
        # 选择接收人
        self._wait_ui_apper(g().get_resource_infor('接收人ui_test1'))
        self._click(g().get_resource_infor('接收人ui_test1'))
        # 点击接收人
        self._click(g().get_resource_infor('再次点击接收人输入框'))
        self._text(secondReceiver)
        # 选择接收人
        self._click(g().get_resource_infor('接收人ui_test2'))
        # 点击删除
        # self._click(g().get_resource_infor('接收人选项框删除图标'))
        # 点击输入正文
        self._click(g().get_resource_infor('协同正文输入框'))
        self._text(content)
        # 点击发送
        self._click(g().get_resource_infor('发送按钮'))
        self._wait_ui_apper(g().get_resource_infor('协同待办按钮'))
        self._performAssert('断言发送自由协同成功',assertDict)

    @ui("OA")
    def revokeSendXieTong(self,reason,revokeType):
        '''
        :return: 撤销已发送协同
        '''
        # 点击协同已发
        self._click(g().get_resource_infor('协同已发按钮'))
        # 点击发送的协同
        if revokeType=='test':
            self._click(g().get_resource_infor('已发送协同'))
        elif revokeType=="oa系统业务申请表":
            self._click(g().get_resource_infor('已发送表单协同'))
        elif revokeType=='test(由ui_test1原发)':
            self._click(g().get_resource_infor('转发的协同'))
        elif revokeType=='test2':
            self._click(g().get_resource_infor('已发送第二个协同'))
        # 点击撤销
        self._click(g().get_resource_infor('撤销按钮'))
        # 点击撤销原因输入框
        self._click(g().get_resource_infor('撤销原因输入框'))
        self._text(reason)
        # 点击确定
        self._click(g().get_resource_infor('确定按钮'))
        # 点击确认撤销
        self._click(g().get_resource_infor('撤销确定按钮'))
        self._wait_ui_apper(g().get_resource_infor('协同已发按钮'))

    @ui("OA")
    def deleteDaiFaXieTong(self,assertDict=None):
        '''
        :return: 删除待发协同
        '''
        # 点击协同待发
        self._click(g().get_resource_infor('协同待发按钮'))
        # 滑动界面出现批量操作
        if not self._exists(g().get_resource_infor('批量操作按钮')):
            self._swipe((0.6,0.3),(0.6,0.5))
        # 点击批量操作
        self._click(g().get_resource_infor('批量操作按钮'))
        # 点击全选
        self._click(g().get_resource_infor('全选按钮'))
        # 点击删除
        self._click(g().get_resource_infor('删除按钮'))
        # 点击删除确定
        self._click(g().get_resource_infor('删除确定按钮'))
        self._performAssert('断言删除待发协同成功',assertDict)
        # 点击提示中的确定
        self._click(g().get_resource_infor('提示框确定按钮'))
        # 点击返回
        self._click(g().get_resource_infor('返回按钮'))

    @ui("OA")
    def searchXieTong(self,searchContent,assertDict):
        '''
        :param assertDict:
        :return: 搜索协同
        '''
        # 点击搜索图标
        self._click(g().get_resource_infor('协同页搜索图标'),focus=(0.3,0.5))
        # 点击搜索输入框
        self._click(g().get_resource_infor('协同搜索输入框'))
        self._text(searchContent)
        self._performAssert('断言搜索协同成功', assertDict)
        # 点击取消
        self._click(g().get_resource_infor('取消按钮'))

    @ui("OA")
    def searchNotExistsXieTong(self, searchContent, assertDict):
        '''
        :param assertDict:
        :return: 搜索不存在协同
        '''
        # 点击协同
        self._click(g().get_resource_infor('OA首页协同按钮'))
        # 点击搜索图标
        self._click(g().get_resource_infor('协同页搜索图标'),focus=(0.3,0.5))
        # 点击搜索输入框
        self._click(g().get_resource_infor('协同搜索输入框'))
        self._text(searchContent)
        self._performAssert('断言搜索不存在协同失败', assertDict)
        self._click_back()

    @ui("OA")
    def sendFormXieTong(self,assertDict):
        '''
        :param assertDict:
        :return: 发送表单协同
        '''
        # 点击协同
        self._click(g().get_resource_infor('OA首页协同按钮'))
        # 点击+号新建协同
        self._click(g().get_resource_infor('协同页搜索图标'), focus=(0.8, 0.5))
        # 点击表单模板
        self._click(g().get_resource_infor('表单模板按钮'))
        # 点击全部模板
        self._click(g().get_resource_infor('全部模板按钮'))
        # 点击行政审批
        self._click(g().get_resource_infor('行政审批按钮'))
        # 点击OA系统业务申请表
        self._click(g().get_resource_infor('OA系统业务申请表'))
        # 点击问题描述输入框
        self._wait_ui_apper(g().get_resource_infor('问题描述输入框'))
        self._click(g().get_resource_infor('问题描述输入框'))
        self._text('test')
        # 点击发送
        self._click(g().get_resource_infor('发送按钮'))
        self._wait_ui_apper(g().get_resource_infor('协同待办按钮'))
        # 点击已发
        self._click(g().get_resource_infor('协同已发按钮'))
        self._performAssert('断言发送表单协同成功',assertDict)

    @ui("OA")
    def saveXieTong(self,assertDict=None):
        '''
        :param assertDict:
        :return: 协同保存待发
        '''
        # 点击协同
        self._click(g().get_resource_infor('OA首页协同按钮'))
        # 点击+号新建协同
        self._click(g().get_resource_infor('协同页搜索图标'), focus=(0.8, 0.5))
        # 点击表单模板
        self._click(g().get_resource_infor('表单模板按钮'))
        # 点击全部模板
        self._click(g().get_resource_infor('全部模板按钮'))
        # 点击行政审批
        self._click(g().get_resource_infor('行政审批按钮'))
        # 点击OA系统业务申请表
        self._click(g().get_resource_infor('OA系统业务申请表'))
        # 点击关闭
        self._click(g().get_resource_infor('关闭按钮'))
        # 点击保存到待发
        self._click(g().get_resource_infor('保存到待发按钮'))
        self._wait_ui_apper(g().get_resource_infor('协同待办按钮'))
        # 点击待发
        self._click(g().get_resource_infor('协同待发按钮'))
        self._performAssert('断言协同保存待发成功',assertDict)

    @ui("OA")
    def saveXieTongToDaiBan(self,assertDict):
        '''
        :param assertDict:
        :return: 协同暂存待办
        '''
        # 点击已发送协同
        self._click(g().get_resource_infor('已发送协同'))
        # 点击处理
        self._click(g().get_resource_infor('协同处理按钮'))
        # 点击暂存待办
        self._click(g().get_resource_infor('协同暂存待办按钮'))
        self._performAssert('断言协同暂存待办成功',assertDict)

    @ui("OA")
    def dealWithXieTong(self,suggestion,assertDict):
        '''
        :param assertDict:
        :return: 处理待办协同
        '''
        # 点击已发送协同
        self._click(g().get_resource_infor('已发送协同'))
        # 点击处理
        self._click(g().get_resource_infor('协同处理按钮'))
        # 输入处理意见
        self._click(g().get_resource_infor('处理意见输入框'))
        time.sleep(2)
        self._text(suggestion,enter=False)
        # 点击提交
        self._click(g().get_resource_infor('协同提交按钮'))
        # 点击待办
        self._click(g().get_resource_infor('协同待办按钮'))
        # 点击已办
        self._click(g().get_resource_infor('协同已办按钮'))
        self._performAssert('断言处理待办协同成功',assertDict)

    @ui("OA")
    def guiDangDaiBanXieTong(self,assertDict):
        '''
        :param assertDict:
        :return: 归档待办协同
        '''
        # 滑动界面出现批量操作
        if not self._exists(g().get_resource_infor('批量操作按钮')):
            self._swipe((0.6,0.3),(0.6,0.5))
        # 点击批量操作
        self._click(g().get_resource_infor('批量操作按钮'))
        # 点击全选
        self._click(g().get_resource_infor('全选按钮'))
        # 点击归档
        self._click(g().get_resource_infor('归档按钮'))
        # 点击我的文档
        self._click(g().get_resource_infor('我的文档按钮'))
        # 点击确定
        self._click(g().get_resource_infor('归档确定按钮'))
        # 点击确定
        self._click(g().get_resource_infor('归档路径确定按钮'),onlyOne=False)
        self._performAssert('断言待办协同归档成功',assertDict)
        self._click(g().get_resource_infor('提示确定按钮'))

    @ui("OA")
    def deleteDaiBanXieTong(self,assertDict):
        '''
        :param assertDict:
        :return: 删除待办协同
        '''
        # 滑动界面出现批量操作
        if not self._exists(g().get_resource_infor('批量操作按钮')):
            self._swipe((0.6, 0.3), (0.6, 0.5))
        # 点击批量操作
        self._click(g().get_resource_infor('批量操作按钮'))
        # 点击全选
        self._click(g().get_resource_infor('全选按钮'))
        # 点击删除
        self._click(g().get_resource_infor('删除按钮'))
        # 点击删除确定
        self._click(g().get_resource_infor('删除确定按钮'))
        self._performAssert('断言删除待办协同成功',assertDict)
        # 点击提示中的确定
        self._click(g().get_resource_infor('提示框确定按钮'))

    @ui("OA")
    def transferDaiBanXieTong(self,assertDict):
        '''
        :param assertDict:
        :return: 转发待办协同
        '''
        # 滑动界面出现批量操作
        if not self._exists(g().get_resource_infor('批量操作按钮')):
            self._swipe((0.6, 0.3), (0.6, 0.5))
        # 点击批量操作
        self._click(g().get_resource_infor('批量操作按钮'))
        # 点击全选
        self._click(g().get_resource_infor('全选按钮'))
        # 点击转发
        self._click(g().get_resource_infor('转发按钮'))
        # 点击转发输入框
        self._click(g().get_resource_infor('转发输入框'))
        self._text('ui_test2')
        # 选择接收人
        self._click(g().get_resource_infor('接收人ui_test2'))
        # 点击选择接收人删除图标
        self._click(g().get_resource_infor('接收人删除图标'))
        # 点击附言输入框
        # self._click(g().get_resource_infor('附言输入框'))
        # self._text('测试转发协同')
        # 点击发送
        self._click(g().get_resource_infor('转发协同发送按钮'))
        self._wait_ui_apper(g().get_resource_infor('协同待办按钮'))
        # 点击已发
        self._click(g().get_resource_infor('协同已发按钮'))
        self._performAssert('断言转发待办协同成功',assertDict)

    @ui("OA")
    def dealWithMoreDaiBanXieTong(self,assertDict):
        '''
        :param assertDict:
        :return: 批处理待办协同
        '''
        # 滑动界面出现批量操作
        if not self._exists(g().get_resource_infor('批量操作按钮')):
            self._swipe((0.6, 0.3), (0.6, 0.5))
        # 点击批量操作
        self._click(g().get_resource_infor('批量操作按钮'))
        # 点击全选
        self._click(g().get_resource_infor('全选按钮'))
        # 点击批处理
        self._click(g().get_resource_infor('批处理按钮'))
        # 点击确定
        self._click(g().get_resource_infor('批处理确定按钮'))
        self._click(g().get_resource_infor('协同已办按钮'))
        self._performAssert('断言批处理待办协同成功',assertDict)

    @ui("OA")
    def getBackYiBanXieTong(self,assertDict):
        '''
        :param assertDict:
        :return: 取回已办协同
        '''
        # 点击已处理协同
        self._click(g().get_resource_infor('已发送协同'))
        # 点击取回
        self._click(g().get_resource_infor('取回按钮'))
        # 点击否，重新处理
        self._click(g().get_resource_infor('重新处理按钮'))
        self._wait_ui_apper(g().get_resource_infor('协同处理按钮'))
        self._click_back()
        # 点击待办
        self._click(g().get_resource_infor('协同待办按钮'))
        self._performAssert('断言取回已办协同成功',assertDict)

    @ui("OA")
    def deleteYiBanXieTong(self,assertDict):
        '''
        :param assertDict:
        :return: 删除已办协同
        '''
        # 点击已发
        self._click(g().get_resource_infor('协同已办按钮'))
        # 滑动界面出现批量操作
        if not self._exists(g().get_resource_infor('批量操作按钮')):
            self._swipe((0.6, 0.3), (0.6, 0.5))
        # 点击批量操作
        self._click(g().get_resource_infor('批量操作按钮'))
        # 点击全选
        self._click(g().get_resource_infor('全选按钮'))
        # 点击删除
        self._click(g().get_resource_infor('删除按钮'))
        # 点击删除确定
        self._click(g().get_resource_infor('删除确定按钮'))
        self._performAssert('断言删除已办协同成功', assertDict)
        # 点击提示中的确定
        self._click(g().get_resource_infor('提示框确定按钮'))

    @ui("OA")
    def guiDangYiBanXieTong(self,assertDict):
        '''
        :param assertDict:
        :return: 归档已办协同
        '''
        # 滑动界面出现批量操作
        if not self._exists(g().get_resource_infor('批量操作按钮')):
            self._swipe((0.6, 0.3), (0.6, 0.5))
        # 点击批量操作
        self._click(g().get_resource_infor('批量操作按钮'))
        # 点击全选
        self._click(g().get_resource_infor('全选按钮'))
        # 点击归档
        self._click(g().get_resource_infor('归档按钮'))
        # 点击我的文档
        self._click(g().get_resource_infor('我的文档按钮'))
        # 点击确定
        self._click(g().get_resource_infor('归档确定按钮'))
        # 点击确定
        self._click(g().get_resource_infor('归档路径确定按钮'),onlyOne=False)
        self._performAssert('断言归档已办协同成功', assertDict)
        self._click(g().get_resource_infor('提示确定按钮'))

    @ui("OA")
    def transferYiBanXieTong(self,assertDict):
        '''
        :param asserDict:
        :return: 转发已办协同
        '''
        # 滑动界面出现批量操作
        if not self._exists(g().get_resource_infor('批量操作按钮')):
            self._swipe((0.6, 0.3), (0.6, 0.5))
        # 点击批量操作
        self._click(g().get_resource_infor('批量操作按钮'))
        # 点击全选
        self._click(g().get_resource_infor('全选按钮'))
        # 点击转发
        self._click(g().get_resource_infor('转发按钮'))
        # 点击转发输入框
        self._click(g().get_resource_infor('转发输入框'))
        self._text('ui_test2')
        # 选择接收人
        self._click(g().get_resource_infor('接收人ui_test2'))
        # 点击选择接收人删除图标
        self._click(g().get_resource_infor('接收人删除图标'))
        # 点击附言输入框
        # self._click(g().get_resource_infor('附言输入框'))
        # self._text('测试转发协同')
        # 点击发送
        self._click(g().get_resource_infor('转发协同发送按钮'))
        self._wait_ui_apper(g().get_resource_infor('协同待办按钮'))
        # 点击已发
        self._click(g().get_resource_infor('协同已发按钮'))
        self._performAssert('断言转发已办协同成功',assertDict)

    @ui("OA")
    def urgeYiFaXieTong(self,assertDict):
        '''
        :param assertDict:
        :return: 催办已发协同
        '''
        # 点击已发
        self._click(g().get_resource_infor('协同已发按钮'))
        # 点击已发送表单协同
        self._click(g().get_resource_infor('已发送表单协同'))
        if self._exists(g().get_resource_infor('知道了提示语')):
            self._click(g().get_resource_infor('知道了提示语'))
        # 点击流程
        self._wait_ui_apper(g().get_resource_infor('流程按钮'))
        self._click(g().get_resource_infor('流程按钮'))
        # 点击催办
        self._click(g().get_resource_infor('催办按钮'))
        # 输入催办理由
        self._click(g().get_resource_infor('催办理由输入框'))
        self._text("测试催办")
        # 点击发送
        self._click(g().get_resource_infor('发送按钮'))
        self._performAssert('断言催办已发协同成功',assertDict)
        # 点击确定
        self._click(g().get_resource_infor('催办成功提示框确定按钮'))
        # 点击返回
        self._click(g().get_resource_infor('流程返回按钮'))
        # 点击协同详情返回
        self._click(g().get_resource_infor('协同详情页返回按钮'))

    @ui("OA")
    def deleteYiFaXieTong(self,assertDict):
        '''
        :param assertDict:
        :return: 删除已发协同
        '''
        # 点击已发
        self._click(g().get_resource_infor('协同已发按钮'))
        # 滑动界面出现批量操作
        if not self._exists(g().get_resource_infor('批量操作按钮')):
            self._swipe((0.6, 0.3), (0.6, 0.5))
        # 点击批量操作
        self._click(g().get_resource_infor('批量操作按钮'))
        # 点击全选
        self._click(g().get_resource_infor('全选按钮'))
        # 点击删除
        self._click(g().get_resource_infor('删除按钮'))
        # 点击删除确定
        self._click(g().get_resource_infor('删除确定按钮'))
        self._performAssert('断言删除已发协同成功', assertDict)
        # 点击提示中的确定
        self._click(g().get_resource_infor('提示框确定按钮'))

    @ui("OA")
    def guiDangYiFaXieTong(self,assertDict):
        '''
        :param assertDict:
        :return: 归档已发协同
        '''
        # 滑动界面出现批量操作
        if not self._exists(g().get_resource_infor('批量操作按钮')):
            self._swipe((0.6, 0.3), (0.6, 0.5))
        # 点击批量操作
        self._click(g().get_resource_infor('批量操作按钮'))
        # 点击全选
        self._click(g().get_resource_infor('全选按钮'))
        # 点击删除
        self._click(g().get_resource_infor('删除按钮'))
        # 点击删除确定
        self._click(g().get_resource_infor('删除确定按钮'))
        # 点击提示中的确定
        self._click(g().get_resource_infor('提示框确定按钮'))
        # 点击已发
        self._click(g().get_resource_infor('协同已发按钮'))
        # 滑动界面出现批量操作
        if not self._exists(g().get_resource_infor('批量操作按钮')):
            self._swipe((0.6, 0.3), (0.6, 0.5))
        # 点击批量操作
        self._click(g().get_resource_infor('批量操作按钮'))
        # 点击全选
        self._click(g().get_resource_infor('全选按钮'))
        # 点击归档
        self._click(g().get_resource_infor('归档按钮'))
        # 点击我的文档
        self._wait_ui_apper(g().get_resource_infor('我的文档按钮'))
        self._click(g().get_resource_infor('我的文档按钮'))
        # 点击确定
        self._click(g().get_resource_infor('归档确定按钮'))
        # 点击确定
        self._click(g().get_resource_infor('归档路径确定按钮'),onlyOne=False)
        self._performAssert('断言归档已发协同成功', assertDict)
        self._click(g().get_resource_infor('提示确定按钮'))

    @ui("OA")
    def transferYiFaXieTong(self,assertDict):
        '''
        :param assertDict:
        :return: 转发已发协同
        '''
        # 点击已发
        self._click(g().get_resource_infor('协同已发按钮'))
        # 滑动界面出现批量操作
        if not self._exists(g().get_resource_infor('批量操作按钮')):
            self._swipe((0.6, 0.3), (0.6, 0.5))
        # 点击批量操作
        self._click(g().get_resource_infor('批量操作按钮'))
        # 点击全选
        self._click(g().get_resource_infor('全选按钮'))
        # 点击转发
        self._click(g().get_resource_infor('转发按钮'))
        # 点击转发输入框
        self._click(g().get_resource_infor('转发输入框'))
        self._text('ui_test2')
        # 选择接收人
        self._click(g().get_resource_infor('接收人ui_test2'))
        # 点击选择接收人删除图标
        self._click(g().get_resource_infor('接收人删除图标'))
        # 点击发送
        self._click(g().get_resource_infor('转发协同发送按钮'))
        time.sleep(2)
        self._performAssert('断言转发已发协同成功', assertDict)

    @ui("OA")
    def sendSavedXieTong(self,assertDict):
        '''
        :param assertDict:
        :return: 发送待发协同
        '''
        # 点击已发送表单协同
        self._click(g().get_resource_infor('已发送表单协同'))
        # 点击编辑
        self._click(g().get_resource_infor('编辑按钮'))
        # 点击问题描述输入框
        self._wait_ui_apper(g().get_resource_infor('问题描述输入框'))
        self._click(g().get_resource_infor('问题描述输入框'))
        self._text('test')
        # 点击发送
        self._click(g().get_resource_infor('发送按钮'))
        # 点击已发
        self._click(g().get_resource_infor('协同已发按钮'))
        self._performAssert('断言发送待发协同成功', assertDict)

    @ui("OA")
    def transferDaiFaXieTong(self,assertDict):
        '''
        :param assertDict:
        :return: 转发待发协同
        '''
        # 滑动界面出现批量操作
        if not self._exists(g().get_resource_infor('批量操作按钮')):
            self._swipe((0.6, 0.3), (0.6, 0.5))
        # 点击批量操作
        self._click(g().get_resource_infor('批量操作按钮'))
        # 点击全选
        self._click(g().get_resource_infor('全选按钮'))
        # 点击转发
        self._click(g().get_resource_infor('转发按钮'))
        # 点击转发输入框
        self._click(g().get_resource_infor('转发输入框'))
        self._text('ui_test2')
        # 选择接收人
        self._click(g().get_resource_infor('接收人ui_test2'))
        # 点击选择接收人删除图标
        self._click(g().get_resource_infor('接收人删除图标'))
        # 点击发送
        self._click(g().get_resource_infor('转发协同发送按钮'))
        # 点击已发
        self._click(g().get_resource_infor('协同已发按钮'))
        self._performAssert('断言转发待发协同成功', assertDict)

    @ui("OA")
    def searchNews(self,searchContent,assertDict):
        '''
        :param assertDict:
        :return: 搜索新闻
        '''
        # 点击新闻
        self._click(g().get_resource_infor('新闻按钮'))
        # 点击搜索
        self._wait_ui_apper(g().get_resource_infor('搜索按钮'))
        self._click(g().get_resource_infor('搜索按钮'))
        # 点击搜索框
        self._click(g().get_resource_infor('新闻搜索输入框'))
        self._text(searchContent)
        self._performAssert('断言搜索新闻成功',assertDict)
        # 点击取消
        self._click(g().get_resource_infor('取消按钮'))
        self._click_back()

    @ui("OA")
    def searchNotExistsNews(self,searchContent,assertDict):
        '''
        :param searchContent:
        :param assertDict:
        :return: 搜索不存在新闻
        '''
        # 点击新闻
        self._click(g().get_resource_infor('新闻按钮'))
        # 点击搜索
        self._wait_ui_apper(g().get_resource_infor('搜索按钮'))
        self._click(g().get_resource_infor('搜索按钮'))
        # 点击搜索框
        self._click(g().get_resource_infor('新闻搜索输入框'))
        self._text(searchContent)
        self._performAssert('断言搜索不存在新闻失败', assertDict)
        # 点击取消
        self._click(g().get_resource_infor('取消按钮'))
        self._click_back()

    @ui("OA")
    def viewNews(self,assertDict):
        '''
        :param assertDict:
        :return: 查看新闻
        '''
        # 点击新闻
        self._click(g().get_resource_infor('新闻按钮'))
        # 点击要查看的新闻
        self._click(g().get_resource_infor('要查看的新闻'))
        self._performAssert('断言查看新闻成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("OA")
    def viewNewsByReadFullText(self,assertDict):
        '''
        :param assertDict:
        :return:
        '''
        # 点击新闻
        self._click(g().get_resource_infor('新闻按钮'))
        # 点击阅读全文
        self._click(g().get_resource_infor('阅读全文按钮'))
        self._performAssert('断言点击阅读全文查看新闻详情成功', assertDict)
        self._click_back()
        self._click_back()

    @ui("OA")
    def commentNews(self,comment,assertDict):
        '''
        :param assertDict:
        :return: 评论新闻
        '''
        # 点击新闻
        self._click(g().get_resource_infor('新闻按钮'))
        # 点击要查看的新闻
        self._click(g().get_resource_infor('要查看的新闻'))
        # 点击评论图标
        self._click(g().get_resource_infor('评论图标'))
        # 点击评论输入框
        self._click(g().get_resource_infor('评论输入框'))
        self._text(comment,enter=False)
        # 点击发送
        self._click(g().get_resource_infor('发送按钮'))
        self._performAssert('断言评论新闻成功',assertDict)
        self._click_back()

    @ui("OA")
    def deleteNewsComment(self,assertDict):
        '''
        :param assertDict:
        :return: 删除新闻评论
        '''
        # 点击新闻
        self._click(g().get_resource_infor('新闻按钮'))
        # 点击要查看的新闻
        self._click(g().get_resource_infor('要查看的新闻'))
        # 点击评论图标
        self._click(g().get_resource_infor('评论图标'))
        # 点击删除图标
        self._click(g().get_resource_infor('删除图标'))
        # 点击确定删除
        self._click(g().get_resource_infor('删除确定按钮'))
        self._performAssert('断言删除新闻评论成功',assertDict)
        self._click_back()

    @ui("OA")
    def collectNews(self,assertDict):
        '''
        :param assertDict:
        :return:
        '''
        # 点击新闻
        self._click(g().get_resource_infor('新闻按钮'))
        # 点击要查看的新闻
        self._click(g().get_resource_infor('要查看的新闻'))
        # 点击收藏
        self._click(g().get_resource_infor('收藏按钮'))
        self._performAssert('断言收藏新闻成功',assertDict)
        self._click_back()

    @ui("OA")
    def cancelCollectNews(self,assertDict):
        '''
        :param assertDict:
        :return: 取消收藏新闻
        '''
        # 点击新闻
        self._click(g().get_resource_infor('新闻按钮'))
        # 点击要查看的新闻
        self._click(g().get_resource_infor('要查看的新闻'))
        # 点击取消收藏
        self._click(g().get_resource_infor('取消收藏按钮'))
        self._performAssert('断言取消收藏新闻成功', assertDict)
        self._click_back()

    @ui("OA")
    def fallBackOfficalDocument(self,assertDict):
        '''
        :param assertDict:
        :return: 回退待办公文
        '''
        # 点击公文
        self._click(g().get_resource_infor('公文按钮'))
        # 点击要回退的公文
        self._click(g().get_resource_infor('要回退的公文'))
        # 点击菜单栏
        self._click(g().get_resource_infor('菜单栏'))
        # 点击回退
        self._click(g().get_resource_infor('回退按钮'))
        # 点击输入回退原因
        self._click(g().get_resource_infor('回退原因输入框'))
        self._text('test')
        # 点击确定
        self._click(g().get_resource_infor('确定图标'))
        self._performAssert('断言回退待办公文成功',assertDict)
        self._click_back()

    @ui("OA")
    def searchOfficalDocument(self,searchContent,assertDict):
        '''
        :param assertDict:
        :return: 搜索公文
        '''
        # 点击公文
        self._click(g().get_resource_infor('公文按钮'))
        # 点击搜索图标
        self._click(g().get_resource_infor('搜索图标'))
        # 点击搜索输入框
        self._click(g().get_resource_infor('公文搜索输入框'))
        self._text(searchContent)
        self._performAssert('断言搜索公文成功',assertDict)
        self._click_back()

    @ui("OA")
    def searchNotExistsOfficalDocument(self,searchContent,assertDict):
        '''
        :param searchContent:
        :param assertDict:
        :return: 搜索不存在公文
        '''
        # 点击公文
        self._click(g().get_resource_infor('公文按钮'))
        # 点击搜索图标
        self._click(g().get_resource_infor('搜索图标'))
        # 点击搜索输入框
        self._click(g().get_resource_infor('公文搜索输入框'))
        self._text(searchContent)
        self._performAssert('断言搜索不存在公文成功', assertDict)
        self._click_back()

    @ui("OA")
    def revokeOfficalDocument(self,assertDict):
        '''
        :param assertDict:
        :return: 撤销待办公文
        '''
        # 点击公文
        self._click(g().get_resource_infor('公文按钮'))
        # 点击要撤销的公文
        self._wait_ui_apper(g().get_resource_infor("撤销的公文"))
        self._click(g().get_resource_infor('撤销的公文'))
        # 点击菜单选项
        self._click(g().get_resource_infor('菜单栏按钮'))
        # 点击撤销
        self._click(g().get_resource_infor('公文撤销按钮'))
        # 点击撤销原因输入框
        self._click(g().get_resource_infor('公文撤销原因输入框'))
        self._text('test')
        # 点击确定
        self._click(g().get_resource_infor('公文确定按钮'))
        self._performAssert('断言撤销待办公文成功',assertDict)

    @ui("OA")
    def saveOfficalDocument(self,assertDict):
        '''
        :param assertDict:
        :return: 暂存待办公文
        '''
        # 点击公文
        self._click(g().get_resource_infor('公文按钮'))
        # 点击要暂存的公文
        self._click(g().get_resource_infor('处理的公文'))
        # 点击处理
        self._click(g().get_resource_infor('公文处理按钮'))
        # 点击暂存待办
        self._click(g().get_resource_infor('暂存待办按钮'))
        self._performAssert('断言暂存待办公文成功',assertDict)

    @ui("OA")
    def dealWithOfficalDocument(self,assertDict):
        '''
        :param assertDict:
        :return: 处理待办公文
        '''
        # 点击公文
        self._click(g().get_resource_infor('公文按钮'))
        # 点击要处理的公文
        self._click(g().get_resource_infor('处理的公文'))
        # 点击处理
        self._click(g().get_resource_infor('公文处理按钮'))
        # 点击提交
        self._click(g().get_resource_infor('提交按钮'))
        # 点击发文
        self._click(g().get_resource_infor('发文选项'))
        # 点击已办
        self._click(g().get_resource_infor('已办按钮'))
        self._performAssert('断言处理待办公文成功',assertDict)

    @ui("OA")
    def getBackOfficalDocument(self,assertDict):
        '''
        :param assertDict:
        :return: 取回已处理公文
        '''
        # 点击公文
        self._click(g().get_resource_infor('公文按钮'))
        # 点击发文
        self._click(g().get_resource_infor('发文选项'))
        # 点击已办
        self._click(g().get_resource_infor('已办按钮'))
        # 点击要处理的公文
        self._click(g().get_resource_infor('处理的公文'))
        # 点击取回
        self._click(g().get_resource_infor('公文取回按钮'))
        # 点击确认
        self._click(g().get_resource_infor('取回确认按钮'))
        self._click_back()
        # 点击全部待办
        self._click(g().get_resource_infor('全部待办按钮'))
        self._performAssert('断言取回已处理公文成功',assertDict)

    @ui("OA")
    def addOfficalDocumentApproval(self,assertDict):
        '''
        :param assertDict:
        :return: 处理待办公文加签审批人员
        '''
        # 点击公文
        self._click(g().get_resource_infor('公文按钮'))
        # 点击要处理的公文
        self._click(g().get_resource_infor('要加签的公文'))
        # 点击处理
        self._click(g().get_resource_infor('公文处理按钮'))
        self._wait_ui_apper(g().get_resource_infor('公文菜单栏'))
        self._wait_ui_apper(g().get_resource_infor('加签按钮'), lambda ui: ui._click(g().get_resource_infor('公文菜单栏'),focus=(0.7,0.5)))
        # 点击加签
        self._click(g().get_resource_infor('加签按钮'))
        # 点击加签人员
        self._click(g().get_resource_infor('联系人ui_test2'))
        # 点击确认
        self._click(g().get_resource_infor('公文确认按钮'))
        self._performAssert('断言处理待办公文加签审批人员成功',assertDict)
        # 点击完成
        self._click(g().get_resource_infor('完成按钮'))
        self._click_back()
        self._click_back()

    @ui("OA")
    def endOfficalDocument(self,assertDict):
        '''
        :param assertDict:
        :return: 终止待办公文
        '''
        # 点击公文
        self._click(g().get_resource_infor('公文按钮'))
        # 点击要处理的公文
        self._click(g().get_resource_infor('终止的公文'))
        # 点击菜单选项
        self._click(g().get_resource_infor('菜单栏按钮'))
        # 点击终止
        self._click(g().get_resource_infor('终止按钮'))
        # 输入终止原因
        self._click(g().get_resource_infor('终止输入框'))
        self._text('test')
        # 点击确定
        self._click(g().get_resource_infor('公文确定按钮'))
        self._performAssert('断言终止待办公文成功',assertDict)

    @ui("OA")
    def revokeSendOfficalDocument(self,assertDict):
        '''
        :param assertDict:
        :return: 取回已处理收文
        '''
        # 点击公文
        self._click(g().get_resource_infor('公文按钮'))
        # 点击要处理的公文
        self._click(g().get_resource_infor('处理的收文'))
        # 点击处理
        self._click(g().get_resource_infor('公文处理按钮'))
        # 点击提交
        self._click(g().get_resource_infor('提交按钮'))
        # 点击收文
        self._wait_ui_apper((g().get_resource_infor('收文按钮')))
        self._click(g().get_resource_infor('收文按钮'))
        # 点击已办
        self._click(g().get_resource_infor('已办按钮'))
        self._click(g().get_resource_infor('处理的收文'))
        # 点击取回
        self._click(g().get_resource_infor('公文取回按钮'))
        # 点击确认
        self._click(g().get_resource_infor('取回确认按钮'))
        self._click_back()
        # 点击全部待办
        self._click(g().get_resource_infor('全部待办按钮'))
        self._performAssert('断言取回已处理收文成功',assertDict)

    @ui("OA")
    def searchNotice(self,assertDict):
        '''
        :param assertDict:
        :return: 搜索公告
        '''
        # 点击公告
        self._click(g().get_resource_infor('公告按钮'))
        # 点击搜索图标
        self._click(g().get_resource_infor('公告搜索图标'))
        #  输入关键字
        self._click(g().get_resource_infor('搜索输入框'))
        self._text('UI自动化测试')
        self._performAssert('断言搜索公告成功',assertDict)
        # 点击取消
        self._click(g().get_resource_infor('取消按钮'))
        self._click_back()

    @ui("OA")
    def viewNotice(self,assertDict):
        '''
        :param assertDict:
        :return: 查看公告
        '''
        # 点击公告
        self._click(g().get_resource_infor('公告按钮'))
        # 点击要查看的公告
        self._click(g().get_resource_infor('查看的公告'))
        self._performAssert('断言查看公告成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("OA")
    def collectNotice(self,assertDict):
        '''
        :param assertDict:
        :return: 收藏公告
        '''
        # 点击公告
        self._click(g().get_resource_infor('公告按钮'))
        # 点击要收藏的公告
        self._click(g().get_resource_infor('查看的公告'))
        # 点击收藏
        self._click(g().get_resource_infor('收藏按钮'))
        self._performAssert('断言收藏公告成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("OA")
    def cancelCollectNotice(self,assertDict):
        '''
        :param assertDict:
        :return: 取消收藏公告
        '''
        # 点击公告
        self._click(g().get_resource_infor('公告按钮'))
        # 点击要取消收藏的公告
        self._click(g().get_resource_infor('查看的公告'))
        # 点击取消收藏
        self._click(g().get_resource_infor('取消收藏按钮'))
        self._performAssert('断言取消收藏公告成功', assertDict)
        self._click_back()
        self._click_back()

    @ui("OA")
    def searchFormTemplate(self,searchContent,assertDict):
        '''
        :param assertDict:
        :return: 搜索表单模板
        '''
        # 点击发起表单
        self._click(g().get_resource_infor('发起表单'))
        # 点击搜索
        self._wait_ui_apper(g().get_resource_infor('表单搜索图标'))
        self._click(g().get_resource_infor('表单搜索图标'),focus=(0.8,0.5))
        # 点击搜索框
        self._wait_ui_apper(g().get_resource_infor('搜索框'))
        self._click(g().get_resource_infor('搜索框'))
        self._text(searchContent)
        self._performAssert('断言搜索表单模板成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("OA")
    def sendFormTemplate(self,assertDict):
        '''
        :param assertDict:
        :return: 发送表单模板
        '''
        # 点击发起表单
        self._click(g().get_resource_infor('发起表单'))
        # 点击全部模板
        self._click(g().get_resource_infor('全部模板按钮'))
        # 点击行政审批
        self._click(g().get_resource_infor('行政审批按钮'))
        # 点击OA系统业务申请表
        self._click(g().get_resource_infor('OA系统业务申请表'))
        # 点击问题描述输入框
        self._wait_ui_apper(g().get_resource_infor('问题描述输入框'))
        self._click(g().get_resource_infor('问题描述输入框'))
        self._text('test')
        # 点击发送
        self._click(g().get_resource_infor('发送按钮'))
        # 点击协同
        self._click(g().get_resource_infor('OA首页协同按钮'))
        # 点击已发
        self._click(g().get_resource_infor('协同已发按钮'))
        self._performAssert('断言发送表单模板成功',assertDict)

    @ui("OA")
    def viewFormTemplate(self,assertDict):
        '''
        :param assertDict:
        :return: 查看最近使用模板
        '''
        # 点击发起表单
        self._click(g().get_resource_infor('发起表单'))
        time.sleep(2)
        self._performAssert('断言查看最近使用模板成功',assertDict)
        self._click_back()

    @ui("OA")
    def addOfficalDocumentNotice(self,assertDict):
        '''
        :param assertDict:
        :return: 处理待办公文添加知会人员
        '''
        # 点击公文
        self._click(g().get_resource_infor('公文按钮'))
        # 点击要处理的公文
        self._click(g().get_resource_infor('要加签的公文'))
        # 点击处理
        self._click(g().get_resource_infor('公文处理按钮'))
        self._wait_ui_apper(g().get_resource_infor('公文菜单栏'))
        self._wait_ui_apper(g().get_resource_infor('知会按钮'), lambda ui: ui._click(g().get_resource_infor('公文菜单栏'), focus=(0.7, 0.5)))
        # 点击加签
        self._click(g().get_resource_infor('知会按钮'))
        # 点击要知会的人员
        self._click(g().get_resource_infor('联系人ui_test3'))
        # 点击确认
        self._click(g().get_resource_infor('确认按钮'))
        self._performAssert('断言处理待办公文添加知会人员成功',assertDict)
        # 点击完成
        self._click(g().get_resource_infor('完成按钮'))
        self._click_back()
        self._click_back()

    @ui("OA")
    def fallBackXieTong(self,assertDict):
        '''
        :param assertDict:
        :return: 回退待办协同
        '''
        # 点击待办
        self._click(g().get_resource_infor('协同待办按钮'))
        # 点击要处理的协同
        self._click(g().get_resource_infor('已发送协同'))
        # 点击处理
        self._click(g().get_resource_infor('协同处理按钮'))
        # 点击协同菜单栏
        self._click(g().get_resource_infor('协同菜单栏'))
        self._wait_ui_apper(g().get_resource_infor('回退按钮'), lambda ui: ui._click(g().get_resource_infor('协同菜单栏')))
        # 点击回退
        self._click(g().get_resource_infor('回退按钮'))
        # 点击确定
        self._click(g().get_resource_infor('协同确定按钮'))
        # 点击待发
        self._click(g().get_resource_infor('协同待发按钮'))
        self._performAssert('断言回退待办协同成功',assertDict)

    @ui("OA")
    def fallBackTheXieTong(self,assertDict):
        '''
        :param assertDict:
        :return: 指定回退待办协同
        '''
        # 点击待办
        self._click(g().get_resource_infor('协同待办按钮'))
        # 点击要处理的协同
        self._click(g().get_resource_infor('已发送协同'))
        # 点击处理
        self._click(g().get_resource_infor('协同处理按钮'))
        # 点击协同菜单栏
        self._click(g().get_resource_infor('协同菜单栏'))
        self._wait_ui_apper(g().get_resource_infor('指定回退按钮'), lambda ui: ui._click(g().get_resource_infor('协同菜单栏')))
        # 点击回退
        self._click(g().get_resource_infor('指定回退按钮'))
        # 点击回退人员
        self._click(g().get_resource_infor('联系人ui_test1'))
        # 点击流程重走
        self._click(g().get_resource_infor('流程重走按钮'))
        # 点击确定
        self._click(g().get_resource_infor('协同确定按钮'))
        # 点击待发
        self._click(g().get_resource_infor('协同待发按钮'))
        self._performAssert('断言指定回退待办协同成功', assertDict)

    @ui("OA")
    def transferXieTong(self,assertDict):
        '''
        :param assertDict:
        :return: 移交待办协同
        '''
        # 点击待办
        self._click(g().get_resource_infor('协同待办按钮'))
        # 点击要处理的协同
        self._click(g().get_resource_infor('已发送协同'))
        # 点击处理
        self._click(g().get_resource_infor('协同处理按钮'))
        # 点击协同菜单栏
        self._click(g().get_resource_infor('协同菜单栏'))
        self._wait_ui_apper(g().get_resource_infor('移交按钮'), lambda ui: ui._click(g().get_resource_infor('协同菜单栏')))
        # 点击移交
        self._click(g().get_resource_infor('移交按钮'))
        # 点击移交人员
        self._click(g().get_resource_infor('联系人ui_test2'))
        # 点击确认
        self._click(g().get_resource_infor('确认'))
        # 点击确定
        self._click(g().get_resource_infor('协同确定按钮'))
        self._click(g().get_resource_infor('协同已发按钮'))
        self._performAssert('断言移交待办协同成功', assertDict)

    @ui("OA")
    def endXieTong(self,assertDict):
        '''
        :param assertDict:
        :return: 终止待办协同
        '''
        # 点击待办
        self._click(g().get_resource_infor('协同待办按钮'))
        # 点击要处理的协同
        self._click(g().get_resource_infor('已发送协同'))
        # 点击处理
        self._click(g().get_resource_infor('协同处理按钮'))
        # 点击协同菜单栏
        self._click(g().get_resource_infor('协同菜单栏'))
        self._wait_ui_apper(g().get_resource_infor('终止按钮'), lambda ui: ui._click(g().get_resource_infor('协同菜单栏')))
        # 点击回退
        self._click(g().get_resource_infor('终止按钮'))
        # 点击确定
        self._click(g().get_resource_infor('协同确定按钮'))
        # 点击已办
        self._click(g().get_resource_infor('协同已办按钮'))
        self._performAssert('断言终止待办协同成功',assertDict)
        # 点击已发
        self._click(g().get_resource_infor('协同已发按钮'))

    @ui("OA")
    def viewOfficalDocument(self,assertDict):
        '''
        :param assertDict:
        :return: 查看公文正文
        '''
        self._click(g().get_resource_infor('公文按钮'))
        # 点击要处理的公文
        self._click(g().get_resource_infor('处理的公文'))
        # 点击正文
        self._click(g().get_resource_infor('正文'))
        self._performAssert('断言查看公文正文成功',assertDict)
        self._click_back()
        self._click_back()


if __name__ == '__main__':
    OA().enterOA()
