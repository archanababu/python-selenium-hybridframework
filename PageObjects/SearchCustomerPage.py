import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchCustomer:
    # Search customer page objects
    text_email_id = "SearchEmail"
    text_firstname_id = "SearchFirstName"
    text_lastname_id = "SearchLastName"
    text_dob_month_id = "SearchMonthOfBirth"
    text_dob_day_id = "SearchDayOfBirth"
    text_company_id = "SearchCompany"
    text_ipaddress_id = "SearchIpAddress"
    list_customer_role_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    button_search_id = "search-customers"

    def __init__(self,driver):
        driver = webdriver.Chrome(executable_path="C:\Workspace\WebDriver\chromedriver.exe")
        self.driver = driver 
    
    def setEmail(self, email):
        self.driver.find_element(By.ID,self.text_email_id).clear()
        self.driver.find_element(By.ID,self.text_email_id).send_keys(email)
    
    def setFirstname(self, firstname):
        self.driver.find_element(By.ID,self.text_firstname_id).clear()
        self.driver.find_element(By.ID,self.text_firstname_id).send_keys(firstname)
    
    def setLastname(self, lastname):
        self.driver.find_element(By.ID,self.text_lastname_id).send_keys(lastname)
    
    def setDOBMonth(self, month):
        self.driver.find_element(By.ID,self.text_dob_month_id).send_keys(month)

    def setDOBDay(self, day):
        self.driver.find_element(By.ID, self.text_dob_day_id).clear()
        self.driver.find_element(By.ID, self.text_dob_day_id).send_keys(day)

    def setIpAddress(self, ip):
        self.driver.find_element(By.ID, self.text_ipaddress_id).clear()
        self.driver.find_element(By.ID, self.text_ipaddress_id).send_keys(ip)

    def setCustomerRole(self, customer):
        self.driver.find_element(By.XPATH, self.list_customer_role_xpath).send_keys(customer)

    def search(self):
        self.driver.find_element(By.ID, self.button_search_id).click()



