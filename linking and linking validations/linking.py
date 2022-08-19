import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)


# NEED TO BE IMPROVED
def green_banner(banner_xpath):
    driver.implicitly_wait(2)
    try:
        green_banner_ = driver.find_element(By.XPATH, banner_xpath).text
        check = str(green_banner_) == 'Այս տվյալներով առկա է գործընկեր'
        if check is True:
            print('Green validation message is present, and text is: ' + str(check))
        else:
            print('WARNING: Green validation message text is incorrect')
    except NoSuchElementException:
        print('WARNING: No green validation message is detected on: ' + str(banner_xpath))
        sys.exit()


def check_field_empty_or_not(element):
    if len(element) == 0:
        # print(f'{field} field is empty')
        print('Warning! field is empty')
    else:
        print(element)


PC_email = 'pcpc@sef.am'
PC_password = 'Password1'
SUPM_email = 'supm@sef.am'
SUPM_password = 'Password3'
store_number_link = '1'
store_number = '4'

driver.get("http://ec2-34-240-105-163.eu-west-1.compute.amazonaws.com/login")
driver.maximize_window()
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

# if we get_attribute from variable , it will not work correctly.
# COLLECTING INFORMATION
# Phone number          (must not be linked if there is a store with this phone number)
phoneNumber_link = driver.find_element(
    By.XPATH, "//label[contains(text(),'Հեռախոսահամար')]/..//input[@type='number']").get_attribute("value")
check_field_empty_or_not(phoneNumber_link)
# BRAND NAME
brandName_link = driver.find_element(By.XPATH, "//input[@name='brandName']").get_attribute("value")
check_field_empty_or_not(brandName_link)
# TAX CODE
taxCode_link = driver.find_element(By.XPATH, "//input[@name='taxCode']").get_attribute("value")
check_field_empty_or_not(taxCode_link)
# AMD ACCOUNT NUMB.
bankAccountAMD_link = driver.find_element(By.XPATH, "//input[@name='bankAccount']").get_attribute("value")
check_field_empty_or_not(bankAccountAMD_link)
# USD ACCOUNT NUMB.
bankAccountUSD_link = driver.find_element(By.XPATH, "//input[@name='bankAccountUsd']").get_attribute("value")
check_field_empty_or_not(bankAccountUSD_link)
# SOCIAL CARD NUMB.
socialCard_link = driver.find_element(By.XPATH, "//input[@name='socialCard']").get_attribute("value")
check_field_empty_or_not(socialCard_link)
# PASSPORT ID
passportId_link = driver.find_element(By.XPATH, "//input[@name='passportId']").get_attribute("value")
check_field_empty_or_not(passportId_link)

partners_tab = driver.find_element(By.XPATH, "//a[.='Գործընկերներ']")
partners_tab.click()
Partner = driver.find_element(
    By.XPATH, f"(//tr[@class='ant-table-row ant-table-row-level-0 users-table-row'])[{store_number}]")
Partner.click()
asCliCode = driver.find_element(By.XPATH, "//input[@name='asCliCode']").get_attribute("value")
asAccountNumber = driver.find_element(By.XPATH, "//input[@name='asAccountNumber']").get_attribute("value")


def phone_number_case():
    # Phone number
    phoneNumber_main = driver.find_element(By.XPATH, '//input[@type="number"]')
    phoneNumber_main.send_keys(Keys.COMMAND + 'a')
    phoneNumber_main.send_keys(Keys.BACKSPACE)
    phoneNumber_main.send_keys(phoneNumber_link)
    save_btn = driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary unblock_button']")
    save_btn.click()
    time.sleep(1)
    try:
        error_banner = driver.find_element(By.XPATH, "//div[@class='ant-message-notice-content']").text
        check = str(error_banner) == \
                'Դուք չեք կարող օգտագործել այս հեռախոսահամարը։ ' \
                'Տվյալ հեռախոսահամարով արդեն առկա են հաճախորդի և գործընկերոջ հաշիվներ։' \
                or str(error_banner) == 'Դուք չեք կարող ' \
                'օգտագործել այս հեռախոսահամարը։ Տվյալ հեռախոսահամարով արդեն առկա են հաճախորդի և գործընկերոջ հաշիվներ։'
        if check is True:
            print('Phone number exist, banner validation message is: ' + str(check))
        else:
            print('WARNING! Banner text is incorrect')
    except NoSuchElementException:
        print('WARNING! No banner detected')
        sys.exit()


def linking_other_fields():
    # BRAND NAME
    brandName_main = driver.find_element(By.XPATH, "//input[@name='brandName']")
    brandName_main.clear()
    brandName_main.send_keys(brandName_link)
    # TAX CODE
    taxCode_main = driver.find_element(By.XPATH, "//input[@name='taxCode']")
    taxCode_main.clear()
    taxCode_main.send_keys(taxCode_link)
    # AMD ACCOUNT NUMB.
    bankAccountAMD_main = driver.find_element(By.XPATH, "//input[@name='bankAccount']")
    bankAccountAMD_main.clear()
    bankAccountAMD_main.send_keys(bankAccountAMD_link)
    # USD ACCOUNT NUMB.
    bankAccountUSD_main = driver.find_element(By.XPATH, "//input[@name='bankAccountUsd']")
    bankAccountUSD_main.clear()
    bankAccountUSD_main.send_keys(bankAccountUSD_link)
    # SOCIAL CARD NUMB.
    socialCard_main = driver.find_element(By.XPATH, "//input[@name='socialCard']")
    socialCard_main.clear()
    socialCard_main.send_keys(socialCard_link)
    # PASSPORT ID
    passportId_main = driver.find_element(By.XPATH, "//input[@name='passportId']")
    passportId_main.clear()
    passportId_main.send_keys(passportId_link)
    # SUBMIT BUTTON
    submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_btn.click()
    time.sleep(1)
    # LINK BUTTON
    try:
        driver.implicitly_wait(2)
        link_btn = driver.find_element(By.XPATH, "//div[@class='ant-modal-footer']//button[@type='submit']")
        link_btn.click()
    except:
        print('WARNING: Փոխկապակցել popup is not located\n')
    # CHECK STORE IS ACTIVATED OR NOT
    if len(asCliCode) == 0 and len(asAccountNumber) == 0:
        print('Warning! Store is not activated, try another store')
    else:
        print('Store is activated')
    # CHECK FOR GREEN VALIDATION UNDER FIELDS
    green_banner(str("(//div[@role='alert'])[1]"))
    green_banner(str("(//div[@role='alert'])[2]"))
    green_banner(str("(//div[@role='alert'])[3]"))
    green_banner(str("(//div[@role='alert'])[4]"))
    green_banner(str("(//div[@role='alert'])[5]"))
    green_banner(str("(//div[@role='alert'])[6]"))


def main():
    phone_number_case()
    # linking_other_fields()


if __name__ == '__main__':
    main()
