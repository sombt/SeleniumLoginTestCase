from common_imports import *
from components import forgotPassword_locator

driver.implicitly_wait(3)

forgotPassword_link = driver.find_element(*forgotPassword_locator)
forgotPassword_link.click()

time.sleep(3)

current_url = driver.current_url
print(driver.current_url)
expected_url = "https://app.talentcapture.us/forgot_password"

if current_url == expected_url:
    print("Test Passed")
else:
    print("Test Failed")

driver.quit()
