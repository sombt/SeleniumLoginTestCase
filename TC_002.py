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

driver.implicitly_wait(3)

input_email = driver.find_element(
    By.ID, "u_email").send_keys("sombsfsadfgcourse@gmail.com" + Keys.ENTER)

input_password = driver.find_element(
    By.ID, "pwd").send_keys("Taleasdnt" + Keys.ENTER)

signIn_button = driver.find_element(
    By.XPATH, '//*[@id="tc-form-buttons"]/button')
signIn_button.click()

time.sleep(3)

alert_msg = driver.find_element(By.CLASS_NAME, "alert.alert-error")
current_alert = alert_msg.text
expected_alert = "Invalid Credentials"

current_url = driver.current_url
print(driver.current_url)
expected_url = "https://app.talentcapture.us/login"

if current_url == expected_url and current_alert == expected_alert:
    print("Test Passed")
else:
    print("Test Failed")


time.sleep(15)

driver.quit()
