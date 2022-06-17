#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://www.snapdeal.com/')
driver.get('https://www.amazon.com/')
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)

