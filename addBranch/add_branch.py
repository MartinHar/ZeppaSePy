import sys

from faker import Faker
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
from selenium.common.exceptions import NoSuchElementException
import time


def start():
    global driver
    # add options for not closing chrome automatically
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service = ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)


fake = Faker()
# fake_eng_description = fake.bs()    // short version of description
fake_eng_description = fake.sentence(nb_words=20)
fake_eng_post_name = fake.catch_phrase()
fake_eng_word = fake.word()
fake_am = Faker('hy_AM')

SUPM_email = 'supm@sef.am'
SUPM_password = 'Password2'




def add_branch():
    start()
    driver.get("http://ec2-34-240-105-163.eu-west-1.compute.amazonaws.com/login")
    driver.maximize_window()
    login_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    login_email.send_keys(SUPM_email)
    login_password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
    login_password.send_keys(SUPM_password)
    login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    login_button.click()
    settings_menu = driver.find_element(By.XPATH, "//span[contains(text(),'Կարգավորումներ')]")
    settings_menu.click()
    branch_page = driver.find_element(By.XPATH, "(//a[contains(text(),'Մասնաճյուղերի տվյալներ')])")
    branch_page.click()
    add_new_branch_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Ավելացնել նոր մասնաճյուղ')]")
    add_new_branch_btn.click()
    branch_name = driver.find_element(By.CSS_SELECTOR, '[name="branchName"]')
    branch_name.send_keys(str(fake_am.administrative_unit()) + " " + str(fake_am.village()))
    branch_street = driver.find_element(By.CSS_SELECTOR, '[name="addressDTOS[0].street"]')
    branch_street.send_keys(fake_am.street())
    branch_house_number = driver.find_element(By.CSS_SELECTOR, '[name="addressDTOS[0].houseNumber"]')
    branch_house_number.send_keys(random.randrange(1,100))
    phone_number = driver.find_element(By.CSS_SELECTOR, '[name="phoneNumber"]')
    phone_number.send_keys(fake.localized_ean8())
    branch_name_eng = driver.find_element(By.CSS_SELECTOR, '[name="branchNameEng"]')
    branch_name_eng.send_keys(fake.administrative_unit())
    branch_street_eng = driver.find_element(By.CSS_SELECTOR, '[name="addressDTOS[0].streetEng"]')
    branch_street_eng.send_keys(fake.street_name())
    branch_house_number_eng = driver.find_element(By.CSS_SELECTOR, '[name="addressDTOS[0].houseNumberEng"]')
    branch_house_number_eng.send_keys(random.randrange(1,100))









def main():
    add_branch()


if __name__ == '__main__':
    add_branch()
