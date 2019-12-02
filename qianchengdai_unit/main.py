from Cases import test_login
import HTMLTestRunnerNew
import unittest

suite=unittest.TestSuite()
loader=unittest.TestLoader()

suite.addTest(loader.loadTestsFromModule(test_login))

with open('Result/report/test.html','wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='前程贷web页面测试',
                                            description='单元测试框架复习',
                                            tester='小明')
    runner.run(suite)