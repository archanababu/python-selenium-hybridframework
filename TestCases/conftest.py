from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture()
def setup():
    # driver = webdriver.Chrome(executable_path="C:\Workspace\WebDriver\chromedriver.exe")
    # serv_obj = Service("C:\Workspace\WebDriver\chromedriver.exe")  
    # driver = webdriver.Chrome(serv_obj)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver 
