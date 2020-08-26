# -*- encoding=utf-8 -*-
from common.globall import g

__title__ = "登录"
__author__ = "韩春芳"
__desc__ = "用户登录，用户名输入错误"

from po.other import Other
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
        g().group='商城UI自动化测试账号1'

        # 构造数据
        userName = g().get_test_data("用户名")
        loginPwd = g().get_test_data("密码")

        # 构造断言数据
        assertDict = {
            "断言登录失败": '''
                #登录失败断言
                self.assert_ui_exists(g().get_resource_infor('登录页登录按钮'),"登录是否失败")
            '''
        }

        # 运行流程
        log('进入主界面')
        login=Other().enterLoginPage()
        login.login(userName,loginPwd,assertDict=assertDict)

