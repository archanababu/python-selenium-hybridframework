import string
import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.AddCustomerPage import AddCustomer
from PageObjects.LoginPage import LoginPage
from Utilities.CustomLogger import LogGen
from Utilities.ReadProperties import ReadConfig


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    email   = ReadConfig.getEmail()
    password= ReadConfig.getPassword()
    logger  = LogGen.loggen()

    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("****************************test_addCustomer***************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.login_page.setEmail(self.email)
        self.login_page.setPassword(self.password)
        self.login_page.clickLogin()                
        self.logger.info("Login successful")
        
        self.logger.info("Validating add customer feature")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()
        self.addCust.clickOnAddNewButton()
        self.logger.info("Clicked Add New button")

        self.logger.info("Providing new customer details")
        self.email = random_generator()+"@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setFirstname("TestFirstName")
        self.addCust.setLastname("TestLastName")
        self.addCust.clickOnGender("female")
        self.addCust.setDOB("4/7/2000")
        self.addCust.setCompany("TestCompany")
        self.addCust.clickOnTaxExcempt()
        # self.addCust.clickOnNewsletter("Your store name")
        self.addCust.clickOnCustomerRoles("Guests")
        self.addCust.clickOnVendorManager("Vendor 1")
        self.addCust.clickOnActive()
        self.addCust.setAdminComment("Testing add new customer feature")
        self.addCust.clickSave()
        self.logger.info("Clicked save button to add new customer")
        # self.driver = webdriver.Chrome(executable_path="C:\Workspace\WebDriver\chromedriver.exe")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        if "The new customer has been added successfully." in self.msg:
            self.logger.info("Adding new customer validation PASSED")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer.png")
            self.logger.info("Adding new customer validation FAILED")
            assert False

        self.driver.close()
        self.logger.info("Ending test_addCustomer test case")


def random_generator(size=8,chars= string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))        


        
        






            

