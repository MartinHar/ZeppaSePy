import sys
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


make_arm_word = 'աբգդեզէ'


def generate_random_arm_word(make_arm_word, n):
    return ''.join(random.choices(make_arm_word, k=n))


make_eng_word = 'abcdefg'


def generate_random_eng_word(make_eng_word, n):
    return ''.join(random.choices(make_eng_word, k=n))


make_rand_number = '0123456789'


def generate_random_number(make_rand_number, n):
    return ''.join(random.choices(make_rand_number, k=n))


SUPM_email = 'supm@sef.am'
SUPM_password = 'Password2'
admin_role = 'ՄՃ'
branch_code = '92'
password = 'Password1'
fixed_passport_start_date = '01-01-2020'
fixed_passport_end_date = '01-01-2030'


def add_admin():
    start()
    driver.get("http://ec2-34-240-105-163.eu-west-1.compute.amazonaws.com/login")
    driver.maximize_window()
    login_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    login_email.send_keys(SUPM_email)
    login_password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
    login_password.send_keys(SUPM_password)
    login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    login_button.click()

    # settings_menu = driver.find_element(By.XPATH, "//span[contains(text(),'Կարգավորումներ')]")
    # settings_menu.click()
    settings_menu = driver.find_element(By.XPATH, "//span[contains(text(),'Կարգավորումներ')]")
    action = ActionChains(driver)
    action.move_to_element(settings_menu).perform()

    roles_menu = driver.find_element(By.XPATH, "//a[contains(text(),'Դերեր')]")
    roles_menu.click()

    add_admin_btn = driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary addNewAdmin']")
    add_admin_btn.click()
    admin = driver.find_element(By.XPATH, "(//input[@role='combobox'])[1]")
    admin.send_keys(admin_role, Keys.RETURN)
    branch = driver.find_element(By.XPATH, "(//input[@role='combobox'])[2]")
    branch.send_keys(branch_code, Keys.RETURN)
    # admin = driver.find_element(By.XPATH, "//form/div[1]/div[2]")
    # dropdown = Select(admin)
    # dropdown.select_by_visible_text('ՎՄ')
    admin_code = driver.find_element(By.CSS_SELECTOR, "[name='adminCode']")
    admin_code.send_keys("AUT"+generate_random_eng_word(make_eng_word, 4))
    asUserCode = driver.find_element(By.CSS_SELECTOR, "[name='asUserCode']")
    asUserCode.send_keys(generate_random_number(make_rand_number, 3))
    tabularNumber = driver.find_element(By.CSS_SELECTOR, "[name='tabularNumber']")
    tabularNumber.send_keys(generate_random_number(make_rand_number, 3))
    firstName = driver.find_element(By.CSS_SELECTOR, "[name='firstName']")
    firstName.send_keys(generate_random_arm_word(make_arm_word, 5))
    lastName = driver.find_element(By.CSS_SELECTOR, "[name='lastName']")
    lastName.send_keys(generate_random_arm_word(make_arm_word, 5))
    patronymic = driver.find_element(By.CSS_SELECTOR, "[name='patronymic']")
    patronymic.send_keys(generate_random_arm_word(make_arm_word, 5))
    admin_email = driver.find_element(By.CSS_SELECTOR, "[name='email']")
    admin_email.send_keys('aut_' + generate_random_eng_word(make_eng_word, 4))

    if admin_role == 'ՎՄ' or admin_role == 'ՄՃ' or admin_role == 'Վաճառք' or admin_role == 'ՄՌ' or admin_role == 'ԻԾ':
        try:
            driver.implicitly_wait(2)
            driver.find_element(By.CSS_SELECTOR, "[name='passportId']")
        except NoSuchElementException:
            print('WARNING!: Field is missing')
            driver.close()
            sys.exit()              #stops script , to not show selenium error messages in console!
        passportId = driver.find_element(By.CSS_SELECTOR, "[name='passportId']")
        passportId.send_keys(generate_random_eng_word(make_eng_word, 2) + generate_random_number(make_rand_number, 4))
        passport_start_date = driver.find_element(By.XPATH, "(//input[@placeholder='Select date'])[1]")
        passport_start_date.send_keys(fixed_passport_start_date)
        passport_end_date = driver.find_element(By.XPATH, "(//input[@placeholder='Select date'])[2]")
        passport_end_date.send_keys(fixed_passport_end_date)
        issuingAuthority = driver.find_element(By.CSS_SELECTOR, "[name='issuingAuthority']")
        issuingAuthority.send_keys(generate_random_number(make_rand_number, 3))
        city = driver.find_element(By.XPATH, "(//input[@role='combobox'])[3]")
        city.send_keys('Երևան', Keys.RETURN)
        time.sleep(1)
        region = driver.find_element(By.XPATH, "(//input[@role='combobox'])[4]")
        region.send_keys('Կենտրոն', Keys.RETURN)
        street = driver.find_element(By.CSS_SELECTOR, "[name='addressDTO.street']")
        street.send_keys('Աբովյան')
        houseNumber = driver.find_element(By.CSS_SELECTOR, "[name='addressDTO.houseNumber']")
        houseNumber.send_keys('7')
        apartmentNumber = driver.find_element(By.CSS_SELECTOR, "[name='addressDTO.apartmentNumber']")
        apartmentNumber.send_keys('111')
    admin_password = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    admin_password.send_keys(password)
    admin_repeatPassword = driver.find_element(By.CSS_SELECTOR, "[name='repeatPassword']")
    admin_repeatPassword.send_keys(password)
    # save_btb = driver.find_element(By.XPATH, "//button[@type='submit']")
    # save_btb.click()


def main():
    add_admin()


if __name__ == '__main__':
    add_admin()
