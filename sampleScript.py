from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Test sample change after username update in github

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
# driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
# driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.XPATH,"//button[contains(text(),'Log in')]").click()
time.sleep(5)
# driver.find_element(By.XPATH,"//a[@href='#'][@class = 'nav-link active']").click()

driver.find_element(By.XPATH,"//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']/li[4]//a[@href='#']/p").click()
driver.find_element(By.XPATH,"//a[@href='/Admin/Customer/List']").click()
driver.find_element(By.XPATH,"//a[@href='/Admin/Customer/Create']").click()


#drive = webdriver.Firefox(executable_path="C:\\Grid\\geckodriver.exe")
#drive = webdriver.Ie(executable_path="C:\\Grid\\geckodriver.exe")



""" driver = webdriver.Chrome(executable_path="C:\Workspace\WebDriver\chromedriver.exe")
#driver.maximize_window()
driver.implicitly_wait(30)
driver.set_page_load_timeout(50)
#driver.get("https://admin-demo.nopcommerce.com")
driver.get("https://qavbox.github.io/demo")
time.sleep(3)
assert "QAVBOX Demo" in driver.title
driver.find_element(By.LINK_TEXT,"SignUp Form").click()
driver.save_screenshot("C:\Workspace\Python\pySeleniumFramework\screenshot\png1.png")
time.sleep(3)
driver.quit()
 """





