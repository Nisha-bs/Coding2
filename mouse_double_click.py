#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3')
driver.maximize_window()
driver.switch_to.frame('iframeResult')
Button = driver.find_element(By.XPATH,'//button[normalize-space() = "Copy Text"]')
mouse = ActionChains(driver)
mouse.double_click(Button).perform()



