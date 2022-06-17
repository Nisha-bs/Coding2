#from tkinter import image_names
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://www.google.com/search?q=indian+peoples+passport+size+photo&rlz=1C1CHBF_enIN963IN963&sxsrf=ALiCzsYNqUmuRMoPz0wBvQ84N-8AgI26Gw:1652875083290&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjl_snB_-j3AhUMBt4KHV1SB2oQ_AUoAXoECAEQAw&biw=1366&bih=695&dpr=1')


count = 0
format = '.png'
images = driver.find_elements(By.XPATH,'//div[@jsname="r5xl4"]/div[@class="isv-r PNCib MSM1fd BUooTd"]/a[@class="wXeWr islib nfEiy"]')
for img in images:
    count+=1
    filename = str(count)+format
    with open(filename,'wb') as image: 
        image.write(img.screenshot_as_png)




   
