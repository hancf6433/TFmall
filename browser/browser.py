from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

'''浏览器重复使用'''
class browser():
    def open_browser(self):
        os.popen('chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"')  # 使用cmd打开浏览器
    def resue_browser(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        chrome_driver = r"C:\Users\TS\AppData\Local\Google\Chrome\Application\chromedriver.exe"
        driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
        driver.maximize_window()
        return driver