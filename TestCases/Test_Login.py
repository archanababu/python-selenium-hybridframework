from PageObjects.LoginPage import LoginPage
from Utilities.ReadProperties import ReadConfig

class Test_001_Login: #For pytest the class
    baseURL     = ReadConfig.getApplicationURL()
    email       = ReadConfig.getEmail
    password    = ReadConfig.getPassword

    def test_homePageTitle(self, setup): 
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        
        if act_title == "Your store. Login":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.login_page.setEmail(self.email)
        self.login_page.setPassword(self.password)
        self.login_page.clickLogin()
        act_title = self.driver.title
                
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            assert False

