class LoginPage():
    #locators of all elements
    #http://admin-demo.nopcommerce.com/
    login_user_name = 'Email'
    login_user_password = 'Password'
    login_user_login = '//div[@class="buttons"]/button'
    login_user_logout = 'Logout'

    def __init__(self, driver):
        self.driver = driver
    
    def setUserName(self,username):
        self.driver.find_element_by_name(self.login_user_name).clear()
        self.driver.find_element_by_name(self.login_user_name).send_keys(username)
    
    def setPassword(self,password):
        self.driver.find_element_by_name(self.login_user_password).clear()
        self.driver.find_element_by_name(self.login_user_password).send_keys(password)
    
    def setLogin(self):
        self.driver.find_element_by_xpath(self.login_user_login).click()
    
    def setLogout(self):
        self.driver.find_element_by_link_text(self.login_user_logout).click()
