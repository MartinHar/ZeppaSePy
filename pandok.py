from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

driverLocation = Service(executable_path="/Users/martinharutyunyan/Desktop/PythonAutomationZeppa/chromedriver")
driver = webdriver.Chrome(service=driverLocation)
driver.get("https://yp-dev.essentialsln.com/")
driver.implicitly_wait(10)


login = driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys('super')
password = driver.find_element(By.XPATH, "(//input[@type='password'])[1]").send_keys('000000')
submit_btn_login = driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
restaurant_list = driver.find_element(By.CLASS_NAME, "MuiInputBase-root.MuiInputBase-adornedEnd")
restaurant_list.click()
all_branches = driver.find_element(By.XPATH, "(//li[@role='menuitem'])[1]").click()
close_btn = driver.find_element(By.XPATH, "(//span[contains(text(),'Փակել')])[1]").click()
enter_in = driver.find_element(By.XPATH, "//button[@type='submit']").click()
