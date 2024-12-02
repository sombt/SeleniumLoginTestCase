from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

email_valid = os.getenv("VALID_EMAIL")
password_valid = os.getenv("VALID_PASSWORD")

email_locator = (
    By.ID, "u_email")
password_locator = (
    By.ID, "pwd")
signIn_locator = (
    By.XPATH, '//*[@id="tc-form-buttons"]/button')
credential_error_locator = (By.CLASS_NAME, "alert.alert-error")
signUp_locator = (
    By.XPATH, '//*[@tabindex="6"]')
forgotPassword_locator = (
    By.LINK_TEXT, "Forgot Password?")
