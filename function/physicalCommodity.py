from common.tools import ui, tools
from po import page
from common.globall import g
import time


class Mall(page.Page):
    '''
    商城
    '''

    @ui("mall")
    def searchGood(self, goodName, assertDict):
        '''
        :return: #搜索商品并进入商品详情页面
        '''
        self._click(g().get_resource_infor('手机银行主导航界面商城按钮'))  # 点击商城
        self._click(g().get_resource_infor('商城首页搜索框'))
        self._wait_ui_appear(g().get_resource_infor("搜索页面搜索框"))
        self._click(g().get_resource_infor("搜索页面搜索框"))
        self._text(goodName)
        time.sleep(3)
        self._performAssert('断言搜索商品成功', assertDict)

    def productDetails(self):
        self._click((288,611))    #点击第一件商品（vivo）
        self._wait_ui_appear(g().get_resource_infor("商品详情页立即购买按钮"))








    @ui("mall")
    def back(self):
        self._wait_ui_appear(g().get_resource_infor('手机银行主导航界面商城按钮'), lambda ui: ui._click_back())