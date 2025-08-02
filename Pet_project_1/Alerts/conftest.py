import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver_fixture1():
    """this fixture opens website"""
    driver = webdriver.Chrome()
    driver.get('https://www.qa-practice.com/elements/alert/alert')
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def driver_fixture2():
    """this fixture opens website"""
    driver = webdriver.Chrome()
    driver.get('https://www.qa-practice.com/elements/alert/confirm')
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def driver_fixture3():
    """this fixture opens website"""
    driver = webdriver.Chrome()
    driver.get('https://www.qa-practice.com/elements/alert/prompt')
    yield driver
    driver.quit()
