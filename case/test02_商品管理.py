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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class commodity_management(unittest.TestCase):
    def test_01_goods_released(self):
        '''商品发布'''
        driver = browser().resue_browser()
        js = "window.scrollTo(0,1000);"
        driver.execute_script(js)
        goodname='python 自动化发布商品3'
        driver.find_element_by_xpath('//*[@id="6180$Menu"]/li[2]/a').click()                  #点击商品发布
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.inputname1')))
        driver.find_element_by_css_selector('.inputname1').send_keys(goodname)  # 填写商品名称
        sleep(1)
        driver.find_elements_by_css_selector('.ant-select-selection__rendered')[0].click()    # 一级分类
        sleep(1)
        driver.find_element_by_xpath("//body/div[3]/div/div/div/ul/li[3]").click()
        sleep(1)
        driver.find_elements_by_css_selector('.ant-select-selection__rendered')[1].click()    # 二级分类
        sleep(1)
        driver.find_element_by_xpath("//body/div[4]/div/div/div/ul/li[2]").click()
        sleep(1)
        driver.find_elements_by_css_selector('.ant-select-selection__rendered')[2].click()    # 三级分类
        sleep(1)
        driver.find_element_by_xpath("//body/div[5]/div/div/div/ul/li[2]").click()
        sleep(1)

        '''商品图片'''
        driver.find_element_by_xpath("//span[text()='商品图片']").click()
        for i in range(1,6):
            element1 = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'avataruploadertrigger')))
            k = PyKeyboard()
            element1.click()
            sleep(1)
            k.type_string(r"E:\selenium\picture\%d.jpg"%i)  # 打开文件夹位置
            sleep(1)
            k.tap_key(k.enter_key)
            sleep(1)
            k.tap_key(k.enter_key)
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH,
            "//div[@class='avatarfl']/div[%d+1]"%i))) #等待新的添加图片按钮出现
            sleep(2)
        '''商品介绍'''
        driver.find_element_by_xpath('//div[@role="tab"][4]').click()
        sleep(2)
        driver.switch_to.frame('ueditor_1')  # 进入frame页面
        body_string = """python自动化测试 商品介绍"""
        driver.find_element_by_tag_name('body').send_keys(body_string)  # 直接往frame里的body里填内容
        driver.switch_to.default_content()  # 退出frame
        sleep(5)
        '''其他设置'''
        driver.find_element_by_xpath('//div[@role="tab"][5]').click()
        sleep(2)
        js = "window.scrollTo(0,1000);"
        driver.execute_script(js)
        sleep(2)
        driver.switch_to_frame('ueditor_0')
        list="""包装清单验证"""
        driver.find_element_by_tag_name('body').send_keys(list)
        driver.switch_to_default_content()

        '''价格及库存'''
        driver.find_element_by_xpath('//div[@role="tab"][6]').click()
        sleep(0.5)
        driver.find_element_by_xpath('//span[text()="价格"]/parent::div//input').send_keys('55')
        driver.find_element_by_xpath('//span[text()="库存"]/parent::div//input').send_keys('12')
        sleep(2)

        '''点击发布'''
        driver.find_elements_by_css_selector('.ant-btn.ant-btn-primary.ant-btn-lg')[0].click()  # 发布
        WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located((By.CLASS_NAME,'add-product-link'))) #等添加商品
        sleep(2)
        name=driver.find_element_by_xpath("//div[@class='goods-manage'][1]//a[@class='nameSty']").get_attribute('title')
        if goodname==name:
            save_picture(driver,'商品发布成功')   # 截图
        else:
            save_picture(driver, '商品发布失败')  # 截图

    def test_02_goods_management(self):
        '''商品管理，商品上下架'''
        driver = browser().resue_browser()
        js = "window.scrollTo(0,1000);"
        driver.execute_script(js)
        driver.find_element_by_xpath('//*[@id="6180$Menu"]/li[3]/a').click()  # 点击商品管理
        WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@class='r-action']//span")))
        driver.find_element_by_xpath('//div[@title="全部"]').click()
        sleep(0.5)
        driver.find_element_by_xpath("//li[@unselectable='unselectable'][6]").click() #筛选在售状态的商品
        driver.find_element_by_xpath("//div[@class='r-action']/button[1]/span").click()   #点击查询
        sleep(1)
        #取第一件商品做上下架
        name = driver.find_element_by_xpath("//div[@class='goods-manage'][1]//a[@class='nameSty']").get_attribute(
            'title')    #取第一件商品的名字

        driver.find_element_by_id('itemName').send_keys(name)  #输入商品名称
        driver.find_element_by_xpath("//div[@title='在售']").click()          #点击在售
        sleep(0.5)
        driver.find_element_by_xpath("//li[@unselectable='unselectable'][1]").click()  #点击选择全部
        sleep(0.5)
        driver.find_element_by_xpath("//div[@class='r-action']/button[1]/span").click()  # 点击查询
        driver.find_element_by_xpath('//tbody/tr/td[8]/span/span[3]/a').click()  #下架
        sleep(3)
        status=driver.find_element_by_xpath('//tbody/tr/td[7]/span').text
        if status=='已下架':
            save_picture(driver,'下架成功')
        else:
            save_picture(driver,"下架失败")
        sleep(2)

        #上架
        driver.find_element_by_xpath('//tbody/tr/td[8]/span/span[3]/a').click()  # 上架
        sleep(3)
        status = driver.find_element_by_xpath('//tbody/tr/td[7]/span').text
        if status=='在售':
            save_picture(driver, '上架成功')
        else:
            save_picture(driver, "上架失败")

# if __name__ == '__main__':
#     unittest.main()






