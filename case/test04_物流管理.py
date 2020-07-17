# coding=utf-8
import unittest
from function import *
from time import sleep
from selenium import webdriver
from pykeyboard import PyKeyboard

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

class logisticsManagement(unittest.TestCase):
    def test_01_new_address(self):
        '''新建发货地址'''
        try:
            driver = browser().resue_browser()
            driver.find_element_by_link_text('地址管理').click()  # 点击 地址管理
            element=WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located((By.XPATH,"//button[@type='button']//span")))
            element.click()
            sleep(0.5)
            addressName='春熙二路'
            driver.find_element_by_id("addressName").send_keys(addressName)
            driver.find_element_by_id("userNameParam").send_keys('春芳')
            driver.find_element_by_id("mobile").send_keys("18883282345")
            driver.find_elements_by_class_name("ant-select-selection__rendered")[0].click()
            sleep(1.5)
            driver.find_element_by_xpath("//div[@style='overflow: auto;']//li[1]").click()
            sleep(0.5)
            driver.find_elements_by_class_name("ant-select-selection__rendered")[1].click()
            sleep(1)
            driver.find_element_by_xpath("//body/div[4]/div/div/div/ul/li[1]").click()
            sleep(0.5)
            driver.find_elements_by_class_name("ant-select-selection__rendered")[2].click()
            sleep(1.5)
            driver.find_element_by_xpath("//body/div[5]/div/div/div/ul/li[1]").click()
            sleep(0.5)
            driver.find_element_by_id("detailAddress").send_keys("下东大街258号四川天府银行")
            driver.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]/span").click()
            sleep(3)
            number=len(driver.find_elements_by_xpath("//tbody/tr"))
            nextworkName=driver.find_element_by_xpath("//tbody/tr[%d]/td[1]"%number).text #取最后一个地址名称
            self.assertEqual(addressName,nextworkName,'新建发货地址成功')
            save_picture(,'新建发货地址成功')
            sleep(3)
        except Exception as e:
            print('新建发货地址出错，错误类型是{}'.format(type(e)))
            save_picture('新建发货地址失败')
            driver.refresh()
            raise

    def test_02_edit_address(self):
        '''编辑发货地址'''
        try:
            driver = browser().resue_browser()
            element = WebDriverWait(driver, 20, 0.5).until(
                EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[6]/div/span[1]/a")))  # 等页面加载完成
            beforeName=driver.find_element_by_xpath("//tbody/tr[1]/td[1]").text #取修改前发货地址名称
            driver.find_element_by_xpath("//tbody/tr[1]/td[6]/div/span[1]/a").click()  # 点击 编辑
            sleep(1)
            driver.find_element_by_id("addressName").clear()   #清空数据
            driver.find_element_by_id("addressName").send_keys('晶融汇')
            driver.find_element_by_xpath('//div[@class="ant-modal-footer"]//button[2]/span').click()  # 点击确定
            sleep(2)
            afterName = driver.find_element_by_xpath("//tbody/tr[1]/td[1]").text  # 取修改后发货地址名称
            self.assertNotEqual(beforeName,afterName, '编辑发货地址成功')
            save_picture('编辑发货地址失败')
            sleep(3)
        except Exception as e:
            print('编辑发货地址出错，错误类型是{}'.format(type(e)))
            save_picture(driver, '编辑发货地址失败')
            driver.refresh()
            raise

    def test_03_delete_address(self):
        '''删除发货地址'''
        try:
            chrome_options = Options()
            chrome_options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
            chrome_driver = r"C:\Users\TS\AppData\Local\Google\Chrome\Application\chromedriver.exe"
            driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
            # driver.find_element_by_link_text('地址管理').click()  # 点击 地址管理
            element = WebDriverWait(driver, 20, 0.5).until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='button']//span"))) #等页面加载完成
            beforeNumber = len(driver.find_elements_by_xpath("//tbody/tr")) #取删除前网点个数
            driver.find_element_by_xpath("//tbody/tr[1]/td[6]/div/span[2]/a").click()   #点击删除
            sleep(0.5)
            driver.find_element_by_xpath('//div[@class="ant-confirm-btns"]//button[2]/span').click() #点击确定
            sleep(3)
            afterNumber = len(driver.find_elements_by_xpath("//tbody/tr"))  # 取删除后网点个数
            self.assertNotEqual(beforeNumber,afterNumber,'删除发货地址成功')
            screenshot.save_picture(driver, '删除发货地址成功')
            sleep(3)
        except Exception as e:
            print('删除发货地址出错，错误类型是{}'.format(type(e)))
            screenshot.save_picture(driver, '删除发货地址失败')
            driver.refresh()
            raise

    def test_04_new_return_address(self):
        '''新建退货地址'''
        try:
            chrome_options = Options()
            chrome_options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
            chrome_driver = r"C:\Users\TS\AppData\Local\Google\Chrome\Application\chromedriver.exe"
            driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
            driver.find_element_by_xpath("//div[@role='tab'][2]").click() #点击退货地址
            sleep(2)
            driver.find_element_by_xpath('//div[@role="tabpanel"][2]/div/div[3]//button/span').click() #点击 新建
            sleep(1)
            returnAdderss='四川天府银行'
            driver.find_element_by_id("addressName").send_keys(returnAdderss)
            driver.find_element_by_id("userNameParam").send_keys('春芳')
            driver.find_element_by_id("mobile").send_keys("18883282345")
            driver.find_elements_by_class_name("ant-select-selection__rendered")[0].click()
            sleep(1)
            driver.find_element_by_xpath("//div[@style='overflow: auto;']//li[1]").click() #省
            sleep(1)
            driver.find_elements_by_class_name("ant-select-selection__rendered")[1].click()
            sleep(1)
            driver.find_element_by_xpath("//body/div[5]/div/div/div/ul/li[1]").click()  #市
            sleep(1)
            driver.find_elements_by_class_name("ant-select-selection__rendered")[2].click()
            sleep(1)
            driver.find_element_by_xpath("//body/div[6]/div/div/div/ul/li[1]").click()  #区
            sleep(1)
            driver.find_element_by_id("detailAddress").send_keys("下东大街258号四川天府银行")
            driver.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]/span").click() #点击确认
            sleep(3)
            number=len(driver.find_elements_by_xpath("//div[@role='tabpanel'][2]//table/tbody/tr")) #统计退货地址个数
            returnAdderss2=driver.find_element_by_xpath("//div[@role='tabpanel'][2]//table/tbody/tr[%d]/td[1]"%number).text  #取列表最后一个地址名称
            self.assertEqual(returnAdderss,returnAdderss2,'新建退货地址成功')
            screenshot.save_picture(driver,'新建退货地址成功')
            sleep(3)
        except Exception as e:
            print('新建退货地址出错，错误类型是{}'.format(type(e)))
            screenshot.save_picture(driver, '新建退货地址失败')
            driver.refresh()
            raise

    def test_05_edit_return_address(self):
        '''编辑退货地址'''
        try:
            chrome_options = Options()
            chrome_options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
            chrome_driver = r"C:\Users\TS\AppData\Local\Google\Chrome\Application\chromedriver.exe"
            driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
            sleep(1)
            afterName='财富中心'
            beforeName=driver.find_element_by_xpath("//div[@role='tabpanel'][2]//table/tbody/tr[1]/td[1]").text #取修改前退货地址名称
            driver.find_element_by_xpath("//div[@role='tabpanel'][2]//table/tbody/tr[1]/td[6]//span[1]/a").click()  # 点击 编辑
            sleep(3)
            driver.find_element_by_id("addressName").clear()   #清空数据
            driver.find_element_by_id("addressName").send_keys(afterName)
            driver.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]/span").click()  # 点击确定
            sleep(2)
            afterName = driver.find_element_by_xpath("//div[@role='tabpanel'][2]//table/tbody/tr[1]/td[1]").text  # 取修改后退货地址名称
            self.assertNotEqual(beforeName,afterName, '编辑退货地址成功')
            screenshot.save_picture(driver,'编辑退货地址成功')
            sleep(3)
        except Exception as e:
            print('编辑退货地址出错，错误类型是{}'.format(type(e)))
            screenshot.save_picture(driver, '编辑退货地址失败')
            driver.refresh()
            raise

    def test_06_delete_retrun_address(self):
        '''删除退货地址'''
        try:
            chrome_options = Options()
            chrome_options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
            chrome_driver = r"C:\Users\TS\AppData\Local\Google\Chrome\Application\chromedriver.exe"
            driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
            # driver.find_element_by_link_text('地址管理').click()  # 点击 地址管理
            element = WebDriverWait(driver, 20, 0.5).until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='button']//span"))) #等页面加载完成
            sleep(2)
            beforeNumber = len(driver.find_elements_by_xpath("//div[@role='tabpanel'][2]//table/tbody/tr")) #取删除前退货地址个数
            driver.find_element_by_xpath("//div[@role='tabpanel'][2]//table/tbody/tr[1]/td[6]//span[2]/a").click()   #点击删除
            sleep(0.5)
            driver.find_element_by_xpath('//div[@class="ant-confirm-btns"]//button[2]/span').click() #点击确定
            sleep(3)
            afterNumber = len(driver.find_elements_by_xpath("//tbody/tr"))  # 取删除后地址个数
            self.assertNotEqual(beforeNumber,afterNumber,'删除退货地址成功')
            screenshot.save_picture(driver, '删除退货地址成功')
            sleep(3)
        except Exception as e:
            print('删除退货地址出错，错误类型是{}'.format(type(e)))
            screenshot.save_picture(driver, '删除退货地址失败')
            driver.refresh()
            raise

if __name__=="__main__":
    unittest.main()