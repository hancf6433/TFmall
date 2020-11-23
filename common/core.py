# -*- encoding=utf-8 -*-
'''
封装和相关框架方法
'''
import functools
import json
import time
from typing import Union

from airtest.core.android.adb import ADB
from airtest.core.cv import Template
from airtest.core.helper import logwrap
from poco.exceptions import PocoNoSuchNodeException
from poot.core.uIProxy import UiProxy

import common.setting as ST
from common.globall import g
from poco.proxy import UIObjectProxy
from airtest.utils.logger import get_logger
from airtest.core.api import (device,swipe,assert_not_exists,assert_exists,wait,exists,install, wake, start_app,stop_app,uninstall,home,assert_equal,assert_not_equal,text,keyevent,touch)
from airtest.core.helper import log
#加上airtest.是方便获取到父日志记录器
from common.ui import PocoUi, PootUi, Coordinate, Picture, Key

LOGGING = get_logger("airtest.||%s||" % __name__)
#动作输出器
def infowrap(fux):
    '''
    装饰器：动作装饰器
    :param fux:
    :return:
    '''
    LOGGING.warn("加载动作：<%s>" % fux.__name__[1:])
    @functools.wraps(fux)
    def wrappear(self,*args,**kwargs):
        method="<%s>:" % fux.__name__[1:]
        data=method
        for arg in args:
            if type(arg) in [PocoUi,PootUi,Picture,Coordinate,Key]:
                data+="%s:%s ," % (str(arg.name),str(arg.print))
            else:
                data+="%s ," % str(arg)
        for key,value in kwargs.items():
            if type(value) in [PocoUi,PootUi,Picture,Coordinate,Key]:
                data+="%s=%s ," % (str(key),str(value.print))
            else:
                data+="%s=%s ," % (str(key),str(value))
        LOGGING.warning("--开始："+data[:-2])
        result=None
        try:
            result=fux(self,*args,**kwargs)
        except PocoNoSuchNodeException as e:
            # 回到桌面
            # 再次打开app
            time.sleep(1)
            try:
                result = fux(self, *args, **kwargs)
            except:
                raise
            else:
                return result
        except:
            raise
        else:
            return result
        finally:
            LOGGING.warning("结束：%s%s" % (method,str(result)))
    return wrappear
#底层封装
class BasePorl(object):
    #查找时间间隔
    __find_time_gaps=ST.FIND_TIME_GAPS
    def __init__(self):
        '''
        核心封装类
        '''
        self.__last_tree="" #type:str

    def __pre_action(self):
        '''
        动作执行前
        :return:
        '''
        time.sleep(ST.FIND_TIME_GAPS)

    @infowrap
    def _exists(self,ui:Union[PocoUi,PootUi,Picture],**kw):
        '''
        是否存在此控件
        :param ui:poco\poot\图片
        :param kw:常规查询的其他参数
        :return:
        '''
        # 参数校验
        self.__para_check(ui, [PocoUi,PootUi,Picture])
        # 逻辑处理
        if type(ui) == Picture:
            return exists(ui.getTemplate())
        self.__pre_action()
        try:
            if type(ui) == PocoUi:
                u = self.__poco(ui.info, **kw)
                return u.exists()
            if type(ui)==PootUi:
                return self.__poot(ui.info) != None
        except:
            return False
        raise BaseException("不支持对类型为{}的操作".format(type(ui)))


    @infowrap
    def _len(self,ui:Union[PocoUi,PootUi],**kw):
        '''
        计算此ui对象的数目
        :param ui:poco\poot\图片
        :param kw:常规查询的其他参数
        :return:
        '''
        self.__para_check(ui, [PocoUi,PootUi])
        # 逻辑处理
        if type(ui)==PocoUi:
            u=self.__poco(ui.info,**kw)
            return len(u)
        elif type(ui)==PootUi:
            return self.__poot(ui.info).get_node_count()
        else:
            raise BaseException("不支持对类型为{}的操作".format(type(ui)))


    @infowrap
    def _get_text(self,ui:Union[PocoUi,PootUi],**kw):
        '''
        返回此控件的文字
        :param ui: QS字符串、POCO链式调用字符串,常规查询
        :param kw:常规查询其他参数
        :return:
        '''
        #参数校验
        self.__para_check(ui,[PocoUi,PootUi])
        #逻辑处理
        if type(ui)==PootUi:
            return self.__poot(ui.info).get_text()
        elif type(ui)==PocoUi:
            u = self.__poco(ui.info, **kw)
            if g().activeDevType == "IOS":
                return u.get_name()
            else:
                return u.get_text()
        else:
            raise BaseException("不支持对类型为{}的操作".format(type(ui)))



    @infowrap
    def _is_enabled(self,ui:PocoUi,**kw):
        '''
        判断控件是否可以操作
        :param ui:poco
        :param kw:
        :return:
        '''
        # 参数校验
        self.__para_check(ui, [PocoUi])
        # 逻辑处理
        if type(ui)==PocoUi:
            u = self.__poco(ui.info, **kw)
            return u.attr("enabled")
        else:
            raise BaseException("不支持对类型为{}的操作".format(type(ui)))

    @infowrap
    def _click(self,ui:Union[PocoUi,PootUi,Picture,Coordinate],focus:tuple=None,times=None,onlyOne=True,assertExist=True,**kw):
        '''
        点击
        :param ui: poco\poot\picture\coordinate
        :param focus:点击焦点，仅支持【poco和poot】
        :param times:点击时长，单位秒，仅支持图像识别】【poco链式字符串】【poot链式字符串】
        :param onlyOne:多个控件是否都点击，仅支持【poco】
        :param kw:其他查询参数
        :return:
        '''
        #尝试先等待控件出现
        if assertExist:
            if(type(ui) in [PocoUi,PootUi,Picture]):
                self._wait_ui_appear(ui)
        #检查入参
        self.__para_check(ui,[PocoUi,PootUi,Picture,Coordinate])
        #图像
        if type(ui)==Picture:
            if times==None:
                touch(ui.getTemplate(), 1, **kw)
            else:
                touch(ui.getTemplate(),times,**kw)
        #坐标
        elif type(ui)==Coordinate:
            if g().isThePootUsed():
                g().activePoot.tap_x_y(ui.x,ui.y)
            else:
                g().activePoco.click((ui.x,ui.y))
        #poot和poco链式
        elif type(ui)==PootUi:
            u = self.__poot(ui.info)
            if not onlyOne:
                for i in u:
                    i.tap(focus, times)
            else:
                u.tap(focus, times)
        elif type(ui)==PocoUi:
            u=self.__poco(ui.info)
            #设置焦点
            if not onlyOne:
                for i in u:
                    i=self.__set_focus(i,focus)
                    if times!=None:
                        i.long_click(times)
                    else:
                        i.click()
            else:
                    u=self.__set_focus(u,focus)
                    if times!=None:
                        u.long_click(times)
                    else:
                        u.click()
        else:
            raise BaseException("不支持对类型为{}的操作".format(type(ui)))

    def __set_focus(self,ui:UIObjectProxy,focus:tuple):
        '''
        设置控件的焦点
        :param ui:
        :param focus:
        :return:
        '''
        if focus==None:
            return ui
        return ui.focus(focus)


    @infowrap
    def _wait_ui_appear(self,ui:Union[PocoUi,PootUi,Picture],actionFunc=None,timeout=ST.TIME_OUT_ABOUT_WAIT_METHOD, intervalfunc=None,**kw) -> object:
        '''
        等待对应ui出现
        :param ui: 图像识别、qs和链式调用字符串、poco常规查询
        :param timeout: 等待超时时间
        :param intervalfunc:查找失败调用方法   图像识别专用
        :param kw:其他查询参数
        :return:
        '''
        #检查参数
        self.__para_check(ui,[PocoUi,PootUi,Picture])
        #图像
        if type(ui)==Picture:
            wait(ui.getTemplate(),timeout,self.__find_time_gaps,intervalfunc)
        elif type(ui) in [PocoUi,PootUi]:
            start = time.time()
            while not self._exists(ui, **kw):
                if actionFunc:
                    actionFunc(self)
                time.sleep(self.__find_time_gaps)
                if time.time() - start > timeout:
                    raise BaseException("等待控件{%s}出现超时：{%s}" % (ui.info, timeout))
        else:
            raise BaseException("不支持对类型为{}的操作".format(type(ui)))

    @infowrap
    def _wait_ui_disappear(self,ui:Union[PocoUi,PootUi,Picture],timeout=ST.TIME_OUT_ABOUT_WAIT_METHOD,**kw):
        '''
        等待控件消失
        :param ui: QS语句、常规查询、ui代理对象、图像识别
        :param timeout: 超时时间
        :param kw: 其他附加查询参数
        :return:None
        '''
        # 检查参数
        self.__para_check(ui, [PocoUi,PootUi,Picture])
        #由于官方提供的方法，不能起到正确的作用，使用自己写的方法替换
        start = time.time()
        while self._exists(ui,**kw):
            time.sleep(self.__find_time_gaps)
            if time.time() - start > timeout:
                raise BaseException("等待控件{%s}消失超时：{%s}" % (ui.name,timeout))

    @infowrap
    def _text(self,msg, enter=True, **kwargs):
        '''
        输入文字(使用输入法输入）
        :param msg:待输入文字
        :param enter:是否点击enter回车符
        :param kwargs:其他参数
        :return:
        '''
        text(str(msg),enter,**kwargs)

    @infowrap
    def _set_text(self,ui:Union[PootUi,PocoUi],text:str,**kw):
        '''
        给指定控件设置文字
        :param ui: 控件
        :param text:要输入的文字
        :param kw: 其他附加查询参数
        :return:
        '''
        # 参数校验
        self.__para_check(ui, [PootUi,PocoUi])
        # 逻辑处理
        if type(ui)==PootUi:
            self.__poot(ui.info).set_text(text)
        elif type(ui)==PocoUi:
            u = self.__poco(ui.info, **kw)
            if g().activeDevType=="IOS":
                u.click()
                if self._exists(g().get_resource_infor('清除文本')):
                    self._click(g().get_resource_infor('清除文本'))
                self._text(str(text))
            else:
                u.set_text(str(text))
        else:
            raise BaseException("不支持对类型为{}的操作".format(type(ui)))


    @infowrap
    def _click_back(self):
        '''
        点击后退按钮
        :return:
        '''
        self.__pre_action()
        if g().activeDevType=="IOS":
            self._click(Coordinate("匿名","0.069, 0.062"))
            pass
        else:
            self._keyevent('KEYCODE_BACK')

    @infowrap
    def _wait_multiple_ui_appear(self,uiList:list,timeout=ST.TIME_OUT_ABOUT_WAIT_METHOD)->Union[PocoUi,PootUi,Picture]:
        '''
        等待多个控件出现，并将出现的控件返回
        :param uiList: 待出现控件列表   图像识别、qs和链式调用字符串
        :param timeout: 超时时间
        :return: UIObjectProxy
        '''
        #参数校验
        self.__para_check(uiList,[list])
        #逻辑
        start = time.time()
        while True:
            for ui in uiList:
                if self._exists(ui):
                    return ui
            if time.time() - start > timeout:
                raise BaseException("所有控件均未在{%s}时间内出现：{%s}" % (timeout,uiList))
            time.sleep(self.__find_time_gaps)

    @infowrap
    def _swipe(self, ui1: Union[Picture,Coordinate,PocoUi],ui2:Union[Picture,Coordinate] = None, direction:tuple=None, focus:tuple=None,duration=0.5,**kw):
        '''
        根据指定的点或者方向进行滑动
        :param ui1: 滑动起始坐标、图像
        :param ui2: 滑动结束坐标、图像
        :param direction: 滑动方向
        :param duration: 滑动时长
        :return:
        '''
        nowUiTree = self._get_ui_tree()
        if self.__last_tree == nowUiTree:
            return True
        #校验参数
        self.__para_check(ui1,[Picture,Coordinate,PocoUi])
        self.__para_check(ui2,[Picture,Coordinate])
        #同时都为图片
        self.__last_tree = self._get_ui_tree()
        if type(ui1)==Picture and type(ui2)==Picture:
            swipe(ui1.getTemplate(),ui2.getTemplate(),direction,duration,**kw)
        #同时都为坐标
        elif type(ui1)==Coordinate and type(ui2)==Coordinate:
            if g().isThePootUsed():
                g().activePoot.swipe(ui1.x,ui1.y,ui2.x,ui2.y,int(duration))
            else:
                g().activePoco.swipe((ui1.x,ui1.y),(ui2.x,ui2.y),direction,duration)
        #ui1为poco，方向不为空时
        elif type(ui1)==PocoUi and direction!=None:
            u1=self.__poco(ui1.info)
            u1.swipe(direction,focus,duration)
        else:
            raise BaseException("不支持的类型组合操作")

    @infowrap
    def _drag_to_center(self,ui:Union[PocoUi,PootUi]):
        '''
        尝试将ui拖至屏幕中央
        :param ui1:
        :return:
        '''
        #校验参数
        self.__para_check(ui,[PocoUi,PootUi])
        if type(ui)==PocoUi:
            u1 = self.__poco(ui.info)
            u1.drag_to((0.5, 0.5))
        elif type(ui)==PootUi:
            x,y=self.__poot(ui.info).get_focus_x_y()
            g().activePoot.swipe(x,y,0.5,0.5)
        else:
            raise BaseException("不支持对类型为{}的操作".format(type(ui)))



    @infowrap
    def _drag(self,ui1:Union[PocoUi,Picture,PootUi],ui2:Union[PocoUi,Picture,PootUi],ui1focus:tuple=None,ui2focus:tuple=None,duration=2):
        '''
        从ui1拖动至ui2，支持图像和poco
        :param ui1:
        :param ui2:
        :param ui1focus:
        :param ui2focus:
        :param duration:
        :return:
        '''
        #校验参数
        self.__para_check(ui2, [PocoUi,Picture,PootUi])
        #坐标
        if type(ui1)==PocoUi and type(ui2)==PocoUi:
            u1=self.__poco(ui1.info)
            self.__set_focus(u1,ui1focus)
            u2 = self.__poco(ui2.info)
            self.__set_focus(u2, ui2focus)
            u1.drag_to(u2, duration)
        elif type(ui1)==Picture and type(ui2)==Picture:
            swipe(ui1.getTemplate(),ui2.getTemplate())
        elif type(ui1)==PootUi and type(ui2)==PootUi:
            ui1x,ui1y=self.__poot(ui1.info).get_focus_x_y(ui1focus)
            ui2x,ui2y=self.__poot(ui2.info).get_focus_x_y(ui2focus)
            g().activePoot.swipe(ui1x,ui1y,ui2x,ui2y,duration)
        else:
            raise BaseException("不支持的类型组合操作")




    @infowrap
    def _scroll(self,ui:[PocoUi]=None,direction:str="vertical",percent:float=0.6,duration:float=2.0,**kw):
        '''
        滚动,
        :param ui:滚动的ui
        :param direction:滚动的方向
        :param percent:
        :param duration:滚动时间 秒
        :return:if True 已滚动到底部
        '''
        # 校验参数
        nowUiTree=self._get_ui_tree()
        if self.__last_tree==nowUiTree:
            return True
        if type(ui)==PocoUi:
            u = self.__poco(ui.info, **kw)
            u.scroll(direction, percent, duration)
            self.__last_tree = self._get_ui_tree()
        elif ui==None:
           if g().isThePootUsed():
               g().activePoot.scroll(direction=direction,percent=percent,duration=duration*1000)
           else:
               g().activePoco.scroll(direction,percent,duration)
        else:
            raise BaseException("不支持对类型为{}的操作".format(type(ui)))

    def _get_ui_tree(self):
        '''
        获取ui树
        :return:
        '''
        if g().isThePootUsed():
            return g().activePoot.get_ui()
        else:
            ui = g().activePoco.agent.hierarchy.dump()
            return json.dumps(ui, indent=4)

    @infowrap
    def _get_pos(self,ui:PocoUi,focus:Union[tuple,list]=None,**kw):
        '''
        返回此控件的pos
        :param ui: QS字符串、POCO链式调用字符串
        :return:
        '''
        # 参数校验
        self.__para_check(ui, [PocoUi])
        # 逻辑处理
        u = self.__poco(ui.info, **kw)
        return u.get_position(focus)

    @infowrap
    def _get_size(self,ui:PocoUi,**kw):
        '''
        返回控件尺寸
        :param ui:
        :param kw:
        :return:
        '''
        #参数校验
        self.__para_check(ui,[PocoUi])
        #逻辑处理
        u = self.__poco(ui.info, **kw)
        return u.get_size()

    #参数检查
    def __para_check(self,para,typeList):
        '''
        校验参数是否符合传入的类型列表，如果不符合则抛出错误
        :param para:
        :param typeList:
        :return:
        '''
        if type(para) not in typeList:
            raise ValueError("传入参数错误，仅支持{%s},不支持{%s}" % (typeList,type(para)))

    ###poco相关方法####
    def __poco(self,name:Union[UIObjectProxy,str]=None,**kw)->Union[UIObjectProxy,None]:
        '''
        仅返回uiproxy对象,无论是否存在此控件
        :param name:常规查询、ui代理对象、链式查询字符串(由airtestide生成的链式字符串）
        :param kw:其他查询参数
        :return:UIObjectProxy
        '''
        if type(name) is UIObjectProxy:
            return name
        if name!=None and len(name)>0 and name[0]=="p":
            qs=name.replace("poco(",ST.POCO_BEGIN_HEAD)
            uiObjectProxy=eval(qs)
            return uiObjectProxy
        return g().activePoco(name,**kw)
    ###poot相关方法
    def __poot(self,chain:str)->UiProxy:
        '''
        poot调用,查找到则返回POOT的ui代理，否则返回None
        :param chain:
        :return:
        '''
        qs=chain.replace("poot(",ST.POOT_BEGIN_HEAD)
        uiProxy=eval(qs)
        return uiProxy

    #airtest方法
    @infowrap
    def _install(self,filePath):
        '''
        安装指定目录文件
        :param filePath:
        :return:
        '''
        install(filePath)

    @infowrap
    def _wake(self):
        '''
        唤醒设备
        :return:
        '''
        wake()

    @infowrap
    def _start_app(self,package:Key, activity=None):
        '''
        启动指定app
        :return:
        '''
        start_app(package.value, activity)



    @infowrap
    def _stop_app(self,package:Key):
        '''
        关闭app
        :param package:app包名
        :return:
        '''
        stop_app(package.value)

    @infowrap
    def _get_screen_size(self):
        '''
        获得屏幕尺寸
        :return:
        '''
        if g().isThePootUsed():
            return g().activePoot.get_screen_size()
        return g().activePoco.get_screen_size()

    @infowrap
    def _get_top_activity(self):
        '''
        仅针对安卓：获得当前activity
        :return:
        '''
        adb:ADB=device()
        return adb.get_top_activity()

    @infowrap
    def _multiple_points_swipe(self,uis:Union[tuple],duration=0.8, steps=5,**kw):
        '''
        多点滑动
        :param ui:
        :return:
        '''
        list=[]
        if type(uis) == tuple:
            for ui in uis:
                if "poot" in ui:
                    g().activePoot.freeze()
                    list.append(self.__poot(ui).get_focus_x_y())
                    g().activePoot.clear_freezed()
                elif "poco" in ui:
                    x,y=self.__poco(ui, **kw).get_position()
                    width,height=g().activePoco.get_screen_size()
                    x=x*width
                    y=y*height
                    list.append((x,y))
                else:
                    list.append(ui)
        g().activeDev.minitouch.swipe_along(list,duration,steps)

    @infowrap
    def _uninstall(self, package):
        '''
        卸载app
        :param package:
        :return:
        '''
        uninstall(package)

    @infowrap
    def _home(self):
        '''
        回到桌面
        :return:
        '''
        home()

    @infowrap
    def _keyevent(self,keyname, **kwargs):
        '''
        执行keyevent
        :param keyname:
        :param kwargs:
        :return:
        '''
        keyevent(keyname,**kwargs)

    '''
    日志
    '''
    def log(self,message, traceback=""):
        '''
        输出文字到报告
        :param message: log message
        :param traceback: log traceback if exists, use traceback.format_exc to get best format
        :return:
        '''
        log(message,traceback)

    '''
    切换设备
    '''

    def setActiveDev(self,devName:str):
        '''
        切换活动设备，此方法全局只需要调用一次
        :param devName:
        :return:
        '''
        g().setActiveDev(devName)

    '''
    断言
    '''
    def assert_not_equal(self,first,second,msg=""):
        '''
        断言相等
        :param first:
        :param second:
        :param msg:
        :return:
        '''
        assert_not_equal(first,second,msg)

    def assert_contains(self,first,second,msg=""):
        '''
        断言second是否被first包含
        :param first:
        :param second:
        :param msg:
        :return:
        '''
        assert_contains(first,second,msg)

    def assert_ui_exists(self, ui:Union[Picture,PootUi,PocoUi], msg="",**kw):
        '''
        ui对象，断言ui对象是否存在
        :param ui: 控件
        :param msg: 附加到报告的信息
        :param kw:其他参数
        :return:
        '''
        #参数校验
        self.__para_check(ui, [Picture,PootUi,PocoUi])
        if type(ui)==Picture:
            assert_exists(ui.getTemplate(),msg)
        elif type(ui) in [PocoUi,PootUi]:
            assert_ui_exists(ui.name,self._exists(ui),msg)

    def assert_ui_not_exists(self, ui:Union[Picture,PootUi,PocoUi], msg="",**kw):
        '''
        ui对象，断言ui对象不存在
        :param ui: 控件
        :param msg: 附加到报告的信息
        :param kw:其他参数
        :return:
        '''
        #参数校验
        self.__para_check(ui, [Picture,PootUi,PocoUi])
        if type(ui)==Picture:
            assert_not_exists(ui.getTemplate(),msg)
        if type(ui)in [PocoUi,PootUi]:
            assert_ui_not_exists(ui.name,not self._exists(ui),msg)

    def assert_equal(self, first, second, msg=""):
        '''
        断言相等
        :param first:第一个
        :param last:第二个
        :param msg:信息
        :return:
        '''
        assert_equal(first, second, msg)
#断言
@logwrap
def assert_ui_exists(uiName,assert_res,msg=""):
    '''
    因为UIObjectProxy对象直接断言会出错，所以换种方式调用
    :param uiName: 断言的ui对象
    :param assert_res: 断言结果
    :param msg: 附加消息
    :return:
    '''
    if not assert_res:
        raise AssertionError("%s does not exist in screen, message: %s" % (uiName, msg))

@logwrap
def assert_ui_not_exists(uiName,assert_res,msg=""):
    '''
        因为UIObjectProxy对象直接断言会出错，所以换种方式调用
        :param uiName: 断言的ui对象
        :param assert_res: 断言结果
        :param msg: 附加消息
        :return:
        '''
    if not assert_res:
        raise AssertionError("%s exist in screen, message: %s" % (uiName, msg))

@logwrap
def assert_contains(first,second,msg=""):
    '''
    断言second是否被first包含
    :param first:
    :param second:
    :param msg:
    :return:
    '''
    if not (second in first):
        raise AssertionError("%s does not contains %s , message: %s" % (first, second, msg))



BasePorl()._click_back()