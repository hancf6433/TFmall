import unittest
import HTMLTestRunnerCN
import time
import os

# 测试用例存放及测试报告路径
runPath=os.path.dirname(__file__)
case_path=os.path.join(runPath,'case')
report_path=os.path.join(runPath,'report')

# 获取所有测试用例
def get_allcase():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")  #批量执行
    # discover = unittest.defaultTestLoader.discover(case_path, pattern="test_05_订单管理.py")  #单条执行
    suite = unittest.TestSuite()
    suite.addTest(discover)
    return suite

# 运行测试用例
if __name__ == '__main__':
    now=time.strftime('%Y_%m_%d %H-%M-%S')          #获取当前时间
    report_name=report_path+'/'+now+'_testReport.html'  #报告文件完整路径
    with open(report_name,'wb') as f:
        runner=HTMLTestRunnerCN.HTMLTestReportCN(stream=f,title='天府商城商户web端测试报告',
                                                 description='自动化测试结果',tester = "韩春芳")
        runner.run(get_allcase())                   #执行所有用例
    f.close()