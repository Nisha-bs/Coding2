#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get('https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/')
left_drag = driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[1]')
right_drag = driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[2]')

print(left_drag.location)
print(right_drag.location)

mouse = ActionChains(driver)
mouse.drag_and_drop_by_offset(left_drag,100,0).perform()
mouse.drag_and_drop_by_offset(right_drag,-100,0).perform()



