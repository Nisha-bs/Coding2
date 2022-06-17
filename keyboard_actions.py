from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)         
driver.get('https://text-compare.com/')
driver.maximize_window()
box1 = driver.find_element(By.XPATH,'//textarea[@id="inputText1"]')
box2 = driver.find_element(By.XPATH,'//textarea[@id="inputText2"]')

keyboard = ActionChains(driver)
box1.send_keys("welcome to selenium")

# keyboard.key_down(Keys.CONTROL)
# keyboard.send_keys('a')
# keyboard.key_up(Keys.CONTROL)
# keyboard.perform()

keyboard.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

# keyboard.key_down(Keys.CONTROL)
# keyboard.send_keys('c')
# keyboard.key_up(Keys.CONTROL)
# keyboard.perform()

keyboard.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

keyboard.send_keys(Keys.TAB).perform()  

# keyboard.key_down(Keys.CONTROL)
# keyboard.send_keys('v')
# keyboard.key_up(Keys.CONTROL)
# keyboard.perform()

keyboard.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()





