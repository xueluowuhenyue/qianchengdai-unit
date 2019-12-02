# -*- coding:utf-8 -*-
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Common.Public import project_path
from Common.Public.Log import Mylog

logger=Mylog()


class BasePage:

    def __init__(self, driver: Chrome):
        self.driver = driver

    def wait(self, locator, timeout=10, poll_frequency=0.5, unm=1) -> WebElement:
        '''本函数用于等待元素'''
        Wait = WebDriverWait(self.driver,timeout,poll_frequency)
        try:
            if unm == 1:
                ele = Wait.until(ec.presence_of_element_located((locator)))
            else:
                ele = Wait.until(ec.presence_of_all_elements_located(locator))
            return ele
        except Exception as e:
            logger.error('出错啦错误是{}'.format(e))
            self.driver.save_screenshot(project_path.img_path)
            raise e

    def wait_click(self,locator,timeout=20,poll_frequency=0.5) -> WebElement:
        '''等待元素可以点击'''
        try:
            Wait = WebDriverWait(self.driver,timeout,poll_frequency)
            ele=Wait.until(ec.element_to_be_clickable(locator))
            return ele.click()
        except Exception as e:
            logger.error('出错啦错误是{}'.format(e))
            self.driver.save_screenshot(project_path.img_path)
            raise e

    def scroll_bar(self,ele):
        # 滚动页面到元素位置
        self.driver.execute_script("arguments[0].scrollIntoView(false);", ele)