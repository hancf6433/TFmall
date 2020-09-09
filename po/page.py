# -*- encoding=utf-8 -*-
'''
PO类
所有PO类的实例方法的约定：
1、方法的结束界面为返回PO所指界面
2、无PO返回的方法使用单下划线开头（功能性的方法，不涉及界面的跳转）
'''
import re
import time
from typing import Union
from airtest.core.cv import Template
from common.core import BasePorl
from common.globall import g
from common.tools import ui, tools


class Page(BasePorl):
    '''
    页面PO对象
    '''

    def __init__(self) -> object:
        super(Page, self).__init__()
        self.__last_ui_tree=None
        self.__upper_regex=re.compile("([A-Z]*)")

    @ui("page")
    def loginTfBank(self, phone, pwd):
        '''
        登录天府手机银行
        :param phone:登陆手机号
        :param pwd:登陆密码
        :return:
        '''
        # 判断当前登录用户是否为本次case所使用用户，不是则重新登录
        if g().userPhone == phone:
            if self._exists(g().get_resource_infor('app界面')):
                for i in range(10):
                    # 点击返回按钮进行返回，共计点击10次
                    if self._exists(g().get_resource_infor('我的按钮')):
                        self._click(g().get_resource_infor('我的按钮'))
                        try:
                            if g().runCount == 0:
                                # 每执行2次case，返回桌面一次
                                self._flushPocoUiTree()
                            from po.myPage import MyPage
                            return MyPage()
                        except:
                            break
                    # 点击后退或者关闭按钮
                    now = self._get_ui_tree()
                    if now != self.__last_ui_tree:
                        self._click_back()
                    else:
                        if self._exists(g().get_resource_infor('弹窗关闭按钮')):
                            self._click(g().get_resource_infor('弹窗关闭按钮'))
                    self.__last_ui_tree = now
        # 未登录重新进入登陆流程
        from po import other
        otherPo = other.OtherPage()
        homePo = otherPo.enterHomePage()
        userPo = homePo.enterLoginPage()
        # 删除常用设备
        tools.delDevice(phone)
        return userPo.login(phone, pwd)

    @ui("myself")
    def _stopTFBank(self):
        '''
        关闭天府手机银行
        :return:
        '''
        self._stop_app(g().get_resource_infor("app包名"))

    @ui("myself")
    def _startTFBank(self):
        '''
        运行天府手机银行
        :return:
        '''
        self._start_app(g().get_resource_infor("app包名"))

    @ui("page")
    def _waitCicleDisappear(self,count=3):
        '''
        等待转圈圈消失
        :param count:等待次数，默认为3次
        :return:
        '''
        if g().activeDevType=="IOS":
            return
        cicleUi1=g().get_resource_infor('等待圈圈2')
        cicleUi2=g().get_resource_infor('等待圈圈')
        if self._exists(cicleUi2):
            nowUi=cicleUi2
        else:
            nowUi=cicleUi1
        for i in range(count):
            self._wait_ui_disappear(nowUi,60)

    @ui("page")
    def _inputSmsCheckCode(self,error:bool=False):
        '''
        短信验证码输入（针对已自动填充的短信验证码输入，将删除最后一位并重新填写）
        :param error:指示是否输入错误
        :return:
        '''
        done=True
        # 等待请输入短信验证码出现
        self._wait_ui_appear(g().get_resource_infor('请输入短信验证码文本框'))
        # 判断存在的短信验证码是哪一个ui
        if self._exists(g().get_resource_infor('验证码输入框')):
            checkCodeUi=g().get_resource_infor('验证码输入框')
            done=False
        elif self._exists(g().get_resource_infor('U盾认证页短信验证码输入框')):
            checkCodeUi=g().get_resource_infor('U盾认证页短信验证码输入框')
        else:
            raise BaseException("未在当前界面找到对应的短信验证码控件")
        checkCode = self._get_text(checkCodeUi)
        # 提取验证码的最后一位
        checkCode = checkCode[-1:]
        #如果错误标志为真
        if error:
            #todo:记得过来修改这里
            checkCode=int(checkCode)+1
        # 验证码重新输入并提交
        self._inputPwdForNumber("{d}%s" % checkCode,done)

    @ui("page")
    def _inputPwdForLatter(self, text,done:bool=True):
        '''
        天府银行密码键盘输入：字母键盘
        :param text:待输入的字符，英文字符、数字、{c}、{d},其中{d}:代表退格键，{c}:代表完成键
        :param done:指示是否自动点击完成按钮，默认自动点击
        :return:
        '''
        if g().activeDevType=="IOS":
            #针对ios
            if not self._exists(g().get_picture('字符转换按钮.png')):
                #数字
                for i in text:
                    self._click(g().get_resource_infor("按键",keys=i))
            else:
                #字母数字键盘
                for i in text:
                    self._click(g().get_resource_infor("按键",keys=i))
        else:
            #对键入值进行处理
            keyList=tools.textProgress(text)
            size=self._get_screen_size()
            while keyList:
                self.__keyboardClick(size, 2, keyList.pop())
            if done:
                self.__keyboardClick(size, 2, "{c}")

    @ui("page")
    def _inputPwdForNumber(self,text,done:bool=True):
        '''
        天府银行密码键盘输入：针对数字键盘的输入
        :param text:待输入的文字，仅支持数字、{c}、{d}
        :param done:指示是否自动点击完成按钮，默认点击
        :return:
        '''
        # 对键入值进行处理
        keyList = tools.textProgress(text)
        size = self._get_screen_size()
        while keyList:
            self.__keyboardClick(size, 1, keyList.pop())
        if done:
            self.__keyboardClick(size, 1, "{c}")

    def __keyboardClick(self,screenSize:list,keyboardType:int,key:str):
        '''
        点击键盘指定键值
        :param screenSize: 屏幕尺寸
        :param keyboardType: 键盘类型 1:数字键盘 2：字母键盘
        :param key: 删除： {d} {delete}  完成： {c} {complete} 大写锁定键 {caps} {ca}
        :return:
        '''
        keyboard={

            #魅族
            "1080,1920":{
                "数字键盘":{
                    "完成": (978, 1252),
                    "删除": (888, 1823),
                    "0": (542, 1841),
                    "1": (179, 1386),
                    "2": (529, 1386),
                    "3": (900, 1386),
                    "4": (179, 1538),
                    "5": (529, 1538),
                    "6": (900, 1538),
                    "7": (179, 1694),
                    "8": (529, 1694),
                    "9": (900, 1694)
                },
                '字母键盘':{
                    "完成":(978, 1252),
                    "大写锁定":(47, 1685),
                    "删除":(1009,1848),
                    "q": (50, 1536),
                    "w": (158, 1536),
                    "e": (274, 1536),
                    "r": (375, 1536),
                    "1": (54, 1384),
                    "2": (158, 1384),
                    "3": (274, 1384),
                    "4": (375, 1384),
                    "5": (488, 1388),
                    "6": (590, 1388)
                }
            },
            "1080,2340":{
                "数字键盘": {
                    "0": (538, 2282),
                    "1": (180, 1809),
                    "2": (538, 1809),
                    "3": (900, 1809),
                    "4": (180, 1956),
                    "5": (538, 1956),
                    "6": (900, 1956),
                    "7": (180, 2111),
                    "8": (538, 2111),
                    "9": (900, 2111)
                }
            },
            "1080,2244":{
                "数字键盘": {
                    "完成": (978, 1574),
                    "删除": None,
                    "0": (539, 2173),
                    "1": (178, 1719),
                    "2": (535, 1707),
                    "3": (375, 1860),
                    "4": (182, 1870),
                    "5": (543, 1862),
                    "6": (900, 1862),
                    "7": (178, 2025),
                    "8": (539, 2022),
                    "9": (904, 2014)
                },
                '字母键盘': {
                    "完成":  (978, 1574),
                    "大写锁定": (47, 2030),
                    "0": (539, 2173),
                    "1": (178, 1719),
                    "2": (535, 1707),
                    "3": (375, 1860),
                    "4": (182, 1870),
                    "5": (543, 1862),
                    "6": (900, 1862),
                    "7": (178, 2025),
                    "8": (539, 2022),
                    "9": (904, 2014)
                }
            },
            "1440,2560": {
                "数字键盘": {
                    "完成": (1311, 1674),
                    "删除": (1311, 2464),
                    "0": (724, 2474),
                    "1": (220, 1846),
                    "2": (712, 1856),
                    "3": (1190, 1877),
                    "4": (241, 2040),
                    "5": (716, 2062),
                    "6": (1158, 2078),
                    "7": (262, 2273),
                    "8": (701, 2229),
                    "9": (1201, 2234)
                },
                '字母键盘': {
                    "完成": (1311, 1674),
                    "大写锁定": (33, 2298),
                    "0": (1391, 1892),
                    "1": (81, 1893),
                    "2": (237, 1865),
                    "3": (378, 1878),
                    "4": (509, 1870),
                    "5": (651, 1866),
                    "6": (784, 1876)
                }
            },
            "1080,2160": {
                "数字键盘": {
                    "完成": (980, 1498),
                    "删除": (917, 2052),
                    "0": (530,2072 ),
                    "1": (148,1632 ),
                    "2": (521,1613 ),
                    "3":(891,1628),
                    "6": (898,1777 ),
                    "9":(876,1929)
                },
                '字母键盘': {
                    "1":(50,1490),
                    "2":(150,1490),
                    "3":(260,1490),
                    "4":(370,1490),
                    "5":(470,1490),
                    "6":(580,1490),
                    "q":(50,1640),
                    "w":(150,1640),
                    "e":(260,1640),
                    "r":(360,1640),
                    "完成":(960,1346)
                    # "完成": (980, 1498),
                    # "大写锁定": (73, 1930),
                    # "6":(590,1632)
                }
            },
            "图像识别":{
                "完成":g().get_picture("完成"),
                "黄删除":g().get_picture("黄删除"),
                "灰删除":g().get_picture("灰删除"),
                "大写锁定锁":g().get_picture("大写锁定锁"),
                "大写锁定解":g().get_picture("大写锁定解"),
                "0":g().get_picture("0"),
                "1":g().get_picture("1"),
                "2":g().get_picture("2"),
                "3":g().get_picture("3"),
                "4":g().get_picture("4"),
                "5":g().get_picture("5"),
                "6":g().get_picture("6"),
                "7":g().get_picture("7"),
                "8":g().get_picture("8"),
                "9":g().get_picture("9"),
                "a":g().get_picture("a"),
                "b":g().get_picture("b"),
                "c":g().get_picture("c"),
                "d":g().get_picture("d"),
                "e":g().get_picture("e"),
                "f":g().get_picture("f"),
                "g":g().get_picture("g"),
                "h":g().get_picture("h"),
                "i":g().get_picture("i"),
                "j":g().get_picture("j"),
                "k":g().get_picture("k"),
                "l":g().get_picture("l"),
                "m":g().get_picture("m"),
                "n":g().get_picture("n"),
                "o":g().get_picture("o"),
                "p":g().get_picture("p"),
                "q":g().get_picture("q"),
                "r":g().get_picture("r"),
                "s":g().get_picture("s"),
                "t":g().get_picture("t"),
                "u":g().get_picture("u"),
                "v":g().get_picture("v"),
                "w":g().get_picture("w"),
                "x":g().get_picture("x"),
                "y":g().get_picture("y"),
                "z":g().get_picture("z"),
                "A":g().get_picture("UA"),
                "B":g().get_picture("UB"),
                "C":g().get_picture("UC"),
                "D":g().get_picture("UD"),
                "E":g().get_picture("UE"),
                "F":g().get_picture("UF"),
                "G":g().get_picture("UG"),
                "H":g().get_picture("UH"),
                "I":g().get_picture("UI"),
                "J":g().get_picture("UJ"),
                "K":g().get_picture("UK"),
                "L":g().get_picture("UL"),
                "M":g().get_picture("UN"),
                "N":g().get_picture("UN"),
                "O":g().get_picture("UO"),
                "P":g().get_picture("UP"),
                "Q":g().get_picture("UQ"),
                "R":g().get_picture("UR"),
                "S":g().get_picture("US"),
                "T":g().get_picture("UT"),
                "U":g().get_picture("UU"),
                "V":g().get_picture("UV"),
                "W":g().get_picture("UW"),
                "X":g().get_picture("UX"),
                "Y":g().get_picture("UY"),
                "Z":g().get_picture("UZ")
            }
        }
        if "{" in key:
            #特殊键
            key=key.lower()
            #键值转换
            if key in ["{d}","{delete}","{del}","{删除}","{删除键}"]:
                key="删除"
            elif key in ["{c}","{complete}","{完成}","{完成键}"]:
                key="完成"
            elif key in ["{caps}","{ca}","{大写锁定}","{大写锁定键}"]:
                key="大写锁定"
            else:
                raise BaseException("此特殊输入键未处理：{%s}" % key)
        if keyboardType==1:
            keyboardType="数字键盘"
            if key not in ['1','2','3','4','5','6','7','8','9','0',"删除","完成"]:
                raise BaseException("数字键盘，不可输入英文及其他字符：{%s}" % key)
        else:
            keyboardType="字母键盘"
        board=keyboard.get("%s,%s" % (screenSize[0],screenSize[1]))
        if board:
            type=board.get(keyboardType)
            if type:
                #针对具体点的点击
                posKey=key.lower()
                pos=type.get(posKey)
                if pos:
                    self._click((pos[0]/screenSize[0],pos[1]/screenSize[1]))
                    return
        #针对图像的点击
        board = keyboard.get("图像识别")
        if key=="删除":
            #删除键特殊处理
            if self._exists(Template(board.get("灰删除"))):
                self._click(Template(board.get("灰删除")))
            else:
                self._click(Template(board.get("黄删除")))
            return
        elif key=="大写锁定":
            if self._exists(Template(board.get("大写锁定锁"))):
                self._click(Template(board.get("大写锁定锁")))
            else:
                self._click(Template(board.get("大写锁定解")))
            return
        pictureKey=board.get(key)
        if not pictureKey:
            raise BaseException("还未配置此键的图像识别：{%s}" % key)
        self._click(Template(pictureKey))

    @ui('page')
    def _inputPwdByNew(self, text):
        '''
        新的密码输入键盘
        :param text:待输入的文字，仅支持数字、{d}(删除)
        :return:
        '''
        letterKeyBoard = True
        if self._exists(g().get_resource_infor('密码键盘字母键盘切换按钮')):
            letterKeyBoard = False
        if self._exists(g().get_resource_infor('密码键盘熊猫标志')):
            letterKeyBoard = False
        if self._exists(g().get_resource_infor('密码键盘空白格')):
            letterKeyBoard = False
        # 对键入值进行处理
        keyList = tools.newTextProgress(text, letterKeyBoard)
        while keyList:
            self.__keyboardClickByNew(keyList.pop(0))

    @ui("page")
    def __keyboardClickByNew(self, key: str):
        '''
        新的键盘输入点击
        :param key: 删除： {d} {delete}   大写锁定键 {caps} {ca}
        :return:
        '''
        if "{" in key:
            # 特殊键
            key = key.lower()
            # 键值转换
            if key in ["{d}", "{delete}", "{del}", "{删除}", "{删除键}"]:
                self._click(g().get_resource_infor('密码键盘删除按钮'))
            elif key in ["{caps}", "{ca}", "{大写锁定}", "{大写锁定键}"]:
                self._click(g().get_resource_infor('密码键盘大小写锁定键按钮'))
            elif key in ["{nu}"]:
                self._click(g().get_resource_infor('密码键盘数字键盘切换按钮'))
            elif key in ["{le}"]:
                self._click(g().get_resource_infor('密码键盘字母键盘切换按钮'))
            else:
                raise BaseException("此特殊输入键未处理：{%s}" % key)
        else:
            keys = key
            self._click(g().get_resource_infor('密码键盘按钮', keys=str(keys)))

    def _listSelectionBySwipe(self,list:str,
                              willChooseItem:Union[str,Template],
                              focus=None,flushPocoUiTree=True,dragItemToCenter=False):
        '''
        列表控件选择：使用滚动的方式来选择列表中的某指定项目，并点击指定的项目
        :param list:待滚动列表
        :param willChooseItem:需要选中的项
        :param focus:选中项的焦点  默认为中心点
        :param flushPocoUiTree:指示是否主动刷新ui树   默认主动刷新
        :param dragItemToCenter:指示点击选中项时，是否先把选中项拖动到屏幕中央   默认不拖动
        :return:
        '''
        origin = self._get_pos(list)
        size = self._get_size(list)
        taget = [origin[0], origin[1] - (size[1] / 2)]
        while True:
            if self._exists(willChooseItem):
                if dragItemToCenter:
                    self._drag_to_center(willChooseItem)
                self._click(willChooseItem,focus=focus)
                time.sleep(1)
                break
            if self._swipe(origin, taget, duration=0.8):
                raise BaseException("在{%s}未找到{%s}" % (list,willChooseItem))
            if flushPocoUiTree:
                self._flushPocoUiTree()

    def _listSelectionBySearch(self,searchUi:str,searchText:str,clickUi:str,searchButton:str=None):
        '''
        列表控件选择：依靠搜索的方式进行项目选择，
        :param searchUi: 搜索文字输入框
        :param searchText: 待搜索文字
        :param clickUi: 搜索完成需要点击的ui
        :param searchButton: 搜索按钮，输入完文字需要点击的按钮，默认为空
        :return:
        '''
        self._flushPocoUiTree()
        self._wait_ui_apper(searchUi)
        self._click(searchUi)
        self._text(searchText,enter=False)
        if searchButton:
            self._click(searchButton)
        self._wait_ui_apper(clickUi)
        self._click(clickUi)
        time.sleep(1)

    def _dropDownListSelection(self,list,item:str):
        '''
        依靠滑动进行选择的控件，仅仅滑动到需要选择的项，不进行点击选择
        :param list:待滑动的列表
        :param item:待选择项
        :return:
        '''
        #todo：调整逻辑以适配李浩的输入需求
        if not self._exists(item):
            raise BaseException("在{%s}未找到{%s}" % (list,item))
        self._flushPocoUiTree()
        listX,listY=self._get_pos(list)
        origin=self._get_pos(list)
        size=self._get_size(list)
        taget=[origin[0],origin[1]-(size[1]/2)]
        while True:
            itemX,itemY=self._get_pos(item)
            if itemY<listY:
                time.sleep(1)
                break
            if self._swipe(origin, taget, duration=0.5):
                raise BaseException("已经滑动到底部")
            self._flushPocoUiTree()

    @ui("page")
    def _getTipsContent(self):
        '''
        获得弹窗提示文字
        :return:
        '''
        if self._exists(g().get_resource_infor('弹窗消息体文本框')):
            return self._get_text(g().get_resource_infor('弹窗消息体文本框'))
        return ""


    @ui("page")
    def _confirmTips(self):
        '''
        点击弹窗确定按钮，如果有
        :return:
        '''
        if self._exists(g().get_resource_infor('弹窗消息确定按钮')):
            self._click(g().get_resource_infor('弹窗消息确定按钮'))

    @ui("page")
    def _cancelTips(self):
        '''
        点击弹窗取消按钮，如果有
        :return:
        '''
        if self._exists(g().get_resource_infor('弹窗消息取消按钮')):
            self._click(g().get_resource_infor('弹窗消息取消按钮'))

    def _scrollDown(self):
        '''
        向下滚动
        :return:
        '''
        # 向下滚动
        self._scroll(duration=1)
        self._flushUiTree()

    @ui("page")
    def _flushUiTree(self):
        '''
        刷新ui树
        :return:
        '''
        # 回到桌面
        self._home()
        # 再次打开app
        self._startTFAnYi()

    @ui("page")
    def _payingByTFCashier(self,payPwd:str):
        '''
        天府收银台付款
        :param payPwd:支付密码
        :return:
        '''
        self._wait_ui_apper(g().get_resource_infor('立即付款按钮'))
        #获取本次支付金额
        # 点击立即付款
        self._click(g().get_resource_infor('立即付款按钮'))
        # 等待圈圈消失
        self._waitCicleDisapper()
        # 输入支付密码
        self._wait_ui_apper(g().get_resource_infor('支付密码输入框'))
        self._inputPwdForNumber(payPwd)

    @ui("page")
    def _payingByTipsConfirmPayment(self,payPwd:str):
        '''

        付款封装：将弹出确认付款弹窗
        :param payPwd:支付密码
        :return:
        '''
        #todo:增加选卡输入
        ui1=g().get_resource_infor('确认按钮')
        ui2=g().get_resource_infor('立即付款按钮')
        self._flushPocoUiTree()
        apperUi=self._wait_multiple_ui_appear([ui1,ui2])
        if apperUi:
            self._click(apperUi)
        # 等待圈圈消失
        self._waitCicleDisapper()
        self._wait_ui_apper(g().get_resource_infor('支付密码输入框'))
        # 输入支付密码
        self._wait_ui_apper(g().get_resource_infor('支付密码输入框'))
        self._inputPwdForNumber(payPwd)
        if "日终" in self._getTipsContent():
            raise BaseException("弹出提示：{%s}" % self._getTipsContent())

    def _performAssert(self,assertKey,assertDict):
        '''
        执行断言
        :param assertKey: 断言的名字
        :param assertDict:断言字典
        :return:断言成功则返回True
        '''
        if not assertDict:
            return
        assertContent=assertDict.get(assertKey)
        if type(assertContent)==type(self._getTipsContent):
            #如果断言体是一个方法，则执行
            assertContent(self)
            return True
        elif type(assertContent)==str:
            #如果断言体是一个字符串，则调用eval执行
            assertContent = re.sub(r"[\t\v ]", "", assertContent)
            exec(assertContent)
            return True
        elif type(assertContent)==type(None):
            return
        else:
            raise BaseException("断言体类型{%s}不符合要求，必须是可动态执行的str或方法" % type(assertContent))


if __name__ == '__main__':
    Page()._getTipsContent()