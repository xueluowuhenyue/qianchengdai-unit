# -*- coding:utf-8 -*-
from selenium.webdriver import Chrome
from Data.test_data import login_data
from selenium.webdriver.chrome.options import Options
from ddt import ddt,data
from Pages.login import LoginPage
import unittest
from time import sleep
from Common.Public.Log import Mylog
import pytest
logger=Mylog()


@ddt
class testLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls)->None:
        cls.driver=Chrome()
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # cls.driver = Chrome(chrome_options=chrome_options)
        cls.login = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls)->None:
        cls.driver.quit()

    @data(*login_data.success_data)
    def test_03_login_success(self,data):
        logger.info('正在执行{}模块第{}条测试用例,用例名字是:{},登录名是:{},登录密码是:{},期望值是:{}'.format(data['module'],
                                data['Caseid'],data['title'], data['username'],data['password'],data['expect']))
        # 登录
        self.login.register(data['username'],data['password'])
        # 获取登录用户名
        login_name=self.login.get_actual_loginname()
        try:
            self.assertEqual(data['expect'],login_name)
            Testresult='pass'
        except AssertionError as e:
            Testresult = 'fail'
            raise e
        finally:
            logger.info('{}模块第{}条测试用例,测试结果是{}'.format(data['module'],data['Caseid'],Testresult))

    @data(*login_data.alter_error)
    def test_02_login_alter_error(self,data):
        logger.info('正在执行{}模块第{}条测试用例,用例名字是:{},登录名是:{},登录密码是:{},期望值是:{}'.format(data['module'],
                                data['Caseid'],data['title'], data['username'],data['password'],data['expect']))

        self.login.register(data['username'], data['password'])
        actual = self.login.get_alter_error()
        try:
            self.assertEqual(data['expect'],actual)
            Testresult = 'pass'
        except AssertionError as e:
            Testresult = 'fail'
            raise e
        finally:
            logger.info('{}模块第{}条测试用例,测试结果是{}'.format(data['module'],data['Caseid'],Testresult))

    @data(*login_data.error_info)
    def test_01_login_error(self ,data):
        logger.info('正在执行{}模块第{}条测试用例,用例名字是:{},登录名是:{},登录密码是:{},期望值是:{}'.format(data['module'],
                                data['Caseid'],data['title'], data['username'],data['password'],data['expect']))

        self.login.register(data['username'], data['password'])
        actual = self.login.get_error_info()
        try:
            self.assertEqual(data['expect'],actual)
            Testresult = 'pass'
        except AssertionError as e:
            Testresult = 'fail'
            raise e
        finally:
            logger.info('{}模块第{}条测试用例,测试结果是{}'.format(data['module'],data['Caseid'],Testresult))


if __name__ == '__main__':
    unittest.main()