import unittest
from time import sleep
from function import *
# from baseSelenium import *
from readXml import *

'''订单管理'''
class order_management(unittest.TestCase):
    def test_code_check(self):
        '''券码核销'''
        # driver = browser().resue_browser()
        # js = 'window.scrollTo(0,400);'
        # driver.execute_script(js)
        # sleep(2)
        # find_element().element((By.XPATH,'//*[@id="6172$Menu"]/li[1]/a')).click()   #点击券码校验
        # find_element().element((By.ID,'orderCode')).send_keys(readxml("mallcode"))  #输入券码
        # find_element().element((By.XPATH,'//button/span')).click()   #点击查询

    def test_confirm_delivery(self):
        '''待发货订单确认发货'''
        driver = browser().resue_browser()
        scroll_length(600)
        sleep(0.5)
        find_element().element((By.XPATH, '//*[@id="6172$Menu"]/li[2]/a')).click()   #点击商城订单
        find_element().elements((By.CSS_SELECTOR,".ant-select-selection__rendered"))[0].click()  #点击全部
        find_element().element((By.XPATH,"//body/div[2]/div/div/div/ul/li[3]")).click()  #筛选待发货订单
        find_element().element((By.XPATH,'//div[@class="r-action"]/button')).click()      #点击查询
        scroll_length(200)
        if isElementExist((By.XPATH,"//form[1]/div[2]/div[2]/div/div/div/div/div[2]")):
            save_picture("无待发货订单")
        else:
            orderNo=find_element().element((By.XPATH,"//tbody/tr[1]/td[2]/div/div/div[1]/span[2]")).text  #取第一个待发货订单的订单号
            driver.refresh()
            find_element().element((By.ID,"orderNo")).send_keys(orderNo)
            find_element().element((By.XPATH, '//div[@class="r-action"]/button')).click()  # 点击查询
            scroll_length(200)
            find_element().element((By.XPATH, "//tbody/tr[2]/td[13]/div/div/a")).click()  # 点击确认发货
            find_element().element((By.CLASS_NAME, 'ant-select-selection__placeholder')).click() #选择物流公司
            find_element().element((By.XPATH, "//div[@class='modifyPriceWrap__panelPaid___24hNM-Et']//li[1]")).click()
            find_element().element((By.ID, 'logisticsNo')).send_keys(readxml("logisticsNo"))  #输入物流单号
            find_element().element((By.XPATH, "//div[@class ='ant-modal-footer']/button[2]/span")).click()  # 确认发货
            save_picture("点击确认发货")
            orderS = find_element().element((By.XPATH, '//tbody/tr[2]/td[11]' )).text  # 获取订单状态
            self.assertEqual(orderS,'待收货')

if __name__=='__main__':
    unittest.main()