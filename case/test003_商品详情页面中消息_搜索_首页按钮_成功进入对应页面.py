# -*- encoding=utf-8 -*-
from common.globall import g

__title__ = "商品详情页面中消息_搜索_首页按钮_成功进入对应页面"
__author__ = "邵佳"
__desc__ = "test003"
from po.other import *
from po.mall import *
from common.runer import (BaseCase, testLog)
from airtest.core.helper import log
from function.login import *
from common.core import *


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
        g().group = '商城测试案例003'
        # 构造数据
        userName = g().get_test_data("用户名")
        vagueUserName = g().get_test_data("模糊用户名")
        loginPwd = g().get_test_data("密码")
        goodName = g().get_test_data("商品名称")

        # 构造断言数据
        assertDict = {
            "断言进入商品详情页成功": '''
                               #断言进入商品详情页成功
                               self.assert_ui_exists(g().get_resource_infor('商品详情页加入购物车按钮'),"断言进入商品详情页成功")
                            ''',
            "断言进入消息页面成功": '''
                               #断言进入消息页面成功
                               self.assert_ui_exists(g().get_resource_infor('消息页面'),"断言进入消息页面成功")
                            ''',
            "断言进入搜索页面成功": '''
                               #断言进入搜索页面成功
                               self.assert_ui_exists(g().get_resource_infor('商城搜索页面'),"断言进入搜索页面成功")
                            ''',
            "断言进入首页页面成功": '''
                               #断言进入首页页面成功
                               self.assert_ui_exists(g().get_resource_infor('商城首页'),"断言进入首页页面成功")
                            '''
        }

        #运行流程
        log('登录手机银行')
        Login().login(userName, vagueUserName, loginPwd)
        time.sleep(2)
        Mall().getIntoGoodsDetail(goodName, assertDict=assertDict)  #搜索商城商品并进入商品详情页面
        time.sleep(2)
        Mall().checkMessageInGoodsDetail(assertDict=assertDict)   #检验商品详情页面消息按钮
        time.sleep(2)
        Mall().checkSearchInGoodsDetail(assertDict=assertDict)    #检验商品详情页面搜索按钮
        time.sleep(2)
        Mall().checkHomepageInGoodsDetail(assertDict=assertDict)  #检验商品详情页面首页按钮

