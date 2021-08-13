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

time.sleep(5)

# not_now = driver.find_element_by_link_text("Not now")
# not_now.click()

# remember_me = driver.find_element_by_link_text("Remember")
# remember_me.click()

# -------------------- Locate the Apply Button -------------------- #
chat_min = driver.find_element_by_class_name("msg-overlay-bubble-header__details")
chat_min.click()

time.sleep(5)


all_listings = driver.find_elements_by_class_name("jobs-search-results__list-item")

for listings in all_listings:
    print("Job Clicked")
    listings.click()
    time.sleep(2.5)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(os.environ.get("PHONE"))

        submit_button = driver.find_element_by_css_selector("footer button")
        driver.back()

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            # Click on the close button
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2.5)

            # Click on discard button
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()

            print("Complex Application Skipped.")
            continue
        else:
            # Submit the application
            submit_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button present, Skipped.")
        continue

time.sleep(5)
