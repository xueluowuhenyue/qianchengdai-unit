# -*- coding:utf-8 -*-
from selenium.webdriver import Chrome
from Data.test_data import bid_data
from ddt import ddt,data
from Pages.login import LoginPage
from Pages.home import HomePage
from Pages.bid import BidPage
from Pages.personal import PersonalPage
import unittest
from Common.Public.Log import Mylog

logger=Mylog()


@ddt
class Bid(unittest.TestCase):

    @classmethod
    def setUpClass(cls)->None:
        cls.driver=Chrome()
        # 登录页面
        cls.login=LoginPage(cls.driver)
        # 首页
        cls.home =HomePage(cls.driver)
        # 投资页面
        cls.bid = BidPage(cls.driver)
        # 个人页面
        cls.personal=PersonalPage(cls.driver)
        # 登录
        cls.login.register(bid_data.login_data['user_name'], bid_data.login_data['password'])
        # 选择投标项目“先借一个亿”
        cls.home.get_bid_project()
        # 滚动滑动条
        cls.bid.scroll()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        # 清空输入框
        self.bid.clear_input()

    @data(*bid_data.seccess_data)
    def test_03_seccess(self,data):
        logger.info('正在执行{}模块第{}条测试用例,用例名字是:{},项目名字是：{},投资金额是:{},期望结果:{}'.format(data['module'],
        data['Caseid'], data['title'], data['bid_name'], data['amount'], data['expect']))

        # 获取投资前的金额
        begin_money=int(self.bid.get_begin_money()*100)
        # print(begin_money)
        # 投资
        self.bid.input_money(data['amount'])
        # 点击投资按钮
        self.bid.get_button()
        # 获取提示
        prompt=self.bid.get_prompt()
        # 点击弹窗按钮
        self.bid.alter_click()
        # 获取投资后的余额
        end_money=int(self.personal.get_balance()*100)
        # print(end_money)
        try:
            self.assertEqual(prompt,data['expect'])
            self.assertEqual(begin_money,end_money+int(data['amount'])*100)
            Testresult = 'pass'
        except AssertionError as e:
            Testresult = 'fail'
            raise e
        finally:
            logger.info('{}模块第{}条测试用例,测试结果是{}'.format(data['module'], data['Caseid'], Testresult))

    @data(*bid_data.error_whole_ten)
    def test_02_whole_ten(self,data):
        logger.info('正在执行{}模块第{}条测试用例,用例名字是:{},项目名字是：{},投资金额是:{},期望结果:{}'.format(data['module'],
                data['Caseid'], data['title'],data['bid_name'], data['amount'],data['expect']))

        # 输入不是10的倍数金额
        self.bid.input_money(data['amount'])
        # 获取提示
        context=self.bid.get_button_prompt()
        try:
            self.assertEqual(context,data['expect'])
            Testresult = 'pass'
        except AssertionError as e:
            Testresult = 'fail'
            raise e
        finally:
            logger.info('{}模块第{}条测试用例,测试结果是{}'.format(data['module'], data['Caseid'], Testresult))

    @data(*bid_data.error_data)
    def test_01_error(self, data):
        logger.info('正在执行{}模块第{}条测试用例,用例名字是:{},项目名字是：{},投资金额是:{},期望结果:{}'.format(data['module'],
                        data['Caseid'], data['title'],data['bid_name'], data['amount'], data['expect']))

        # 输入投资金额
        self.bid.input_money(data['amount'])
        # 点击投资按钮
        self.bid.get_button()
        # 获取错误提示
        context=self.bid.get_error_prompt()
        # 点击确认
        self.bid.click_confirm()
        try:
            self.assertEqual(context,data['expect'])
            Testresult = 'pass'
        except AssertionError as e:
            Testresult = 'fail'
            raise e
        finally:
            logger.info('{}模块第{}条测试用例,测试结果是{}'.format(data['module'], data['Caseid'], Testresult))


if __name__ == '__main__':
    unittest.main()