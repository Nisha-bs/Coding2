from lib2to3.pgen2 import driver
from requests import options
from selenium  import webdriver
from selenium.webdriver.common.by import By
import os
location = os.getcwd()

# def Chrome_setup():

 
#     preferences = {"download.default_directory":location,"plugins.always_open_pdf_externally":True}
#     ops = webdriver.ChromeOptions()
#     ops.add_experimental_option("prefs",preferences)
#     driver = webdriver.Chrome(options = ops)
#     return driver



def Firefox_setup():
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf")
    ops.set_preference("browser.download.manager.showWhenStrating",False)
    ops.set_preference("browser.download.folderList",2)
    ops.set_preference("browser.download.dir",location)
    ops.set_preference("pdfjs.disabled",True)
    driver = webdriver.Firefox(options = ops)
    return driver

driver = Firefox_setup()
driver.get('https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/')
driver.maximize_window()
driver.find_element(By.XPATH,'//tbody/tr[1]/td[5]/a').click()