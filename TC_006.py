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

signUp_button = driver.find_element(
    By.XPATH, '//*[@tabindex="6"]')
signUp_button.click()

time.sleep(3)

current_url = driver.current_url
print(driver.current_url)
expected_url = "https://app.talentcapture.us/register"

if current_url == expected_url:
    print("Test Passed")
else:
    print("Test Failed")


time.sleep(15)

driver.quit()
