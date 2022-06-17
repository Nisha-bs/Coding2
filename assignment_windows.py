from multiprocessing.sharedctypes import Value
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://testautomationpractice.blogspot.com/')
# #first_frame = driver.find_element(By.CLASS_NAME,'column-left-outer')
# #driver.switch_to.frame('sidebar-left-1')

# driver.find_element(By.ID,'Wikipedia1_wikipedia-search-input').send_keys('selenium')
# driver.find_element(By.CLASS_NAME,'wikipedia-search-button').click()
# links = driver.find_elements(By.XPATH,'//div[@id="wikipedia-search-result-link"]')
# for link in links:
#     print(link.text)

# driver.find_element(By.LINK_TEXT,'Selenium').click()
# driver.find_element(By.LINK_TEXT,'Selenium in biology').click()
# driver.find_element(By.LINK_TEXT,'Selenium (software)').click()
# driver.find_element(By.LINK_TEXT,'Selenium disulfide').click()
# driver.find_element(By.LINK_TEXT,'Selenium dioxide').click()

# windows = driver.window_handles
# for window in windows:
#     print(driver.title)


driver.switch_to.frame(0)
driver.find_element(By.ID,'RESULT_TextField-1').send_keys("Nisha")
driver.find_element(By.ID,'RESULT_TextField-2').send_keys("Venkatesan")
driver.find_element(By.ID,'RESULT_TextField-3').send_keys("9790438091")
driver.find_element(By.ID,'RESULT_TextField-4').send_keys("India")
driver.find_element(By.ID,'RESULT_TextField-5').send_keys("Chennai")
driver.find_element(By.ID,'RESULT_TextField-6').send_keys("aswinkasthuriaswin@gmail.com")
driver.find_element(By.XPATH,'//label[@for="RESULT_RadioButton-7_1"]').click()
week_days = driver.find_elements(By.XPATH,'//input[@type="checkbox"]')
driver.find_element(By.XPATH,"/label[@for='RESULT_CheckBox-8_2']").click()
driver.find_element(By.XPATH,"/label[@for='RESULT_CheckBox-8_3']").click()
driver.find_element(By.XPATH,"/label[@for='RESULT_CheckBox-8_4']").click()
driver.find_element(By.XPATH,"/label[@for='RESULT_CheckBox-8_5']").click()




# for available_week_days in range(len(week_days)-1):
#     #print(week_days[available_week_days].get_attribute('value'))
#     week_days[available_week_days].click()
#driver.quit()

