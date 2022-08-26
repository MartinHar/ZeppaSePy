import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
# from os import path


make_rand_number = '0123456789'


def generate_random_number(make_rand_number, n):
    return ''.join(random.choices(make_rand_number, k=n))


make_eng_word = 'abcdefg'


def generate_random_eng_word(make_eng_word, n):
    return ''.join(random.choices(make_eng_word, k=n))


make_arm_word = 'աբգդեզէ'


def generate_random_arm_word(make_arm_word, n):
    return ''.join(random.choices(make_arm_word, k=n))


def add_user_from_swagger():
    phone_number = generate_random_number(make_rand_number, 8)
    first_name = generate_random_eng_word(make_eng_word, 4)
    last_name = generate_random_eng_word(make_eng_word, 4)
    nickname = generate_random_eng_word(make_eng_word, 4)
    password = 'Password1'

    send_code_url = 'http://ec2-99-80-111-210.eu-west-1.compute.amazonaws.com/swagger/user/api/user/authentication/send-code?phone='
    send_sms = requests.get(send_code_url + phone_number)
    print(send_sms.content)

    submit_code_url = 'http://ec2-99-80-111-210.eu-west-1.compute.amazonaws.com/swagger/user/api/user/authentication/submit-code?phone='
    sms_code = input('Enter SMS code: ')

    submit_code = requests.get(submit_code_url + phone_number + '&code=' + sms_code)
    print(submit_code.content)

    reg_url = 'http://ec2-99-80-111-210.eu-west-1.compute.amazonaws.com/swagger/user/api/user/registration/'
    reg_details = {
        "phoneNumber": phone_number,
        "firstNameEng": first_name,
        "lastNameEng": last_name,
        "nickname": nickname,
        "password": password,
        "repeatPassword": password
    }

    reg_user = requests.post(reg_url, json=reg_details)
    print(reg_user.content)


def user_verification():
    born_date_of_user = '01-01-1999'
    social_card_issue_date = '01-01-2019'
    passport_issue_date = '01-12-2020'
    passport_exp_date = '01-01-2035'
    email_address = 'user_selenium.py@python.py'
    passportID = generate_random_eng_word(make_eng_word, 2) + generate_random_number(make_rand_number, 4)
    user_street_adr = generate_random_arm_word(make_arm_word, 3) + '1 / -'
    user_house_num = generate_random_arm_word(make_arm_word, 3) + '1/-'
    user_apt_num = generate_random_arm_word(make_arm_word, 3) + '1/-'
    # main_file = path.abspath(path.join(path.dirname(__file__), 'mainFile.zip'))           #need to be automated ...
    LO_email = 'loii@sef.am'
    LO_password = 'Password2'

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)

    driver.get("http://ec2-34-240-105-163.eu-west-1.compute.amazonaws.com/login")
    driver.maximize_window()

    login_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    login_email.send_keys(LO_email)
    login_password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
    login_password.send_keys(LO_password)
    login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    login_button.click()
    user = driver.find_element(By.XPATH, "(//tr[@class='ant-table-row ant-table-row-level-0 users-table-row'])[1]")
    user.click()
    time.sleep(1)
    verification_page = driver.find_element(By.XPATH, "//div[contains(text(),'Վավերացում')]")
    verification_page.click()
    time.sleep(1)
    born_date = driver.find_element(By.XPATH, "//div[@class='ant-picker']//input[@placeholder='Select date']")
    born_date.click()
    born_date.send_keys(born_date_of_user, Keys.RETURN)
    residency_city = driver.find_element(By.XPATH, "(//input[@role='combobox'])[1]")
    residency_city.send_keys('Հայաստան', Keys.RETURN)
    gender = driver.find_element(By.XPATH, "//span[contains(text(),'Արական')]")
    gender.click()
    nationality = driver.find_element(By.CSS_SELECTOR, "[aria-owns='rc_select_3_list']")
    nationality.send_keys('ՀՀ քաղաքացի', Keys.RETURN)
    admin_code = driver.find_element(By.CSS_SELECTOR, "[aria-owns='rc_select_4_list']")
    admin_code.send_keys('LOII', Keys.RETURN)
    children = driver.find_element(By.XPATH, "(//input[@role='combobox'])[6]")
    children.send_keys('1', Keys.RETURN)
    asCliCode = driver.find_element(By.XPATH, "//input[@name='asCliCode']")
    asCliCode.send_keys(generate_random_number(make_rand_number, 8))
    asAccountNumber = driver.find_element(By.XPATH, "//input[@name='asAccountNumber']")
    asAccountNumber.send_keys(generate_random_number(make_rand_number, 11))
    first_name = driver.find_element(By.CSS_SELECTOR, '[name="firstName"]')
    first_name.send_keys(generate_random_arm_word(make_arm_word, 4))
    last_name = driver.find_element(By.CSS_SELECTOR, '[name="lastName"]')
    last_name.send_keys(generate_random_arm_word(make_arm_word, 4))
    patronymic = driver.find_element(By.CSS_SELECTOR, '[name="patronymic"]')
    patronymic.send_keys(generate_random_arm_word(make_arm_word, 4))
    socialCard = driver.find_element(By.CSS_SELECTOR, '[name="socialCard"]')
    socialCard.send_keys(generate_random_number(make_rand_number, 10))
    socialCardDate = driver.find_element(By.XPATH, "(//input[@placeholder='Select date'])[4]")
    socialCardDate.send_keys(social_card_issue_date, Keys.RETURN)
    user_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    user_email.send_keys(email_address)
    user_passport = driver.find_element(By.CSS_SELECTOR, "[aria-owns='rc_select_2_list']")
    user_passport.send_keys('Անձնագիր', Keys.RETURN)
    user_passportID = driver.find_element(By.CSS_SELECTOR, '[name="passportId"]')
    user_passportID.send_keys(passportID)
    p_issuingAuthority = driver.find_element(By.CSS_SELECTOR, '[name="issuingAuthority"]')
    p_issuingAuthority.send_keys(generate_random_number(make_rand_number, 3))
    p_issue_date = driver.find_element(By.XPATH, "(//input[contains(@placeholder,'Select date')])[2]")
    p_issue_date.send_keys(passport_issue_date)
    p_exp_date = driver.find_element(By.XPATH, "(//input[contains(@placeholder,'Select date')])[3]")
    p_exp_date.send_keys(passport_exp_date)
    user_region = driver.find_element(By.XPATH, "(//input[@role='combobox'])[7]")
    user_region.send_keys('Երևան', Keys.RETURN)
    user_district = driver.find_element(By.XPATH, "//span[@title='Չընտրված']")
    user_district.click()
    user_district = driver.find_element(By.XPATH, "(//input[@role='combobox'])[8]")
    user_district.send_keys('Կենտրոն', Keys.RETURN)
    user_street = driver.find_element(By.CSS_SELECTOR, "[name='addressDTOS.REGISTRATION.street']")
    user_street.send_keys(user_street_adr)
    user_bld = driver.find_element(By.CSS_SELECTOR, "[name='addressDTOS.REGISTRATION.houseNumber']")
    user_bld.send_keys(user_house_num)
    user_apt = driver.find_element(By.CSS_SELECTOR, "[name='addressDTOS.REGISTRATION.apartmentNumber']")
    user_apt.send_keys(user_apt_num)
    same_checkbox = driver.find_element(By.XPATH, "//span[contains(text(),'Նույնն է')]")
    same_checkbox.click()
    upload_mainFile_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Ընտրել ֆայլ')]")
    upload_mainFile_btn.click()
    time.sleep(1)
    upload_mainFile_rd = driver.find_element(By.XPATH, "(//span[@class='ant-radio'])[2]")
    upload_mainFile_rd.click()
    time.sleep(1)
    next_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Հաջորդ')]")
    next_btn.click()
    time.sleep(2000)


def main():
    add_user_from_swagger()
    user_verification()


if __name__ == '__main__':
    main()
