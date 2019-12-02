# -*- coding:utf-8 -*-
from Pages.basepage import BasePage
from Data.locator.personal_locator import end_money


class PersonalPage(BasePage):
    '''个人信息界面'''
    def get_balance(self):
        '''获取投资后的余额'''
        ele=self.wait(end_money)
        return float(ele.text[:-1])
