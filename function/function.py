from browser import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import os

def element(locator, timeout=5):
    '''等待元素出现并定位元素 - 单个元素，参数locator是元祖类型'''
    driver = browser().resue_browser()
    element = WebDriverWait(driver,timeout,1).until(EC.presence_of_element_located(locator))
    return element

def elements(locator, timeout=5):
    '''等待元素出现并定位元素 - 一组元素，参数locator是元祖类型'''
    driver = browser().resue_browser()
    elements = WebDriverWait(driver,timeout,1).until(EC.presence_of_all_elements_located(locator))
    return elements

def save_picture(pictureName):
    driver = browser().resue_browser()
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'screenshots')  # 获取截图保存地址
    now = time.strftime('%Y_%m_%d %H_%M_%S')  # 获取当前时间
    picture = file_path + '/' + now + '_' + pictureName + '.png'  # 拼接截图保存地址
    driver.save_screenshot(picture)  # 截图

def isElementExist(locator):
    '''判断元素是否存在，存在返回True,不存在返回False'''
    flag = True
    driver = browser().resue_browser()
    try:
        WebDriverWait(driver,10,1).until(EC.presence_of_element_located(locator))
        return flag
    except:
        flag = False
        return flag

def scroll_top():
    '''滚到顶部'''
    driver = browser().resue_browser()
    js = "window.scrollTo(0,0);"
    driver.execute_script(js)


def scroll_end():
    '''滚动到底部'''
    driver = browser().resue_browser()
    js = "window.scrollTo(0,document.body.scrollHeight);"
    driver.execute_script(js)
def scroll_length(y):
    '''向下滚动指定长度'''
    driver = browser().resue_browser()
    js = 'window.scrollTo(0,%d);'%y
    driver.execute_script(js)