#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2doB4z']").click()
time.sleep(1)
driver.find_element(By.LINK_TEXT,"Electronics Store").click()
time.sleep(1)
driver.close()
#driver.quit()
