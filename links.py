from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()
#driver.find_element(By.LINK_TEXT,'Apparel').click()
#driver.find_element(By.PARTIAL_LINK_TEXT,'App').click()

#find no.of links in page
links = driver.find_elements(By.XPATH,'//a')
for link in links:
    #print(link.get_attribute('href'))
    print(link.text)