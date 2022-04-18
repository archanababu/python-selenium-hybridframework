from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    #Login page elements
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[contains(text(),'Log in')]"
    link_logout_linktext = "Logout"

    def __init__(self,driver):
        # driver = webdriver.Chrome(executable_path="C:\Workspace\WebDriver\chromedriver.exe")
        self.driver = driver        
    
    def setEmail(self, email):
        self.driver.find_element(By.ID,self.textbox_email_id).clear()
        self.driver.find_element(By.ID,self.textbox_email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()

    
    
