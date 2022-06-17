from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://www.pin-up465.com/en/slots/spribe/aviator')


# values = driver.find_elements(By.XPATH,'//div[@class="payouts-block"]')
# for val in values:
#     print(val.text)

values = driver.find_elements(By.XPATH,'//div[@class="payouts-block"]/app-payout-item')
for val in values:
    print(val.text)
# driver.find_element(By.LINK_TEXT,' 1.02x ').click()   

