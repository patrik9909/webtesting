from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver= webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
driver.get('https://www.haldorado.hu/')
time.sleep(2)

driver.find_element_by_xpath('//a[contains(@href,"/bejelentkezes")]').click()

time.sleep(2)
elem = WebDriverWait(driver, 120, 1).until(
        expect.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Azonosító']"))).send_keys('webshopteszt')
time.sleep(2)

elem2 = WebDriverWait(driver, 120, 1).until(
        expect.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Jelszó']"))).send_keys('Asd12345')
time.sleep(2)

#https://stackoverflow.com/questions/46213397/why-cant-i-find-an-input-element-with-a-placeholder-in-selenium
#driver.find_element_by_id('recaptcha-anchor-label').click()
#time.sleep(3)
driver.find_element_by_xpath('//button[text()="Belépés"]').click()

time.sleep(4)



# https://stackoverflow.com/questions/30874690/python-selenium-selecting-div-class/30874856

driver.find_element_by_xpath("//div[contains(@class, 'navbar-top__menu-item hldSearchLink')]").click()

# https://stackoverflow.com/questions/30874690/python-selenium-selecting-div-class/30874856

time.sleep(1)

elem3 = WebDriverWait(driver, 120, 1).until(
        expect.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Keresés']"))).send_keys('OKUMA')
time.sleep(2)
elem4 = WebDriverWait(driver, 120, 1).until(
        expect.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Keresés']"))).send_keys(Keys.RETURN)

time.sleep(3)
driver.find_element_by_css_selector('[alt="OKUMA 8K FD pótdob"]').click()

time.sleep(2)
button= driver.find_element_by_xpath("//button[@type='button' and @class='btn btn-primary btn-add-to-cart addToCart']")
driver.execute_script("arguments[0].click();", button)
#https://pretagteam.com/question/seleniumcommonexceptionselementclickinterceptedexception-message-element-click-intercepted-element-is-not-clickable-with-selenium-and-python

time.sleep(2)

button2= driver.find_element_by_xpath('//a[contains(@href,"/kosar")]')
driver.execute_script("arguments[0].click();", button2)



