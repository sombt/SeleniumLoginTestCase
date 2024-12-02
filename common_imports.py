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
