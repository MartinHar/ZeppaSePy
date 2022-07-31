from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from os import path


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)


jpg = path.abspath(path.join(path.dirname(__file__), '1.jpg'))
pdf = path.abspath(path.join(path.dirname(__file__), '2.pdf'))
png = path.abspath(path.join(path.dirname(__file__), '3.png'))
url = 'http://ec2-63-34-222-67.eu-west-1.compute.amazonaws.com/login'
LGL_email = 'testlgl@sef.am'
LGL_password = 'Password3'
comment_for = 'Lorem ipsum dolor sit amet, Римский император Константин I Великий, Լոռեմ իպսում դոլոր սիթ ամետ'


class filteringPotentialPartner:
    driver.get(url)
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
    lastPartner = driver.find_element(By.CSS_SELECTOR, '[data-row-key="1"]')
    lastPartner.click()

    filterPartner = driver.find_element(By.CSS_SELECTOR, '[value="FILTER"]')
    filterPartner.click()
    comment = driver.find_element(By.CSS_SELECTOR, '[name="decisionFeedback"]')
    comment.send_keys(comment_for)
    uploadFile_1 = driver.find_element(By.XPATH, "(//input[contains(@type,'file')])[1]")
    uploadFile_1.send_keys(jpg)
    uploadFile_2 = driver.find_element(By.XPATH, "(//input[contains(@type,'file')])[2]")
    uploadFile_2.send_keys(pdf)
    uploadFile_3 = driver.find_element(By.XPATH, "(//input[contains(@type,'file')])[3]")
    uploadFile_3.send_keys(png)
    uploadFile_4 = driver.find_element(By.XPATH, "(//input[contains(@type,'file')])[4]")
    uploadFile_4.send_keys(jpg)
    save_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    # save_button.click()
