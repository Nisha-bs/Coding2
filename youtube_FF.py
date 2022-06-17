#!/usr/bin/python3
#from selenium.webdriver.Firefox.service import Service
#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
#driver_obj = Service("/home/nisha/Downloads/geckodriver-v0.31.0-linux64")
driver = webdriver.Firefox()
driver.get('https://www.youtube.com/')
driver.find_element(By.NAME,value='search_query').send_keys('hello')
#time.sleep(2)
driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button/yt-icon").click()
#drive = driver.find_element(By.CLASS_NAME,'style-scope').click()
#drive.click()
