# -*- encoding=utf-8 -*-
from common.globall import g

__title__ = "登录手机银行"
__author__ = "韩春芳"
__desc__ = "用户登录手机银行"

# from po.other import Other
from function.login import *
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
        g().group='商城UI自动化测试账号2'
        # 构造数据
        userName = g().get_test_data("用户名")
        vagueUserName = g().get_test_data("模糊用户名")
        loginPwd = g().get_test_data("密码")

        # 构造断言数据
        assertDict = {
            "断言登录成功": '''
                #登录成功断言
                self.assert_ui_exists(g().get_resource_infor('我的页面设置按钮'),"断言登录成功")
            '''
        }

        # 运行流程
        log('登录手机银行')
        Login().login(userName, vagueUserName, loginPwd, assertDict=assertDict)
