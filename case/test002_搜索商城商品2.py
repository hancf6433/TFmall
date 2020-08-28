# -*- encoding=utf-8 -*-
from common.globall import g

__title__ = "搜索商品"
__author__ = "韩春芳"
__desc__ = "搜索商品"

from po.mall import *
from common.runer import (BaseCase, testLog)
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
        # 指定数据集
        g().group = '搜索商城商品名称'
        # 构造数据
        goodName = g().get_test_data("商品名称")

        # 构造断言数据
        assertDict = {
            "断言搜索商品成功": '''
                #断言搜索商品是否成功
                self.assert_ui_exists(g().get_resource_infor('搜索商品成功商品列表综合按钮'),"搜索商品是否成功？")
            '''
        }

        # 运行流程
        log('进入主界面')
        Mall().searchGood(goodName,assertDict)
