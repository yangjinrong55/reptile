#coding:utf-8
from unittest import TestSuite,makeSuite
from web.case import  *
from HTMLTestReportCN import HTMLTestRunner
import time
suite = TestSuite()
for i in range(2):
    suite.addTest(makeSuite(login,'test_login_success'))
suite.addTest(makeSuite(login,'test_login_error_password'))
suite.addTest(makeSuite(login,'test_login_error_username'))
suite.addTest(makeSuite(login,'test_all_empty'))
suite.addTest(makeSuite(login,'test_empty_username'))
suite.addTest(makeSuite(login,'test_empty_password'))
suite.addTest(makeSuite(login,'test_special_character'))

suite.addTest(makeSuite(order,'test_packages1'))
suite.addTest(makeSuite(order,'test_packages2'))
suite.addTest(makeSuite(order,'test_packages3'))
suite.addTest(makeSuite(order,'test_packages4'))
suite.addTest(makeSuite(order,'test_packages5'))
suite.addTest(makeSuite(order,'test_packages6'))

#当前时间
now = time.strftime("%Y-%m-%d", time.localtime(time.time()))
path = './' + now + 'result.html'

with open(path,'wb') as f:
    HTMLTestRunner(f,title='自动化测试报告',tester='Allen').run(suite)
