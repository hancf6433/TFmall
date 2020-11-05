from common.tools import ui
from po import page
from common.globall import g
import time


class CreditCard(page.Page):
    '''
    天府安逸首页第三屏信用卡应用
    '''

    @ui("AnYi","creditCard")
    def enterCreditCard(self):
        '''
        :return:点击信用卡
        '''
        self._click(g().get_resource_infor('我的应用信用卡'))

    @ui("creditCard")
    def viewHomePage(self,assertDict):
        '''
        :param assertDict:
        :return: 查看信用卡首页
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        self._performAssert('断言查看信用卡首页成功',assertDict)
        self._click_back()

    @ui("creditCard")
    def viewQRCode(self,assertDict):
        '''
        :param assertDict:
        :return: 查看信用卡二维码
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        self._performAssert('断言查看信用卡二维码成功', assertDict)
        self._click_back()

    @ui("creditCard")
    def viewList(self,assertDict):
        '''
        :param assertDict:
        :return: 查看抢单列表
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击抢单
        self._click(g().get_resource_infor('信用卡抢单按钮'))
        self._performAssert('断言查看抢单列表成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("creditCard")
    def searchList(self,searchContent,assertDict):
        '''
        :param assertDict:
        :return: 搜索抢单客户
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击抢单
        self._click(g().get_resource_infor('信用卡抢单按钮'))
        # 点击搜索图标
        self._click(g().get_resource_infor('抢单列表搜索图标'))
        # 点击搜索输入框
        self._click(g().get_resource_infor('搜索输入框'))
        self._text(searchContent)
        # 点击搜索
        self._click(g().get_resource_infor('搜索按钮'))
        self._performAssert('断言搜索抢单池客户成功',assertDict)
        self._click_back()
        self._click_back()
        self._click_back()

    @ui("creditCard")
    def viewToDoList(self,assertDict):
        '''
        :param assertDict:
        :return: 查看我的待办
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击我的待办
        self._click(g().get_resource_infor('信用卡我的待办按钮'))
        self._performAssert('断言查看我的待办成功',assertDict)
        self._click_back()

    @ui("creditCard")
    def viewExclusiveList(self,assertDict):
        '''
        :param assertDict:
        :return:  查看专属客户面签列表
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击我的待办
        self._click(g().get_resource_infor('信用卡我的待办按钮'))
        # 点击面签
        self._click(g().get_resource_infor('面签按钮'))
        self._performAssert('断言查看专属客户面签列表成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("creditCard")
    def searchExclusiveList(self,searchContent,assertDict):
        '''
        :param assertDict:
        :return: 搜索专属待面签客户
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击我的待办
        self._click(g().get_resource_infor('信用卡我的待办按钮'))
        # 点击面签
        self._click(g().get_resource_infor('面签按钮'))
        # 点击搜索图标
        self._click(g().get_resource_infor('专属客户搜索图标'))
        # 点击搜索输入框
        self._click(g().get_resource_infor('搜索输入框'))
        self._text(searchContent)
        # 点击搜索
        self._click(g().get_resource_infor('搜索按钮'))
        self._performAssert('断言搜索专属待面签客户成功', assertDict)
        self._click_back()
        self._click_back()
        self._click_back()

    @ui("creditCard")
    def viewNotExclusiveList(self,assertDict):
        '''
        :param assertDict:
        :return: 查看非专属客户面签页
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击我的待办
        self._click(g().get_resource_infor('信用卡我的待办按钮'))
        # 点击面签
        self._click(g().get_resource_infor('面签按钮'))
        # 点击非专属客户
        self._click(g().get_resource_infor('非专属客户按钮'))
        self._performAssert('断言查看非专属客户面签页成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("creditCard")
    def searchNotInputIDNumberList(self,assertDict):
        '''
        :param assertDict:
        :return: 搜索非专属待面签客户未输入身份证
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击我的待办
        self._click(g().get_resource_infor('信用卡我的待办按钮'))
        # 点击面签
        self._click(g().get_resource_infor('面签按钮'))
        # 点击非专属客户
        self._click(g().get_resource_infor('非专属客户按钮'))
        # 点击身份证输入框
        # self._click(g().get_resource_infor('身份证输入框'))
        # 点击搜索
        self._click(g().get_resource_infor('非专属客户搜索按钮'))
        self._performAssert('断言搜索非专属待面签客户未输入身份证，搜索失败成功',assertDict)
        # 点击确定
        self._click(g().get_resource_infor('确定按钮'))
        self._click_back()
        self._click_back()

    @ui("creditCard")
    def searchInputIDNumberList(self,assertDict):
        '''
        :param assertDict:
        :return: 搜索非专属待面签客户正确身份证
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击我的待办
        self._click(g().get_resource_infor('信用卡我的待办按钮'))
        # 点击面签
        self._click(g().get_resource_infor('面签按钮'))
        # 点击非专属客户
        self._click(g().get_resource_infor('非专属客户按钮'))
        # 点击身份证输入框
        self._click(g().get_resource_infor('身份证输入框'))
        self._text('522425199207176920')
        # 点击搜索
        self._click(g().get_resource_infor('非专属客户搜索按钮'))
        self._performAssert('断言搜搜索非专属待面签客户_正确身份证号，搜索失败成功', assertDict)
        # 点击确定
        self._click(g().get_resource_infor('确定按钮'))
        self._click_back()
        self._click_back()

    @ui("creditCard")
    def viewPatchList(self,assertDict):
        '''
        :param assertDict:
        :return: 查看我的补件列表
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击我的待办
        self._click(g().get_resource_infor('信用卡我的待办按钮'))
        # 点击补件
        self._click(g().get_resource_infor('补件按钮'))
        self._performAssert('断言查看补件列表成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("creditCard")
    def searchPatchList(self,searchContent,assertDict):
        '''
        :param assertDict:
        :return: 搜索补件客户
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击我的待办
        self._click(g().get_resource_infor('信用卡我的待办按钮'))
        # 点击补件
        self._click(g().get_resource_infor('补件按钮'))
        # 点击搜索图标
        self._click(g().get_resource_infor('补件列表搜索图标'))
        # 点击搜索输入框
        self._click(g().get_resource_infor('搜索输入框'))
        self._text(searchContent)
        # 点击搜索
        self._click(g().get_resource_infor('搜索按钮'))
        self._performAssert('断言搜索补件客户成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("creditCard")
    def viewHelpList(self,assertDict):
        '''
        :param assertDict:
        :return: 查看帮助列表
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击帮助
        self._click(g().get_resource_infor('帮助按钮'))
        self._performAssert('断言查看帮助列表成功',assertDict)
        self._click_back()

    @ui("creditCard")
    def viewCustomerList(self,assertDict):
        '''
        :param assertDict:
        :return: 查看我的客户
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击我的客户
        self._click(g().get_resource_infor('我的客户按钮'))
        self._performAssert('断言查看我的客户成功',assertDict)
        self._click_back()

    @ui("creditCard")
    def viewApplyProgressList(self,assertDict):
        '''
        :param assertDict:
        :return: 查看申请进度查询列表
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击我的客户
        self._click(g().get_resource_infor('我的客户按钮'))
        # 点击申请进度
        self._click(g().get_resource_infor('申请进度查询按钮'))
        self._performAssert('断言查看申请进度查询列表成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("creditCard")
    def searchApplyProgressList(self,assertDict):
        '''
        :param assertDict:
        :return: 搜索客户申请进度
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击我的客户
        self._click(g().get_resource_infor('我的客户按钮'))
        # 点击申请进度
        self._click(g().get_resource_infor('申请进度查询按钮'))
        # 点击搜索图标
        self._click(g().get_resource_infor('进度查询列表搜索图标'))
        # 点击搜索输入框
        self._click(g().get_resource_infor('搜索输入框'))
        self._text('test')
        # 点击搜索
        self._click(g().get_resource_infor('搜索按钮'))
        self._performAssert('断言搜索客户申请进度成功', assertDict)
        self._click_back()
        self._click_back()

    @ui("creditCard")
    def customerManageList(self,assertDict):
        '''
        :param assertDict:
        :return: 查看客户管理列表
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击我的客户
        self._click(g().get_resource_infor('我的客户按钮'))
        # 点击客户管理
        self._click(g().get_resource_infor('客户管理按钮'))
        self._performAssert('断言查看客户管理列表成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("creditCard")
    def searchCustomerManageList(self,searchContent,assertDict):
        '''
        :param assertDict:
        :return: 搜索客户管理列表用户
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击我的客户
        self._click(g().get_resource_infor('我的客户按钮'))
        # 点击客户管理
        self._click(g().get_resource_infor('客户管理按钮'))
        # 点击搜索图标
        self._click(g().get_resource_infor('客户管理列表搜索图标'))
        # 点击搜索输入框
        self._wait_ui_appear(g().get_resource_infor('搜索输入框'))
        self._click(g().get_resource_infor('搜索输入框'))
        self._text(searchContent)
        # 点击搜索
        self._click(g().get_resource_infor('搜索按钮'))
        self._performAssert('断言搜索客户管理列表用户成功', assertDict)
        self._click_back()
        self._click_back()

    @ui("creditCard")
    def customerNotActivatedList(self,assertDict):
        '''
        :param assertDict:
        :return: 查看客户管理成功核发未激活列表
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击我的客户
        self._click(g().get_resource_infor('我的客户按钮'))
        # 点击客户管理
        self._click(g().get_resource_infor('客户管理按钮'))
        # 点击未激活
        self._click(g().get_resource_infor('未激活按钮'))
        self._performAssert('断言查看客户管理成功核发未激活列表成功',assertDict)
        self._click_back()
        self._click_back()

    @ui("creditCard")
    def customerOverdueList(self,assertDict):
        '''
        :param assertDict:
        :return: 查看客户管理逾期列表
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击我的客户
        self._click(g().get_resource_infor('我的客户按钮'))
        # 点击客户管理
        self._click(g().get_resource_infor('客户管理按钮'))
        # 点击逾期
        self._click(g().get_resource_infor('逾期按钮'))
        self._performAssert('断言查看客户管理逾期列表成功', assertDict)
        self._click_back()
        self._click_back()

    @ui("creditCard")
    def searchInputErrorIDNumberList(self,assertDict):
        '''
        :param assertDict:
        :return: 搜索非专属待面签客户，输入少于18位身份证号
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击我的待办
        self._click(g().get_resource_infor('信用卡我的待办按钮'))
        # 点击面签
        self._click(g().get_resource_infor('面签按钮'))
        # 点击非专属客户
        self._click(g().get_resource_infor('非专属客户按钮'))
        # 点击身份证输入框
        self._click(g().get_resource_infor('身份证输入框'))
        self._text('52242519920717692')
        # 点击搜索
        self._click(g().get_resource_infor('非专属客户搜索按钮'))
        self._performAssert('断言搜索非专属待面签客户_输入少于18位身份证号,搜索失败', assertDict)
        # 点击确定
        self._click(g().get_resource_infor('确定按钮'))
        self._click_back()
        self._click_back()

    @ui("creditCard")
    def searchInputNotNumberList(self,assertDict):
        '''
        :param assertDict:
        :return: 搜索非专属待面签客户，输入非数字
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击我的待办
        self._click(g().get_resource_infor('信用卡我的待办按钮'))
        # 点击面签
        self._click(g().get_resource_infor('面签按钮'))
        # 点击非专属客户
        self._click(g().get_resource_infor('非专属客户按钮'))
        # 点击身份证输入框
        self._click(g().get_resource_infor('身份证输入框'))
        self._text('qazwsxedcrfvtgbyhn')
        # 点击搜索
        self._click(g().get_resource_infor('非专属客户搜索按钮'))
        self._performAssert('断言搜索非专属待面签客户_输入非数字,搜索失败', assertDict)
        # 点击确定
        self._click(g().get_resource_infor('确定按钮'))
        self._click_back()
        self._click_back()

    @ui("creditCard")
    def viewHelpDetailList(self,assertDict):
        '''
        :param assertDict:
        :return: 查看帮助详情
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击帮助
        self._click(g().get_resource_infor('帮助按钮'))
        # 点击帮助内容
        self._click(g().get_resource_infor('帮助内容'))
        self._performAssert('断言查看帮助详情成功', assertDict)
        self._click_back()
        self._click_back()

    @ui("creditCard")
    def customerOverdueSwitchNotActivatedList(self,assertDict):
        '''
        :param assertDict:
        :return: 客户管理逾期列表切换到成功核发未激活列表
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('信用卡首页'))
        # 点击我的客户
        self._click(g().get_resource_infor('我的客户按钮'))
        # 点击客户管理
        self._click(g().get_resource_infor('客户管理按钮'))
        # 点击逾期
        self._click(g().get_resource_infor('逾期按钮'))
        # 点击成功核发
        self._click(g().get_resource_infor('成功核发按钮'))
        # 点击未激活
        self._click(g().get_resource_infor('未激活按钮'))
        self._performAssert('断言客户管理逾期列表切换到成功核发未激活列表成功', assertDict)
        self._click_back()
        self._click_back()

if __name__ == '__main__':
    CreditCard().enterCreditCard()
