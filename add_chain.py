from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import random

driverLocation = Service(executable_path="/Users/martinharutyunyan/Desktop/PythonAutomationZeppa/chromedriver")
driver = webdriver.Chrome(service=driverLocation)
driver.get("http://ec2-34-240-105-163.eu-west-1.compute.amazonaws.com/login")
driver.implicitly_wait(10)


email_of_store = 'selenium@python.py'
url_of_store = 'https://www.selenium.dev/documentation/'
born_date_of_store = '01-01-1991'
social_card_issue_date = '01-01-2010'
passport_issue_date = '01-01-2022'
passport_exp_date = '01-01-2032'
PE_issue_day = '01-01-2000'



make_arm_word = 'աբգդեզէ'


def generate_random_arm_word(make_arm_word, n):
    return ''.join(random.choices(make_arm_word, k=n))


make_rand_number = '0123456789'


def generate_random_number(make_rand_number, n):
    return ''.join(random.choices(make_rand_number, k=n))


make_eng_word = 'abcdefg'


def generate_random_eng_word(make_eng_word, n):
    return ''.join(random.choices(make_eng_word, k=n))


LGL_email = 'testlo@sef.am'
LGL_password = 'Password2'

LO_email = 'loii@sef.am'
LO_password = 'Password1'


class add_chain:
    driver.get("http://ec2-34-240-105-163.eu-west-1.compute.amazonaws.com/login")
    login_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    login_email.send_keys(LO_email)
    login_password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
    login_password.send_keys(LO_password)
    login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    login_button.click()

    partners_tab = driver.find_element(By.XPATH, "//a[.='Գործընկերներ']")
    partners_tab.click()
    potentialPartners_tab = driver.find_element(By.XPATH, "//div[.='Հավանական գործընկերներ']")
    potentialPartners_tab.click()
    lastPartner = driver.find_element(By.CSS_SELECTOR, '[data-row-key="1"]')
    lastPartner.click()

    reg_btn = driver.find_element(By.XPATH, "//span[contains(text(),'Գրանցել')]")
    reg_btn.click()

    phoneNumber = driver.find_element(By.CSS_SELECTOR, '[name="phoneNumber"]')
    phoneNumber.send_keys(generate_random_number(make_rand_number, 8))
    contactNumber = driver.find_element(By.CSS_SELECTOR, '[name="contactNumber"]')
    contactNumber.send_keys(generate_random_number(make_rand_number, 8))
    contactEmail = driver.find_element(By.CSS_SELECTOR, '[name="contactEmail"]')
    contactEmail.send_keys(email_of_store)
    PE_radioBTN = driver.find_element(By.CSS_SELECTOR, '[value="PE"]')
    PE_radioBTN.click()
    pageLink = driver.find_element(By.CSS_SELECTOR, '[name="pageLink"]')
    pageLink.send_keys(url_of_store)
    brandName = driver.find_element(By.CSS_SELECTOR, '[name="brandName"]')
    brandName.send_keys('se.' + generate_random_eng_word(make_eng_word, 5))
    nickname = driver.find_element(By.CSS_SELECTOR, '[name="nickname"]')
    nickname.send_keys('se.' + generate_random_eng_word(make_eng_word, 5))
    emailAddr = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    emailAddr.send_keys(email_of_store)
    bankAccount = driver.find_element(By.CSS_SELECTOR, '[name="bankAccount"]')
    bankAccount.send_keys(generate_random_number(make_rand_number, 10))
    bankAccountUsd = driver.find_element(By.CSS_SELECTOR, '[name="bankAccountUsd"]')
    bankAccountUsd.send_keys(generate_random_number(make_rand_number, 10))
    adminCode = driver.find_element(By.XPATH, "(//input[@role='combobox'])[1]")
    adminCode.send_keys('LOII', Keys.RETURN)
    bornDate = driver.find_element(By.XPATH, "(//input[@placeholder='Select date'])[1]")
    bornDate.send_keys(born_date_of_store, Keys.RETURN)
    residency = driver.find_element(By.XPATH, "(//input[contains(@role,'combobox')])[2]")
    residency.send_keys('Հայաստան', Keys.RETURN)
    nationality = driver.find_element(By.XPATH, "(//input[contains(@role,'combobox')])[3]")
    nationality.send_keys('ՀՀ', Keys.RETURN)
    nationality = driver.find_element(By.CSS_SELECTOR, '[value="MALE"]')
    nationality.click()
    childrenCount = driver.find_element(By.XPATH, "(//input[contains(@role,'combobox')])[4]")
    childrenCount.send_keys('1', Keys.RETURN)
    socialCard = driver.find_element(By.CSS_SELECTOR, '[name="socialCard"]')
    socialCard.send_keys(generate_random_number(make_rand_number, 10))
    socialCardIssueDate = driver.find_element(By.XPATH, "(//input[@placeholder='Select date'])[2]")
    socialCardIssueDate.send_keys(social_card_issue_date)
    passport = driver.find_element(By.XPATH, "(//input[contains(@role,'combobox')])[5]")
    passport.send_keys('ՀՀ նույնականացման քարտ', Keys.RETURN)
    passportID = driver.find_element(By.CSS_SELECTOR, '[name="passportId"]')
    passportID.send_keys(generate_random_number('se' + make_rand_number, 5))
    issuingAuthority = driver.find_element(By.CSS_SELECTOR, '[name="issuingAuthority"]')
    issuingAuthority.send_keys(generate_random_number(make_rand_number, 3))
    passportIssueDate = driver.find_element(By.XPATH, "(//input[@placeholder='Select date'])[3]")
    passportIssueDate.send_keys(passport_issue_date, Keys.RETURN)
    passportExpDate = driver.find_element(By.XPATH, "(//input[@placeholder='Select date'])[4]")
    passportExpDate.send_keys(passport_exp_date, Keys.RETURN)
    regNumber = driver.find_element(By.CSS_SELECTOR, '[name="stateRegistrationNumber"]')
    regNumber.send_keys('se.' + generate_random_number(make_rand_number, 4))
    regNumberForPE = driver.find_element(By.CSS_SELECTOR, '[name="registrationNumberForPE"]')
    regNumberForPE.send_keys('se.' + generate_random_number(make_rand_number, 4))
    PEIssueD = driver.find_element(By.XPATH, "(//input[@placeholder='Select date'])[5]")
    PEIssueD.send_keys(PE_issue_day, Keys.RETURN)
    productCheckbox = driver.find_element(By.XPATH, "(//input[@name='addressDTOS[0].productChecked'])[1]")
    productCheckbox.click()
    productSelect = driver.find_element(By.XPATH, "(//input[contains(@role,'combobox')])[8]")
    productSelect.send_keys('Ապրանք - Մթերք', Keys.RETURN)
    serviceCheckbox = driver.find_element(By.XPATH, "(//input[contains(@name,'addressDTOS[0].serviceChecked')])[1]")
    serviceCheckbox.click()
    serviceSelect = driver.find_element(By.XPATH, "(//input[contains(@role,'combobox')])[8]")
    serviceSelect.send_keys('Այս գարուն', Keys.RETURN)
    sameCheckbox = driver.find_element(By.XPATH, "//span[contains(text(),'Նույնն է')]")
    sameCheckbox.click()
    attachZIP = driver.find_element(By.XPATH, "//input[@type='file']")
    attachZIP.send_keys('/Users/martinharutyunyan/Documents/SeleniumPYFiles/zip.zip')
    saveBTN = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    saveBTN.click()



