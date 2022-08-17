import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.implicitly_wait(10)


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
        driver.find_element(By.CSS_SELECTOR, '[name="asCliCode"]') and \
        driver.find_element(By.CSS_SELECTOR, '[name="asAccountNumber"]')
        print('ՀԾ հաճախորդի կոդ and ՀԾ հաշվի համար fields are present')
    except NoSuchElementException:
        print('WARNING!: ՀԾ հաճախորդի կոդ and ՀԾ հաշվի համար fields are missing')


store_number = '1'
LO_email = 'automation_lo24@sef.am'
LO_password = 'Password5'
BM_email = 'automation_bm24@sef.am'
BM_password = 'Password5'
PC_email = 'automation_pc@sef.am'
PC_password = 'Password5'

threeMonthsCashMoneyCirculation = '5000000'
threeMonthsNonCashMoneyCirculation = '2000000'
seasonCirculation = '123000000-230000000'
currentLoanAmount = '34567800'
currentMaxExpiredAmount = '0'
maxLoanAmount = '10000000'
additionalInfo = 'Lorem ipsum dolor sit amet, Римский император Константин I Великий, Լոռեմ իպսում դոլոր սիթ ամետ'


def lo_cycle():
    driver.get('http://ec2-63-34-222-67.eu-west-1.compute.amazonaws.com/login')
    driver.maximize_window()
    login_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    login_email.send_keys(LO_email)
    login_password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
    login_password.send_keys(LO_password)
    login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    login_button.click()

    partners_tab = driver.find_element(By.XPATH, "//a[.='Գործընկերներ']")
    partners_tab.click()
    Partner = driver.find_element(
        By.XPATH, f"(//tr[@class='ant-table-row ant-table-row-level-0 users-table-row'])[{store_number}]")
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
    save_btn = driver.find_element(By.XPATH, "//span[contains(text(),'Պահպանել')]")
    save_btn.click()
    time.sleep(2)


def bm_cycle():
    driver.get('http://ec2-63-34-222-67.eu-west-1.compute.amazonaws.com/login')
    driver.maximize_window()
    login_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    login_email.send_keys(BM_email)
    login_password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
    login_password.send_keys(BM_password)
    login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    login_button.click()

    partners_tab = driver.find_element(By.XPATH, "//a[.='Գործընկերներ']")
    partners_tab.click()
    Partner = driver.find_element(
        By.XPATH, f"(//tr[@class='ant-table-row ant-table-row-level-0 users-table-row'])[{store_number}]")
    Partner.click()

    monitoring_page = driver.find_element(By.XPATH, "//div[contains(text(),'Մոնիթորինգ')]")
    monitoring_page.click()

    BM_Sales_btn = driver.find_element(By.XPATH, "//span[contains(text(),'ՄՃ/Վաճառք հաստատում')]")
    BM_Sales_btn.click()
    time.sleep(2)


def pc_assign():
    driver.get('http://ec2-63-34-222-67.eu-west-1.compute.amazonaws.com/login')
    driver.maximize_window()
    login_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    login_email.send_keys(PC_email)
    login_password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
    login_password.send_keys(PC_password)
    login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    login_button.click()

    partners_tab = driver.find_element(By.XPATH, "//a[.='Գործընկերներ']")
    partners_tab.click()
    Partner = driver.find_element(
        By.XPATH, f"(//tr[@class='ant-table-row ant-table-row-level-0 users-table-row'])[{store_number}]")
    Partner.click()

    monitoring_page = driver.find_element(By.XPATH, "//div[contains(text(),'Մոնիթորինգ')]")
    monitoring_page.click()
    assign_btn = driver.find_element(By.XPATH, "//span[contains(text(),'Հանձնարարել')]")
    assign_btn.click()
    time.sleep(1)
    adm = driver.find_element(By.XPATH, "//div[@class='ant-select-selector']")
    adm.click()
    time.sleep(1)
    s_admin = driver.find_element(By.XPATH, "//div[@title='autLO - Լօ Լօ']")
    s_admin.click()
    assign_comment = driver.find_element(By.XPATH, "//div[@class='ant-modal-body']//textarea[@class='ant-input']")
    assign_comment.send_keys(additionalInfo)
    assign_btn = driver.find_element(By.XPATH, "//div[@class='ant-modal-footer']//span[contains(text(),'Հանձնարարել')]")
    assign_btn.click()
    time.sleep(2)


def lo_approval():

    driver.get('http://ec2-63-34-222-67.eu-west-1.compute.amazonaws.com/login')
    driver.maximize_window()
    login_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    login_email.send_keys(LO_email)
    login_password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
    login_password.send_keys(LO_password)
    login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    login_button.click()

    partners_tab = driver.find_element(By.XPATH, "//a[.='Գործընկերներ']")
    partners_tab.click()
    Partner = driver.find_element(
        By.XPATH, f"(//tr[@class='ant-table-row ant-table-row-level-0 users-table-row'])[{store_number}]")
    Partner.click()
    monitoring_page = driver.find_element(By.XPATH, "//div[contains(text(),'Մոնիթորինգ')]")
    monitoring_page.click()
    execute_btn = driver.find_element(By.XPATH, "//span[contains(text(),'Կատարել')]")
    execute_btn.click()
    time.sleep(2)


def bm_cycle_2():
    driver.get('http://ec2-63-34-222-67.eu-west-1.compute.amazonaws.com/login')
    driver.maximize_window()
    login_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    login_email.send_keys(BM_email)
    login_password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
    login_password.send_keys(BM_password)
    login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    login_button.click()

    partners_tab = driver.find_element(By.XPATH, "//a[.='Գործընկերներ']")
    partners_tab.click()
    Partner = driver.find_element(
        By.XPATH, f"(//tr[@class='ant-table-row ant-table-row-level-0 users-table-row'])[{store_number}]")
    Partner.click()

    monitoring_page = driver.find_element(By.XPATH, "//div[contains(text(),'Մոնիթորինգ')]")
    monitoring_page.click()

    BM_Sales_btn = driver.find_element(By.XPATH, "//span[contains(text(),'ՄՃ/Վաճառք հաստատում')]")
    BM_Sales_btn.click()
    time.sleep(2)


def pc_approval():
    driver.get('http://ec2-63-34-222-67.eu-west-1.compute.amazonaws.com/login')
    driver.maximize_window()
    login_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    login_email.send_keys(PC_email)
    login_password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
    login_password.send_keys(PC_password)
    login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    login_button.click()

    partners_tab = driver.find_element(By.XPATH, "//a[.='Գործընկերներ']")
    partners_tab.click()
    Partner = driver.find_element(
        By.XPATH, f"(//tr[@class='ant-table-row ant-table-row-level-0 users-table-row'])[{store_number}]")
    Partner.click()
    monitoring_page = driver.find_element(By.XPATH, "//div[contains(text(),'Մոնիթորինգ')]")
    monitoring_page.click()
    PC_approve_btn = driver.find_element(By.XPATH, "//span[contains(text(),'ՀՊ հաստատում')]")
    PC_approve_btn.click()
    time.sleep(2)
    general_page = driver.find_element(By.XPATH, "//div[contains(text(),'Ընդհանուր')]")
    general_page.click()
    driver.refresh()
    time.sleep(2)
    as_codes()


def main():
    # lo_cycle()
    # bm_cycle()
    pc_assign()
    lo_approval()
    bm_cycle_2()
    pc_approval()


if __name__ == '__main__':
    main()
