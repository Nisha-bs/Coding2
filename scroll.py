from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)


driver.get('https://www.google.com/search?q=car+number+plate+images&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiqsZjU55j4AhVX7nMBHVXBBTQQ_AUoAXoECAEQAw&biw=1294&bih=621')



last_height = driver.execute_script('\
    return document.body.scrollHeight')
 
while True:
    driver.execute_script('\
    window.scrollTo(0,document.body.scrollHeight)')
 
    # waiting for the results to load
    # Increase the sleep time if your internet is slow
    time.sleep(3)
 
    new_height = driver.execute_script('\
    return document.body.scrollHeight')
 
    # click on "Show more results" (if exists)
    try:
        driver.find_element_by_css_selector(".YstHxe input").click()
 
            # waiting for the results to load
            # Increase the sleep time if your internet is slow
        time.sleep(3)
 
    except:
        pass
 
        # checking if we have reached the bottom of the page
    if new_height == last_height:
        break
 
    last_height = new_height