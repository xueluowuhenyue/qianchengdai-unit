# -*- coding:utf-8 -*-
from Pages.basepage import BasePage
from Data.locator import bid_locator


class BidPage(BasePage):
    ' ' '项目页面' ' '

    def get_input(self):
        '''定位输入框'''
        input_ele=self.wait(bid_locator.input_ele)
        return input_ele

    def get_button(self):
        # 点击投标按钮
        self.wait_click(bid_locator.button)

    def get_begin_money(self):
        ' ' '获取开始余额 ' ' '
        money=self.get_input().get_attribute('data-amount')
        return float(money)

    def input_money(self,money):
        '''输入投资金额'''
        self.get_input().send_keys(money)

    def get_prompt(self):
        '''获取投标提示'''
        ele=self.wait(bid_locator.bid_prompt)
        return ele.text

    def alter_click(self):
        '''点击弹框中的按钮'''
        self.wait_click(bid_locator.alert_button)

    def get_button_prompt(self):
        '''获取按钮上的提示'''
        ele=self.wait(bid_locator.error_button)
        return ele.text

    def click_confirm(self):
        '''点击弹框确认'''
        self.wait_click(bid_locator.alter_confirm)

    def get_error_prompt(self):
        '''错误提示'''
        ele=self.wait(bid_locator.error_prompt)
        return ele.text

    def scroll(self):
        # 滚动页面到指定元素位置
        self.scroll_bar(self.get_input())

    def quit_login(self):
        self.wait_click(bid_locator.quit_button)

    def clear_input(self):
        '''清空输入框'''
        return self.get_input().clear()


if __name__ == '__main__':
   pass