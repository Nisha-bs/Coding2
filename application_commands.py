#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.snapdeal.com/')

'''#page_tile
title_ = driver.title
page_title = 'Shop Online for Men, Women & Kids Clothing, Shoes, Home Decor Items'
if title_ == page_title:
    print(title_)
else:
    print("no")'''

'''#current_url
print(driver.current_url)'''

#pagesoure
#print(driver.page_source)


driver.close()

