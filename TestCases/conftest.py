from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

import pytest

@pytest.fixture()
def setup(browser):
    # driver = webdriver.Chrome(executable_path="C:\Workspace\WebDriver\chromedriver.exe")
    # serv_obj = Service("C:\Workspace\WebDriver\chromedriver.exe")  
    # driver = webdriver.Chrome(serv_obj)
    
    if browser ==  'chrome' or browser == 'Chrome' or browser == 'CHROME':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser ==  'firefox' or browser == 'Firefox' or browser == 'FIREFOX':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    else:
        # driver = webdriver.Ie(IEDriverManager().install()) #IE is pretty slow, hence defaulting to Chrome
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser") 
