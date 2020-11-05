from common.tools import ui
from po import page
from common.globall import g
import time


class Contact(page.Page):
    '''
    天府安逸首页第二屏
    '''

    @ui("AnYi","Contact")
    def enterContact(self):
        '''
        :return:点击通讯录
        '''
        self._click(g().get_resource_infor('主页面导航栏第二个按钮通讯录'))

    @ui("Contact")
    def searchContact(self,searchContent,assertDict):
        '''
        :param assertDict:
        :return: 通讯录搜索联系人
        '''
        # 点击搜索图标
        self._click(g().get_resource_infor('通讯录页搜索图标'))
        # 输入搜索联系人
        self._click(g().get_resource_infor('通讯录页搜索输入框'))
        self._text(searchContent)
        self._performAssert('断言通讯录搜索联系人成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("Contact")
    def searchDepartment(self,searchContent,assertDict):
        '''
        :param assertDict:
        :return: 通讯录搜索部门
        '''
        # 点击搜索图标
        self._click(g().get_resource_infor('通讯录页搜索图标'))
        # 输入搜索部门
        self._click(g().get_resource_infor('通讯录页搜索输入框'))
        self._text(searchContent)
        self._performAssert('断言通讯录搜索部门成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("Contact")
    def viewAddContact(self,assertDict):
        '''
        :param assertDict:
        :return: 查看通讯录添加联系人页
        '''
        # 点击+号
        self._click(g().get_resource_infor('通讯录页+号图标'))
        self._performAssert('断言查看通讯录添加联系人页成功',assertDict)
        self._click_back()

    @ui("AnYi","Contact")
    def addContact(self,addContact,assertDict):
        '''
        :param assertDict:
        :return: 通讯录添加联系人
        '''
        # 点击+号
        self._click(g().get_resource_infor('通讯录页+号图标'))
        # 点击按姓名查找
        self._click(g().get_resource_infor('按姓名查找按钮'))
        # 输入姓名
        self._click(g().get_resource_infor('按姓名查找输入框'))
        self._text(addContact)
        # 点击查找
        self._click(g().get_resource_infor('查找按钮'))
        self._click(g().get_resource_infor('查找用户'))
        # 点击加为联系人
        self._click(g().get_resource_infor('加为联系人按钮'))
        time.sleep(1)
        contact=g().get_resource_infor('主页面导航栏第二个按钮通讯录')
        self._wait_ui_appear(contact, lambda ui: ui._click_back())
        self._performAssert('断言通讯录添加联系人成功',assertDict)

    @ui("AnYi","Contact")
    def addCompanyContact(self,assertDict):
        '''
        :param assertDict:
        :return: 公司通讯录添加联系人
        '''
        # 点击+号
        self._click(g().get_resource_infor('通讯录页+号图标'))
        # 点击公司通讯录
        self._click(g().get_resource_infor(('添加联系人页公司通讯录按钮')))
        # 点击添加的联系人
        self._click(g().get_resource_infor('通讯录联系人ui_test3'))
        # 点击加为联系人
        self._click(g().get_resource_infor('加为联系人按钮'))
        time.sleep(1)
        contact = g().get_resource_infor('主页面导航栏第二个按钮通讯录')
        self._wait_ui_appear(contact, lambda ui: ui._click_back())
        self._performAssert('断言公司通讯录添加联系人成功', assertDict)
        # 点击已添加的联系人
        self._click(g().get_resource_infor('已添加的联系人'))
        # 点击删除联系人
        self._click(g().get_resource_infor('删除联系人按钮'))
        # 点击确定
        self._click(g().get_resource_infor('删除联系人确定按钮'))
        self._click_back()
        self._click_back()

    @ui("Contact")
    def deleteContact(self,assertDict):
        '''
        :param assertDict:
        :return: 删除联系人
        '''
        # 点击已添加的联系人
        self._click(g().get_resource_infor('通讯录添加的联系人'))
        # 点击删除联系人
        self._click(g().get_resource_infor('删除联系人按钮'))
        # 点击确定
        self._click(g().get_resource_infor('删除联系人确定按钮'))
        time.sleep(1)
        self._performAssert('断言删除联系人成功', assertDict)

    @ui("Contact")
    def viewContact(self,assertDict):
        '''
        :param assertDict:
        :return: 查看通讯录页
        '''
        self._performAssert('断言查看通讯录页成功',assertDict)

    @ui("AnYi","Contact")
    def viewSaveGroupChat(self,assertDict):
        '''
        :param assertDict:
        :return: 查看已保存群聊
        '''
        # 点击群聊
        self._click(g().get_resource_infor('通讯录页群聊按钮'))
        self._performAssert('断言查看已保存群聊成功',assertDict)
        # 点击已保存群聊
        self._click(g().get_resource_infor('已保存群聊'))
        # 点击群组图标
        self._click(g().get_resource_infor('群聊页右上角群组图标'))
        # 等待群管理图标出现
        self._wait_ui_appear(g().get_resource_infor('群管理按钮'))
        # 点击群管理
        self._click(g().get_resource_infor('群管理按钮'))
        # 等待解散群聊图标出现
        self._wait_ui_appear(g().get_resource_infor('群管理页解散群聊按钮'))
        # 点击解散群聊
        self._click(g().get_resource_infor('群管理页解散群聊按钮'))
        # 点击解散群聊确认框确认
        self._click(g().get_resource_infor('解散群聊确认框确认按钮'))
        if self._exists(g().get_resource_infor('已保存群聊')):
            self._click(g().get_resource_infor('已保存群聊'),times=3)
            self._click(g().get_resource_infor('删除该聊天按钮'))
        # 点击通讯录
        self._click(g().get_resource_infor('主页面导航栏第二个按钮通讯录'))
        # 点击群聊
        self._click(g().get_resource_infor('通讯录页群聊按钮'))
        if self._exists(g().get_resource_infor('已保存群聊')):
            self._click(g().get_resource_infor('已保存群聊'),times=3)
            self._click(g().get_resource_infor('删除群聊确认按钮'))
        self._click_back()

    @ui("AnYi", "Contact")
    def setSpecialFollow(self,assertDict):
        '''
        :return: 设置特别关注
        '''
        # 点击公司通讯录
        self._click(g().get_resource_infor('通讯录页公司通讯录按钮'))
        # 点击要设置特别关注的联系人
        self._click(g().get_resource_infor('通讯录联系人ui_test2'))
        special=g().get_resource_infor('联系人信息页特别关注按钮')
        if not self._exists(special):
            self._swipe((0.5, 0.6), (0.5, 0.4))
        # 点击特别关注
        self._click(g().get_resource_infor('联系人信息页特别关注按钮'))
        self._click_back()
        self._click_back()
        # 点击通讯录页特别关注
        self._click(g().get_resource_infor('通讯录页特别关注按钮'))
        self._performAssert('断言设置特别关注成功',assertDict)
        # 长按特别关注联系人
        self._click(g().get_resource_infor('设置的特别关注'),times=3)
        # 点击确定
        self._click(g().get_resource_infor('特别关注删除确定按钮'))
        self._click_back()

    @ui("AnYi","Contact")
    def sendSMSToContact(self,assertDict):
        '''
        :param assertDict:
        :return: 向通讯录联系人发送短信
        '''
        # 点击公司通讯录
        self._click(g().get_resource_infor('通讯录页公司通讯录按钮'))
        # 点击联系人
        self._click(g().get_resource_infor('通讯录联系人ui_test3'))
        # 点击手机号
        self._click(g().get_resource_infor('联系人手机号'))
        # 点击发送短信
        self._click(g().get_resource_infor('发送短信按钮'))
        time.sleep(2)
        self._performAssert('断言向通讯录联系人发送短信成功',assertDict)
        contact=g().get_resource_infor('主页面导航栏第二个按钮通讯录')
        self._wait_ui_appear(contact, lambda ui: ui._click_back())

    @ui("AnYi", "Contact")
    def viewCompanyContact(self,assertDict):
        '''
        :param assertDict:
        :return: 查看公司通讯录页
        '''
        # 点击公司通讯录
        self._click(g().get_resource_infor('通讯录页公司通讯录按钮'))
        # 等待进入通讯录页
        self._wait_ui_appear(g().get_resource_infor('公司通讯录详情页'))
        self._performAssert('断言查看公司通讯录页成功', assertDict)
        self._click_back()

    @ui("AnYi","Contact")
    def closeCompanyContact(self,assertDict):
        '''
        :param assertDict:
        :return: 关闭公司通讯录页
        '''
        # 点击公司通讯录
        self._click(g().get_resource_infor('通讯录页公司通讯录按钮'))
        # 点击关闭
        self._click(g().get_resource_infor('公司通讯录页关闭按钮'))
        self._performAssert('断言关闭公司通讯录页成功',assertDict)

    @ui("AnYi","Contact")
    def saveContactPhone(self,assertDict):
        '''
        :param assertDict:
        :return: 保存通讯录联系人电话到本地
        '''
        # 点击公司通讯录
        self._click(g().get_resource_infor('通讯录页公司通讯录按钮'))
        # 点击联系人
        self._click(g().get_resource_infor('通讯录联系人ui_test3'))
        # 点击手机号
        self._click(g().get_resource_infor('联系人手机号'))
        # 点击保存至手机
        self._click(g().get_resource_infor('保存至手机按钮'))
        self._performAssert('断言保存通讯录联系人电话到本地成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("AnYi","Contact")
    def sendMessageToContact(self,assertDict):
        '''
        :param assertDict:
        :return: 向通讯录联系人发消息
        '''
        # 点击公司通讯录
        self._click(g().get_resource_infor('通讯录页公司通讯录按钮'))
        # 点击联系人
        self._click(g().get_resource_infor('通讯录联系人ui_test3'))
        # 点击发消息
        self._click(g().get_resource_infor('发消息按钮'))
        # 点击表情图标
        self._click(g().get_resource_infor('表情图标'))
        # 点击要发送的表情
        self._text('/::)')
        # 点击发送
        self._click(g().get_resource_infor('消息发送按钮'))
        self._performAssert('断言向通讯录联系人发消息成功', assertDict)
        self._click_back()
        self._click_back()

    @ui("AnYi","Contact")
    def callContact(self,assertDict):
        '''
        :param assertDict:
        :return: 拨打通讯录联系人电话
        '''
        # 点击公司通讯录
        self._click(g().get_resource_infor('通讯录页公司通讯录按钮'))
        # 点击联系人
        self._click(g().get_resource_infor('通讯录联系人ui_test3'))
        # 点击手机号
        self._click(g().get_resource_infor('联系人手机号'))
        # 点击拨打电话
        self._click(g().get_resource_infor('拨打电话按钮'))
        self._performAssert('断言拨打通讯录联系人电话成功',assertDict)

    @ui("AnYi","Contact")
    def viewContactWorkCicle(self,assertDict):
        '''
        :param assertDict:
        :return: 查看通讯录联系人工作圈
        '''
        # 点击公司通讯录
        self._click(g().get_resource_infor('通讯录页公司通讯录按钮'))
        # 点击联系人
        self._click(g().get_resource_infor('通讯录联系人ui_test2'))
        # 点击工作圈
        self._click(g().get_resource_infor('联系人信息页工作圈按钮'))
        self._performAssert('断言查看通讯录联系人工作圈成功',assertDict)
        self._click_back()
        self._click_back()
        self._click_back()

    @ui("AnYi","Contact")
    def viewContactFile(self,assertDict):
        '''
        :param assertDict:
        :return: 查看通讯录联系人文件
        '''
        # 点击公司通讯录
        self._click(g().get_resource_infor('通讯录页公司通讯录按钮'))
        # 点击联系人
        self._click(g().get_resource_infor('通讯录联系人ui_test2'))
        # 点击文件
        self._click(g().get_resource_infor('联系人信息页文件按钮'))
        self._performAssert('断言查看通讯录联系人文件成功', assertDict)
        self._click_back()
        self._click_back()
        self._click_back()

    @ui("AnYi","Contact")
    def searchContactByPinYin(self,searchContent,assertDict):
        '''
        :param assertDict:
        :return: 通过拼音搜索联系人
        '''
        # 点击搜索图标
        self._click(g().get_resource_infor('通讯录页搜索图标'))
        # 输入搜索联系人
        self._click(g().get_resource_infor('通讯录页搜索输入框'))
        self._text(searchContent)
        self._performAssert('断言通过拼音搜索联系人成功', assertDict)
        self._click_back()
        self._click_back()

    @ui("Contact")
    def searchNotExistsContact(self,searchContent,assertDict):
        '''
        :param searchContent:
        :param assertDict:
        :return: 通讯录搜索联系人失败（输入不存在的联系人）
        '''
        # 点击搜索图标
        self._click(g().get_resource_infor('通讯录页搜索图标'))
        # 输入搜索联系人
        self._click(g().get_resource_infor('通讯录页搜索输入框'))
        self._text(searchContent)
        self._performAssert('断言通讯录搜索联系人失败', assertDict)
        self._click_back()
        self._click_back()

    @ui("AnYi","Contact")
    def findContactByPinYin(self,findContact,assertDict):
        '''
        :param assertDict:
        :return: 按姓名查找联系人，通过拼音查找成功
        '''
        # 点击+号
        self._click(g().get_resource_infor('通讯录页+号图标'))
        # 点击按姓名查找
        self._click(g().get_resource_infor('按姓名查找按钮'))
        # 输入姓名
        self._click(g().get_resource_infor('按姓名查找输入框'))
        self._text(findContact)
        # 点击查找
        self._click(g().get_resource_infor('查找按钮'))
        self._performAssert('断言按姓名查找联系人，通过拼音查找成功',assertDict)
        self._click_back()
        self._click_back()
        self._click_back()

    @ui("AnYi","Contact")
    def findNotExistsContact(self,findContact,assertDict):
        '''
        :param assertDict:
        :return: 按姓名查找不存在联系人
        '''
        # 点击+号
        self._click(g().get_resource_infor('通讯录页+号图标'))
        # 点击按姓名查找
        self._click(g().get_resource_infor('按姓名查找按钮'))
        # 输入姓名
        self._click(g().get_resource_infor('按姓名查找输入框'))
        self._text(findContact)
        # 点击查找
        self._click(g().get_resource_infor('查找按钮'))
        self._click_back()
        self._performAssert('断言按姓名查找不存在联系人失败', assertDict)
        self._click_back()
        self._click_back()

    @ui("AnYi","Contact")
    def clearInputContact(self,findContact,assertDict):
        '''
        :param assertDict:
        :return: 清除查找联系人输入内容
        '''
        # 点击+号
        self._click(g().get_resource_infor('通讯录页+号图标'))
        # 点击按姓名查找
        self._click(g().get_resource_infor('按姓名查找按钮'))
        # 输入姓名
        self._click(g().get_resource_infor('按姓名查找输入框'))
        self._text(findContact)
        # 点击清除
        self._click(g().get_resource_infor('按姓名查找页清除按钮'))
        self._performAssert('断言清除查找联系人输入内容成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("AnYi","Contact")
    def addContactAgain(self,assertDict):
        '''
        :param assertDict:
        :return: 添加联系人后不能进行再次添加
        '''
        # 点击公司通讯录
        self._click(g().get_resource_infor('通讯录页公司通讯录按钮'))
        # 点击添加的联系人
        self._click(g().get_resource_infor('通讯录联系人ui_test3'))
        # 点击加为联系人
        self._click(g().get_resource_infor('加为联系人按钮'))
        time.sleep(1)
        contact = g().get_resource_infor('主页面导航栏第二个按钮通讯录')
        self._wait_ui_appear(contact, lambda ui: ui._click_back())
        # 点击已添加的联系人
        self._click(g().get_resource_infor('已添加的联系人'))
        self._performAssert('断言添加联系人后不能进行再次添加成功',assertDict)
        # 点击删除联系人
        self._click(g().get_resource_infor('删除联系人按钮'))
        # 点击确定
        self._click(g().get_resource_infor('删除联系人确定按钮'))
        self._click_back()

    @ui("AnYi","Contact")
    def addOwnFail(self,assertDict):
        '''
        :param assertDict:
        :return: 不能将自己添加为联系人
        '''
        # 点击公司通讯录
        self._click(g().get_resource_infor('通讯录页公司通讯录按钮'))
        # 点击添加的联系人
        self._click(g().get_resource_infor('通讯录联系人ui_test1'))
        self._performAssert('断言不能将自己添加为联系人成功',assertDict)
        self._click_back()
        self._click_back()

if __name__ == '__main__':
    Contact().enterContact()
