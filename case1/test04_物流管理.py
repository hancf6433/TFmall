# coding=utf-8
import unittest
from function import *
from selenium.webdriver.common.by import By
from readXml import *

class logistics_management(unittest.TestCase):
    def test_01_new_address(self):
        '''新建发货地址111'''
        try:
            element((By.LINK_TEXT,'地址管理')).click()  # 点击 地址管理
            element(((By.XPATH,"//button[@type='button']//span"))).click()
            element((By.ID,"addressName")).send_keys(readxml("addressName"))
            element((By.ID,"userNameParam")).send_keys(readxml("userNameParam"))
            element((By.ID,"mobile")).send_keys(readxml("mobile"))
            elements((By.CLASS_NAME,"ant-select-selection__rendered"))[0].click()
            element((By.XPATH,"//div[@style='overflow: auto;']//li[1]")).click()
            elements((By.CLASS_NAME,"ant-select-selection__rendered"))[1].click()
            element((By.XPATH,"//body/div[4]/div/div/div/ul/li[1]")).click()
            elements((By.CLASS_NAME,"ant-select-selection__rendered"))[2].click()
            element((By.XPATH,"//body/div[5]/div/div/div/ul/li[1]")).click()
            element((By.ID,"detailAddress")).send_keys(readxml("detailAddress"))
            element((By.XPATH,"//div[@class='ant-modal-footer']/button[2]/span")).click()  #点击提交
            save_picture("新建发货地址")
            number=len(elements((By.XPATH,"//tbody/tr")))
            nextworkName=element((By.XPATH,"//tbody/tr[%d]/td[1]"%number)).text #取最后一个地址名称
            self.assertEqual(readxml("addressName"),nextworkName,'新建发货地址成功')
        except Exception as e:
            print('新建发货地址出错，错误类型是{}'.format(type(e)))
            save_picture('新建发货地址失败')
            raise

    def test_02_edit_address(self):
        '''编辑发货地址'''
        try:
            element((By.XPATH, "//tbody/tr[1]/td[6]/div/span[1]/a"))  # 等页面加载完成
            beforeName=element((By.XPATH,'//div[@aria-hidden="false"]//tbody/tr[1]/td[1]')).text #取修改前发货地址名称
            element((By.XPATH,'//div[@aria-hidden="false"]//tbody/tr[1]/td[6]//span[1]/a')).click()  # 点击 编辑
            element((By.ID,"addressName")).clear()   #清空数据
            element((By.ID,"addressName")).send_keys(readxml("mo_addressName"))
            element((By.XPATH,'//div[@class="ant-modal-footer"]//button[2]/span')).click()  # 点击确定
            save_picture('编辑发货地址')
            afterName = element((By.XPATH,'//div[@aria-hidden="false"]//tbody/tr[1]/td[1]')).text  # 取修改后发货地址名称
            self.assertNotEqual(beforeName,afterName, '编辑发货地址成功')
        except Exception as e:
            driver = browser().resue_browser()
            print('编辑发货地址出错，错误类型是{}'.format(type(e)))
            driver.refresh()
            raise

    def test_03_delete_address(self):
        '''删除发货地址'''
        try:
            element((By.XPATH, "//button[@type='button']//span"))   #等页面加载完成
            beforeNumber = len(elements((By.XPATH,"//tbody/tr")))   #取删除前网点个数
            element((By.XPATH,'//div[@aria-hidden="false"]//tbody/tr[1]/td[6]//span[2]/a')).click()   #点击删除
            element((By.XPATH,'//div[@class="ant-confirm-btns"]//button[2]/span')).click() #点击确定
            save_picture('删除发货地址')
            afterNumber = len(elements((By.XPATH,"//tbody/tr")))  # 取删除后网点个数
            self.assertNotEqual(beforeNumber,afterNumber,'删除发货地址成功')
        except Exception as e:
            driver = browser().resue_browser()
            print('删除发货地址出错，错误类型是{}'.format(type(e)))
            driver.refresh()
            raise

    def test_04_new_return_address(self):
        '''新建退货地址'''
        try:
            element((By.XPATH,"//div[@role='tab'][2]")).click() #点击退货地址
            element((By.XPATH,'//div[@role="tabpanel"][2]/div/div[3]//button/span')).click() #点击 新建
            element((By.ID,"addressName")).send_keys(readxml("returnAdderss"))
            element((By.ID,"userNameParam")).send_keys(readxml("re_userNameParam"))
            element((By.ID,"mobile")).send_keys(readxml("re_mobile"))
            elements((By.CLASS_NAME,"ant-select-selection__rendered"))[0].click()
            element((By.XPATH,"//div[@style='overflow: auto;']//li[1]")).click() #省
            elements((By.CLASS_NAME,"ant-select-selection__rendered"))[1].click()
            element((By.XPATH,"//body/div[5]/div/div/div/ul/li[1]")).click()  #市
            elements((By.CLASS_NAME,"ant-select-selection__rendered"))[2].click()
            element((By.XPATH,"//body/div[6]/div/div/div/ul/li[1]")).click()  #区
            element((By.ID,"detailAddress")).send_keys(readxml("re_detailAddress"))
            element((By.XPATH,"//div[@class='ant-modal-footer']/button[2]/span")).click() #点击确认
            save_picture("新建退货地址")
            number=len(elements((By.XPATH,"//div[@role='tabpanel'][2]//table/tbody/tr"))) #统计退货地址个数
            returnAdderss2=element((By.XPATH,"//div[@role='tabpanel'][2]//table/tbody/tr[%d]/td[1]"%number)).text  #取列表最后一个地址名称
            self.assertEqual(readxml("returnAdderss"),returnAdderss2,'新建退货地址成功')
        except Exception as e:
            driver = browser().resue_browser()
            print('新建退货地址出错，错误类型是{}'.format(type(e)))
            driver.refresh()
            raise

    def test_05_edit_return_address(self):
        '''编辑退货地址'''
        try:
            beforeName=element((By.XPATH,"//div[@role='tabpanel'][2]//table/tbody/tr[1]/td[1]")).text #取修改前退货地址名称
            element((By.XPATH,"//div[@role='tabpanel'][2]//table/tbody/tr[1]/td[6]//span[1]/a")).click()  # 点击 编辑
            element((By.ID,"addressName")).clear()   #清空数据
            element((By.ID,"addressName")).send_keys(readxml("mo_returnAdderss"))
            element((By.XPATH,"//div[@class='ant-modal-footer']/button[2]/span")).click()  # 点击确定
            save_picture("编辑地址")
            afterName = element((By.XPATH,"//div[@role='tabpanel'][2]//table/tbody/tr[1]/td[1]")).text  # 取修改后退货地址名称
            self.assertNotEqual(beforeName,afterName, '编辑退货地址成功')
        except Exception as e:
            driver = browser().resue_browser()
            print('编辑退货地址出错，错误类型是{}'.format(type(e)))
            driver.refresh()
            raise

    def test_06_delete_retrun_address(self):
        '''删除退货地址'''
        try:
            element((By.XPATH, "//button[@type='button']//span")) #等页面加载完成
            beforeNumber = len(elements((By.XPATH,"//div[@role='tabpanel'][2]//table/tbody/tr"))) #取删除前退货地址个数
            element((By.XPATH,"//div[@role='tabpanel'][2]//table/tbody/tr[1]/td[6]//span[2]/a")).click()   #点击删除
            element((By.XPATH,'//div[@class="ant-confirm-btns"]//button[2]/span')).click() #点击确定
            save_picture("删除退货地址")
            afterNumber = len(elements((By.XPATH,"//tbody/tr")))  # 取删除后地址个数
            self.assertNotEqual(beforeNumber,afterNumber,'删除退货地址成功')
        except Exception as e:
            driver = browser().resue_browser()
            print('删除退货地址出错，错误类型是{}'.format(type(e)))
            driver.refresh()
            raise