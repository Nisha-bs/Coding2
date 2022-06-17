#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException,ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import pyautogui


try :
#open chrome
        driver = webdriver.Chrome()
        #implicit wait
        #driver.implicitly_wait(10)
        #maximize window
        driver.maximize_window()
        #open google page
        driver.get('https://www.google.com')
        #searchbox
        search = driver.find_element(By.XPATH,"//input[@title='Search']")
        #type flipkart
        search.send_keys('flipkart')
        #enter
        search.submit()
        #for explicit wait
        mywait = WebDriverWait(driver,10,poll_frequency = 2, ignored_exceptions = [NoSuchElementException, ElementNotVisibleException,ElementNotSelectableException,Exception])
        #check flipkart is present or not using explicit wait
        searchlink = mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Flipkart']")))
        #if present click
        searchlink.click()
        #created object for login page
        login = driver.find_element(By.XPATH,'//div[@class="_2QfC02"]')
        #if loginpage is opened moved for login process
        if login:
                #enter username or phonenumber
                driver.find_element(By.XPATH,'//input[@class="_2IX_2- VJZDxU"]').send_keys('9790438091')
                #enter the password
                driver.find_element(By.XPATH,"//input[@type='password']").send_keys('nisha')
                #click login
                driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _2HKlqd _3AWRsL"]').click()
        else:
                driver.find_element(By.LINK_TEXT,'Login').click()
                #enter username or phonenumber
                driver.find_element(By.XPATH,'//input[@class="_2IX_2- VJZDxU"]').send_keys('9790438091')
                #enter the password
                driver.find_element(By.XPATH,"//input[@type='password']").send_keys('nisha')
                #click login
                driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _2HKlqd _3AWRsL"]').click()
        mouse = ActionChains(driver)
        time.sleep(5)
        Electronics = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[2]/div/div/div[5]/a/div[1]/div/img')
        mouse.move_to_element(Electronics).perform()
        Gaming = driver.find_element(By.LINK_TEXT,'Gaming') 
        mouse.move_to_element(Gaming).perform()
        time.sleep(3)
        Gaming_mouse = driver.find_element(By.LINK_TEXT,'Games')
        Gaming_mouse.click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//a[normalize-space()='Gaming Mouse']").click()
        links = driver.find_elements(By.XPATH,"//div[@class='_1AtVbE col-12-12'] /div[@class='_13oc-S']")
        print(len(links))
except:
        pass

