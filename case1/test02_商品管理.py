'''
author：韩春芳
date：20191218
直接使用已打开的浏览器
'''

# coding=utf-8
import unittest
from function import *
from time import sleep
from pykeyboard import PyKeyboard
from selenium.webdriver.common.by import By
from readXml import *

class commodity_management(unittest.TestCase):
    def test_01_goods_released(self):
        '''商品发布'''
        try:
            driver = browser().resue_browser()
            scroll_length(1000)
            element((By.XPATH,'//*[@id="6180$Menu"]/li[2]/a')).click()                 #点击商品发布
            element((By.CSS_SELECTOR,'.inputname1')).send_keys(readxml("goodsName"))   # 填写商品名称
            elements((By.CSS_SELECTOR,'.ant-select-selection__rendered'))[0].click()    # 一级分类
            element((By.XPATH,"//body/div[3]/div/div/div/ul/li[3]")).click()
            elements((By.CSS_SELECTOR,'.ant-select-selection__rendered'))[1].click()    # 二级分类
            element((By.XPATH,"//body/div[4]/div/div/div/ul/li[2]")).click()
            elements((By.CSS_SELECTOR,'.ant-select-selection__rendered'))[2].click()    # 三级分类
            element((By.XPATH,"//body/div[5]/div/div/div/ul/li[2]")).click()

            '''商品图片'''
            driver.find_element_by_xpath("//span[text()='商品图片']").click()
            for i in range(1, 6):
                k = PyKeyboard()
                element((By.CLASS_NAME, 'avataruploadertrigger')).click()
                sleep(1)
                k.type_string(r"E:\selenium\picture\%d.jpg" % i)  # 打开文件夹位置
                sleep(1)
                k.tap_key(k.enter_key)
                sleep(1)
                k.tap_key(k.enter_key)
                element(((By.XPATH,"//div[@class='avatarfl']/div[%d+1]" % i)))  # 等待新的添加图片按钮出现
                sleep(2)

            '''商品介绍'''
            element((By.XPATH,'//div[@role="tab"][4]')).click()
            sleep(2)
            driver.switch_to.frame('ueditor_1')  # 进入frame页面
            driver.find_element_by_tag_name('body').send_keys(readxml('goodsIntroduction'))  # 直接往frame里的body里填内容
            sleep(5)
            driver.switch_to.default_content()  # 退出frame

            '''其他设置'''
            element((By.XPATH,'//div[@role="tab"][5]')).click()
            scroll_length(1000)
            sleep(2)
            driver.switch_to_frame('ueditor_0')
            driver.find_element_by_tag_name('body').send_keys(readxml("packList"))
            driver.switch_to_default_content()

            '''价格及库存'''
            element((By.XPATH,'//div[@role="tab"][6]')).click()
            element((By.XPATH,'//span[text()="价格"]/parent::div//input')).send_keys(readxml("price"))
            element((By.XPATH,'//span[text()="库存"]/parent::div//input')).send_keys(readxml("inventory"))

            '''点击发布'''
            elements((By.CSS_SELECTOR,'.ant-btn.ant-btn-primary.ant-btn-lg'))[0].click()  # 发布
            element((By.CLASS_NAME,'add-product-link')) #等添加商品
            sleep(2)
            newname=element((By.XPATH,"//div[@class='goods-manage'][1]//a[@class='nameSty']")).get_attribute('title')
            self.assertEqual(newname,readxml("goodsName"),"商品发布失败")
        finally:
            save_picture("商品发布结果")

    def test_02_goods_management(self):
        '''商品管理，商品上下架'''
        # browser().open_browser()
        driver = browser().resue_browser()
        scroll_length(1000)
        element((By.XPATH,'//*[@id="6180$Menu"]/li[3]/a')).click()  # 点击商品管理
        element((By.XPATH,"//div[@class='r-action']//span"))
        element((By.XPATH,'//div[@title="全部"]')).click()
        element((By.XPATH,"//li[@unselectable='unselectable'][6]")).click() #筛选在售状态的商品
        element((By.XPATH,"//div[@class='r-action']/button[1]/span")).click()   #点击查询
        #取第一件商品做上下架
        name = element((By.XPATH,"//div[@class='goods-manage'][1]//a[@class='nameSty']")).get_attribute(
            'title')    #取第一件商品的名字

        element((By.ID,'itemName')).send_keys(name)  #输入商品名称
        element((By.XPATH,"//div[@title='在售']")).click()          #点击在售
        element((By.XPATH,"//li[@unselectable='unselectable'][1]")).click()  #点击选择全部
        element((By.XPATH,"//div[@class='r-action']/button[1]/span")).click()  # 点击查询
        element((By.XPATH,'//tbody/tr/td[8]/span/span[3]/a')).click()  #下架
        save_picture("下架")
        status=element((By.XPATH,'//tbody/tr/td[7]/span')).text
        self.assertEqual(status,'已下架',"商品下架成功")

        #上架
        element((By.XPATH,'//tbody/tr/td[8]/span/span[3]/a')).click()  # 上架
        status = element((By.XPATH,'//tbody/tr/td[7]/span')).text
        save_picture('上架')
        self.assertEqual(status,'在售',"商品下架成功")






