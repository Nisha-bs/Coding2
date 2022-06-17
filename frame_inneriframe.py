from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('http://demo.automationtesting.in/Frames.html')
driver.find_element(By.XPATH,'//a[normalize-space()="Iframe with in an Iframe"]').click()

innerframe1 = driver.find_element(By.XPATH,'//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(innerframe1)
innerframe2 = driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe2)

driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('welcome')
driver.switch_to.parent_frame() #directly  switch to outerframe
