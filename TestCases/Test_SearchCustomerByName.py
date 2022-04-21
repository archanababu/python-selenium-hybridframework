import time
from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomerPage import AddCustomer
from PageObjects.SearchCustomerPage import SearchCustomer
from Utilities.ReadProperties import ReadConfig
from Utilities.CustomLogger import LogGen

class Test_005_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL()
    email   = ReadConfig.getEmail()
    password= ReadConfig.getPassword()
    logger  = LogGen.loggen()

    def test_searchCustomerByName(self, setup):
        self.logger.info("****************************test_searchCustomerByName***************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.login_page.setEmail(self.email)
        self.login_page.setPassword(self.password)
        self.login_page.clickLogin()                
        self.logger.info("Login successful")
        
        self.logger.info("Validating search customer by email testing")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()

        self.searchCustomer = SearchCustomer(self.driver)
        self.firstname = "Victoria"        
        self.lastname = "Terces"
        self.fullname = self.firstname+" "+self.lastname
        self.searchCustomer.setFirstname(self.firstname)
        self.searchCustomer.setLastname(self.lastname)
        self.searchCustomer.search()

        time.sleep(5)        

        self.status = self.searchCustomer.searchCustomerByName(self.fullname)
        if self.status == True:
            self.logger.info("Search customer by name validation PASSED")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_searchCustomerByName.png")
            self.logger.info("Search customer by email validation FAILED")
            assert False

        self.driver.close()
        self.logger.info("Ending test_searchCustomerByName test case")

