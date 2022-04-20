import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class AddCustomer:
    #Add Customer Page object elements

    linkCustomers_menu_xpath = "//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']/li[4]//a[@href='#']/p"
    linkCustomers_menuItems_xpath = "//a[@href='/Admin/Customer/List']"
    button_addNew_xpath = "//a[@href='/Admin/Customer/Create']"
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    textbox_firtname_id = "FirstName"
    textbox_lastname_id = "LastName"
    radiobutton_male_xpath = "//label[contains(text(),'Male')]"
    radiobutton_female_xpath = "//label[contains(text(),'Female')]"
    textbox_dob_id = "DateOfBirth"
    textbox_company_id = "Company"
    checkbox_taxexempt_id = "IsTaxExempt"
    text_NewsletterStores_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']//input[@class='k-input k-readonly']"
    list_newsletter_1_xpath = "//li[contains(text(),'Your store name')]"
    list_newsletter_2_xpath = "//li[contains(text(),'Test store 2')]"
    dropdown_vendor_id = "VendorId"
    dropdown_notvendor_xpath = "//option[contains(text(),'Not a vendor')]"
    dropdown_vendor_1_xpath = "//option[contains(text(),'Vendor 1')]"
    dropdown_vendor_2_xpath = "//option[contains(text(),'Vendor 2')]"
    text_customer_role_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']//input[@class='k-input k-readonly'][@aria-describedby='SelectedCustomerRoleIds_taglist']"
    list_administrator_xpath = "//ul[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(),'Administrators')]"
    list_forum_moderators_xpath = "//ul[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(),'Forum Moderators')]"
    list_guest_xpath = "//ul[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(),'Guests')]"
    list_registered_xpath = "//ul[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(),'Registered')]"
    list_vendor_xpath = "//ul[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(),'Vendors')]"
    checkbox_active_id = "Active"
    textbox_admincomment_id = "AdminComment"
    button_save_xpath = "//button[@name='save']"
    role = ""

    def __init__(self,driver):
        # driver = webdriver.Chrome(executable_path="C:\Workspace\WebDriver\chromedriver.exe")
        self.driver = driver 

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.linkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH,self.linkCustomers_menuItems_xpath).click()

    def clickOnAddNewButton(self):
        self.driver.find_element(By.XPATH,self.button_addNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.ID,self.textbox_email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def setFirstname(self, firstname):
        self.driver.find_element(By.ID,self.textbox_firtname_id).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element(By.ID,self.textbox_lastname_id).send_keys(lastname)

    def clickOnGender(self, gender):
        if gender == "male":
            self.driver.find_element(By.XPATH,self.radiobutton_male_xpath).click()
        elif gender == "female":
            self.driver.find_element(By.XPATH,self.radiobutton_female_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.radiobutton_female_xpath).click()

    def setDOB(self, dob):
        self.driver.find_element(By.ID,self.textbox_dob_id).send_keys(dob)

    def setCompany(self, company):
        self.driver.find_element(By.ID,self.textbox_company_id).send_keys(company)

    def clickOnTaxExcempt(self):
        self.driver.find_element(By.ID,self.checkbox_taxexempt_id).click()

    def clickOnNewsletter(self, newsLetter):
        self.driver.find_element(By.XPATH,self.text_NewsletterStores_xpath).click()
        time.sleep(3)
        # select = self.driver.find_element(By.ID,self.select_NewsletterStores_id)
        # dataset_drop_down_element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.ID, self.select_NewsletterStores_id)))
        # dataset_drop_down_element = Select(dataset_drop_down_element)
        # actionChains = ActionChains(self.driver)
        # actionChains.move_to_element(dataset_drop_down_element).perform()
        # select = Select(dataset_drop_down_element)
        
        if newsLetter == "Your store name":
            # self.driver.find_element(By.XPATH,self.list_Newslettertaglist_xpath).send_keys(newsLetter).submit()
            # self.driver.find_element(By.ID,"6d06edf4-9b63-464a-b333-c263980280a2").click()
            self.driver.find_element(By.XPATH,self.list_newsletter_1_xpath).click()
        elif newsLetter == "Test store 2":
            # select = Select(self.driver.find_element(By.XPATH,self.list_Newslettertaglist_xpath).send_keys(newsLetter))            
            # select.select_by_visible_text(newsLetter)
            # dataset_drop_down_element.select_by_visible_text(newsLetter)
            self.driver.find_element(By.XPATH,self.list_newsletter_2_xpath).click()
        else:
            select = Select(self.driver.find_element(By.XPATH,self.list_Newslettertaglist_xpath).send_keys("Test store 2"))            
            select.select_by_visible_text(newsLetter)
            # dataset_drop_down_element.select_by_visible_text("Test store 2")
            # self.driver.find_element(By.XPATH,self.list_newsletter_2_xpath).click()
        
    def clickOnCustomerRoles(self, role):
        self.role = role
        #remove default registered option        
        self.driver.find_element(By.XPATH,"//ul[@id = 'SelectedCustomerRoleIds_taglist']/li/span[2]").click()
        self.driver.find_element(By.XPATH,self.text_customer_role_xpath).click()
        time.sleep(3)

        if role == "Administrators":
            self.driver.find_element(By.XPATH,self.list_administrator_xpath).click()
        elif role == "Forum Moderators":
            self.driver.find_element(By.XPATH,self.list_forum_moderators_xpath).click()
        elif role == "Guests":
            self.driver.find_element(By.XPATH,self.list_guest_xpath).click()
        elif role == "Registered":
            self.driver.find_element(By.XPATH,self.list_registered_xpath).click()
        elif role == "Vendors":
            self.driver.find_element(By.XPATH,self.list_vendor_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.list_guest_xpath).click()

    def clickOnVendorManager(self, vendor):
        self.driver.find_element(By.ID,self.dropdown_vendor_id).click()
        time.sleep(3)
        if vendor == "Not a vendor" and self.role != " Vendors":
            self.driver.find_element(By.XPATH,self.dropdown_notvendor_xpath).click()
        elif vendor == "Not a vendor" and self.role == " Vendors":
            self.driver.find_element(By.XPATH,self.dropdown_vendor_1_xpath).click()
        elif vendor == "Vendor 1":
            self.driver.find_element(By.XPATH,self.dropdown_vendor_1_xpath).click()
        elif vendor == "Vendor 2":
            self.driver.find_element(By.XPATH,self.dropdown_vendor_2_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.dropdown_notvendor_xpath).click()

    def clickOnActive(self):
        self.driver.find_element(By.ID,self.checkbox_active_id).click()

    def setAdminComment(self, adminComment):
        self.driver.find_element(By.ID,self.textbox_admincomment_id).send_keys(adminComment)

    def clickSave(self):
        self.driver.find_element(By.XPATH,self.button_save_xpath).click()



    
    






    
    
    
