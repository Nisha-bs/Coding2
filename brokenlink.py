from itertools import count
from lib2to3.pgen2 import driver
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get('http://www.deadlinkcity.com/')
driver.maximize_window() 
links = driver.find_elements(By.XPATH,'//a')
count = 0
for ele in links:
    link = ele.get_attribute('href')
    try:
        url = requests.head(link)
    except:
        None
    if url.status_code>=400:
        #print('broken url is  ',link)
        count += 1
    else:
        #print(url)
        pass

print(count)