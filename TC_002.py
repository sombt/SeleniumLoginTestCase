from common_imports import *
from components import email_locator, password_locator, signIn_locator, credential_error_locator

driver.implicitly_wait(3)

input_email = driver.find_element(
    *email_locator).send_keys("sombsfsadfgcourse@gmail.com" + Keys.ENTER)

input_password = driver.find_element(
    *password_locator).send_keys("Taleasdnt" + Keys.ENTER)

signIn_button = driver.find_element(*signIn_locator)
signIn_button.click()

time.sleep(3)

alert_msg = driver.find_element(*credential_error_locator)
current_alert = alert_msg.text
expected_alert = "Invalid Credentials"

current_url = driver.current_url
print(driver.current_url)
expected_url = "https://app.talentcapture.us/login"

if current_url == expected_url and current_alert == expected_alert:
    print("Test Passed")
else:
    print("Test Failed")

driver.quit()
