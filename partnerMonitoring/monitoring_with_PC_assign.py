import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

store_number = input('Enter store location number from partners list: ')


def start_webdriver():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)


def cycle_choice():
    user_choice = input('Please choose admin cycle, for LO type 1 , for BR press 2: ')
    if user_choice == '1':
        admin_email_ = 'loii@sef.am'
        admin_password_ = 'Password3'
        # admin_email_ = 'supm@sef.am'
        # admin_password_ = 'Password2'
        BM_email = 'mj11@sef.am'
        BM_password = 'Password1'
        admin_code_ = 'LOIII'
        return admin_email_, admin_password_, BM_email, BM_password, admin_code_

    elif user_choice == '2':
        admin_email_ = 'testbr@sef.am'
        admin_password_ = 'Password3'
        # admin_email_ = 'supm@sef.am'
        # admin_password_ = 'Password2'
        SALES_email = 'spd@sef.am'
        SALES_password = 'Password1'
        admin_code_ = 'LHK'
        return admin_email_, admin_password_, SALES_email, SALES_password, admin_code_
    else:
        print('Wrong input!')
        return cycle_choice()


cycle = cycle_choice()
admin_email = cycle[0]
admin_password = cycle[1]
second_admin_email = cycle[2]
second_admin_password = cycle[3]
admin_code = cycle[4]
PC_email = 'pcpc@sef.am'
PC_password = 'Password1'


def generate_random_arm_word(make_arm_word, n):
    return ''.join(random.choices(make_arm_word, k=n))


make_eng_word = 'abcdefg'


def generate_random_eng_word(make_eng_word, n):
    return ''.join(random.choices(make_eng_word, k=n))


make_rand_number = '0123456789'


def generate_random_number(make_rand_number, n):
    return ''.join(random.choices(make_rand_number, k=n))


def as_codes():
    driver.implicitly_wait(2)
    try:
        driver.find_element(By.CSS_SELECTOR, '[name="asCliCode"]') and driver.find_element(By.CSS_SELECTOR, '[name="asAccountNumber"]')
        print('ՀԾ հաճախորդի կոդ and ՀԾ հաշվի համար fields are present')
    except NoSuchElementException:
        print('WARNING!: ՀԾ հաճախորդի կոդ and ՀԾ հաշվի համար fields are missing')


threeMonthsCashMoneyCirculation = '5000000'
threeMonthsNonCashMoneyCirculation = '2000000'
seasonCirculation = '123000000-230000000'
currentLoanAmount = '34567800'
currentMaxExpiredAmount = '0'
maxLoanAmount = '10000000'
additionalInfo = 'Lorem ipsum dolor sit amet, Римский император Константин I Великий, Լոռեմ իպսում դոլոր սիթ ամետ'


def admin_cycle():
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
    time.sleep(1)
    Partner = driver.find_element(By.XPATH, f"//tbody/tr[{int(store_number)+1}]")
    Partner.click()

    monitoring_page = driver.find_element(By.XPATH, "//div[contains(text(),'Մոնիթորինգ')]")
    monitoring_page.click()
    Money_Circulation = driver.find_element(By.CSS_SELECTOR, '[name="threeMonthsCashMoneyCirculation"]')
    Money_Circulation.send_keys(threeMonthsCashMoneyCirculation)
    Money_Circulation_nonCash = driver.find_element(By.CSS_SELECTOR, '[name="threeMonthsNonCashMoneyCirculation"]')
    Money_Circulation_nonCash.send_keys(threeMonthsNonCashMoneyCirculation)
    season_Circulation = driver.find_element(By.CSS_SELECTOR, '[name="seasonCirculation"]')
    season_Circulation.send_keys(seasonCirculation)
    radio_btn_1 = driver.find_element(By.XPATH, "(//span[contains(text(),'Այո')])[1]")
    radio_btn_1.click()
    radio_btn_2 = driver.find_element(By.XPATH, "(//span[contains(text(),'Այո')])[2]")
    radio_btn_2.click()
    current_LoanAmount = driver.find_element(By.CSS_SELECTOR, '[name="currentLoanAmount"]')
    current_LoanAmount.send_keys(currentLoanAmount)
    current_Max_Expired_Amount = driver.find_element(By.CSS_SELECTOR, '[name="currentMaxExpiredAmount"]')
    current_Max_Expired_Amount.send_keys(currentMaxExpiredAmount)
    max_Loan_Amount = driver.find_element(By.CSS_SELECTOR, '[name="maxLoanAmount"]')
    max_Loan_Amount.send_keys(maxLoanAmount)
    additional_Info = driver.find_element(By.CSS_SELECTOR, '[name="additionalInfo"]')
    additional_Info.send_keys(additionalInfo)
    save_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Պահպանել')]")
    save_btn.click()


def second_admin_cycle():
    driver.get("http://ec2-34-240-105-163.eu-west-1.compute.amazonaws.com/login")
    driver.maximize_window()
    login_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    login_email.send_keys(second_admin_email)
    login_password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
    login_password.send_keys(second_admin_password)
    login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    login_button.click()

    partners_tab = driver.find_element(By.XPATH, "//a[.='Գործընկերներ']")
    partners_tab.click()
    time.sleep(1)
    Partner = driver.find_element(By.XPATH, f"//tbody/tr[{int(store_number)+1}]")
    Partner.click()

    monitoring_page = driver.find_element(By.XPATH, "//div[contains(text(),'Մոնիթորինգ')]")
    monitoring_page.click()

    BM_Sales_btn = driver.find_element(By.XPATH, "//button[contains(text(),'ՄՃ/Վաճառք հաստատում')]")
    BM_Sales_btn.click()
    time.sleep(2)


def pc_assign():
    driver.get("http://ec2-34-240-105-163.eu-west-1.compute.amazonaws.com/login")
    driver.maximize_window()
    login_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    login_email.send_keys(PC_email)
    login_password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
    login_password.send_keys(PC_password)
    login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    login_button.click()

    partners_tab = driver.find_element(By.XPATH, "//a[.='Գործընկերներ']")
    partners_tab.click()
    time.sleep(1)
    Partner = driver.find_element(By.XPATH, f"//tbody/tr[{int(store_number)+1}]")
    Partner.click()

    monitoring_page = driver.find_element(By.XPATH, "//div[contains(text(),'Մոնիթորինգ')]")
    monitoring_page.click()
    assign_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Հանձնարարել')]")
    assign_btn.click()
    time.sleep(1)
    adm = driver.find_element(By.XPATH, "//div[@class='ant-select-selector']")
    adm.click()
    time.sleep(1)
    select_admin = driver.find_element(By.XPATH, "//input[@role='combobox']")
    # select_admin.click()
    select_admin.send_keys(admin_code, Keys.RETURN)
    assign_comment = driver.find_element(By.XPATH, "//div[@class='ant-modal-body']//textarea[@class='ant-input']")
    assign_comment.send_keys(additionalInfo)
    assign_btn = driver.find_element(By.XPATH, "//div[@class='ant-modal-footer']//button[@type='button'][contains(text(),'Հանձնարարել')]")
    assign_btn.click()
    time.sleep(2)


def admin_approval():

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
    time.sleep(1)
    Partner = driver.find_element(By.XPATH, f"//tbody/tr[{int(store_number)+1}]")
    Partner.click()
    monitoring_page = driver.find_element(By.XPATH, "//div[contains(text(),'Մոնիթորինգ')]")
    monitoring_page.click()
    execute_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Կատարել')]")
    execute_btn.click()
    time.sleep(2)


def pc_approval():
    driver.get("http://ec2-34-240-105-163.eu-west-1.compute.amazonaws.com/login")
    driver.maximize_window()
    login_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    login_email.send_keys(PC_email)
    login_password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
    login_password.send_keys(PC_password)
    login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    login_button.click()

    partners_tab = driver.find_element(By.XPATH, "//a[.='Գործընկերներ']")
    partners_tab.click()
    time.sleep(1)
    Partner = driver.find_element(By.XPATH, f"//tbody/tr[{int(store_number)+1}]")
    Partner.click()
    monitoring_page = driver.find_element(By.XPATH, "//div[contains(text(),'Մոնիթորինգ')]")
    monitoring_page.click()
    PC_approve_btn = driver.find_element(By.XPATH, "//button[contains(text(),'ՀՊ հաստատում')]")
    PC_approve_btn.click()
    time.sleep(2)
    general_page = driver.find_element(By.XPATH, "//div[contains(text(),'Ընդհանուր')]")
    general_page.click()
    driver.refresh()
    time.sleep(2)
    as_codes()


def main():
    start_webdriver()
    admin_cycle()
    second_admin_cycle()
    pc_assign()
    admin_approval()
    pc_approval()


if __name__ == '__main__':
    main()
