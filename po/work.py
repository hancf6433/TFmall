import time
from common.tools import ui
from po import page
from common.globall import g
import time


class work(page.Page):
    '''
    天府安逸首页第五屏：我的页面
    '''

    @ui("work","anyi")
    def inputmessage(self,content,assertDict=None):
        '''
        :return:进入工作圈页面
        '''
        self._click(g().get_resource_infor('发布按钮'))
        self._click(g().get_resource_infor('发布消息'))
        self._click(g().get_resource_infor('文档输入框'))
        self._set_text(g().get_resource_infor('文档输入框'),content)

    @ui("work", "anyi")
    def canceldelmessage(self, assertDict=None):
        '''
        :return:进入工作圈页面
        '''
        self._click(g().get_resource_infor('删除按钮'))
        self._click(g().get_resource_infor('取消'))
        self._performAssert('删除按钮',assertDict)

    @ui("work", "anyi")
    def delmessage(self, assertDict=None):
        '''
        :return:进入工作圈页面
        '''
        self._click(g().get_resource_infor('删除按钮'))
        self._click(g().get_resource_infor('删除'))
        #self._performAssert(self.assert_ui_not_exists(g().get_resource_infor('删除按钮')), assertDict)

    @ui("work", "anyi")
    def postmessage(self, assertDict=None):
        #self._wait_ui_disapper(g().get_resource_infor('图片发送中'))
        self._click(g().get_resource_infor('发送'))
        if self._exists(g().get_resource_infor('提示')):
            self._click(g().get_resource_infor('确定'))
        time.sleep(3)
        self._performAssert('回到工作圈页面', assertDict)
        self._performAssert('失败停留在当前页面', assertDict)
    @ui("work", "anyi")
    def addpicture(self):
        self._click(g().get_resource_infor('拍照按钮'))
        time.sleep(3.0)
        self._click(g().get_resource_infor('拍照片'))
        time.sleep(3.0)
        self._click(g().get_resource_infor('拍照'))
        self._wait_ui_appear(g().get_resource_infor('拍照确定'))
        self._click(g().get_resource_infor('拍照确定'))

    @ui("work", "anyi")
    def addlove(self, assertDict=None):
        self._click(g().get_resource_infor('第一个更多按钮'))
        self._click(g().get_resource_infor('赞'))
        time.sleep(2)
        self._performAssert('点赞成功', assertDict)

    @ui("work", "anyi")
    def dellove(self, assertDict=None):
        self._click(g().get_resource_infor('第一个更多按钮'))
        self._click(g().get_resource_infor('取消赞'))
        self._performAssert(self.assert_ui_not_exists(g().get_resource_infor('点赞成功')), assertDict)

    @ui("work", "anyi")
    def replymessage(self, replycontent,assertDict=None):
        time.sleep(5)
        self._click(g().get_resource_infor('第一个更多按钮'))
        self._click(g().get_resource_infor('回复'))
        time.sleep(1)
        self._text(replycontent)
        self._click(g().get_resource_infor('发送'))
        time.sleep(5)
        self._performAssert('发布按钮', assertDict)
        self._performAssert('发送', assertDict)

    @ui("work", "anyi")
    def sharegroup(self, assertDict=None):
        self._click(g().get_resource_infor('第一个更多按钮'))
        self._click(g().get_resource_infor('分享'))
        self._click(g().get_resource_infor('分享到工作圈'))
        self._text('分享到工作圈')
        self._click(g().get_resource_infor('分享'))
        self._click(g().get_resource_infor('确定'))
        time.sleep(3)
        self._performAssert('发布按钮', assertDict)

    @ui("work", "anyi")
    def sharetomenber(self, assertDict=None):
        self._click(g().get_resource_infor('第一个更多按钮'))
        self._click(g().get_resource_infor('分享'))
        self._click(g().get_resource_infor('分享给同事'))
        self._wait_ui_appear(g().get_resource_infor('分享页标题'))
        if self._exists(g().get_resource_infor('联系人')):
            self._click(g().get_resource_infor('联系人'))
        else:
            self._click(g().get_resource_infor('创建新聊天'))
            self._click(g().get_resource_infor('公司通讯录'))
            self._click(g().get_resource_infor('选择框'))
            self._click(g().get_resource_infor('确定按钮'))
        self._performAssert('发布按钮', assertDict)

    @ui("work", "anyi")
    def workname(self, name,assertDict=None):
        self._click(g().get_resource_infor('所有'))
        self._click(g().get_resource_infor('创建工作圈'))
        self._click(g().get_resource_infor('输入框'))
        self._text(name)
        self._click(g().get_resource_infor('确定'))
        #self._click(g().get_resource_infor('确定创建'))
        self._performAssert('不合法的工作圈名称', assertDict)

    @ui("work", "anyi")
    def addworkcircle(self,assertDict=None):
        self._wait_ui_appear(g().get_resource_infor('确定创建'))
        self._click(g().get_resource_infor('确定创建'))
        self._click(g().get_resource_infor('搜索按钮'))
        self._text('test')
        self._click(g().get_resource_infor('选择框'))
        self._click(g().get_resource_infor('确定按钮'))
        time.sleep(2)
        self._click(g().get_resource_infor('所有'))
        self._performAssert('工作圈测试', assertDict)

    @ui("work", "anyi")
    def enterwork(self, assertDict=None):
        self._click(g().get_resource_infor('所有'))
        self._click(g().get_resource_infor('工作圈测试'))
        self._performAssert('新工作圈当前无数据', assertDict)

    @ui("work", "anyi")
    def addworkmember(self, assertDict=None):
        self._click(g().get_resource_infor('所有'))
        self._click(g().get_resource_infor('成员按钮'))
        self._click(g().get_resource_infor('添加成员按钮'))
        self._click(g().get_resource_infor('成员搜索'))
        self._text('test')
        self._click(g().get_resource_infor('成员选择'))
        self._click(g().get_resource_infor('确定按钮'))
        self._performAssert('加入工作圈人数3人', assertDict)

    @ui("work", "anyi")
    def delworkmember(self, assertDict=None):
        self._click(g().get_resource_infor('所有'))
        self._click(g().get_resource_infor('成员按钮'))
        time.sleep(3)
        self._click(g().get_resource_infor('删除成员按钮'))
        self._click(g().get_resource_infor('删除成员'))
        self._performAssert('加入工作圈人数2人', assertDict)

    @ui("work", "anyi")
    def delwork(self, assertDict=None):
        self._click(g().get_resource_infor('所有'))
        self._click(g().get_resource_infor('成员按钮'))
        time.sleep(3)
        self._click(g().get_resource_infor('删除工作圈'))
        self._click(g().get_resource_infor('确定'))
        self._performAssert('发布按钮', assertDict)

    @ui("work", "anyi")
    def exitwork(self, assertDict=None):
        self._click(g().get_resource_infor('成员按钮'))
        self._click(g().get_resource_infor('退出工作圈'))
        self._performAssert('发布按钮', assertDict)

    @ui("work", "anyi")
    def exitworkbymore(self, assertDict=None):
        self._click(g().get_resource_infor('更多工作圈'))
        self._click(g().get_resource_infor('退出'))
        self._performAssert(self.assert_ui_not_exists(g().get_resource_infor('退出')), assertDict)

    @ui("work", "anyi")
    def taskname(self, taskname,assertDict=None):
        self._click(g().get_resource_infor('发布按钮'))
        self._click(g().get_resource_infor('创建任务'))
        time.sleep(1)
        self._text(taskname)

    @ui("work", "anyi")
    def posttask(self, taskname, assertDict=None):
        self._click(g().get_resource_infor('发送'))
        self._click(g().get_resource_infor('确定'))
        self._performAssert('所有', assertDict)
        self._performAssert('发送', assertDict)
        self._performAssert('新建话题', assertDict)

    @ui("work", "anyi")
    def addtaskitem(self, itemname, assertDict=None):
        self._click(g().get_resource_infor('添加'))
        time.sleep(1)
        self._text('itemname')
        self._click(g().get_resource_infor('确定'))

    @ui("work", "anyi")
    def addtopic(self,assertDict=None):
        self._click(g().get_resource_infor('添加话题'))
        self._click(g().get_resource_infor('话题选项框'))
        self._click(g().get_resource_infor('保存'))

    @ui("work", "anyi")
    def addpic(self, assertDict=None):
        self._click(g().get_resource_infor('添加图片'))
        self._click(g().get_resource_infor('拍照片'))
        time.sleep(3.0)
        self._click(g().get_resource_infor('拍照'))
        self._wait_ui_appear(g().get_resource_infor('拍照确定'))
        self._click(g().get_resource_infor('拍照确定'))

    @ui("work", "anyi")
    def modifytask(self,modifyname, assertDict=None):
        self._click(g().get_resource_infor('修改'))
        self._text(modifyname)
        self._click(g().get_resource_infor('修改'))
        self._click(g().get_resource_infor('确定'))
        self._performAssert('所有', assertDict)

    @ui("work", "anyi")
    def finishtask(self, assertDict=None):
        self._click(g().get_resource_infor('完成任务'))
        self._click(g().get_resource_infor('确定'))
        time.sleep(5)
        self._performAssert('有一个任务已完成', assertDict)

    @ui("work", "anyi")
    def cancelfinishtask(self, assertDict=None):
        self._click(g().get_resource_infor('完成任务'))
        self._click(g().get_resource_infor('取消'))
        self._performAssert('完成任务', assertDict)

    @ui("work", "anyi")
    def addtasktopic(self,topicname,assertDict=None):
        self._click(g().get_resource_infor('添加话题'))
        self._wait_ui_appear(g().get_resource_infor('新建话题'))
        self._click(g().get_resource_infor('新建话题'))
        self._text(topicname)
        self._click(g().get_resource_infor('确定'))
        self._performAssert('保存', assertDict)



    @ui("work", "anyi")
    def savetopic(self, assertDict=None):
        self._click(g().get_resource_infor('保存'))

    @ui("work", "anyi")
    def organame(self, organame, assertDict=None):
        self._click(g().get_resource_infor('发布按钮'))
        self._click(g().get_resource_infor('组织活动'))
        self._text(organame)

    @ui("work", "anyi")
    def postorga(self, taskname, assertDict=None):
        self._click(g().get_resource_infor('发送'))
        self._click(g().get_resource_infor('确定'))
        self._performAssert('所有', assertDict)
        self._performAssert('发送', assertDict)
        self._performAssert('新建话题', assertDict)