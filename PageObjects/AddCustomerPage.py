import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class AddCustomer:
    #Add Customer Page object elements
    linkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(), 'Customers')]"
    linkCustomers_menuItems_xpath = "//a[@href='/Admin/Customer/List']//span[contains(text(), 'Customers')]"
    button_addNew_xpath = "//a[@href='/Admin/Customer/Create']//span[contains(text(), 'Add new')]"
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    textbox_firtname_id = "FirstName"
    textbox_lastname_id = "LastName"
    radiobutton_male_xpath = "//label[contains(text(),'Male')]"
    radiobutton_female_xpath = "//label[contains(text(),'Female')]"
    textbox_dob_id = "DateOfBirth"
    textbox_company_id = "Company"
    checkbox_taxexempt_id = "IsTaxExempt"
    list_newsletter_1_xpath = "//li[contains(text(),'Your store name')]"
    list_newsletter_2_xpath = "//li[contains(text(),'Test store 2')]"
    dropdown_vendor_id = "VendorId"
    dropdown_notvendor_xpath = "//option[contains(text(),'Not a vendor')]"
    dropdown_vendor_1_xpath = "//option[contains(text(),'Vendor 1')]"
    dropdown_vendor_2_xpath = "//option[contains(text(),'Vendor 2')]"
    tagList_CustomerRoleIds_id = "SelectedCustomerRoleIds_taglist"
    list_administrator_xpath = "//li[contains(text(),'Administrators')]"
    list_forum_moderators_xpath = "//li[contains(text(),'Forum Moderators')]"
    list_guest_xpath = "//li[contains(text(),'Guests')]"
    list_registered_xpath = "//li[contains(text(),'Registered')]"
    list_vendor_xpath = "//li[contains(text(),'Vendors')]"
    checkbox_active_id = "Active"
    textbox_admincomment_id = "AdminComment"
    button_save_xpath = "//button[@name='save']"
    role = ""

    def __init__(self,driver):
        driver = webdriver.Chrome(executable_path="C:\Workspace\WebDriver\chromedriver.exe")
        self.driver = driver 

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH(self.linkCustomers_menu_xpath)).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH(self.linkCustomers_menuItems_xpath)).click()

    def clickOnAddNewButton(self):
        self.driver.find_element(By.XPATH(self.button_addNew_xpath)).click()

    def setEmail(self, email):
        self.driver.find_element(By.ID(self.textbox_email_id)).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID(self.textbox_password_id)).send_keys(password)

    def setFirstname(self, firstname):
        self.driver.find_element(By.ID(self.textbox_firtname_id)).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element(By.ID(self.textbox_lastname_id)).send_keys(lastname)

    def clickOnGender(self, gender):
        if gender == "male":
            self.driver.find_element(By.XPATH(self.radiobutton_male_xpath)).click()
        elif gender == "female":
            self.driver.find_element(By.XPATH(self.radiobutton_female_xpath)).click()
        else:
            self.driver.find_element(By.XPATH(self.radiobutton_female_xpath)).click()

    def setDOB(self, dob):
        self.driver.find_element(By.ID(self.textbox_dob_id)).send_keys(dob)

    def setCompany(self, company):
        self.driver.find_element(By.ID(self.textbox_company_id)).send_keys(company)

    def clickOnTaxExcempt(self):
        self.driver.find_element(By.ID(self.checkbox_taxexempt_id)).click()

    def clickOnNewsletter(self, newsLetter):
        if newsLetter == "Your store name":
            self.driver.find_element(By.XPATH(self.list_newsletter_1_xpath)).click()
        elif newsLetter == "Test store 2":
            self.driver.find_element(By.XPATH(self.list_newsletter_2_xpath)).click()
        else:
            self.driver.find_element(By.XPATH(self.list_newsletter_2_xpath)).click()
        
    def clickOnCustomerRoles(self, role):
        self.role = role
        #remove default registered option
        self.driver.find_element(By.ID(self.tagList_CustomerRoleIds_id)).click()
        self.driver.find_element(By.XPATH(self.list_registered_xpath)).click()
        self.driver.find_element(By.ID(self.tagList_CustomerRoleIds_id)).click()
        time.sleep(3)
        if role == "Administrators":
            self.driver.find_element(By.XPATH(self.list_administrator_xpath)).click()
        elif role == "Forum Moderators":
            self.driver.find_element(By.XPATH(self.list_forum_moderators_xpath)).click()
        elif role == "Guests":
            self.driver.find_element(By.XPATH(self.list_guest_xpath)).click()
        elif role == "Registered":
            self.driver.find_element(By.XPATH(self.list_registered_xpath)).click()
        elif role == "Vendors":
            self.driver.find_element(By.XPATH(self.list_vendor_xpath)).click()
        else:
            self.driver.find_element(By.XPATH(self.list_guest_xpath)).click()

    def clickOnVendorManager(self, vendor):
        self.driver.find_element(By.ID(self.dropdown_vendor_id)).click()
        time.sleep(3)
        if vendor == "Not a vendor" and self.role != " Vendors":
            self.driver.find_element(By.XPATH(self.dropdown_notvendor_xpath)).click()
        elif vendor == "Not a vendor" and self.role == " Vendors":
            self.driver.find_element(By.XPATH(self.dropdown_vendor_1_xpath)).click()
        elif vendor == "Vendor 1":
            self.driver.find_element(By.XPATH(self.dropdown_vendor_1_xpath)).click()
        elif vendor == "Vendor 2":
            self.driver.find_element(By.XPATH(self.dropdown_vendor_2_xpath)).click()
        else:
            self.driver.find_element(By.XPATH(self.dropdown_notvendor_xpath)).click()

    def clickOnActive(self):
        self.driver.find_element(By.ID(self.checkbox_active_id)).click()

    def setAdminComment(self, adminComment):
        self.driver.find_element(By.ID(self.textbox_admincomment_id)).send_keys(adminComment)

    def clickSave(self):
        self.driver.find_element(By.XPATH(self.button_save_xpath)).click()



    
    






    
    
    
