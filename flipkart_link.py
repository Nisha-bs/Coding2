from lib2to3.pgen2 import driver
from platform import java_ver
from shutil import move
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('https://www.flipkart.com/gaming/games/pr?sid=4rr,fa6&fm=neo%2Fmerchandising&iid=M_6851d8b1-4b03-48ef-9b5d-227a4af1b896_1_372UD5BXDFYS_MC.7OVL0P8FJ3EW&otracker=hp_rich_navigation_6_1.navigationCard.RICH_NAVIGATION_Electronics~Gaming~Games_7OVL0P8FJ3EW&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_6_L2_view-all&cid=7OVL0P8FJ3EW')
next_page = '1'

def stored_books():
    global next_page
    links = driver.find_elements(By.XPATH,"//a[@class='s1Q9rs']")
    book_name_list = []
    for name in links:
        book_name_list.append(name.get_attribute('title'))       
    book_name = input("enter the book name   ")
    
    if book_name not in book_name_list:
        if next_page >= '6':
            driver.close()
        else:
            pass
    else:
        print(book_name)
        driver.close()
    next_page = input('enter next page')    
  
    if next_page == '2':
            page = driver.find_element(By.LINK_TEXT,'2')
            page.click()
            stored_books()
    elif next_page == '3':
            page = driver.find_element(By.LINK_TEXT,'3')
            page.click()
            stored_books()
    elif next_page == '4':
            page = driver.find_element(By.LINK_TEXT,'4')
            page.click()
            stored_books()
    elif next_page == '5':
            page = driver.find_element(By.LINK_TEXT,'5')
            page.click()
            stored_books()
    elif next_page == '6':
            page = driver.find_element(By.LINK_TEXT,'6')
            page.click()
            stored_books()

stored_books()
