import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
from os import path
from faker import Faker


fake = Faker()
fake_eng_company = fake.company()
# fake_eng_description = fake.bs()    // short version of description
fake_eng_description = fake.sentence(nb_words=20)
fake_eng_post_name = fake.catch_phrase()
fake_eng_word = fake.word()
fake_am = Faker('hy_AM')
fake_am_word = fake_am.word()

price_generator = random.randrange(10, 500000, 10)

admin_email = 'supm@sef.am'
admin_password = 'Password2'


def start():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)


list_of_radio_btns = ['PRODUCT', 'SERVICE']


def fake_image():
    my_width = 1280
    my_height = 1024
    image_url = fake.image_url(my_width, my_height)
    s = requests.get(image_url)
    img = fake.word()+'.jpg'
    print(img)
    with open(img, "wb") as file:
        file.write(s.content)
    time.sleep(1)
    jpg = path.abspath(path.join(path.dirname(__file__), img))
    return jpg


def add_post():
    choice = input("Enter user/store number or name: ")
    start()
    driver.get("http://ec2-34-240-105-163.eu-west-1.compute.amazonaws.com/login")
    driver.maximize_window()
    login_email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    login_email.send_keys(admin_email)
    login_password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
    login_password.send_keys(admin_password)
    login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    login_button.click()

    driver.find_element(By.XPATH, "//span[contains(text(),'Հրապարակումներ')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(text(),'Ստանդարտ հրապարակումներ')]").click()
    time.sleep(1)
    add_btn = driver.find_element(By.XPATH, "//button[.='Ավելացնել']")
    add_btn.click()
    user_store_dropdown = driver.find_element(By.XPATH, "(//input[@role='combobox'])[1]")
    time.sleep(1)
    user_store_dropdown.send_keys(str(choice) + Keys.RETURN)
    time.sleep(1)
    # determine user/store dropdown length of text
    length_of_user_store_dropdown = len(driver.find_element(By.XPATH, "//span[@title][1]").text)
    # print(str(length_of_user_store_dropdown) + ' digits')
    if length_of_user_store_dropdown == 0:
        print(f'No user/store found with following ID: {choice}')
        driver.quit()
        exit()
    post_name = driver.find_element(By.CSS_SELECTOR, '[name="title"]')
    post_name.send_keys(fake_eng_post_name)
    post_price = driver.find_element(By.CSS_SELECTOR, '[name="price"]')
    post_price.send_keys(price_generator)
    # randomly choose between 2 radio buttons
    radio_type_choose = driver.find_element(By.XPATH, f"//input[@value='{random.choice(list_of_radio_btns)}']")
    radio_type_choose.click()
    subcategory_dropdown = driver.find_element(By.XPATH, "(//div[@class='ant-select-selector'])[2]")
    subcategory_dropdown.click()
    time.sleep(0.5)
    first_category_to_select = driver.find_element(By.XPATH, f"//form/div[5]/div[2]//div[2]//div[2]/div[1]//div[{random.randrange(1,4)}]/div")
    first_category_to_select.click()
    time.sleep(0.5)
    region_dropdown = driver.find_element(By.XPATH, "(//div[@class='ant-select-selector'])[3]")
    region_dropdown.click()
    time.sleep(0.5)
    region_to_select = driver.find_element(By.XPATH, f"//main//form/div[6]/div[2]//div[2]//div[2]/div[1]/div/div/div[{random.randrange(1,4)}]/div")
    region_to_select.click()
    time.sleep(0.5)
    city_village_dropdown = driver.find_element(By.XPATH, "(//div[@class='ant-select-selector'])[4]")
    city_village_dropdown.click()
    time.sleep(0.5)
    city_village_select = driver.find_element(By.XPATH, f"//form/div[7]/div[2]//div[2]//div[2]/div[1]/div/div/div[{random.randrange(1,4)}]/div")
    city_village_select.click()
    # time.sleep(1)
    description_field = driver.find_element(By.CSS_SELECTOR, '[name="description"]')
    description_field.send_keys("Made with Selenium..." + fake_eng_description)
    # time.sleep(1)
    hashtags_field = driver.find_element(By.XPATH, "//input[contains(@placeholder,'Մուտքագրեք և սեղմեք enter')]")
    hashtags_field.send_keys(fake_eng_word + Keys.RETURN, fake_am_word + Keys.RETURN)
    # time.sleep(1)
    add_picture_1 = driver.find_element(By.XPATH, "(//input[contains(@type,'file')])[1]")
    add_picture_1.send_keys(fake_image())
    add_picture_2 = driver.find_element(By.XPATH, "(//input[contains(@type,'file')])[2]")
    add_picture_2.send_keys(fake_image())
    add_picture_3 = driver.find_element(By.XPATH, "(//input[contains(@type,'file')])[3]")
    add_picture_3.send_keys(fake_image())


def main():
    add_post()


if __name__ == '__main__':
    main()
