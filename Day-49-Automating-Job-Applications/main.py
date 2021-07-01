import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


# -------------------- Initiate Selenium -------------------- #
chrome_driver_path = "C:\Development_Driver\chromedriver.exe"
# Configure Chrome to open in fullScreen / kiosk mode.
options = webdriver.ChromeOptions()
options.add_argument("--kiosk")
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)


# -------------------- Load search results and login. -------------------- #
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102257491&keywords=python%20developer&location"
           "=London%2C%20England%2C%20United%20Kingdom&sortBy=R")

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

# Wait for the next page to load
time.sleep(5)

email_field = driver.find_element_by_id("username")
email_field.send_keys(os.environ.get("USERNAME"))

password_field = driver.find_element_by_id("password")
password_field.send_keys(os.environ.get("PASSWORD"))
password_field.send_keys(Keys.ENTER)

# not_now = driver.find_element_by_link_text("Not now")
# not_now.click()

# remember_me = driver.find_element_by_link_text("Remember")
# remember_me.click()

# Locate the Apply Button
time.sleep(5)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

min_msg_bubble = driver.find_element_by_class_name("msg-overlay-bubble-header__details")
min_msg_bubble.click()

# If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(os.environ.get("PHONE"))

# Submit the application
submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()
