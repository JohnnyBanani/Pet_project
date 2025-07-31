import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def test_button1_exist():
    """this test checks for the presence of a button on the page"""
    driver.get('http://www.qa-practice.com/elements/button/simple')
    assert driver.find_element('id', 'submit-id-submit').is_displayed()

def test_button1_clicked():
    """this test checks the clickability of the button and its correct operation on the page"""
    driver.get('http://www.qa-practice.com/elements/button/simple')
    driver.find_element('id', 'submit-id-submit').click()
    assert 'Submitted' == driver.find_element('id', 'result-text').text

def test_button2_exist():
    """this test checks the presence and visibility of an element that looks like a button but is implemented through a link"""
    driver.get('https://www.qa-practice.com/elements/button/like_a_button')
    assert driver.find_element('link text', 'Click').is_displayed()

def test_button2_clicked():
    """this test checks the clickability of an element styled as a button"""
    driver.get('https://www.qa-practice.com/elements/button/like_a_button')
    driver.find_element('link text', 'Click').click()
    assert 'Submitted' == driver.find_element('id', 'result-text').text
