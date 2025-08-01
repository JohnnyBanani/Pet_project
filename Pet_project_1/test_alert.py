import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

def test_alert_button1():
    """this test checks for the presence of a button on the page"""
    driver.get('https://www.qa-practice.com/elements/alert/alert')
    assert driver.find_element('xpath', '//a[@class="a-button"]').is_displayed()

def test_alert_button1_click():
    """this test checks the clickability of the button"""
    driver.get('https://www.qa-practice.com/elements/alert/alert')
    driver.find_element('xpath', '//a[@class="a-button"]').click()
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        assert True
    except:
        assert False, 'Аллерт не появился после клика'

def test_alert_button1_click_ok():
    """this test clicks 'ok' on the alert"""
    driver.get('https://www.qa-practice.com/elements/alert/alert')
    driver.find_element('xpath', '//a[@class="a-button"]').click()
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        assert True
    except:
        assert False, 'Некорректная работа алерта'

def test_alert_button2():
    """this test checks for the presence of a button on the page"""
    driver.get('https://www.qa-practice.com/elements/alert/confirm')
    assert driver.find_element('xpath', '//a[@class="a-button"]').is_displayed()

def test_alert_button2_click():
    """this test checks the clickability of the button"""
    driver.get('https://www.qa-practice.com/elements/alert/confirm')
    driver.find_element('xpath', '//a[@class="a-button"]').click()
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        assert True
    except:
        assert False, 'Аллерт не появился после клика'

def test_alert_button2_click_ok():
    """this test clicks 'ok' on the alert"""
    driver.get('https://www.qa-practice.com/elements/alert/confirm')
    driver.find_element('xpath', '//a[@class="a-button"]').click()
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    assert 'Ok' == driver.find_element('id', 'result-text').text

def test_alert_button2_click_cancel():
    """this test clicks 'cancel' on the alert"""
    driver.get('https://www.qa-practice.com/elements/alert/confirm')
    driver.find_element('xpath', '//a[@class="a-button"]').click()
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.dismiss()
    assert 'Cancel' == driver.find_element('id', 'result-text').text


def test_alert_button3():
    """this test checks for the presence of a button on the page"""
    driver.get('https://www.qa-practice.com/elements/alert/prompt')
    assert driver.find_element('xpath', '//a[@class="a-button"]').is_displayed()

def test_alert_button3_click():
    """this test checks the clickability of the button"""
    driver.get('https://www.qa-practice.com/elements/alert/prompt')
    driver.find_element('xpath', '//a[@class="a-button"]').click()
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        assert True
    except:
        assert False, 'Аллерт не появился после клика'

def test_alert_button3_click_input():
    """this test clicks 'cancel' on the alert"""
    something_text = 'Делай, как надо. Как не надо, не делай. (c)Jason Statham'
    driver.get('https://www.qa-practice.com/elements/alert/prompt')
    driver.find_element('xpath', '//a[@class="a-button"]').click()
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert.send_keys(something_text)
    alert.accept()
    assert something_text == driver.find_element('id', 'result-text').text

