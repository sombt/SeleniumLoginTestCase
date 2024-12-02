from common_imports import *
from components import email_locator, email_valid, password_locator, password_valid, signIn_locator

input_email = driver.find_element(
    *email_locator).send_keys(email_valid + Keys.ENTER)


input_password = driver.find_element(
    *password_locator).send_keys(password_valid + Keys.ENTER)

signIn_button = driver.find_element(*signIn_locator)
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
