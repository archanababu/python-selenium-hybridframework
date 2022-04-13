from selenium import webdriver
import time

#drive = webdriver.Firefox(executable_path="C:\\Grid\\geckodriver.exe")
#drive = webdriver.Ie(executable_path="C:\\Grid\\geckodriver.exe")

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Workspace\WebDriver\chromedriver.exe")
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
