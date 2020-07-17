import unittest
from function import *
from selenium.webdriver.common.keys import Keys  #导入键盘类
from time import sleep


url='https://passport.tfsandbox-dev.jcloudec.com/service-passport-view/login'
class login(unittest.TestCase):
    def test_login(self):
        browser().open_browser()
        driver=browser().resue_browser()
        driver.get(url)
        wait_element().wait_id('pin')   #等待元素出现
        driver.find_element_by_id("pin").send_keys(Keys.CONTROL, 'a')
        driver.find_element_by_id("pin").send_keys('test01')
        driver.find_element_by_id("password").send_keys(Keys.CONTROL, 'a')
        driver.find_element_by_id("password").send_keys('qwer12345')
        driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary ant-btn-lg']").click() #获取验证码
        wait_element().wait_class_name('yidun_tips')  #等待元素出现
        driver.find_element_by_class_name('yidun - fallback__tip').click()
        sleep(2)




if __name__=="__main__":
    unittest.main()