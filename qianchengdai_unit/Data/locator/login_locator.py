# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

username = (By.XPATH, "//input[@name='phone']")
password = (By.XPATH, "//input[@name='password']")
button = (By.XPATH, "//button[text()='登录']")
login_name = (By.XPATH, "//a[contains(@href,'Member')]")
alter_error=(By.XPATH, "//div[@class='layui-layer-content']")
error_info= (By.XPATH,"//div[@class='form-error-info']")