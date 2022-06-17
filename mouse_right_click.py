#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get('http://swisnl.github.io/jQuery-contextMenu/demo.html')
mouse = ActionChains(driver)
click = driver.find_element(By.XPATH,"//span[normalize-space() = 'right click me']")
mouse.context_click(click).perform()
