# -*- encoding=utf8 -*-
__author__ = "韩春芳"

#元素定位：账号输入框，密码输入框，登录按钮，登录成功后页面元素
acct_loc = ("id", "pin")
psw_loc = ("id", "password")
loginBtn_loc = ("class name", "ant-btn")
loginFlag_loc = ("class name", "ui-hd")

def loginWebMall(driver, *parms):
    '''
    账号登录
    param driver:获取浏览器对象
    param *params:登录需要的账密
    return
    '''
    driver.send_keys(acct_loc, parms[0])
    driver.send_keys(psw_loc,  parms[1])
    driver.click(loginBtn_loc)
    if driver.is_exists(loginFlag_loc):
        return True