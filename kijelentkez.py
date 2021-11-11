from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *

@given('the Haldorádó page is opened')
def step_impl(context):
    global driver
    driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://www.haldorado.hu/')
    time.sleep(2)
    driver.find_element_by_xpath('//a[contains(@href,"/bejelentkezes")]').click()
    time.sleep(2)


@when('the username is typed in the username input  field')
def step_impl(context):
    elem = WebDriverWait(driver, 120, 1).until(
        expect.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Azonosító']"))).send_keys('webshopteszt')
    time.sleep(2)


@step('the password is typed in the password input  field')
def step_impl(context):
    elem2 = WebDriverWait(driver, 120, 1).until(
        expect.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Jelszó']"))).send_keys('Asd12345')
    time.sleep(2)


@step('the "Bejelentkezés"  button is clicked')
def step_impl(context):
    driver.find_element_by_xpath('//button[text()="Belépés"]').click()

    time.sleep(4)
@step('the „ Szia,(felhasználónév) ” button is clicked')
def step_impl(context):
    driver.find_element_by_xpath("//span[.='Szia,']").click()
    time.sleep(2)


@step('And the „Kijelentkezés” button is clicked')
def step_impl(context):
    driver.find_element_by_xpath('//a[contains(@href,"/kijelentkezes")]').click()
    time.sleep(2)

@then('the „Bejelentkezés” button should be displayed')
def step_impl(context):
    elementbej = driver.find_element_by_xpath('//a[contains(@href,"/bejelentkezes")]').is_displayed()

    assert elementbej == True