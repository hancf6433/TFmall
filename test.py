# from poot.core.api import Poot
# from common import *
# from common.tools import ui
# from po import page
# import time
# from common.tools import ui, tools
# from common.globall import g

#poot=poot(name="android.widget.ListView")


#print(poot().get_tree())

# -*- encoding=utf-8 -*-
from common.globall import g

from po.other import *
from po.mall import *
from common.runer import (BaseCase, testLog)
from airtest.core.helper import log
from function.login import *
from airtest.core.helper import log


class Test(BaseCase):

    @classmethod
    def setUpClass(cls):
        # 初始化父类
        cls.file = __file__
        super().setUpClass()

    # 测试的用例需要用testLog装饰器装饰
    @testLog
    def test(self):
        # 指定登录数据集
        g().group = '商城UI自动化测试账号2'
        # 构造数据
        userName = g().get_test_data("用户名")
        vagueUserName = g().get_test_data("模糊用户名")
        loginPwd = g().get_test_data("密码")

        # 构造断言数据
        assertDict1 = {
            "断言登录成功": '''
                        #登录成功断言
                        self.assert_ui_exists(g().get_resource_infor('我的页面设置按钮'),"断言登录成功")
                    '''
        }

        #运行流程
        log('登录手机银行')
        Login().login(userName, vagueUserName, loginPwd, assertDict=assertDict1)

        # 指定数据集
        g().group = '搜索商城商品名称'
        # 构造数据
        goodName = g().get_test_data("商品名称")

        # 构造断言数据
        assertDict2 = {
            "断言搜索商品成功": '''
                        #断言搜索商品是否成功
                        self.assert_ui_exists(g().get_resource_infor('搜索有结果'),"断言搜索商品成功")
                    '''
        }

        # 运行流程
        log('搜索商城商品')
        Mall().searchGood(goodName, assertDict=assertDict2)  #搜索商城商品






