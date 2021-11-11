from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('The Haldorado homepage is opened')
def step_impl(context):
    global driver
    driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://www.haldorado.hu/')
    time.sleep(2)
    driver.find_element_by_xpath('//a[contains(@href,"/bejelentkezes")]').click()
    time.sleep(2)


@when('the username is typed in the username field')
def step_impl(context):
    elem = WebDriverWait(driver, 120, 1).until(
        expect.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Azonosító']"))).send_keys('webshopteszt')
    time.sleep(2)


@step('the password is typed in the password field')
def step_impl(context):
    elem2 = WebDriverWait(driver, 120, 1).until(
        expect.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Jelszó']"))).send_keys('rosszjelszo')
    time.sleep(2)


@step('the "Bejelentkezés" button is  clicked')
def step_impl(context):
    driver.find_element_by_xpath('//button[text()="Belépés"]').click()

    time.sleep(4)

@then('the error message should be displayed')
def step_impl(context):
    hibauzenet = 'Sikertelen bejelentkezés, ellenőrizd a megadott adatokat!'
    hibauzenet_element = driver.find_element_by_class_name('alert-danger').text
    print(hibauzenet_element)
    assert hibauzenet == hibauzenet_element
