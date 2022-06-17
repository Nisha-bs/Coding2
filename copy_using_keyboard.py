from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get('https://en.wikipedia.org/wiki/Apress')
mouse = ActionChains(driver)
mouse.key_down(Keys.CONTROL)
heading = driver.find_element(By.ID,'firstHeading')
mouse.send_keys("a")\
.key_up(Keys.CONTROL)\
#         .key_down(Keys.CONTROL)\
#         .send_keys("c")\
#         .key_up(Keys.CONTROL)\
#         .perform()