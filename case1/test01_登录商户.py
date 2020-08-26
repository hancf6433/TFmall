import unittest
from function import *
from readXml import *
from selenium.webdriver.common.keys import Keys  #导入键盘类
from time import sleep

class login(unittest.TestCase):
    def test_login(self):
        browser().open_browser()
        driver=browser().resue_browser()
        driver.get(readxml("url"))
        element((By.ID,'pin')).send_keys(Keys.CONTROL, 'a')          #全选
        element((By.ID, 'pin')).send_keys(readxml("name"))           #输入账户名
        element((By.ID, "password")).send_keys(Keys.CONTROL, 'a')    #全选
        element((By.ID, "password")).send_keys(readxml("password"))  #输入密码
        element((By.XPATH,"//button[@class='ant-btn ant-btn-primary ant-btn-lg']")).click() #获取验证码
        element((By.CLASS_NAME,'yidun_tips'))  #等待元素出现
        element((By.CLASS_NAME,'yidun - fallback__tip')).click()
        sleep(2)

if __name__=="__main__":
    unittest.main()