import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        # driver = webdriver.Chrome()
        print("launching chrome browser........")
        driver = webdriver.Chrome(executable_path="C:/Nitin/Drivers/chromedriver_win32/chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching firefox browser........")
    else:
        driver = webdriver.Ie
    return driver


def pytest_addoption(parser):  # this will get value from CLI/hook
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return browser value to setup method
    return request.config.getoption("--browser")


###### PyTest HTML Report #####

# It is hook for adding Environment info to HTMl Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'

# It is hook to delete/Modify Environment info to HTMl Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_Home", None)
    metadata.pop("Plugins", None)

