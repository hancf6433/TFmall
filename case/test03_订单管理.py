import unittest,os
from time import sleep
from function import *
from baseSelenium import *
from test_data import *


'''订单管理'''
class order_management(unittest.TestCase):
    def test_code_check(self):
        '''券码核销'''
        driver = browser().resue_browser()
        js = 'window.scrollTo(0,400);'
        driver.execute_script(js)
        sleep(2)
        position().xpath('//*[@id="6172$Menu"]/li[1]/a').click()  #点击券码校验
        wait_element().wait_id('orderCode')         #等待页面加载
        code=get_code()                             #获取券码
        position().id('orderCode').send_keys(code)  #输入券码
        position().xpath('//button/span').click()   #点击查询
        // body / div / div / span / div / div / div / span



    # def test_confirm_delivery(self):
    #     '''待发货订单确认发货'''
    #     driver = browser().resue_browser()
    #     js='window.scrollTo(0,200);'
    #     driver.execute_script(js)
    #     sleep(0.5)
    #     for i in range(2,12):
    #         orderS=driver.find_element_by_xpath('//tbody/tr[%d]/td[11]'%(i+2)).text #获取订单状态
    #         if orderS=='待发货':
    #             driver.find_element_by_xpath("//tbody/tr[%d]/td[12]/div/div/a"%(i+2)).click()
    #             sleep(1)
    #             driver.find_element_by_class_name('ant-select-selection__placeholder').click()
    #             sleep(0.5)
    #             driver.find_element_by_xpath("//div[@class='modifyPriceWrap__panelPaid___24hNM-Et']//li[1]").click()
    #             driver.find_element_by_id('logisticsNo').send_keys('7890123456')
    #             driver.find_element_by_xpath("//div[@class ='ant-modal-footer']/button[2]/span").click() #确认发货
    #             save_picture(driver,'发货成功')
    #             break
    #         else:
    #             save_picture(driver,'无待发货订单')


if __name__=='__main__':
    unittest.main()