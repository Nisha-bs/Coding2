#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pyautogui import click
driver = webdriver.Firefox()
#open webpage
driver.get('https://www.google.com/search?q=word+to+pdf+converter+online&client=ubuntu&hs=1IW&channel=fs&sxsrf=APq-WBuxn9jZ8X7McFtjoBWTI6cPVGbTFA%3A1650451115314&ei=q-JfYvblEpGO-AaVv7_ADg&ved=0ahUKEwi258nDuaL3AhURB94KHZXfD-gQ4dUDCA0&uact=5&oq=word+to+pdf+converter+online&gs_lcp=Cgdnd3Mtd2l6EAMyBwgjELADECcyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAELADEENKBAhBGABKBAhGGABQAFgAYHloAXABeACAAQCIAQCSAQCYAQDIAQrAAQE&sclient=gws-wiz')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div/a/h3').click()
time.sleep(5)
#Got it
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[2]/button/div/span').click()
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/header/div[2]/div/div[1]/div/div[2]/label/div/div[2]/form/label/div/div[2]/button[2]').click()
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/header/div[2]/div/div[1]/div/div[2]/label/div/div[2]/form/label/div/div[2]/div/button[1]').click()
click(192,248)
click(399,175)
click(1280,48)
driver.find_element(By.XPATH,"//span[text() = 'Download']").click()
driver.find_element(By.XPATH,"//span[text() = 'Save to device']").click()
time.sleep(20)
click(1288,131)
time.sleep(5)
click(1274,48)
