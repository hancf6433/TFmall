from browser import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import os

# '''等待元素出现'''
# class wait_element(browser):
#
#     def wait_id(self,id):
#         driver = browser().resue_browser()
#         WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, id)))
#     def wait_xpath(self, xpath):
#         driver = browser().resue_browser()
#         WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH,xpath)))
#
#     def wait_css(self, css):
#         driver = browser().resue_browser()
#         WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
#
#     def wait_name(self, name):
#         driver = browser().resue_browser()
#         WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.NAME, name)))
#
#     def wait_link_txt(self, link_txt):
#         driver = browser().resue_browser()
#         WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, link_txt)))
#
#     def wait_partial_link_txt(self, partial_link_txt):
#         driver = browser().resue_browser()
#         WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, partial_link_txt)))
#
#     def wait_tag_name(self, tag_name):
#         driver = browser().resue_browser()
#         WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.TAG_NAME, tag_name)))
#
#     def wait_class_name(self, class_name):
#         driver = browser().resue_browser()
#         WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
#
# '''元素定位'''
# class position(browser):
#     #定位单个元素
#     def id(self,id):
#         driver = browser().resue_browser()
#         element=driver.find_element_by_id(id)
#         return element
#
#
#     def xpath(self,xpath):
#         driver = browser().resue_browser()
#         element=driver.find_element_by_xpath(xpath)
#         return element
#
#     def name(self,name):
#         driver = browser().resue_browser()
#         driver.find_element_by_name(name)
#
#     def class_name(self,class_name):
#         driver = browser().resue_browser()
#         driver.find_element_by_class_name(class_name)
#
#     def tag_name(self,tag_name):
#         driver = browser().resue_browser()
#         driver.find_element_by_tag_name(tag_name)
#
#     def link_text(self,link_txt):
#         driver = browser().resue_browser()
#         driver.find_element_by_link_text(link_txt)
#
#     def partial_link_text(self,partial_link_text):
#         driver = browser().resue_browser()
#         driver.find_element_by_partial_link_text(partial_link_text)
#
#     def css(self, css):
#         driver = browser().resue_browser()
#         driver.find_element_by_css_selector(css)
#
#    #定义一组元素
#     def ids(self, id):
#         driver = browser().resue_browser()
#         driver.find_elements_by_id(id)
#
#     def xpaths(self, xpath):
#         driver = browser().resue_browser()
#         driver.find_elements_by_xpath(xpath)
#
#     def names(self, name):
#         driver = browser().resue_browser()
#         driver.find_elements_by_name(name)
#
#     def class_names(self, class_name):
#         driver = browser().resue_browser()
#         driver.find_elements_by_class_name(class_name)
#
#     def tag_names(self, tag_name):
#         driver = browser().resue_browser()
#         driver.find_elements_by_tag_name(tag_name)
#
#     def link_texts(self, link_txt):
#         driver = browser().resue_browser()
#         driver.find_elements_by_link_text(link_txt)
#
#     def partial_link_texts(self, partial_link_text):
#         driver = browser().resue_browser()
#         driver.find_elements_by_partial_link_text(partial_link_text)
#
#     def csses(self, css):
#         driver = browser().resue_browser()
#         driver.find_elements_by_css_selector(css)
#
# def save_picture(driver, name):
#     file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'screenshots')  # 获取截图保存地址
#     now = time.strftime('%Y_%m_%d %H_%M_%S')  # 获取当前时间
#     picture = file_path + '/' + now + '_' + name + '.png'  # 拼接截图保存地址
#     driver.save_screenshot(picture)  # 截图


class baseSelenium(object):
    def 