import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def test_button1(driver_fixture_button1):
    """this test checks for the presence of a button on the page"""
    assert driver_fixture_button1.find_element('id', 'submit-id-submit').is_displayed()

def test_button1_click(driver_fixture_button1):
    """this test checks the clickability of the button"""
    driver_fixture_button1.find_element('id', 'submit-id-submit').click()
    assert 'Submitted' == driver_fixture_button1.find_element('id', 'result-text').text

def test_button2_exist(driver_fixture_button2):
    """this test checks the presence and visibility of an element that looks like a button but is implemented through a link"""
    assert driver_fixture_button2.find_element('link text', 'Click').is_displayed()

def test_button2_clicked(driver_fixture_button2):
    """this test checks the clickability of an element styled as a button"""
    driver_fixture_button2.find_element('link text', 'Click').click()
    assert 'Submitted' == driver_fixture_button2.find_element('id', 'result-text').text
