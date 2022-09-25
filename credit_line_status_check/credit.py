import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(2)

url = 'http://ec2-34-240-105-163.eu-west-1.compute.amazonaws.com/login'
admin_email = 'supm@sef.am'
admin_password = 'Password3'

driver.get(url)
driver.maximize_window()
login_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
login_email.send_keys(admin_email)
login_password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
login_password.send_keys(admin_password)
login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
login_button.click()

more_btn = driver.find_element(By.XPATH, "//span[contains(text(),'Ընդլայնված որոնում')]")
more_btn.click()
time.sleep(2)
# ongoing_loans_checkbox = driver.find_element(By.XPATH, "//span[contains(text(),'Ընթացիկ')]")
# ongoing_loans_checkbox.click()
# checkboxs list (//div[@class='users-filter-block'])[7]//div//div[i]

# declined_loans_checkbox = driver.find_element(By.XPATH, "//span[contains(text(),'Համակարգի կողմից մերժված')]")
# declined_loans_checkbox.click()
# checkbox_text = driver.find_element(By.XPATH, "//span[contains(text(),'Համակարգի կողմից մերժված')]").text         old version
checkboxes_for = driver.find_elements(By.XPATH, "(//div[@class='users-filter-block'])[7]//div//div")
# checkbox_text = driver.find_element(By.XPATH, "(//div[@class='users-filter-block'])[7]//div//div[3]").text
more_close_btn = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
to_click = driver.find_element(By.XPATH, "(//div[@class='users-filter-block'])[7]//div//div//input")


def comparing(checkbox):
    check_list = []
    list_len = driver.find_elements(By.XPATH, "//tr//td[13]")
    list_len = len(list_len)
    # print(list_len)
    for i in range(list_len-1):
        list_ = driver.find_element(By.XPATH, f"//tr{[i + 2]}//td[13]")
        check_list.append(list_.text)
        # print(f"{i+1} {list_.text}")
    next_page = driver.find_element(By.XPATH, "(//button[@type='button'])[6]")
    next_page.click()
    time.sleep(2)
    list_len = driver.find_elements(By.XPATH, "//tr//td[13]")
    list_len = len(list_len)
    # print(list_len)
    for i in range(list_len-1):
        list_ = driver.find_element(By.XPATH, f"//tr{[i + 2]}//td[13]")

        check_list.append(list_.text)
        # print(f"{i} {list_.text}")
    # print(check_list)
    # print(len(check_list))
    for i in check_list:
        print(i)
        if i != checkbox:
            print('not matching, we have a bug!')
            break
        else:
            print('ok')
    driver.quit()


for row in checkboxes_for:
    print(row.text)
    time.sleep(2)
    to_click.click()
    time.sleep(2)
    more_close_btn.click()
    time.sleep(2)
    comparing(row)
    time.sleep(2)
    more_btn.click()





# time.sleep(2)
# canceled_loans_checkbox = driver.find_element(By.XPATH, "//span[contains(text(),'Չեղարկված')]")
# canceled_loans_checkbox.click()
#
# time.sleep(2)





# def check():
#     for i in range(list_len):
#         try:
#             list = driver.find_element(By.XPATH, f"//tr{[i+2]}//td[13]")
#             print(f"{i} {list.text}")
#         except NoSuchElementException:
#             next_page = driver.find_element(By.XPATH, "(//button[@type='button'])[6]")
#             next_page.click()
#             pass


# def main():
    # comparing(checkbox_text)
#
#
# if __name__ == '__main__':
#     main()
