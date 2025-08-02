import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_alert_button1(driver_fixture1):
    """this test checks for the presence of a button on the page"""
    assert driver_fixture1.find_element('xpath', '//a[@class="a-button"]').is_displayed()

def test_alert_button1_click(driver_fixture1):
    """this test checks the clickability of the button"""
    driver_fixture1.find_element('xpath', '//a[@class="a-button"]').click()
    try:
        WebDriverWait(driver_fixture1, 5).until(EC.alert_is_present())
        assert True
    except:
        assert False, 'Аллерт не появился после клика'

def test_alert_button1_click_ok(driver_fixture1):
    """this test clicks 'ok' on the alert"""
    driver_fixture1.find_element('xpath', '//a[@class="a-button"]').click()
    try:
        WebDriverWait(driver_fixture1, 5).until(EC.alert_is_present())
        alert = driver_fixture1.switch_to.alert
        alert.accept()
        assert True
    except:
        assert False, 'Некорректная работа алерта'

def test_alert_button2(driver_fixture2):
    """this test checks for the presence of a button on the page"""
    assert driver_fixture2.find_element('xpath', '//a[@class="a-button"]').is_displayed()

def test_alert_button2_click(driver_fixture2):
    """this test checks the clickability of the button"""
    driver_fixture2.find_element('xpath', '//a[@class="a-button"]').click()
    try:
        WebDriverWait(driver_fixture2, 5).until(EC.alert_is_present())
        assert True
    except:
        assert False, 'Аллерт не появился после клика'

def test_alert_button2_click_ok(driver_fixture2):
    """this test clicks 'ok' on the alert"""
    driver_fixture2.find_element('xpath', '//a[@class="a-button"]').click()
    WebDriverWait(driver_fixture2, 5).until(EC.alert_is_present())
    alert = driver_fixture2.switch_to.alert
    alert.accept()
    assert 'Ok' == driver_fixture2.find_element('id', 'result-text').text

def test_alert_button2_click_cancel(driver_fixture2):
    """this test clicks 'cancel' on the alert"""
    driver_fixture2.find_element('xpath', '//a[@class="a-button"]').click()
    WebDriverWait(driver_fixture2, 5).until(EC.alert_is_present())
    alert = driver_fixture2.switch_to.alert
    alert.dismiss()
    assert 'Cancel' == driver_fixture2.find_element('id', 'result-text').text


def test_alert_button3(driver_fixture3):
    """this test checks for the presence of a button on the page"""
    assert driver_fixture3.find_element('xpath', '//a[@class="a-button"]').is_displayed()

def test_alert_button3_click(driver_fixture3):
    """this test checks the clickability of the button"""
    driver_fixture3.find_element('xpath', '//a[@class="a-button"]').click()
    try:
        WebDriverWait(driver_fixture3, 5).until(EC.alert_is_present())
        assert True
    except:
        assert False, 'Аллерт не появился после клика'

def test_alert_button3_click_input(driver_fixture3):
    """this test clicks 'cancel' on the alert"""
    something_text = 'Делай, как надо. Как не надо, не делай. (c)Jason Statham'
    driver_fixture3.find_element('xpath', '//a[@class="a-button"]').click()
    alert = WebDriverWait(driver_fixture3, 5).until(EC.alert_is_present())
    alert.send_keys(something_text)
    alert.accept()
    assert something_text == driver_fixture3.find_element('id', 'result-text').text
