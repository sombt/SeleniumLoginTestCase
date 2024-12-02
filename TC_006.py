from common_imports import *
from components import signUp_locator

driver.implicitly_wait(3)

signUp_button = driver.find_element(*signUp_locator)
signUp_button.click()

time.sleep(3)

current_url = driver.current_url
print(driver.current_url)
expected_url = "https://app.talentcapture.us/register"

if current_url == expected_url:
    print("Test Passed")
else:
    print("Test Failed")

driver.quit()
