from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('The haldorado page is  opened')
def step_impl(context):
    global driver
    driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://www.haldorado.hu/')
    time.sleep(2)

@When ('the „okuma”  is typed in the search input field')
def step_impl(context):
    driver.find_element_by_xpath("//div[contains(@class, 'navbar-top__menu-item hldSearchLink')]").click()

    time.sleep(1)
    elem3 = WebDriverWait(driver, 120, 1).until(
        expect.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Keresés']"))).send_keys('OKUMA')
    time.sleep(2)
@step('the search button is clicked')
def step_impl(context):
    elem4 = WebDriverWait(driver, 120, 1).until(
        expect.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Keresés']"))).send_keys(Keys.RETURN)
    time.sleep(5)

@then('the results should be displayed')
def step_impl(context):
    pass
@step('the results should contain the „okuma” word')
def step_impl(context):
    driver.find_element_by_css_selector('[alt="OKUMA 8K FD pótdob"]').click()
    time.sleep(2)
    #assert elementokuma == True

