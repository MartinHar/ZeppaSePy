from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
from os import path


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


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


jpg = path.abspath(path.join(path.dirname(__file__), '1.jpg'))
pdf = path.abspath(path.join(path.dirname(__file__), '2.pdf'))
png = path.abspath(path.join(path.dirname(__file__), '3.png'))
main_file = path.abspath(path.join(path.dirname(__file__), '4.zip'))
url = 'http://ec2-63-34-222-67.eu-west-1.compute.amazonaws.com/login'
LO_email = 'lo24@sef.am'
LO_password = 'Password1'
LGL_email = 'testlgl@sef.am'
LGL_password = 'Password3'
email_of_store = 'partner_selenium.py@python.py'
url_of_store = 'https://www.selenium.dev/documentation/'
born_date_of_store = '01-01-1991'
social_card_issue_date = '01-01-2010'
passport_issue_date = '01-01-2022'
passport_exp_date = '01-01-2032'
PE_issue_day = '01-01-2000'



class addPotentialPartner:
    driver.get(url)
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
    addPotentialPartner_btn = driver.find_element(By.XPATH, "//span[.='Գրանցել գործընկերոջը']")
    addPotentialPartner_btn.click()

    legalName_fld = driver.find_element(By.CSS_SELECTOR, '[name="legalName"]')
    legalName_fld.send_keys(generate_random_arm_word(make_arm_word, 5))
    taxCode_fld = driver.find_element(By.CSS_SELECTOR, '[name="taxCode"]')
    taxCode_fld.send_keys(generate_random_number(make_rand_number, 8))
    firstName_fld = driver.find_element(By.CSS_SELECTOR, '[name="firstName"]')
    firstName_fld.send_keys(generate_random_arm_word(make_arm_word, 5))
    lastName_fld = driver.find_element(By.CSS_SELECTOR, '[name="lastName"]')
    lastName_fld.send_keys(generate_random_arm_word(make_arm_word, 5))
    patronymic_fld = driver.find_element(By.CSS_SELECTOR, '[name="patronymic"]')
    patronymic_fld.send_keys(generate_random_arm_word(make_arm_word, 5))
    BR_number = driver.find_element(By.XPATH, "(//input[@role='combobox'])[1]")
    BR_number.send_keys('Y24', Keys.RETURN)
    region = driver.find_element(By.XPATH, "(//span[@class='ant-select-selection-item'])[2]")
    region.click()
    region_yerevan = driver.find_element(By.XPATH, "(//div[contains(text(),'Երևան')])[1]")
    region_yerevan.click()
    c_v_c = driver.find_element(By.XPATH, "(//span[@class='ant-select-selection-item'])[3]")
    c_v_c.click()
    c_v_c_center = driver.find_element(By.XPATH, "(//div[contains(text(),'Կենտրոն')])[1]")
    c_v_c_center.click()
    address_str = driver.find_element(By.CSS_SELECTOR, '[name="addressDTOS.street"]')
    address_str.send_keys(generate_random_arm_word(make_arm_word, 5))
    address_house = driver.find_element(By.CSS_SELECTOR, '[name="addressDTOS.houseNumber"]')
    address_house.send_keys(generate_random_number(make_rand_number, 1))
    address_apartment = driver.find_element(By.CSS_SELECTOR, '[name="addressDTOS.apartmentNumber"]')
    address_apartment.send_keys(generate_random_number(make_rand_number, 3))
    save_btn = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    save_btn.click()


class filteringPotentialPartner:
    driver.get(url)
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
    lastPartner = driver.find_element(By.CSS_SELECTOR, '[data-row-key="1"]')
    lastPartner.click()

    filterPartner = driver.find_element(By.CSS_SELECTOR, '[value="FILTER"]')
    filterPartner.click()
    comment = driver.find_element(By.CSS_SELECTOR, '[name="decisionFeedback"]')
    comment.send_keys(generate_random_arm_word(make_arm_word, 5))
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