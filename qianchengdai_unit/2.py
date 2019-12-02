# -*- coding:utf-8 -*-
# from time import sleep
# from selenium.webdriver import Chrome
#
# driver=Chrome()
#
# driver.get('http://120.78.128.25:8765/Index/login.html')
#
# driver.find_element_by_name('phone').send_keys('18684720553')
#
# driver.find_element_by_name('password').send_keys('python')
#
# driver.find_element_by_xpath("//button[text()='登录']").click()
# sleep(20)
# driver.find_element_by_xpath("//a[text()='我的帐户[小蜜蜂96027921]']").click()
# sleep(10)
# driver.find_element_by_xpath("//div[@class='px_card']//*[text()='交易记录']").click()
# sleep(10)
# list=driver.find_elements_by_xpath("/html/body/div[3]/div[5]/div[6]/table/tbody/tr[1]")
# list='2019-05-12\n16:56\n投资借出\n交易单号：00311951050512165659668\n成功\n-100.00\n投资项目“先借一个亿”，预计收益：0.17元'
# a=list.split('\n')
# print(a)
# for i in a:
#     print(i)
# print(len(a))
#
# print('-100.00' in a)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://www.baidu.com")
ele=driver.find_element_by_xpath("//input[@id='kw']")
#打印内容
print(ele)
driver.quit()
