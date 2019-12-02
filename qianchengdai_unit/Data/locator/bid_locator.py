# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

# 输入框
input_ele=(By.XPATH,"//input[@data-url='/Invest/invest']")
# 投标按钮
button=(By.XPATH,"//button[text()='投标']")
# 投标成功提示
bid_prompt=(By.XPATH,"//div[contains(@class,'content')]//div[text()='投标成功！']")
# 定位弹窗按钮
alert_button=(By.XPATH,"//div[contains(@class,'content')]//button")
# 输入非整拾数
error_button=(By.XPATH,"//div[@class='pd-right']//button")
# 弹框确认按钮
alter_confirm=(By.XPATH,"//div[@class='text-center']/parent::div/following-sibling::div/a")
# 获取投标失败提示
error_prompt=(By.XPATH,"//div[@class='text-center']")
# 退出登录按钮
quit_button=(By.XPATH,"//a[text()='退出']")