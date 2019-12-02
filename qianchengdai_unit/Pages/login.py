# -*- coding:utf-8 -*-
from Pages.basepage import BasePage
from selenium.webdriver import Chrome
from Data.locator import login_locator
from time import sleep


class LoginPage(BasePage):
    '''登录页面'''

    def register(self,username,password):
        '''定位登录界面元素'''
        #进入登录界面
        self.driver.get('http://120.78.128.25:8765/Index/login.html')
        #清空用户名和密码
        self.clear_user_name()
        self.clear_pass_word()
        #输入用户名
        self.get_user_name().send_keys(username)
        #输入密码
        self.get_passwork().send_keys(password)
        #点击登录
        self.get_button().click()

    def get_url(self):
        self.driver.get('http://120.78.128.25:8765/Index/login.html')

    def get_user_name(self):
        '''定位用户名'''
        user_name=self.wait(login_locator.username)
        return user_name

    def get_passwork(self):
        '''定位密码'''
        pass_word=self.wait(login_locator.password)
        return pass_word

    def get_button(self):
        '''定位登录按钮'''
        button=self.wait(login_locator.button)
        return button

    def get_actual_loginname(self):
        '''获取登录用户名'''
        name=self.wait(login_locator.login_name)
        return name.text

    def get_alter_error(self):
        '''获取弹框错误'''
        alter_error=self.wait(login_locator.alter_error)
        return alter_error.text

    def get_error_info(self):
        '''获取错误提示'''
        error_info=self.wait(login_locator.error_info)
        return  error_info.text

    def clear_user_name(self):
        '''清空用户名输入框'''
        ele=self.get_user_name().clear()
        return ele

    def clear_pass_word(self):
        '''清空密码输入框'''
        ele = self.get_passwork().clear()
        return ele


if __name__ == '__main__':
     LoginPage(Chrome()).register('18684720553','python')