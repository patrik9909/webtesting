from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('The Haldorado  homepage is opened')
def step_impl(context):
    global driver
    driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://www.haldorado.hu/')
    time.sleep(2)
    driver.find_element_by_xpath('//a[contains(@href,"/bejelentkezes")]').click()
    time.sleep(2)


@when('the username  is typed in the username field')
def step_impl(context):
    elem = WebDriverWait(driver, 120, 1).until(
        expect.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Azonosító']"))).send_keys('webshopteszt')
    time.sleep(2)


@step('the password  is typed in the password field')
def step_impl(context):
    elem2 = WebDriverWait(driver, 120, 1).until(
        expect.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Jelszó']"))).send_keys('Asd12345')
    time.sleep(2)


@step('the "Bejelentkezés"  button is  clicked')
def step_impl(context):
    driver.find_element_by_xpath('//button[text()="Belépés"]').click()

    time.sleep(4)

@step('the „okuma” is typed in the search input field')
def step_impl(context):
    driver.find_element_by_xpath("//div[contains(@class, 'navbar-top__menu-item hldSearchLink')]").click()

    time.sleep(1)
    elem3 = WebDriverWait(driver, 120, 1).until(
        expect.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Keresés']"))).send_keys('OKUMA')
    time.sleep(2)
    elem4 = WebDriverWait(driver, 120, 1).until(
        expect.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Keresés']"))).send_keys(Keys.RETURN)
    time.sleep(5)


@step('the first result is clicked')
def step_impl(context):
    driver.find_element_by_css_selector('[alt="OKUMA 8K FD pótdob"]').click()

    time.sleep(2)

@step('the "kosárba" button is clicked')
def step_impl(context):
    button = driver.find_element_by_xpath(
        "//button[@type='button' and @class='btn btn-primary btn-add-to-cart addToCart']")
    driver.execute_script("arguments[0].click();", button)

    time.sleep(2)
    button2 = driver.find_element_by_xpath('//a[contains(@href,"/kosar")]')
    driver.execute_script("arguments[0].click();", button2)
    time.sleep(2)


@then('the item should be displayed in the basket')
def step_impl(context):
    elementg = driver.find_element_by_xpath("//span[.='140 g']").is_displayed()

    assert elementg == True