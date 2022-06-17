from atexit import register
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()
driver.find_element(By.XPATH,'//button[normalize-space() = "Click for JS Prompt"]').click()

popup = driver.switch_to.alert
print(popup.text)
popup.send_keys("welcome")      
#popup.accept()   #to accept alert window using ok button
popup.dismiss() #to close alert window using cancel button