from browser import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import os

'''定位元素'''
class find_element(browser):
    def element(self, locator, timeout=20):
        '''等待元素出现并定位元素 - 单个元素，参数locator是元祖类型'''
        driver = browser().resue_browser()
        element = WebDriverWait(driver,timeout,1).until(EC.presence_of_element_located(locator))
        return element
    def elements(self, locator, timeout=20):
        '''等待元素出现并定位元素 - 一组元素，参数locator是元祖类型'''
        driver = browser().resue_browser()
        element = WebDriverWait(driver,timeout,1).until(EC.presence_of_all_elements_located(locator))
        return element

def save_picture(pictureName):
    driver = browser().resue_browser()
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'screenshots')  # 获取截图保存地址
    now = time.strftime('%Y_%m_%d %H_%M_%S')  # 获取当前时间
    picture = file_path + '/' + now + '_' + pictureName + '.png'  # 拼接截图保存地址
    driver.save_screenshot(picture)  # 截图