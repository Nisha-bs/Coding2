#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()
driver.get('https://smallpdf.com/result#r=4aab499fd98c8afaf6b1c10483cff554&t=word')
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[2]/button/div/span').click()
driver.find.element(By.CLASS_NAME,'sc-14gpp6l-0 yfNpi').click()
driver.find_element(By.LINK_TEXT,'Button').click()
