from common.tools import ui
from po import page
from common.globall import g
import time


class Attendance(page.Page):
    '''
    天府安逸首页第三屏智能考勤应用
    '''

    @ui("attendance")
    def enterAttendance(self):
        '''
        :return:点击智能考勤
        '''
        self._click(g().get_resource_infor('我的应用智能考勤'))

    @ui("attendance")
    def viewHomePage(self,assertDict):
        '''
        :param assertDict:
        :return: 查看智能考勤首页
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('智能考勤首页'))
        # 点击取消
        self._click(g().get_resource_infor('智能考勤打卡位置选择取消按钮'))
        time.sleep(1)
        self._performAssert('断言查看智能考勤首页成功',assertDict)

    @ui("attendance")
    def clockIn(self,assertDict):
        '''
        :param assertDict:
        :return: 智能考勤打卡
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('智能考勤首页'))
        # 点击取消
        self._click(g().get_resource_infor('智能考勤打卡位置选择取消按钮'))
        # 打卡
        self._wait_ui_appear(g().get_resource_infor('智能考勤打卡图标'))
        self._click(g().get_resource_infor('智能考勤打卡图标'))
        time.sleep(10)
        # 点击取消
        self._click(g().get_resource_infor('智能考勤打卡位置选择取消按钮'))
        # 点击确认打卡
        self._click(g().get_resource_infor('智能考勤确认打卡图标'))
        self._performAssert('断言打卡成功',assertDict)
        self._click_back()

    @ui("attendance")
    def cancelClockIn(self,assertDict):
        '''
        :param assertDict:
        :return: 智能考勤取消打卡
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('智能考勤首页'))
        # 点击取消
        self._click(g().get_resource_infor('智能考勤打卡位置选择取消按钮'))
        # 打卡
        self._wait_ui_appear(g().get_resource_infor('智能考勤打卡图标'))
        self._click(g().get_resource_infor('智能考勤打卡图标'))
        # 点击取消
        self._click(g().get_resource_infor('智能考勤打卡位置选择取消按钮'))
        # 点击取消打卡
        self._click(g().get_resource_infor('智能考勤取消打卡图标'))
        self._performAssert('断言取消打卡成功', assertDict)
        self._click_back()

    @ui("attendance")
    def viewAttendance(self,assertDict):
        '''
        :param assertDict:
        :return: 查看智能记录
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('智能考勤首页'))
        # 点击取消
        self._click(g().get_resource_infor('智能考勤打卡位置选择取消按钮'))
        # 等待打卡图标出现
        self._wait_ui_appear(g().get_resource_infor('智能考勤打卡图标'))
        # 点击考勤记录
        self._click(g().get_resource_infor('考勤记录按钮'))
        self._performAssert('',assertDict)
        self._click_back()
        self._click_back()

    @ui("attendance")
    def viewAttendanceDailyList(self,assertDict):
        '''
        :param assertDict:
        :return: 查看勤劳小蜜蜂行部日榜
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('智能考勤首页'))
        # 点击取消
        self._click(g().get_resource_infor('智能考勤打卡位置选择取消按钮'))
        # 等待打卡图标出现
        self._wait_ui_appear(g().get_resource_infor('智能考勤打卡图标'))
        # 滑动到勤劳小蜜蜂行部日榜
        self._wait_ui_appear(g().get_resource_infor('勤劳小蜜蜂行部日榜'), lambda ui: ui._swipe((0.6,0.9),(0.6,0.6)))
        self._performAssert('断言查看勤劳小蜜蜂行部日榜成功',assertDict)
        self._click_back()

    @ui("attendance")
    def viewAttendancePersonalList(self,assertDict):
        '''
        :param assertDict:
        :return: 查看勤劳小蜜蜂行部日榜
        '''
        # 等待首页
        self._wait_ui_appear(g().get_resource_infor('智能考勤首页'))
        # 点击取消
        self._click(g().get_resource_infor('智能考勤打卡位置选择取消按钮'))
        # 等待打卡图标出现
        self._wait_ui_appear(g().get_resource_infor('智能考勤打卡图标'))
        # 滑动到勤劳小蜜蜂个人排行榜
        self._wait_ui_appear(g().get_resource_infor('勤劳小蜜蜂个人排行榜'), lambda ui: ui._swipe((0.6, 0.9), (0.6, 0.6)))
        self._performAssert('断言查看勤劳小蜜蜂个人排行榜成功', assertDict)
        self._click_back()

if __name__ == '__main__':
    Attendance().Attendance()
