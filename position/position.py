from browser import*

class postion(browser):
    def test_id(self):
        driver=browser().resueBrowser()
        driver.get('http://www.baidu.com')
        driver.find_element_by_id(id).send_keys('测试')
if __name__=='__main__':
    id='kw'
    unittest.main()
