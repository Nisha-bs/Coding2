#!/usr/bin/python3
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver_obj = Service("/home/nisha/Downloads/chromedriver")
driver = webdriver.Chrome(service = driver_obj)
driver.get('https://www.youtube.com/')
driver.find_element(By.NAME,'search_query').send_keys('hello')
#time.sleep(2)
driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button/yt-icon").click()
#drive = driver.find_element(By.CLASS_NAME,'style-scope').click()
#drive.click()
