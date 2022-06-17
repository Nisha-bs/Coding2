#!/usr/bin/python3

from selenium import webdriver

driver = webdriver.Chrome("/home/nisha/Downloads/chromedriver")
driver.get("https://acoe.annauniv.edu/sems/login/student")
driver.find_element_by_name("username").send_keys("2019236033")
driver.find_element_by_id("password").send_keys("nishasowmi")
#driver.find_element_by_name("captcha_code").send_keys("")

