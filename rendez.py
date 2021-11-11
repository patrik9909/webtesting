from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('The  haldorado page is opened')
def step_impl(context):
    global driver
    driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://www.haldorado.hu/')
    time.sleep(2)

@when('the "top termékek" is clicked')
def step_impl(context):
    driver.find_element_by_xpath("//span[.='Top termékek']").click()
    time.sleep(2)

@step('the "ár szerint növekvő" is choosen')
def step_impl(context):
    driver.find_element_by_xpath("//span[@class='select2-selection__placeholder']").click()

    time.sleep(2)
    driver.find_element_by_xpath("//li[.='Ár szerint növekvő']").click()

@then('the "Ár szerint növekvő" should be displayed')
def step_impl(context):
    elementar = driver.find_element_by_xpath("//span[.='Ár szerint növekvő']").is_displayed()

    assert elementar == True

