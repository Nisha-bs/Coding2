from lib2to3.pgen2 import driver
# from multiprocessing.sharedctypes import Value
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://github.com/new')
driver.find_element(By.XPATH,'//input[@id="login_field"]').send_keys('nishavengetsha@gmail.com')
driver.find_element(By.XPATH,'//input[@id="password"]').send_keys('Nisha@9790438091')
driver.find_element(By.XPATH,'//input[@name="commit"]').click()

# #verification page
# login_check = driver.find_element(By.XPATH,'//div[@id="login"]/p/a')
# print(login_check.text)

# if login_check.text == 'two-factor authentication':
#     time.sleep(40)
# else:
#     pass


# #create repository
# driver.find_element(By.XPATH,'//input[@id="repository_name"]').send_keys(input('enter the repositoyr name'))

# while True:
#     check_error = driver.find_element(By.XPATH,'//auto-check[@class="js-repo-name-autocheck"]/dl/dd[2]')
#     if check_error.get_attribute('class') == 'error':
#         driver.find_element(By.XPATH,'//input[@id="repository_name"]').clear()
#         driver.find_element(By.XPATH,'//input[@id="repository_name"]').send_keys(input('enter the repositoyr name'))
#         time.sleep(2)
#     elif check_error.get_attribute('class') == 'success':
#         break
#     else:
#         break

# driver.find_element(By.XPATH,'//button[@type="submit" and @data-view-component="true"]').click()


# #uploading a file
# driver.find_element(By.LINK_TEXT,'uploading an existing file').click()
# driver.find_element(By.XPATH,'//input[@id="upload-manifest-files-input"]').send_keys(input('enter the location'))
# time.sleep(5)
# driver.find_element(By.XPATH,'//button[@data-edit-text="Commit changes"]').click()

#delete a repository
# my_wait = WebDriverWait(driver, 10, poll_frequency=2)
# profile_page = my_wait.until(EC.presence_of_element_located((By.XPATH,'//img[@alt="@Nisha-bs" and @class="avatar avatar-small circle"]'))).click()

driver.find_element(By.XPATH,'//header[@role="banner"]/div[@class="Header-item position-relative mr-0 d-none d-md-flex"]').click()
driver.find_element(By.LINK_TEXT,'Your repositories').click()
repositories = driver.find_elements(By.XPATH,'//a[@itemprop="name codeRepository"]')
# print(repositories)
#
available_repository = input('enter profile name with "/" ' )
repo_list = []
for repository in repositories:
    print(repository.text)
    repo_list.append(repository.text)
print('repository',repository)

while True:
    repository_name = input("enter the repository name")
    for i in range(len(repo_list)):
        if repository_name == repo_list[i]:
            repositories[i].click()
        
            # if repository_name in repo_list:
            #     repository.click()
            #     break
            # else:
            #     continue

            print(repo_list)

            time.sleep(10)
            #click settings

            my_wait = WebDriverWait(driver, 10)
            settings = my_wait.until(EC.element_to_be_clickable((By.XPATH,'//span[@data-content="Settings"]')))

            # settings.click()

            driver.find_element(By.XPATH,'//*[@id="settings-tab"]').click()
            #click delete button
            time.sleep(5)

            driver.find_element(By.XPATH,'/html/body/div[5]/div/main/div[2]/div[2]/div/div[2]/div/div/div/div[8]/ul/li[4]/details/summary').click()
            #verify repository
            verification_repository = available_repository+repository_name
            print(verification_repository)
            driver.find_element(By.XPATH,'//input[@name="verify" and @aria-label="Type in the name of the repository to confirm that you want to change the visibility of this repository."]').send_keys('Nisha-bs/nisha')
            driver.find_element(By.XPATH,'//*[@id="options_bucket"]/div[8]/ul/li[4]/details/summary').click()
        else:
            continue
                    
