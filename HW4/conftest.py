import pytest
import yaml

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from send_to_email import sendemail
import requests

with open(r"C:\Users\omen1\PycharmProjects\pythonProject\HW4\testdata.yaml") as f:
    testdata = yaml.safe_load(f)


# scope="function"
@pytest.fixture(scope="session")
def browser():
    if testdata['browser'] == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    elif testdata['browser'] == 'chrome':
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def send_email():
    yield
    sendemail()


@pytest.fixture
def auth_token():
    with open(r'C:\Users\omen1\PycharmProjects\pythonProject\HW4\config.yaml') as f:
        testdata = yaml.safe_load(f)

    result = requests.post(url=testdata['url1'], data={"username": testdata['username'],
                                                       "password": testdata['password']})
    return result.json()["token"]
