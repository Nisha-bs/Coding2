#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()
driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')

##scroll down page by pixel
#driver.execut_script("window.scrollBy(0,3000)","")
#value = driver.execut_script("return window.pageYOffset;")
#print(value)

##scroll down the pae till the element is visible
#flag = driver.find_element(By.XPATH,'//img[@src="flags-normal/flag-of-India.png"]')
#driver.execute_script("arguments[0].scrollIntoView();",flag)
#value = driver.execute_script("return window.pageYOffset;")
#print(value)

#scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print(value)

#scroll upto starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print(value)



