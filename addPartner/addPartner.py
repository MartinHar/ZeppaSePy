import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import names
from os import path


def cycle_choice():
    user_choice = input("Please choose admin cycle, for LO type 1 , for BR press 2: ")
    if user_choice == '1':
        admin_email_ = 'loii@sef.am'
        admin_password_ = 'Password3'
        # admin_email_ = 'supm@sef.am'
        # admin_password_ = 'Password2'
        branch_number_ = 'E11'
        admin_code_ = 'LOII'
        return admin_email_, admin_password_, branch_number_, admin_code_
    elif user_choice == '2':
        admin_email_ = 'testbr@sef.am'
        admin_password_ = 'Password3'
        branch_number_ = 'Y20'
        admin_code_ = 'LHK'
        return admin_email_, admin_password_, branch_number_, admin_code_
    else:
        print('Wrong input!')
        return cycle_choice()


def start():
    global driver
    # add options for not closing chrome automatically
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service = ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)


# def start():
#     global driver
#     driver = webdriver.Chrome('/Users/martinharutyunyan/Desktop/ZeppaAutomation/chromedriver')


def generate_random_number(n):
    make_rand_number = '0123456789'
    return ''.join(random.choices(make_rand_number, k=n))


jpg = path.abspath(path.join(path.dirname(__file__), '1.jpg'))
pdf = path.abspath(path.join(path.dirname(__file__), '2.pdf'))
png = path.abspath(path.join(path.dirname(__file__), '3.png'))
main_file = path.abspath(path.join(path.dirname(__file__), '4.zip'))

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

LGL_email = 'testlo@sef.am'
LGL_password = 'Password3'
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
arm_street_director = random.choice(arm_street_names)


def add_potential_partner():
    driver.get("http://ec2-34-240-105-163.eu-west-1.compute.amazonaws.com/login")
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
    addPotentialPartner_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Գրանցել գործընկերոջը')]")
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
    address_str.send_keys(f'{arm_street} {generate_random_number(1)}')
    address_house = driver.find_element(By.CSS_SELECTOR, '[name="addressDTOS.houseNumber"]')
    address_house.send_keys(generate_random_number(1))
    address_apartment = driver.find_element(By.CSS_SELECTOR, '[name="addressDTOS.apartmentNumber"]')
    address_apartment.send_keys(generate_random_number(2))
    save_btn = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    save_btn.click()
    time.sleep(5)


def filtering_potential_partner():
    driver.get("http://ec2-34-240-105-163.eu-west-1.compute.amazonaws.com/login")
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

    # upload files
    driver.find_element(By.XPATH, "//button[contains(text(),'Ընտրել ֆայլ')]").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//input[@value='COURT_PROCESS_EXISTENCE']").click()
    time.sleep(0.5)
    second_file_input = driver.find_element(By.XPATH, "//input[@type='file']")
    second_file_input.send_keys(png)
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@value='E_REGISTER']").click()
    first_file_input = driver.find_element(By.XPATH, "//input[@type='file']")
    first_file_input.send_keys(jpg)
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[@class='ant-modal-close-x']").click()
    time.sleep(1)
    save_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    save_button.click()
    time.sleep(2)


def add_chain():
    print(driver.title)
    print(driver.name)
    driver.get("http://ec2-34-240-105-163.eu-west-1.compute.amazonaws.com/login")
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

    reg_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Գրանցել')]")
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
    director_region = driver.find_element(By.XPATH, "(//span[contains(@class,'ant-select-selection-item')])[6]")
    director_region.click()
    director_region_shirak = driver.find_element(By.XPATH, "//div[contains(@title,'Շիրակ')]")
    director_region_shirak.click()
    director_c_v_c = driver.find_element(By.XPATH, "(//span[contains(@class,'ant-select-selection-item')])[7]")
    director_c_v_c.click()
    director_c_v_c_gyumri = driver.find_element(By.XPATH, "//div[contains(text(),'Գյումրի')]")
    director_c_v_c_gyumri.click()
    director_street = driver.find_element(By.CSS_SELECTOR, '[name="addressDTOS[0].street"]')
    director_street.send_keys(f'{arm_street_director} {generate_random_number(1)}')
    director_house = driver.find_element(By.CSS_SELECTOR, '[name="addressDTOS[0].houseNumber"]')
    director_house.send_keys(generate_random_number(2))
    director_apt = driver.find_element(By.CSS_SELECTOR, '[name="addressDTOS[0].apartmentNumber"]')
    director_apt.send_keys(generate_random_number(2))
    productCheckbox = driver.find_element(By.XPATH, "(//input[@name='addressDTOS[1].productChecked'])")
    productCheckbox.click()
    productSelect = driver.find_element(By.XPATH, "(//input[contains(@role,'combobox')])[10]")
    productSelect.send_keys('Ապրանք - Մթերք', Keys.RETURN)
    serviceCheckbox = driver.find_element(By.XPATH, "(//input[@name='addressDTOS[1].serviceChecked'])")
    serviceCheckbox.click()
    serviceSelect = driver.find_element(By.XPATH, "(//input[contains(@role,'combobox')])[10]")
    serviceSelect.send_keys('Այս գարուն', Keys.RETURN)
    sameCheckbox = driver.find_element(By.XPATH, "//input[@class='ant-checkbox-input']")
    sameCheckbox.click()
    driver.find_element(By.XPATH, "//input[@type='file']").send_keys(main_file)
    # time.sleep(40000)
    # saveBTN = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    # saveBTN.click()


def main():
    add_potential_partner()
    filtering_potential_partner()
    add_chain()


if __name__ == '__main__':
    main()
