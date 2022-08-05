import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.implicitly_wait(10)


def generate_random_arm_word(make_arm_word, n):
    return ''.join(random.choices(make_arm_word, k=n))


make_eng_word = 'abcdefg'


def generate_random_eng_word(make_eng_word, n):
    return ''.join(random.choices(make_eng_word, k=n))


make_rand_number = '0123456789'


def generate_random_number(make_rand_number, n):
    return ''.join(random.choices(make_rand_number, k=n))


def as_codes():
    driver.implicitly_wait(2)
    try:
        driver.find_element(By.CSS_SELECTOR, '[name="asCliCode"]') and \
        driver.find_element(By.CSS_SELECTOR, '[name="asAccountNumber"]')
        print('ՀԾ հաճախորդի կոդ and ՀԾ հաշվի համար fields are present')
    except NoSuchElementException:
        print('WARNING!: ՀԾ հաճախորդի կոդ and ՀԾ հաշվի համար fields are missing')


PC_email = 'pcpc@sef.am'
PC_password = 'Password1'
SUPM_email = 'supm@sef.am'
SUPM_password = 'Password3'
store_number_link = '5'
store_number = '4'

driver.get("http://ec2-34-240-105-163.eu-west-1.compute.amazonaws.com/login")
login_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
# login_email.send_keys(PC_email)
login_email.send_keys(SUPM_email)
login_password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
# login_password.send_keys(PC_password)
login_password.send_keys(SUPM_password)
login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
login_button.click()

partners_tab = driver.find_element(By.XPATH, "//a[.='Գործընկերներ']")
partners_tab.click()
Partner = driver.find_element(
    By.XPATH, f"(//tr[@class='ant-table-row ant-table-row-level-0 users-table-row'])[{store_number_link}]")
Partner.click()

# print(Partner.split()[2])
# if we get_attribute from variable , it will not work correctly.

# Phone number          (must not be linked if there is a store with this phone number)
phoneNumber_link = driver.find_element(
    By.XPATH, "//label[contains(text(),'Հեռախոսահամար')]/..//input[@type='number']").get_attribute("value")
print(phoneNumber_link)
# BRAND NAME
brandName_link = driver.find_element(By.XPATH, "//input[@name='brandName']").get_attribute("value")
print(brandName_link)
# TAX CODE
taxCode_link = driver.find_element(By.XPATH, "//input[@name='taxCode']").get_attribute("value")
print(taxCode_link)
# AMD ACCOUNT NUMB.
bankAccountAMD_link = driver.find_element(By.XPATH, "//input[@name='bankAccount']").get_attribute("value")
print(bankAccountAMD_link)
# USD ACCOUNT NUMB.
bankAccountUSD_link = driver.find_element(By.XPATH, "//input[@name='bankAccountUsd']").get_attribute("value")
print(bankAccountUSD_link)
# SOCIAL CARD NUMB.
socialCard_link = driver.find_element(By.XPATH, "//input[@name='socialCard']").get_attribute("value")
print(socialCard_link)
# PASSPORT ID
passportId_link = driver.find_element(By.XPATH, "//input[@name='passportId']").get_attribute("value")
print(passportId_link)

partners_tab = driver.find_element(By.XPATH, "//a[.='Գործընկերներ']")
partners_tab.click()
Partner = driver.find_element(
    By.XPATH, f"(//tr[@class='ant-table-row ant-table-row-level-0 users-table-row'])[{store_number}]")
Partner.click()
