from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
from os import path
import sys


def start():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)


def generate_random_number(n):
    make_rand_number = '0123456789'
    return ''.join(random.choices(make_rand_number, k=n))


def cycle_choice():
    user_choice = input("Please choose admin cycle, for LO type 1 , for BR press 2: ")
    if user_choice == '1':
        admin_email_ = 'automation_lo24@sef.am'
        admin_password_ = 'Password5'
        branch_number_ = 'Y24'
        admin_code_ = 'autLO'
        return admin_email_, admin_password_, branch_number_, admin_code_
    elif user_choice == '2':
        admin_email_ = 'automation_br@sef.am'
        admin_password_ = 'Password5'
        branch_number_ = 'Y20'
        admin_code_ = 'autBR'
        return admin_email_, admin_password_, branch_number_, admin_code_
    else:
        print('Wrong input!')
        sys.exit()


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


def name_generator():
    choice = random.choice((arm_girl_name, arm_boy_name))
    if choice == arm_boy_name:
        name_gender_ = 'Boy'
    else:
        name_gender_ = 'Girl'
    # print(name_gender_)
    name_gender = random.choice(choice)
    return name_gender, name_gender_


def a():
    if gender__ == 'Boy':
        g = 'MALE'
    else:
        g = 'FEMALE'
    return g


cycle = cycle_choice()
# Start webdriver
start()
store_number = '1'
admin_email = cycle[0]
admin_password = cycle[1]
branch_number = cycle[2]
admin_code = cycle[3]

main_file = path.abspath(path.join(path.dirname(__file__), '4.zip'))
url = 'http://ec2-63-34-222-67.eu-west-1.compute.amazonaws.com/login'
LO_email = 'automation_lo24@sef.am'
LO_password = 'Password5'
email_of_store = 'partner_selenium.py@python.py'
url_of_store = 'https://www.selenium.dev/documentation/'
born_date_of_store = '01-01-1991'
social_card_issue_date = '01-01-2010'
passport_issue_date = '01-01-2022'
passport_exp_date = '01-01-2032'
PE_issue_day = '01-01-2000'
name_generator_ = name_generator()
firstName_gen = name_generator_[0]
gender__ = name_generator_[1]

patronymic_gen = random.choice(arm_boy_name)
lastName_gen = random.choice(arm_surnames)
arm_street = random.choice(arm_street_names)


def add_potential_partner():
    driver.get("http://ec2-63-34-222-67.eu-west-1.compute.amazonaws.com/login")
    driver.maximize_window()
    login_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    login_email.send_keys(admin_email)
    login_password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
    login_password.send_keys(admin_password)
    login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    login_button.click()

    partners_tab = driver.find_element(By.XPATH, "//a[.='Գործընկերներ']")
    partners_tab.click()
    potentialPartners_tab = driver.find_element(By.XPATH, "//div[.='Հավանական գործընկերներ']")
    potentialPartners_tab.click()
    addPotentialPartner_btn = driver.find_element(By.XPATH, "//span[.='Գրանցել գործընկերոջը']")
    addPotentialPartner_btn.click()

    legalName_fld = driver.find_element(By.CSS_SELECTOR, '[name="legalName"]')
    legalName_fld.send_keys(f"{firstName_gen} {lastName_gen} ԱՁ")
    taxCode_fld = driver.find_element(By.CSS_SELECTOR, '[name="taxCode"]')
    taxCode_fld.send_keys(generate_random_number(8))
    firstName_fld = driver.find_element(By.CSS_SELECTOR, '[name="firstName"]')
    firstName_fld.send_keys(firstName_gen)
    lastName_fld = driver.find_element(By.CSS_SELECTOR, '[name="lastName"]')
    lastName_fld.send_keys(lastName_gen)
    patronymic_fld = driver.find_element(By.CSS_SELECTOR, '[name="patronymic"]')
    patronymic_fld.send_keys(patronymic_gen)
    BR_number = driver.find_element(By.XPATH, "(//input[@role='combobox'])[1]")
    BR_number.send_keys(branch_number, Keys.RETURN)
    region = driver.find_element(By.XPATH, "(//span[@class='ant-select-selection-item'])[2]")
    region.click()
    region_yerevan = driver.find_element(By.XPATH, "(//div[contains(text(),'Երևան')])[1]")
    region_yerevan.click()
    c_v_c = driver.find_element(By.XPATH, "(//span[@class='ant-select-selection-item'])[3]")
    c_v_c.click()
    c_v_c_center = driver.find_element(By.XPATH, "(//div[contains(text(),'Կենտրոն')])[1]")
    c_v_c_center.click()
    address_str = driver.find_element(By.CSS_SELECTOR, '[name="addressDTOS.street"]')
    address_str.send_keys(arm_street)
    address_house = driver.find_element(By.CSS_SELECTOR, '[name="addressDTOS.houseNumber"]')
    address_house.send_keys(generate_random_number(1))
    address_apartment = driver.find_element(By.CSS_SELECTOR, '[name="addressDTOS.apartmentNumber"]')
    address_apartment.send_keys(generate_random_number(2))
    save_btn = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    save_btn.click()


def main():
    add_potential_partner()


if __name__ == '__main__':
    main()
