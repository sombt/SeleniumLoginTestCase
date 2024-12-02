from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

service = Service("geckodriver.exe")
driver = webdriver.Firefox(service=service)
action = ActionChains(driver)


driver.get("https://app.talentcapture.us/login")
input_email = driver.find_element(
    By.ID, "u_email").send_keys("sombdrtmgcourse@gmail.com" + Keys.ENTER)


input_password = driver.find_element(
    By.ID, "pwd").send_keys("Talent" + Keys.ENTER)

signIn_button = driver.find_element(
    By.XPATH, '//*[@id="tc-form-buttons"]/button')
signIn_button.click()

time.sleep(5)

current_url = driver.current_url

print(driver.current_url)
expected_url = "https://app.talentcapture.us/candidate/profile/viewMyProfile"

if current_url == expected_url:
    print("Test Passed")
else:
    print("Test Failed")

driver.quit()
