import time
from common.tools import ui
from po import page
from common.globall import g

class mail(page.Page):
    '''
    天府安逸首页第五屏：我的页面
    '''

    @ui("mail","anyi")
    def entermail(self,assertDict=None):
        '''
        :return:进入邮箱页面
        '''
        self._click(g().get_resource_infor('我的应用邮件'))
        if self._exists(g().get_resource_infor('安装应用确定按钮')):
            self._click(g().get_resource_infor('安装应用确定按钮'))
            time.sleep(10)
            # 点击敏邮
            self._click(g().get_resource_infor('我的应用邮件'))

    @ui("mail", "anyi")
    def loginmail(self, userName: str,password, assertDict=None):
        '''
        :return:
        '''
        # 输入用户名
        self._set_text(g().get_resource_infor('邮箱账号输入框'), userName)
        # 输入密码
        self._click(g().get_resource_infor('输入密码'))
        self._text(password)
        self._click(g().get_resource_infor('登录'))
        time.sleep(15)
        self._performAssert('错误提示框', assertDict)
        self._performAssert('进入收件箱', assertDict)


    @ui("mail", "anyi")
    def openmailsuccess(self, assertDict=None):
        self._click(g().get_resource_infor('成功打开第一封邮件'))
        if self._exists(g().get_resource_infor('邮件列表')):
            self._click(g().get_resource_infor('成功打开第一封邮件'))
        self._performAssert('打开邮件有更多按钮',assertDict)

    @ui("mail", "anyi")
    def replymailsuccess(self, assertDict=None):
        self._click(g().get_resource_infor('回复'))
        self._text('回复邮件专用')
        self._click(g().get_resource_infor('发送'))
        self._performAssert('打开邮件有更多按钮', assertDict)

    @ui("mail", "anyi")
    def replyallmailsuccess(self, assertDict=None):
        self._click(g().get_resource_infor('回复全部'))
        self._text('回复全部邮件专用')
        self._click(g().get_resource_infor('发送'))
        self._performAssert('打开邮件有更多按钮', assertDict)

    @ui("mail", "anyi")
    def fawordmailsuccess(self, assertDict=None):
        self._click(g().get_resource_infor('转发'))
        self._text('838884541@qq.com')
        self._click(g().get_resource_infor('点击邮件内容'))
        self._text('转发邮件')
        self._click(g().get_resource_infor('发送'))
        self._performAssert('打开邮件有更多按钮', assertDict)

    @ui("mail", "anyi")
    def fawordmailfail(self, assertDict=None):
        self._click(g().get_resource_infor('转发'))
        self._click(g().get_resource_infor('点击邮件内容'))
        self._text('转发邮件')
        self._click(g().get_resource_infor('发送'))
        self._performAssert('发送', assertDict)

    @ui("mail", "anyi")
    def Canceldelmail(self, assertDict=None):
        self._click(g().get_resource_infor('删除'))
        self._click(g().get_resource_infor('不要删除'))
        self._performAssert('打开邮件有更多按钮', assertDict)

    @ui("mail", "anyi")
    def delmail(self, assertDict=None):
        self._click(g().get_resource_infor('删除'))
        self._click(g().get_resource_infor('删除'))
        self._performAssert('成功打开第一封邮件', assertDict)

    @ui("mail", "anyi")
    def readmore(self, assertDict=None):
        self._click(g().get_resource_infor('打开邮件有更多按钮'))
        self._performAssert('隐藏', assertDict)

    @ui("mail", "anyi")
    def returninbox(self, assertDict=None):
        self._click(g().get_resource_infor('收件箱返回按钮'))
        if self._exists(g().get_resource_infor('收件箱返回按钮')):
            self._click(g().get_resource_infor('收件箱返回按钮'))
        self._performAssert('进入收件箱',assertDict)

    @ui("mail", "anyi")
    def checkmore(self, assertDict=None):
        self._click(g().get_resource_infor('更多'))
        self._performAssert('隐藏',assertDict)

    @ui("mail", "anyi")
    def tapwritemail(self):
        self._click(g().get_resource_infor('写邮件'))

    @ui("mail", "anyi")
    def writemail(self,sendTo,subject,content,assertDict=None):
        self._click(g().get_resource_infor('收件人'))
        self._text(sendTo)
        self._click(g().get_resource_infor('主题'))
        self._text(subject)
        self._click(g().get_resource_infor('邮件内容'))
        self._text(content)

    @ui("mail", "anyi")
    def sendmail(self, assertDict=None):
        self._click(g().get_resource_infor('发送'))
        self._performAssert('断言发件人为空发送邮件失败', assertDict)
        self._performAssert('断言返回主界面', assertDict)

    @ui("mail", "anyi")
    def addattachment(self):
        self._click(g().get_resource_infor('附件'))
        self._click(g().get_resource_infor('添加照片'))
        self._click(g().get_resource_infor('任一选择框'))
        self._click(g().get_resource_infor('选择确定'))

    @ui("mail", "anyi")
    def deldraft(self,assertDict=None):
        self._click(g().get_resource_infor('返回按钮'))
        self._click(g().get_resource_infor('删除草稿'))
        self._performAssert('断言返回主界面', assertDict)

    @ui("mail", "anyi")
    def savedraft(self, assertDict=None):
        self._click(g().get_resource_infor('返回按钮'))
        self._click(g().get_resource_infor('保存草稿'))
        self._performAssert('断言返回主界面', assertDict)

    @ui("mail", "anyi")
    def Choosemail(self, assertDict=None):
        self._click(g().get_resource_infor('编辑'))
        self._click(g().get_resource_infor('点击任一选择框'))
        self._click(g().get_resource_infor('删除'))
        self._performAssert('断言返回主界面', assertDict)

    @ui("mail", "anyi")
    def CanceldelChoosemail(self, assertDict=None):
        self._click(g().get_resource_infor('不要删除'))
        self._performAssert('断言取消删除成功', assertDict)

    @ui("mail", "anyi")
    def delChoosemail(self, assertDict=None):
        self._click(g().get_resource_infor('删除'))
        self._performAssert('断言返回主界面', assertDict)

    @ui("mail", "anyi")
    def directdelmail(self, assertDict=None):
        self._click(g().get_resource_infor('编辑'))
        self._click(g().get_resource_infor('删除'))
        self._performAssert('断言取消删除成功', assertDict)

    @ui("mail", "anyi")
    def selectall(self, assertDict=None):
        self._click(g().get_resource_infor('编辑'))
        self._wait_ui_appear(g().get_resource_infor('全选'))
        self._click(g().get_resource_infor('全选'))
        self._performAssert('断言出现取消全选', assertDict)
        self._click(g().get_resource_infor('取消全选'))
        self._performAssert('断言出现全选', assertDict)

    @ui("mail", "anyi")
    def searchmail(self, content,assertDict=None):
        time.sleep(3)
        self._click(g().get_resource_infor('搜索'))
        time.sleep(3)
        self._text(content)
        self._performAssert('搜索邮件成功', assertDict)
        self._performAssert('当前没有数据', assertDict)

    @ui("mail", "anyi")
    def openfile(self, boxname,assertDict=None):
        self._click(g().get_resource_infor('菜单栏'))
        self._click(g().get_resource_infor(boxname))
        self._performAssert('进入对应邮件箱', assertDict)

    @ui("mail", "anyi")
    def senddraft(self, address,assertDict=None):
        self._click(g().get_resource_infor('草稿箱主题'))
        self._click(g().get_resource_infor('草稿箱收件人'))
        self._text(address)
        self._click(g().get_resource_infor('发送'))
        self._performAssert('断言返回主界面', assertDict)

    @ui("mail", "anyi")
    def canceldelaccount(self, assertDict=None):
        self._click(g().get_resource_infor('菜单栏'))
        self._click(g().get_resource_infor('设置'))
        self._click(g().get_resource_infor('账号'))
        self._click(g().get_resource_infor('删除账号'))
        self._click(g().get_resource_infor('取消'))
        self._performAssert('删除账号', assertDict)

    @ui("mail", "anyi")
    def addaccount(self, assertDict=None):
        self._click(g().get_resource_infor('菜单栏'))
        self._click(g().get_resource_infor('添加邮箱账号'))

    @ui("mail", "anyi")
    def delallaccount(self, assertDict=None):
        self._click(g().get_resource_infor('菜单栏'))
        self._swipe((0.6, 0.8), (0.6, 0.4))
        self._click(g().get_resource_infor('设置'))
        for i in range(2):
            self._click(g().get_resource_infor('账号'))
            self._click(g().get_resource_infor('删除账号'))
            self._click(g().get_resource_infor('确定'))

