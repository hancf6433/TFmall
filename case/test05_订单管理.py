import unittest,os
from time import sleep
from selenium import webdriver
from config import screenshot,exist
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from browserReuse import browserReuse

class orderManagement(browserReuse):
    def test_01_coupon_code_check(self):
        '''券码校验'''
        try:
            Driver=browserReuse().browser()
            # chrome_options = Options()
            # chrome_options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
            # chrome_driver = r"C:\Users\TS\AppData\Local\Google\Chrome\Application\chromedriver.exe"
            # driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
            Driver.find_element_by_link_text('券码校验').click()  # 点击 地址管理
            WebDriverWait(Driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, "//form//span")))
            Driver.find_element_by_id('orderCode').send_keys('907451000249')
            Driver.find_element_by_xpath('//form//span').click()
            screenshot.save_picture(Driver,'查询结果')
            sleep(3)
            #判断是否有查询结果
            flag=exist.xpathExist("//div[@class='ant-table-placeholder']/span/text()")
            if flag:
                screenshot.save_picture(Driver,'无查询结果')
            else:
                pass
        except Exception as e:
            pass
            # print('券码校验失败，错误为：{}'.format(type(e)))
            # screenshot.save_picture(driver,'券码校验出错')

if __name__=="__main__":
    orderManagement().test_01_coupon_code_check()
    # unittest.main()