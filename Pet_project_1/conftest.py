import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver_fixture1():
    """this fixture opens website"""
    driver = webdriver.Chrome()
    driver.get('https://www.qa-practice.com/elements/alert/alert')
    yield driver
    driver.quit()

