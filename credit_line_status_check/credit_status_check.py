import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


# def start_webdriver():
#     global driver
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.implicitly_wait(10)

def start_webdriver():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(7)


# len of checkboxes at more page
def checkboxes_list_count():
    driver.find_element(By.XPATH, "//span[contains(text(),'Ընդլայնված որոնում')]").click()
    loan_status_checkboxes = driver.find_elements(By.XPATH, "//div[@class='ant-col ant-col-6']//div[@class='users-filter-block']//div//div")
    loan_status_checkboxes_count = len(loan_status_checkboxes)
    driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
    return loan_status_checkboxes_count


def users_count_on_page():
    count = len(driver.find_elements(By.XPATH, "//tbody/tr/td[13]"))
    print("Users count is: " + str(count-1))
    return count-1


class Credit_status_check:
    url = 'http://ec2-34-240-105-163.eu-west-1.compute.amazonaws.com/login'
    admin_email = 'supm@sef.am'
    admin_password = 'Password2'

    start_webdriver()
    driver.get(url)
    driver.maximize_window()
    login_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    login_email.send_keys(admin_email)
    login_password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
    login_password.send_keys(admin_password)
    login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    login_button.click()
    checkboxes_count = checkboxes_list_count()
    print(checkboxes_count)

    # more_btn = driver.find_element(By.XPATH, "//span[contains(text(),'Ընդլայնված որոնում')]")
    # more_btn.click()
    # time.sleep(2)
    # loan_status_checkboxes = driver.find_elements(By.XPATH, "//div[@class='ant-col ant-col-6']//div[@class='users-filter-block']//div//div")
    # loan_status_checkboxes_count = len(loan_status_checkboxes)
    # first_loan = driver.find_element(By.XPATH, "//div[@class='ant-col ant-col-6']//div[@class='users-filter-block']//div//div[1]//input")
    # first_loan.click()
    # time.sleep(2)
    # print(loan_status_checkboxes_count)
    # close_btn = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
    # close_btn.click()

        # loan_status_column = driver.find_elements(By.XPATH, "//tbody/tr/td[13]")
        # loan_status_column_length = len(loan_status_column)
        # print("loan status column length is: " + str(loan_status_column_length - 1))
        # for row in range(loan_status_column_length-1):
        #     el = driver.find_element(By.XPATH, f"//tbody/tr{[row + 1]}/td[13]")
        #     el_in_text = el.text
        #     print(el_in_text)
        #     # if el_in_text !=

    for checkbox in range(checkboxes_count):
        # go to selection menu
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(),'Ընդլայնված որոնում')]").click()
        time.sleep(1)

        # get row name
        loan_list_row_name = driver.find_element(By.XPATH, f"//div[@class='ant-col ant-col-6']//div[@class='users-filter-block']//div//div[{checkbox + 1}]").text
        print(loan_list_row_name)

        # select checkbox
        driver.find_element(By.XPATH, f"//div[@class='ant-col ant-col-6']//div[@class='users-filter-block']//div//div[{checkbox+1}]//input").click()

        # close checkboxes modal
        driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
        time.sleep(1)

        # comparing actions
        # get rows
        users_count = users_count_on_page()
        for user in range(users_count):
            el = driver.find_element(By.XPATH, f"//tbody/tr[{2 + user}]/td[13]").text
            print("User status is: " + el)

            # if status is not the same
            if el != loan_list_row_name:
                print("User status is: " + el)
                print("But User status should be: " + loan_list_row_name)
                print('Not matching!')
                break

        #   next_button = driver.find_element(By.XPATH, "(//button[@type='button'])[6]")





        # deseclect checkbox
        # open more menu
        driver.find_element(By.XPATH, "//span[contains(text(),'Ընդլայնված որոնում')]").click()
        time.sleep(1)

        # click to checkbox
        driver.find_element(By.XPATH, f"//div[@class='ant-col ant-col-6']//div[@class='users-filter-block']//div//div{[checkbox+1]}//input").click()
        time.sleep(1)

        # close more menu
        driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
        time.sleep(1)
    driver.quit()



    # def compare(self):



def main():
    Credit_status_check()


if __name__ == '__main__':
    main()
