import pytest
from selenium import webdriver
@pytest.fixture(scope='function')
def driver_fixture_button1():
    """this fixture opens website"""
    driver = webdriver.Chrome()
    driver.get('https://www.qa-practice.com/elements/button/simple')
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def driver_fixture_button2():
    """this fixture opens website"""
    driver = webdriver.Chrome()
    driver.get('https://www.qa-practice.com/elements/button/like_a_button')
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def driver_fixture_button3():
    """this fixture opens website"""
    driver = webdriver.Chrome()
    driver.get('https://www.qa-practice.com/elements/button/disabled')
    yield driver
    driver.quit()