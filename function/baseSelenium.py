# -*- encoding=utf8 -*-
__author__ = "lenovo"

from airtest.core.api import *
auto_setup(__file__)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from airtest_selenium.proxy import WebChrome



class BaseSelenium(object):
    '''
    基于原生selenium做二次封装
    :param dcap：浏览器信息
    ：return
    '''
    def __init__(self, paramdcap,dict=None):
        self.dcap = None
        if paramdcap!= None:
            self.dcap = paramdcap
        else:
            self.dcap = dict(DesiredCapabilities.CHROME)
            self.dcap['chrome.page.settings.userAgent'] = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0')                     
        
    def open(self, url):
        '''打开页面'''
        #self.driver = WebChrome()
        self.driver = webdriver.Chrome(desired_capabilities = self.dcap)
        self.driver.get(url)
        self.driver.maximize_window()
        
    def find_element(self, locator, timeout=10):
        
        '''定位元素，参数locator是元祖类型'''
        element = WebDriverWait(self.driver, timeout,1).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator, timeout=10):
        '''定位一组元素'''
        elements = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_all_elements_located(locator))
        return elements

    def click(self, locator):
        '''点击操作'''
        element = self.find_element(locator)
        element.click()
                                                           
    def send_keys(self, locator, text, is_clear=True):
        '''
        发送文本，清空后输入
        Usage:
        locator = ("id","xxx")
        driver.send_keys(locator, text)
        '''
        element = self.find_element(locator)
        if is_clear==True: element.clear()
        element.send_keys(text)
                                              
    def is_title(self, title, timeout=10):
        '''判断title完全等于'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_is(title))
        return result
    
    def is_located(self, locator, timeout=10):
        '''判断元素被定为到（并不意味着可见），定为到返回element,没定位到返回False'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(locator))
        return result
    
    def is_exists(self, locator):
        '''判断元素存在'''
        try:
            self.is_located(locator)
            return True
        except:
            return False
    
    def get_text(self, locator):
        '''获取文本'''
        t = self.find_element(locator).text
        return t

    def get_title(self):
        '''获取title'''
        return self.driver.title
    
    def get_current_handle(self):
        '''获取当前的句柄'''
        return self.driver.current_window_handle

    def get_handle(self):
        '''获取要切换的标签句柄'''
        time.sleep(1)
        handles = self.driver.window_handles
        for handle in handles:
            if self.driver.current_window_handle != handle:
                return handle
            
    def switch_handle(self, window_name):
        '''切换浏览器标签句柄'''
        self.driver.switch_to.window(window_name)
    
    def js_scroll_top(self):
        '''滚到底部'''
        js = "window.scrollTo(0,0);" 
        self.driver.execute_script(js)
    
    def js_scroll_end(self):
        '''滚动到底部'''
        js = "window.scrollTo(0,document.body.scrollHeight);" 
        self.driver.execute_script(js)
    
    @property
    def nativedriver(self):
        return self.driver


    def save_picture(self,name):
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'screenshots')  # 获取截图保存地址
        now = time.strftime('%Y_%m_%d %H_%M_%S')  # 获取当前时间
        picture = file_path + '/' + now + '_' + name + '.png'  # 拼接截图保存地址
        self.driver.save_screenshot(picture)  # 截图


