from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('The haldorado page  is  opened')
def step_impl(context):
    global driver
    driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
    driver.maximize_window()
    driver.get('https://www.haldorado.hu/')
    time.sleep(2)

@when('the "termékek" is opened')
def step_impl(context):
    driver.find_element_by_xpath('//a[contains(@href,"/termekek")]').click()
    time.sleep(3)

@step('the "gyártóra szűrés" button is clicked')
def step_impl(context):
    driver.find_element_by_xpath("//span[.='Gyártóra szűrés']").click()

    time.sleep(2)

@step('the "haldorádó" manufacturer is choosen')
def step_impl(context):
    driver.find_element_by_xpath("//span[.='973']").click()

    time.sleep(2)

    driver.find_element_by_xpath("//button[@type='submit' and @class='btn btn-primary btn-block']").click()

    time.sleep(2)


@then("the results  should be displayed")
def step_impl(context):
    elemhaldorado = driver.find_element_by_id('itemElement35069').is_displayed()
    assert elemhaldorado == True

