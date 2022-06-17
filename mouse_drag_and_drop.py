#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

drag = driver.find_element(By.ID,'box1')
drop = driver.find_element(By.ID,'box101')

mouse = ActionChains(driver)

mouse.drag_and_drop(drag,drop).perform()
