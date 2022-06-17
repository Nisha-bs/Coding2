from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://itera-qa.azurewebsites.net/home/automation')
driver.maximize_window()

# #select specifc checkbox
# driver.find_element(By.XPATH,'//input[@id="monday"]').click()

# #select all the checkboxes
all_checkboxes = driver.find_elements(By.XPATH,'//input[@type="checkbox" and contains(@id,"day")]')
# for checkbox in all_checkboxes:
#     checkbox.click()

# #select multiple checkboxes
# checkboxes = driver.find_elements(By.XPATH,"//input[@id='monday' or @id='sunday']")
# for checkbox in checkboxes:
#     checkbox.click()

# for weekday in all_checkboxes:
#     checkbox = weekday.get_attribute('id')
#     if checkbox == 'monday' or checkbox == 'sunday':
#         weekday.click()
#     else:
#         pass

# #select last two checkboxes
total_checkboxes = len(all_checkboxes)
select_count = int(input('how many checkboxes you have to select'))
starts_from = total_checkboxes - select_count
for check_box in range(total_checkboxes-select_count,total_checkboxes):
    all_checkboxes[check_box].click()


# for check_box in range(total_checkboxes):
#     if check_box >= starts_from:
#         all_checkboxes[check_box].click()
#     else:
#         pass

# #select first two check_boxes
# total_checkboxes = len(all_checkboxes)
# select_count = int(input('how many checkboxes you have to select'))
# starts_from = total_checkboxes - select_count
# for check_box in range(select_count):
#     all_checkboxes[check_box].click()

# #clear all the checkboxes 
# for checkbox in all_checkboxes:
#     if checkbox.is_selected():
#         checkbox.click()
#     else:
#         pass
    
