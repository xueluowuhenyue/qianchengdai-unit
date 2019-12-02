# -*- coding:utf-8 -*-

from Pages.basepage import BasePage
from Data.locator import home_locator


class HomePage(BasePage):
    '''首页'''

    # 选择投标项目“先借一个亿”
    def get_bid_project(self):
        self.wait_click(home_locator.bid_project)

