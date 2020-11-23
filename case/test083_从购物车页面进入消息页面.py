# -*- encoding=utf-8 -*-
from common.globall import g

__title__ = "从购物车页面进入消息页面"
__author__ = "韩春芳"
__desc__ = "test083"

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
        # 构造断言数据
        assertDict = {
            "进入消息页面成功": '''
                                self.assert_ui_exists(g().get_resource_infor('消息页面'),"断言进入消息页面成功")
                            '''
        }

        # 运行流程
        log("从购物车进入消息中心")
        Mall().enterShoppingCart(assertDict=assertDict)  # 从购物车进入消息页面
        Mall().back()  #返回到商城界面
