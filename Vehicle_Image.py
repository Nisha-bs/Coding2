#!/usr/bin/python3

#from tkinter import image_names
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://www.google.com/search?q=indian+vehicle+number+plate+images&sxsrf=ALiCzsYN76Z1eFYqXRKyfWPwTX6inQLZkA:1654515768242&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjLuJDF35j4AhX1jOYKHUWXBowQ_AUoAXoECAEQAw&biw=1294&bih=636&dpr=1')


count = 0
format = '.png'
images = driver.find_elements(By.XPATH,'//div[@jsname="r5xl4"]/div[@class="isv-r PNCib MSM1fd BUooTd"]/a[@class="wXeWr islib nfEiy"]')
time.sleep(5)
for img in images:
    count+=1
    filename = str(count)+format
    with open(filename,'wb') as image:
        image.write(img.screenshot_as_png)
