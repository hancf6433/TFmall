from common.tools import ui, tools
from po import page
from common.globall import g
from common.core import *

class Back(page.Page):
    def back_mallPage(self):
        '''返回到商城首页'''
        self._wait_ui_appear(g().get_resource_infor('手机银行主导航界面商城按钮'), lambda ui: ui._click_back())