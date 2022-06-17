from atexit import register
from itertools import count
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://demoqa.com/select-menu')
driver.maximize_window()
colors = driver.find_element(By.ID,'oldSelectMenu')

#colors.click()
color = Select(colors) 

#color.select_by_visible_text("Blue")
#color.select_by_value('1')
#color.select_by_index(1)

# #cpature all options
# color_options = color.options
# print(len(color_options))

color_options = driver.find_elements(By.XPATH,'//option')

# #select option from dropdown without using inbuiltin function
for col in color_options:
    if col.text == 'Blue':
        col.click()
        break
    else:
        pass
