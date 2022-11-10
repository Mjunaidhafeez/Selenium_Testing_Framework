import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
@pytest.fixture()
def setup(browser):

    if browser=='chrome':
        service_obj = Service('H:\\Selenium_Test_Project\Driver\chromedriver.exe')
        print('launching chrome browser')
        driver = webdriver.Chrome()
        driver = webdriver.Chrome(service=service_obj)
    elif browser=='firefox':
        print('launching chrome browser')
        driver = webdriver.Firefox()
        # service_obj = Service('H:\\Selenium_Test_Project\Driver\chromedriver.exe')
        # driver = webdriver.Chrome(service=service_obj)
    elif browser=='edge':
        print('launching chrome browser')
        driver = webdriver.Ie()
    else:
        service_obj = Service('H:\\Selenium_Test_Project\Driver\chromedriver.exe')
        print('launching chrome browser')
        driver = webdriver.Chrome()
        driver = webdriver.Chrome(service=service_obj)
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
###############################pyest html report###################
# IT IS A HOOOK FOR ADDING ENVIORNMENT INFO TO HTML REPORT
def pytest_html_report_title(report):
    report.title = "Ethizo Report"
def pytest_configure(config):
    config._metadata['Project Name'] ='Ethezo'
    config._metadata['Module Name'] ='patient'
    config._metadata['Tester']='Junaid Hafeez'
    # IT IS A HOOOK FOR DELELTE/MODIFY ENVIORNMENT INFO TO HTML REPORT
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)


