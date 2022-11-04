import time
from os import path
import names
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import sys


arm_surnames = ['Հովհաննիսյան', 'Սարգսյան', 'Գրիգորյան', 'Հարությունյան', 'Գրիգորյան', 'Սարիբեկյան', 'Խաչատրյան',
                'Ադամյան', 'Խաչատուրյան', 'Հակոբյան', 'Պետրոսյան', 'Կարապետյան', 'Գևորգյան',
                'Խորխորունի', 'Մամիկոնյան', 'Ղարամանյան', 'Ծառուկյան', 'Մկրտչյան', 'Վարդանյան', 'Ղազարյան',
                'Գասպարյան', 'Մանուկյան', 'Մանուչարյան', 'Մակիչյան', 'Ավետիսյան', 'Պողոսյան', 'Սահակյան',
                'Պեպելյան', 'Սիմոնյան', 'Արիստակեսյան', 'Բագրատյան', 'Բզնունի', 'Յայլոյան', 'Բաղդասարյան']


arm_girl_name = ['Ագապի', 'Ազատուհի', 'Այծեմնիկ', 'Անի', 'Անթառամ', 'Աշխէն', 'Ասթինէ', 'Աստղիկ', 'Արեգնազան',
                 'Արշակուհի', 'Արտեմիս', 'Արփենիկ', 'Արփի', 'Բերկրուհի', 'Գոհար', 'Գոհարիկ', 'Դալար',
                 'Դեղձանիկ', 'Դշխուհի', 'Դիցուհի', 'Եսթեր', 'Երանիկ', 'Երանուհի', 'Թագուհի', 'Ժպտանոյշ',
                 'Իմաստուհի', 'Իշխանուհի', 'Իսկուհի', 'Լալա', 'Լիլիթ', 'Լուսաբեր', 'Լուսածին', 'Լուսարփի',
                 'Լուսնթագ', 'Խոսրովանոյշ', 'Խոսրովիդուխտ', 'Ծովինար', 'Կատարինէ', 'Մարալ', 'Մարգարիտ']


arm_boy_name = ['Աբգար', 'Աբէլ', 'Աբրահամ', 'Ադամ', 'Ազատ', 'Ալիշան', 'Ահարոն', 'Աղասի', 'Արծրուն', 'Արման',
                'Արմենակ', 'Արմեն', 'Արշակ', 'Բագրատ', 'Բեգլար', 'Բենիամին', 'Գագիկ', 'Գալուստ', 'Գառնիկ',
                'Գասպար', 'Գարեգին', 'Գեղամ', 'Գեղարդ', 'Խաժակ', 'Խաչատուր', 'Խաչիկ', 'Խոսրով', 'Կամսար',
                'Կայծակ', 'Կարապետ', 'Կարեն', 'Կարպիս', 'Մհեր', 'Մուշեղ', 'Նազարեթ', 'Նժդեհ', 'Շիրազ', 'Շիրակ',
                'Ոսկան', 'Ոսկեբերան', 'Ռազմիկ', 'Ռաֆֆի', 'Ռշտունի', 'Սերոբ', 'Սեւադա', 'Սեւակ', 'Սեւան', 'Սիմոն',
                'Սիսակ', 'Սիրակ', 'Սիրական', 'Սիփան', 'Համազասպ', 'Համբարձում', 'Համո', 'Հայկ', 'Հայկազ',
                'Հայկազուն', 'Ղազարոս', 'Ղուկաս', 'Մամիկոն', 'Մակար', 'Մարկոս', 'Մինաս', 'Մխիթար']


arm_street_names = ['Աբելյան', 'Աբովյան', 'Ագաթանգեղոսի', 'Ազատամարտիկների', 'Ազատության պողոտա', 'Աթենքի',
                    'Աթոյան', 'Ալեք Մանուկյան', 'Ալիխանյան', 'Աղայան', 'Աղյուսագործների', 'Ամիրյան', 'Այասի',
                    'Անտառային', 'Անրի Վեռնոյի', 'Գյուլբենկյան', 'Գոհար Գասպարյան', 'Գրիգոր Հարությունյան',
                    'Գրիգոր Տեր-Գրիգորյան', 'Դեղատան', 'Դերենիկ Դեմիրճյան', 'Եզնիկ Կողբացու', 'Եկմալյան',
                    'Երվանդ Քոչարի', 'Զավարյան', 'Զարոբյան', 'Զաքյան', 'Էրեբունու', 'Թաիրովի', 'Ռոստովյան',
                    'Ռուսթավելու', 'Սայաթ-Նովայի պողոտա', 'Սասունցի Դավթի', 'Սարալանջի', 'Սարմենի', 'Սարյան',
                    'Սերգեյ Փարաջանովի', 'Սևանի', 'Սիլվա Կապուտիկյան', 'Սիմեոն Երևանցու', 'Ծատուրյան',
                    'Ծխախոտագործների', 'Ծովակալ Իսակովի պողոտա', 'Կալենցի', 'Կասյան', 'Կարեն Դեմիրճյան',
                    'Կիևյան', 'Կոմիտասի պողոտա', 'Տիգրան Մեծի պողոտա', 'Տոլստոյի', 'Տպագրիչների', 'Ցախի',
                    'Փավստոս Բուզանդի', 'Քաջազնունու', 'Քոչինյան', 'Քրիստափորի', 'Օստրովսկու', 'Օրբելի եղբայրների',
                    'Ֆիզկուլտուրնիկների', 'Ֆիրդուս']


def name_generator():
    choice = random.choice((arm_girl_name, arm_boy_name))
    if choice == arm_boy_name:
        name_gender_ = 'Boy'
    else:
        name_gender_ = 'Girl'
    # print(name_gender_)
    name_gender = random.choice(choice)
    return name_gender, name_gender_


def generate_random_eng_word(n):
    make_eng_word = 'abcdefg'
    return ''.join(random.choices(make_eng_word, k=n))


def generate_random_number(n):
    make_rand_number = '0123456789'
    return ''.join(random.choices(make_rand_number, k=n))


def generate_random_arm_word(n):
    make_arm_word = 'աբգդեզէ'
    return ''.join(random.choices(make_arm_word, k=n))


def add_user_from_swagger():
    phone_number = generate_random_number(8)
    eng_first_name = names.get_first_name()
    eng_last_name = names.get_last_name()
    nickname = f'{eng_first_name}.{eng_last_name}'
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
        "firstNameEng": eng_first_name,
        "lastNameEng": eng_last_name,
        "nickname": nickname,
        "password": password,
        "repeatPassword": password
    }

    reg_user = requests.post(reg_url, json=reg_details)
    print(reg_user.content)
    if reg_user.status_code != 200:
        sys.exit()


def user_verification():

    born_date_of_user = '01-01-1999'
    social_card_issue_date = '01-01-2019'
    passport_issue_date = '01-12-2020'
    passport_exp_date = '01-01-2035'
    email_address = 'user_selenium.py@python.py'
    passportID = generate_random_eng_word(2) + generate_random_number(4)
    user_street_adr = random.choice(arm_street_names) + ' ./-'
    user_house_num = generate_random_arm_word(1) + '1/- ա'
    user_apt_num = generate_random_arm_word(1) + '1/- բն'
    name_generator_ = name_generator()
    firstName_gen = name_generator_[0]
    gender__ = name_generator_[1]
    LO_email = 'loii@sef.am'
    LO_password = 'Password3'
    main_file = path.abspath(path.join(path.dirname(__file__), '4.zip'))

    def a():
        if gender__ == 'Boy':
            g = 'MALE'
        else:
            g = 'FEMALE'
        return g

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
    nationality = driver.find_element(By.CSS_SELECTOR, "[aria-owns='rc_select_3_list']")
    nationality.send_keys('ՀՀ քաղաքացի', Keys.RETURN)
    admin_code = driver.find_element(By.CSS_SELECTOR, "[aria-owns='rc_select_4_list']")
    admin_code.send_keys('LOII', Keys.RETURN)
    children = driver.find_element(By.XPATH, "(//input[@role='combobox'])[6]")
    children.send_keys('1', Keys.RETURN)
    asCliCode = driver.find_element(By.XPATH, "//input[@name='asCliCode']")
    asCliCode.send_keys(generate_random_number(8))
    asAccountNumber = driver.find_element(By.XPATH, "//input[@name='asAccountNumber']")
    asAccountNumber.send_keys(generate_random_number(11))
    first_name = driver.find_element(By.CSS_SELECTOR, '[name="firstName"]')
    first_name.send_keys(firstName_gen)
    last_name = driver.find_element(By.CSS_SELECTOR, '[name="lastName"]')
    last_name.send_keys(random.choice(arm_surnames))
    patronymic = driver.find_element(By.CSS_SELECTOR, '[name="patronymic"]')
    patronymic.send_keys(random.choice(arm_boy_name))
    gender = driver.find_element(By.CSS_SELECTOR, f'[value="{a()}"]')
    gender.click()
    socialCard = driver.find_element(By.CSS_SELECTOR, '[name="socialCard"]')
    socialCard.send_keys(generate_random_number(10))
    socialCardDate = driver.find_element(By.XPATH, "(//input[@placeholder='Select date'])[4]")
    socialCardDate.send_keys(social_card_issue_date, Keys.RETURN)
    user_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    user_email.send_keys(email_address)
    user_passport = driver.find_element(By.CSS_SELECTOR, "[aria-owns='rc_select_2_list']")
    user_passport.send_keys('Անձնագիր', Keys.RETURN)
    user_passportID = driver.find_element(By.CSS_SELECTOR, '[name="passportId"]')
    user_passportID.send_keys(passportID)
    p_issuingAuthority = driver.find_element(By.CSS_SELECTOR, '[name="issuingAuthority"]')
    p_issuingAuthority.send_keys(generate_random_number(3))
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
    upload_mainFile_rd = driver.find_element(By.XPATH, "//input[@value='USER_MAIN_DOCUMENT']")
    upload_mainFile_rd.click()
    time.sleep(1)
    input_file = driver.find_element(By.XPATH, "//input[@type='file']")
    input_file.send_keys(main_file)
    time.sleep(2)
    close_popup = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
    close_popup.click()
    time.sleep(50)  # need to be improved , without this page is closing after close_pupup is executed


def main():
    add_user_from_swagger()
    user_verification()


if __name__ == '__main__':
    main()
