from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://meet.google.com/')
driver.find_element(By.XPATH,'//select[@id="lang-selector"]').click()
driver.find_element(By.XPATH,'//select/option[@value="/intl/en/meet/"]').click()
driver.find_element(By.XPATH,'//a[@event-action="start a meeting" and @event-category="hero"]/button').click()
driver.find_element(By.XPATH,'//input[@id="identifierId"]').send_keys(input('enter gmail'))
time.sleep(5)
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys(input('enter the password'))
driver.find_element(By.XPATH,'//span[@jsname="V67aGc"]').click()