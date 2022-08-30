from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import names
import sys
import os
from os import path


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


def start():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)


def generate_random_number(n):
    make_rand_number = '0123456789'
    return ''.join(random.choices(make_rand_number, k=n))


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# jpg = resource_path('1.jpg')
# pdf = resource_path('2.pdf')
# png = resource_path('3.png')
# main_file = resource_path('4.zip')
jpg = path.abspath(path.join(path.dirname(__file__), '1.jpg'))
pdf = path.abspath(path.join(path.dirname(__file__), '../addPartner/2.pdf'))
png = path.abspath(path.join(path.dirname(__file__), '../addPartner/3.png'))
main_file = path.abspath(path.join(path.dirname(__file__), '../addPartner/4.zip'))

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


# Ask user for cycle
cycle = cycle_choice()
# Start webdriver
start()
store_number = '1'
admin_email = cycle[0]
admin_password = cycle[1]
branch_number = cycle[2]
admin_code = cycle[3]

LGL_email = 'automation_lgl@sef.am'
LGL_password = 'Password5'
email_of_store = 'partner_selenium.py@python.py'
url_of_store = 'https://www.selenium.dev/documentation/'
born_date_of_store = '01-01-1991'
social_card_issue_date = '01-01-2010'
passport_issue_date = '01-01-2022'
passport_exp_date = '01-01-2032'
PE_issue_day = '01-01-2000'
comment = 'Lorem ipsum dolor sit amet, Римский император Константин I Великий, Լոռեմ իպսում դոլոր սիթ ամետ'
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


def filtering_potential_partner():
    driver.get("http://ec2-63-34-222-67.eu-west-1.compute.amazonaws.com/login")
    driver.maximize_window()
    login_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    login_email.send_keys(LGL_email)
    login_password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
    login_password.send_keys(LGL_password)
    login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    login_button.click()

    partners_tab = driver.find_element(By.XPATH, "//a[.='Գործընկերներ']")
    partners_tab.click()
    potentialPartners_tab = driver.find_element(By.XPATH, "//div[.='Հավանական գործընկերներ']")
    potentialPartners_tab.click()
    lastPartner = driver.find_element(By.XPATH, f"(//tr[@class='ant-table-row ant-table-row-level-0'])[{store_number}]")
    lastPartner.click()

    filterPartner = driver.find_element(By.CSS_SELECTOR, '[value="FILTER"]')
    filterPartner.click()
    comment_ = driver.find_element(By.CSS_SELECTOR, '[name="decisionFeedback"]')
    comment_.send_keys(comment)
    uploadFile_1 = driver.find_element(By.XPATH, "(//input[contains(@type,'file')])[1]")
    uploadFile_1.send_keys(jpg)
    uploadFile_2 = driver.find_element(By.XPATH, "(//input[contains(@type,'file')])[2]")
    uploadFile_2.send_keys(pdf)
    uploadFile_3 = driver.find_element(By.XPATH, "(//input[contains(@type,'file')])[3]")
    uploadFile_3.send_keys(png)
    uploadFile_4 = driver.find_element(By.XPATH, "(//input[contains(@type,'file')])[4]")
    uploadFile_4.send_keys(jpg)
    save_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    save_button.click()


def add_chain():
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
    # lastPartner = driver.find_element(By.CSS_SELECTOR, f"[data-row-key='[{store_number}]'") #not working with {store_number}
    lastPartner = driver.find_element(By.XPATH, f"(//tr[@class='ant-table-row ant-table-row-level-0'])[{store_number}]")
    lastPartner.click()

    reg_btn = driver.find_element(By.XPATH, "//span[contains(text(),'Գրանցել')]")
    reg_btn.click()

    phoneNumber = driver.find_element(By.CSS_SELECTOR, '[name="phoneNumber"]')
    phoneNumber.send_keys(generate_random_number(8))
    contactNumber = driver.find_element(By.CSS_SELECTOR, '[name="contactNumber"]')
    contactNumber.send_keys(generate_random_number(8))
    contactEmail = driver.find_element(By.CSS_SELECTOR, '[name="contactEmail"]')
    contactEmail.send_keys(email_of_store)
    PE_radioBTN = driver.find_element(By.CSS_SELECTOR, '[value="PE"]')
    PE_radioBTN.click()
    pageLink = driver.find_element(By.CSS_SELECTOR, '[name="pageLink"]')
    pageLink.send_keys(url_of_store)
    brandName = driver.find_element(By.CSS_SELECTOR, '[name="brandName"]')
    brandName.send_keys('sel.' + names.get_last_name())
    nickname = driver.find_element(By.CSS_SELECTOR, '[name="nickname"]')
    nickname.send_keys('sel.' + names.get_last_name())
    emailAddr = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    emailAddr.send_keys(email_of_store)
    bankAccount = driver.find_element(By.CSS_SELECTOR, '[name="bankAccount"]')
    bankAccount.send_keys(generate_random_number(10))
    bankAccountUsd = driver.find_element(By.CSS_SELECTOR, '[name="bankAccountUsd"]')
    bankAccountUsd.send_keys(generate_random_number(10))
    adminCode = driver.find_element(By.XPATH, "(//input[@role='combobox'])[1]")
    adminCode.send_keys(admin_code, Keys.RETURN)
    bornDate = driver.find_element(By.XPATH, "(//input[@placeholder='Select date'])[1]")
    bornDate.send_keys(born_date_of_store, Keys.RETURN)
    residency = driver.find_element(By.XPATH, "(//input[contains(@role,'combobox')])[2]")
    residency.send_keys('Հայաստան', Keys.RETURN)
    nationality = driver.find_element(By.XPATH, "(//input[contains(@role,'combobox')])[3]")
    nationality.send_keys('ՀՀ', Keys.RETURN)
    gender = driver.find_element(By.CSS_SELECTOR, f'[value="{a()}"]')
    gender.click()
    childrenCount = driver.find_element(By.XPATH, "(//input[contains(@role,'combobox')])[4]")
    childrenCount.send_keys('1', Keys.RETURN)
    socialCard = driver.find_element(By.CSS_SELECTOR, '[name="socialCard"]')
    socialCard.send_keys(generate_random_number(10))
    socialCardIssueDate = driver.find_element(By.XPATH, "(//input[@placeholder='Select date'])[2]")
    socialCardIssueDate.send_keys(social_card_issue_date)
    passport = driver.find_element(By.XPATH, "(//input[contains(@role,'combobox')])[5]")
    passport.send_keys('ՀՀ նույնականացման քարտ', Keys.RETURN)
    passportID = driver.find_element(By.CSS_SELECTOR, '[name="passportId"]')
    passportID.send_keys('se' + generate_random_number(5))
    issuingAuthority = driver.find_element(By.CSS_SELECTOR, '[name="issuingAuthority"]')
    issuingAuthority.send_keys(generate_random_number(3))
    passportIssueDate = driver.find_element(By.XPATH, "(//input[@placeholder='Select date'])[3]")
    passportIssueDate.send_keys(passport_issue_date, Keys.RETURN)
    passportExpDate = driver.find_element(By.XPATH, "(//input[@placeholder='Select date'])[4]")
    passportExpDate.send_keys(passport_exp_date, Keys.RETURN)
    regNumber = driver.find_element(By.CSS_SELECTOR, '[name="stateRegistrationNumber"]')
    regNumber.send_keys('sel.' + generate_random_number(4))
    regNumberForPE = driver.find_element(By.CSS_SELECTOR, '[name="registrationNumberForPE"]')
    regNumberForPE.send_keys('sel.' + generate_random_number(4))
    PEIssueD = driver.find_element(By.XPATH, "(//input[@placeholder='Select date'])[5]")
    PEIssueD.send_keys(PE_issue_day, Keys.RETURN)
    productCheckbox = driver.find_element(By.XPATH, "(//input[@name='addressDTOS[0].productChecked'])[1]")
    productCheckbox.click()
    productSelect = driver.find_element(By.XPATH, "(//input[contains(@role,'combobox')])[8]")
    productSelect.send_keys('Ապրանք - Անշարժ գույք', Keys.RETURN)
    serviceCheckbox = driver.find_element(By.XPATH, "(//input[contains(@name,'addressDTOS[0].serviceChecked')])[1]")
    serviceCheckbox.click()
    serviceSelect = driver.find_element(By.XPATH, "(//input[contains(@role,'combobox')])[8]")
    serviceSelect.send_keys('Ծառայություն - Այլ', Keys.RETURN)
    sameCheckbox = driver.find_element(By.XPATH, "//span[contains(text(),'Նույնն է')]")
    sameCheckbox.click()
    attachZIP = driver.find_element(By.XPATH, "//input[@type='file']")
    attachZIP.send_keys(main_file)
    # saveBTN = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    # saveBTN.click()


def main():
    add_potential_partner()
    # filtering_potential_partner()
    # add_chain()


if __name__ == '__main__':
    main()
