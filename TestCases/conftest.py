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

#Pytest HTML Report

# Edit report title by using the pytest_html_report_title hook:
def pytest_html_report_title(report):    
    report.title = "Nop commerce validation"

# To access the metadata from a plugin, you can use the _metadata attribute of the config object. This can be used to read/add/modify the metadata:
def pytest_configure(config):
    config._metadata['Project Name'] = 'nopcommerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'arcbabu'
    

# To add/modify/delete metadata at the end of metadata collection, you can use the pytest_metadata hook:
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


